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
  m_gps_x=0;
  m_gps_y=0;
  m_imu_heading=0;
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
    else if (msg.GetKey() == "IMU_HEADING" && msg.IsDouble()) {
      m_imu_heading = msg.GetDouble();
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
  m_sensor_speed=m_dvl_speed;
  m_sensor_x=m_gps_x;
  m_sensor_y=m_gps_y;
  m_sensor_heading=m_imu_heading;
  m_Comms.Notify("SENSOR_SPEED", m_sensor_speed);
  m_Comms.Notify("SENSOR_X", m_sensor_x);
  m_Comms.Notify("SENSOR_Y", m_sensor_y);
  m_Comms.Notify("SENSOR_HEADING", m_sensor_heading);
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

void Sensor::registerVariables()
{
  AppCastingMOOSApp::RegisterVariables();
  Register("DVL_SPEED", 0);
  Register("GPS_X", 0);
  Register("GPS_Y", 0);
  Register("IMU_HEADING", 0);
}


//------------------------------------------------------------
// Procedure: buildReport()

bool Sensor::buildReport() 
{
  m_msgs << "============================================" << endl;
  m_msgs << "File:                                       " << endl;
  m_msgs << "============================================" << endl;

  ACTable actab(4);
  actab << "Alpha | Bravo | Charlie | Delta";
  actab.addHeaderLines();
  actab << "one" << "two" << "three" << "four";
  m_msgs << actab.getFormattedString();

  return(true);
}




