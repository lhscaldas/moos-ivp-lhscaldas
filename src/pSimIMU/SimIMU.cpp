/************************************************************/
/*    NAME: lhscaldas                                       */
/*    ORGN: USP, São Paulo SP                               */
/*    FILE: SimIMU.cpp                                      */
/*    DATE: 14/06/2021                                      */
/************************************************************/

#include <iterator>
#include "MBUtils.h"
#include "ACTable.h"
#include "SimIMU.h"
#include <math.h>

using namespace std;

#define RAD2DEG 180/M_PI

//---------------------------------------------------------
// Constructor

SimIMU::SimIMU()
{
   m_real_rot=0;
   m_dt=0;
   m_t_ant=0;
   m_t_now=0;
   m_counter=0;
   m_imu_heading=90;
}

//---------------------------------------------------------
// Destructor

SimIMU::~SimIMU()
{
}

//---------------------------------------------------------
// Procedure: OnNewMail

bool SimIMU::OnNewMail(MOOSMSG_LIST &NewMail)
{
  AppCastingMOOSApp::OnNewMail(NewMail);

  MOOSMSG_LIST::iterator p;
  for(p=NewMail.begin(); p!=NewMail.end(); p++) {
    CMOOSMsg &msg = *p;
    if (msg.GetKey() == "REAL_ROT" && msg.IsDouble()) {
      m_real_rot = msg.GetDouble();
    } else if (msg.GetKey() == "DB_UPTIME" && msg.IsDouble()) {
      m_t_now = msg.GetDouble();
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

bool SimIMU::OnConnectToServer()
{
   registerVariables();
   return(true);
}

//---------------------------------------------------------
// Procedure: Iterate()
//            happens AppTick times per second

bool SimIMU::Iterate()
{
  AppCastingMOOSApp::Iterate();
  // m_counter++;
  // if(m_counter==10){
  m_dt = m_t_now - m_t_ant;
  m_imu_heading-= RAD2DEG*m_real_rot*m_dt;
  if(m_imu_heading>360)
  {
    m_imu_heading=0;
  }
  else if (m_imu_heading<0)
  {
    m_imu_heading=360;
  }
  m_Comms.Notify("IMU_HEADING", m_imu_heading);
  m_t_ant=m_t_now;
  m_counter=0;
  // }
  AppCastingMOOSApp::PostReport();
  return(true);
}

//---------------------------------------------------------
// Procedure: OnStartUp()
//            happens before connection is open

bool SimIMU::OnStartUp()
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

void SimIMU::registerVariables()
{
  AppCastingMOOSApp::RegisterVariables();
  Register("REAL_ROT", 0);
  Register("DB_UPTIME", 0);	
}


//------------------------------------------------------------
// Procedure: buildReport()

bool SimIMU::buildReport() 
{
  m_msgs << "============================================" << endl;
  m_msgs << "File:                                       " << endl;
  m_msgs << "============================================" << endl;

  ACTable actab(5);
  actab << "t_ant | t_now | dt | m_real_rot | m_imu_heading";
  actab.addHeaderLines();
  actab << m_t_ant << m_t_now << m_dt << m_real_rot << m_imu_heading;
  m_msgs << actab.getFormattedString();

  return(true);
}




