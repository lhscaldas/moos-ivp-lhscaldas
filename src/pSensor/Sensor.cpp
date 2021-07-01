/************************************************************/
/*    NAME: lhscaldas                                              */
/*    ORGN: MIT, Cambridge MA                               */
/*    FILE: Sensor.cpp                                        */
/*    DATE: December 29th, 1963                             */
/************************************************************/

#include <iterator>
#include "MBUtils.h"
#include "ACTable.h"
#include "Sensor.h"

using namespace std;

//---------------------------------------------------------
// Constructor

Sensor::Sensor()
{
  m_dvl_speed=0;
  m_imu_x=0;
  m_imu_y=0;
  m_imu_speed=0;
  m_imu_heading=0;
  m_gps_x=0;
  m_gps_y=0;
  m_gps_speed=0;
  m_gyro_heading=0;

  m_sensor_speed=0;
  m_sensor_x=0;
  m_sensor_y=0;
  m_sensor_heading=0;
}

//---------------------------------------------------------
// Destructor

Sensor::~Sensor()
{
}

//---------------------------------------------------------
// Procedure: OnNewMail

bool Sensor::OnNewMail(MOOSMSG_LIST &NewMail)
{
  AppCastingMOOSApp::OnNewMail(NewMail);

  MOOSMSG_LIST::iterator p;
  for(p=NewMail.begin(); p!=NewMail.end(); p++) {
    CMOOSMsg &msg = *p;
    if (msg.GetKey() == "DVL_SPEED" && msg.IsDouble()) {
      m_dvl_speed = msg.GetDouble();
    }
    else if (msg.GetKey() == "GPS_X" && msg.IsDouble()) {
      m_gps_x = msg.GetDouble();
    }
    else if (msg.GetKey() == "GPS_Y" && msg.IsDouble()) {
      m_gps_y = msg.GetDouble();
    }
    else if (msg.GetKey() == "GPS_SPEED" && msg.IsDouble()) {
      m_gps_speed = msg.GetDouble();
    }
    else if (msg.GetKey() == "GYRO_HEADING" && msg.IsDouble()) {
      m_gyro_heading = msg.GetDouble();
    }
    else if (msg.GetKey() == "IMU_SPEED" && msg.IsDouble()) {
      m_imu_speed = msg.GetDouble();
    }
    else if (msg.GetKey() == "IMU_HEADING" && msg.IsDouble()) {
      m_imu_heading = msg.GetDouble();
    }
    else if (msg.GetKey() == "IMU_X" && msg.IsDouble()) {
      m_imu_x = msg.GetDouble();
    }
    else if (msg.GetKey() == "IMU_Y" && msg.IsDouble()) {
      m_imu_y = msg.GetDouble();
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

bool Sensor::OnConnectToServer()
{
   registerVariables();
   return(true);
}

//---------------------------------------------------------
// Procedure: Iterate()
//            happens AppTick times per second

bool Sensor::Iterate()
{
  AppCastingMOOSApp::Iterate();
  // m_sensor_speed=m_dvl_speed;
  // m_sensor_x=m_gps_x;
  // m_sensor_y=m_gps_y;
  // m_sensor_heading=m_gyro_heading;
  m_sensor_speed=m_w_dvl_speed*m_dvl_speed+m_w_imu_speed*m_imu_speed+m_w_gps_speed*m_gps_speed;
  m_sensor_x=m_w_gps_pos*m_gps_x+m_w_imu_pos*m_imu_x;
  m_sensor_y=m_w_gps_pos*m_gps_y+m_w_imu_pos*m_imu_y;
  m_sensor_heading=m_w_gyro_hdg*m_gyro_heading+m_w_imu_hdg*m_imu_heading;
  m_Comms.Notify("NAV_SPEED", m_sensor_speed);
  m_Comms.Notify("NAV_X", m_sensor_x);
  m_Comms.Notify("NAV_Y", m_sensor_y);
  m_Comms.Notify("NAV_HEADING", m_sensor_heading);
  AppCastingMOOSApp::PostReport();
  return(true);
}

//---------------------------------------------------------
// Procedure: OnStartUp()
//            happens before connection is open

bool Sensor::OnStartUp()
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
    string param = toupper(biteStringX(line, '='));
    string value = tolower(line);
    double dval  = atof(value.c_str());

    bool handled = false;
    if(param == "W_DVL_SPEED") {
      m_w_dvl_speed=dval;
      handled = true;
    }
    else if(param == "W_IMU_SPEED") {
      m_w_imu_speed=dval;
      handled = true;
    }
    else if(param == "W_GPS_SPEED") {
      m_w_gps_speed=dval;
      handled = true;
    }
    else if(param == "W_IMU_POS") {
      m_w_imu_pos=dval;
      handled = true;
    }
    else if(param == "W_GPS_POS") {
      m_w_gps_pos=dval;
      handled = true;
    }
    else if(param == "W_IMU_HDG") {
      m_w_imu_hdg=dval;
      handled = true;
    }
    else if(param == "W_GYRO_HDG") {
      m_w_gyro_hdg=dval;
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

void Sensor::registerVariables()
{
  AppCastingMOOSApp::RegisterVariables();
  Register("DVL_SPEED", 0);
  Register("GPS_X", 0);
  Register("GPS_Y", 0);
  Register("GPS_SPEED", 0);
  Register("GYRO_HEADING", 0);
  Register("IMU_X", 0);
  Register("IMU_Y", 0);
  Register("IMU_SPEED", 0);
  Register("IMU_HEADING", 0);
}


//------------------------------------------------------------
// Procedure: buildReport()

bool Sensor::buildReport() 
{
  m_msgs << "============================================" << endl;
  m_msgs << "File:                                       " << endl;
  m_msgs << "============================================" << endl;

  ACTable actab(6);
  actab << " | GPS | DVL | Gyro | IMU | NAV";
  actab.addHeaderLines();
  actab << "x" << m_gps_x << " " << " " << m_imu_x << m_sensor_x;
  actab << "y" << m_gps_y << " " << " " << m_imu_y << m_sensor_y;
  actab << "speed" << m_gps_speed << m_dvl_speed << " " << m_imu_speed << m_sensor_speed;
  actab << "hdg" << " " << m_gyro_heading << " " << m_imu_heading << m_sensor_heading;
  m_msgs << actab.getFormattedString();

  return(true);
}




