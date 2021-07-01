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
#define DEG2RAD M_PI/180

//---------------------------------------------------------
// Constructor

SimIMU::SimIMU()
{
   m_dt=0;
   m_t_ant=0;
   m_t_now=0;

   m_imu_heading=0;
   m_real_rot=0;

   m_real_accx=0;
   m_real_accy=0;
   m_imu_vx=0;
   m_imu_vy=0;
   m_imu_speed=0;

   m_imu_x=0;
   m_imu_y=0;
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
    } else if (msg.GetKey() == "REAL_ACC_X" && msg.IsDouble()) {
      m_real_accx = msg.GetDouble();
    } else if (msg.GetKey() == "REAL_ACC_Y" && msg.IsDouble()) {
      m_real_accy = msg.GetDouble();
    } else if (msg.GetKey() == "GPS_X" && msg.IsDouble()) {
      m_calib_x = msg.GetDouble();
    } else if (msg.GetKey() == "GPS_Y" && msg.IsDouble()) {
      m_calib_y = msg.GetDouble();
    } else if (msg.GetKey() == "GYRO_HEADING" && msg.IsDouble()) {
      m_calib_heading = msg.GetDouble();
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
  m_t_now = MOOSTime();
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

  m_imu_vx+= m_real_accx*m_dt;
  m_imu_vy+= m_real_accy*m_dt;
  m_imu_speed = sqrt(m_imu_vx*m_imu_vx + m_imu_vy*m_imu_vy);
  m_Comms.Notify("IMU_SPEED", m_imu_speed);

  m_imu_x+= m_imu_vx*m_dt*cos(DEG2RAD*(90-m_imu_heading)) + m_imu_vy*m_dt*sin(DEG2RAD*(90-m_imu_heading));
  m_imu_y+= -m_imu_vx*m_dt*sin(DEG2RAD*(90-m_imu_heading)) + m_imu_vy*m_dt*cos(DEG2RAD*(90-m_imu_heading));
  m_Comms.Notify("IMU_X", m_imu_x);
  m_Comms.Notify("IMU_Y", m_imu_y);

  m_t_ant=m_t_now;

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
  if(!m_MissionReader.GetConfiguration("iPydyna", sParams))
    reportConfigWarning("No config block found for iPydyna");

  STRING_LIST::iterator p;
  for(p=sParams.begin(); p!=sParams.end(); p++) {
    string orig  = *p;
    string line  = *p;
    string param = toupper(biteStringX(line, '='));
    string value = tolower(line);
    double dval  = atof(value.c_str());

    bool handled = false;
    if(param == "START_X") {
      m_imu_x=dval;
      handled = true;
    }
    else if(param == "START_Y") {
      m_imu_y=dval;
      handled = true;
    }
    else if(param == "START_HEADING") {
      m_imu_heading=dval;
      handled = true;
    }

    if(!handled)
      reportUnhandledConfigWarning(orig);

  }
  m_t_ant=MOOSTime();
  m_t_now=MOOSTime();
  
  registerVariables();
 
  return(true);
}

//---------------------------------------------------------
// Procedure: registerVariables

void SimIMU::registerVariables()
{
  AppCastingMOOSApp::RegisterVariables();
  Register("REAL_ROT", 0);
  Register("REAL_ACC_X", 0);
  Register("REAL_ACC_Y", 0);
  Register("GYRO_HEADING", 0);
  Register("GPS_X", 0);
  Register("GPS_Y", 0);
}


//------------------------------------------------------------
// Procedure: buildReport()

bool SimIMU::buildReport() 
{
  m_msgs << "============================================" << endl;
  m_msgs << "File:                                       " << endl;
  m_msgs << "============================================" << endl;

  ACTable actab(6);
  actab << "t_ant | t_now | dt | m_real_rot | m_imu_heading | app_name";
  actab.addHeaderLines();
  actab << m_t_ant << m_t_now << m_dt << m_real_rot << m_imu_heading << GetAppName();
  m_msgs << actab.getFormattedString();

  return(true);
}




