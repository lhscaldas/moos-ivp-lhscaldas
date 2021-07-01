/************************************************************/
/*    NAME: lhscaldas                                              */
/*    ORGN: MIT, Cambridge MA                               */
/*    FILE: TrajectPID.cpp                                        */
/*    DATE: December 29th, 1963                             */
/************************************************************/

#include <iterator>
#include "MBUtils.h"
#include "ACTable.h"
#include "TrajectPID.h"
#include <stdlib.h> 

using namespace std;

//---------------------------------------------------------
// Constructor

TrajectPID::TrajectPID()
{
  m_desired_speed=0;
  m_desired_heading=0;
  m_nav_speed=0;
  m_nav_heading=0;
  m_desired_rudder=0;
  m_desired_rotation=0;
  m_speed_kp=4.944*2;
  m_speed_ki=0.1629*5;
  m_speed_kd=0;
  m_course_kp=3.97;
  m_course_ki=0.269;
  m_course_kd=3.95;
  m_dt=0.1/3;
  m_speed_int_err=0;
  m_speed_prev_err=0;
  m_speed_setpoint=0;
  m_speed_maxout=17.5;
  m_speed_saturated=0;
  m_course_int_err=0;
  m_course_prev_err=0;
  m_course_setpoint=0;
  m_course_maxout=35;
  m_course_saturated=0;
}

//---------------------------------------------------------
// Destructor

TrajectPID::~TrajectPID()
{
}

//---------------------------------------------------------
// Procedure: OnNewMail

bool TrajectPID::OnNewMail(MOOSMSG_LIST &NewMail)
{
  AppCastingMOOSApp::OnNewMail(NewMail);

  MOOSMSG_LIST::iterator p;
  for(p=NewMail.begin(); p!=NewMail.end(); p++) {
    CMOOSMsg &msg = *p;
    if (msg.GetKey() == "DESIRED_HEADING" && msg.IsDouble()) {
      m_desired_heading = msg.GetDouble();
    } else if (msg.GetKey() == "NAV_HEADING" && msg.IsDouble()) {
      m_nav_heading = msg.GetDouble();
    } else if (msg.GetKey() == "DESIRED_SPEED" && msg.IsDouble()) {
      m_desired_speed = msg.GetDouble();
    }else if (msg.GetKey() == "NAV_SPEED" && msg.IsDouble()) {
      m_nav_speed = msg.GetDouble();
    }
  }

#if 0 // Keep these around just for template
    string comm  = msg.GetCommunity();
    double dval  = msg.GetDouble();
    string sval  = msg.GetString(); 
    string msrc  = msg.GetSource();
    double mtime = msg.GetTime();
    bool   mdbl  = msg.IsDouble();
    bool   mstr  = msg.IsString();
#endif

   return(true);
}

//---------------------------------------------------------
// Procedure: OnConnectToServer

bool TrajectPID::OnConnectToServer()
{
   registerVariables();
   return(true);
}

//---------------------------------------------------------
// Procedure: Iterate()
//            happens AppTick times per second

bool TrajectPID::Iterate()
{
  AppCastingMOOSApp::Iterate();
  m_speed_setpoint=m_desired_speed;
  speedPID(m_nav_speed);
  m_course_setpoint=m_desired_heading;
  speedPID(m_nav_heading);
  m_Comms.Notify("DESIRED_ROTATION", m_desired_rotation);
  m_Comms.Notify("DESIRED_RUDDER", m_desired_rudder);
  AppCastingMOOSApp::PostReport();
  return(true);
}

//---------------------------------------------------------
// Procedure: OnStartUp()
//            happens before connection is open

bool TrajectPID::OnStartUp()
{
  AppCastingMOOSApp::OnStartUp();

  STRING_LIST sParams;
  m_MissionReader.EnableVerbatimQuoting(false);
  if(!m_MissionReader.GetConfiguration(GetAppName(), sParams))
    reportConfigWarning("No config block found for " + GetAppName());

  STRING_LIST::iterator p;
  for(p=sParams.begin(); p!=sParams.end(); p++) {
    string orig  = *p;
    string line  = *p;
    string param = tolower(biteStringX(line, '='));
    string value = line;

    bool handled = false;
    if(param == "foo") {
      handled = true;
    }
    else if(param == "bar") {
      handled = true;
    }

    if(!handled)
      reportUnhandledConfigWarning(orig);

  }
  
  registerVariables();	
  return(true);
}

//---------------------------------------------------------
// Procedure: registerVariables

void TrajectPID::registerVariables()
{
  AppCastingMOOSApp::RegisterVariables();
  Register("DESIRED_SPEED", 0);
  Register("NAV_SPEED", 0);
  Register("DESIRED_HEADING", 0);
  Register("NAV_HEADING", 0);
}


//------------------------------------------------------------
// Procedure: buildReport()

bool TrajectPID::buildReport() 
{
  m_msgs << "============================================" << endl;
  m_msgs << "File:                                       " << endl;
  m_msgs << "============================================" << endl;

  ACTable actab(5);
  actab << "setpoint | speed | error | int_err | output";
  actab.addHeaderLines();
  actab << m_speed_setpoint << m_nav_speed << (m_speed_setpoint-m_nav_speed) << m_speed_int_err << m_desired_rotation;
  m_msgs << actab.getFormattedString();

  return(true);
}

//--------------------------------------------------------
// PID functions
void TrajectPID::speedPID(double y)
{
  double error = m_speed_setpoint-y;
  double diff_error = (error-m_speed_prev_err)/m_dt;
  m_speed_int_err += error*m_dt;
  double output = m_speed_kp*error; //m_speed_kp*error + (1-m_speed_saturated)*m_speed_ki*m_speed_int_err + m_speed_kd*diff_error;
  if(abs(output)>m_speed_maxout){
    output = output/abs(output)*m_speed_maxout;
    m_speed_saturated=1;
    m_speed_int_err=0;
  }
  else{
    m_speed_saturated=0;
  }
  m_desired_rotation=output;
  m_speed_prev_err= error;
}

void TrajectPID::coursePID(double y)
{
  double error = m_course_setpoint-y;
  double diff_error = (error-m_course_prev_err)/m_dt;
  m_course_int_err += error*m_dt;
  double output = m_course_kp*error + (1-m_course_saturated)*m_course_ki*m_course_int_err + m_course_kd*diff_error;
  if(output>m_course_maxout){
    if(output>=0){
      output=m_course_maxout;
    } else{
      output=-m_course_maxout;
    }
    m_course_saturated=1;
    m_course_int_err=0;
  }
  else{
    m_course_saturated=0;
  }
  m_desired_rudder=output;
  m_course_prev_err= error;
}




