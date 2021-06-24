/************************************************************/
/*    NAME: lhscaldas                                              */
/*    ORGN: MIT, Cambridge MA                               */
/*    FILE: Sensor.h                                          */
/*    DATE: December 29th, 1963                             */
/************************************************************/

#ifndef Sensor_HEADER
#define Sensor_HEADER

#include "MOOS/libMOOS/Thirdparty/AppCasting/AppCastingMOOSApp.h"

class Sensor : public AppCastingMOOSApp
{
 public:
   Sensor();
   ~Sensor();

 protected: // Standard MOOSApp functions to overload  
   bool OnNewMail(MOOSMSG_LIST &NewMail);
   bool Iterate();
   bool OnConnectToServer();
   bool OnStartUp();

 protected: // Standard AppCastingMOOSApp function to overload 
   bool buildReport();

 protected:
   void registerVariables();

 protected:
   double m_dvl_speed;
   double m_imu_x;
   double m_imu_y;
   double m_imu_speed;
   double m_imu_heading;
   double m_gps_x;
   double m_gps_y;
   double m_gps_speed;
   double m_gyro_heading;


   double m_sensor_speed;
   double m_sensor_x;
   double m_sensor_y;
   double m_sensor_heading;

   double m_w_dvl_speed;
   double m_w_imu_speed;
   double m_w_gps_speed;
   double m_w_imu_pos;
   double m_w_gps_pos;
   double m_w_imu_hdg;
   double m_w_gyro_hdg;

 private: // Configuration variables

 private: // State variables
};

#endif 
