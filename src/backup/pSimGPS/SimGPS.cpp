/************************************************************/
/*    NAME: lhscaldas                                       */
/*    ORGN: USP, São Paulo SP                               */
/*    FILE: SimGPS.cpp                                      */
/*    DATE: 14/06/2021                                      */
/************************************************************/

#include <iterator>
#include "MBUtils.h"
#include "ACTable.h"
#include "SimGPS.h"
#include <math.h>

using namespace std;

//---------------------------------------------------------
// Constructor

SimGPS::SimGPS()
{
   m_real_x=0;
   m_gps_x=0;
   m_real_y=0;
   m_gps_y=0;
   m_nav_lat=0;
   m_nav_lon=0;

   m_xant=0;
   m_yant=0;
   m_vx=0;
   m_vy=0;
   m_t_now=0;
   m_t_ant=0;
   m_dt=0;
   m_gps_speed=0;
   m_counter=0;
}

//---------------------------------------------------------
// Destructor

SimGPS::~SimGPS()
{
}

//---------------------------------------------------------
// Procedure: OnNewMail

bool SimGPS::OnNewMail(MOOSMSG_LIST &NewMail)
{
  AppCastingMOOSApp::OnNewMail(NewMail);

  MOOSMSG_LIST::iterator p;
  for(p=NewMail.begin(); p!=NewMail.end(); p++) {
    CMOOSMsg &msg = *p;
    if (msg.GetKey() == "REAL_X" && msg.IsDouble()) {
      m_real_x = msg.GetDouble();
    } else if (msg.GetKey() == "REAL_Y" && msg.IsDouble()) {
      m_real_y = msg.GetDouble();
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

bool SimGPS::OnConnectToServer()
{
   registerVariables();
   return(true);
}

//---------------------------------------------------------
// Procedure: Iterate()
//            happens AppTick times per second

bool SimGPS::Iterate()
{
  AppCastingMOOSApp::Iterate();
  m_t_now=MOOSTime();

  m_gps_x=m_real_x;
  m_gps_y=m_real_y;
  m_Comms.Notify("GPS_X", m_gps_x);
  m_Comms.Notify("GPS_Y", m_gps_y);

  m_geodesy.LocalGrid2LatLong(m_gps_x, m_gps_y, m_nav_lat, m_nav_lon);
  m_Comms.Notify("NAV_LAT", m_nav_lat);
  m_Comms.Notify("NAV_LONG", m_nav_lon);
  m_Comms.Notify("REAL_LAT", m_nav_lat);
  m_Comms.Notify("REAL_LONG", m_nav_lon);
  
  m_counter++;
  if(m_counter==40){
    m_dt = (m_t_now - m_t_ant);
    m_vx= (m_gps_x-m_xant)/m_dt;
    m_vy= (m_gps_y-m_yant)/m_dt;
    m_gps_speed=sqrt(m_vx*m_vx + m_vy*m_vy);
    m_Comms.Notify("GPS_SPEED", m_gps_speed);
    m_xant=m_gps_x;
    m_yant=m_gps_y;
    m_t_ant=m_t_now;
    m_counter=0;
  }

  AppCastingMOOSApp::PostReport();
  return(true);
}

//---------------------------------------------------------
// Procedure: OnStartUp()
//            happens before connection is open

bool SimGPS::OnStartUp()
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

    // look for latitude, longitude global variables
    double latOrigin, longOrigin;
    m_MissionReader.GetValue("LatOrigin", latOrigin);
    m_MissionReader.GetValue("LongOrigin", longOrigin);
    m_geodesy.Initialise(latOrigin, longOrigin);

  }
  m_t_ant=MOOSTime();
  m_t_now=MOOSTime();
  registerVariables();
  return(true);
}

//---------------------------------------------------------
// Procedure: registerVariables

void SimGPS::registerVariables()
{
  AppCastingMOOSApp::RegisterVariables();
  Register("REAL_X", 0);
  Register("REAL_Y", 0);
}


//------------------------------------------------------------
// Procedure: buildReport()

bool SimGPS::buildReport() 
{
  m_msgs << "============================================" << endl;
  m_msgs << "File:                                       " << endl;
  m_msgs << "============================================" << endl;

  ACTable actab(6);
  actab << "t_ant | t_now | dt | vx | vy | gps_speed";
  actab.addHeaderLines();
  actab << m_t_ant << m_t_now << m_dt << m_vx << m_vy << m_gps_speed;
  m_msgs << actab.getFormattedString();

  return(true);
}




