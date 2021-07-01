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

//---------------------------------------------------------
// Constructor

SimIMU::SimIMU()
{
   m_real_speed=0;
   m_real_heading=0;
   m_real_x=0;
   m_real_y=0;
   
   m_imu_speed=0;
   m_imu_heading=0;
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
    if (msg.GetKey() == "REAL_X" && msg.IsDouble()) {
      m_real_x = msg.GetDouble();
    } else if (msg.GetKey() == "REAL_Y" && msg.IsDouble()) {
      m_real_y = msg.GetDouble();
    } else if (msg.GetKey() == "REAL_HEADING" && msg.IsDouble()) {
      m_real_heading = msg.GetDouble();
    } else if (msg.GetKey() == "REAL_SPEED" && msg.IsDouble()) {
      m_real_speed = msg.GetDouble();
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

  m_imu_heading = m_real_heading;
  m_imu_speed = m_real_speed;
  m_imu_x = m_real_x;
  m_imu_y = m_real_y;
  
  m_Comms.Notify("IMU_HEADING", m_imu_heading);
  m_Comms.Notify("IMU_SPEED", m_imu_speed);
  m_Comms.Notify("IMU_X", m_imu_x);
  m_Comms.Notify("IMU_Y", m_imu_y);

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
  if(!m_MissionReader.GetConfiguration("pSimIMU", sParams))
    reportConfigWarning("No config block found for pSimIMU");
  
  
  registerVariables();
 
  return(true);
}

//---------------------------------------------------------
// Procedure: registerVariables

void SimIMU::registerVariables()
{
  AppCastingMOOSApp::RegisterVariables();
  Register("REAL_X", 0);
  Register("REAL_Y", 0);
  Register("REAL_SPEED", 0);
  Register("REAL_HEADING", 0);
}


//------------------------------------------------------------
// Procedure: buildReport()

bool SimIMU::buildReport() 
{
  m_msgs << "============================================" << endl;
  m_msgs << "File:                                       " << endl;
  m_msgs << "============================================" << endl;

  // ACTable actab(6);
  // actab << "t_ant | t_now | dt | m_real_rot | m_imu_heading | app_name";
  // actab.addHeaderLines();
  // actab << m_t_ant << m_t_now << m_dt << m_real_rot << m_imu_heading << GetAppName();
  // m_msgs << actab.getFormattedString();

  return(true);
}




