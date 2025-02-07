/************************************************************/
/*    NAME: lhscaldas                                       */
/*    ORGN: USP, São Paulo SP                               */
/*    FILE: SimIMU.h                                        */
/*    DATE: 14/06/2021                                      */
/************************************************************/

#ifndef SimIMU_HEADER
#define SimIMU_HEADER

#include "MOOS/libMOOS/Thirdparty/AppCasting/AppCastingMOOSApp.h"

class SimIMU : public AppCastingMOOSApp
{
 public:
   SimIMU();
   ~SimIMU();

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
   double m_real_rot;
   double m_dt;
   double m_t_ant;
   double m_t_now;
   double m_imu_heading;
   double m_real_accx;
   double m_real_accy;
   double m_imu_vx;
   double m_imu_vy;
   double m_imu_speed;
   double m_imu_x;
   double m_imu_y;
   double m_calib_x;
   double m_calib_y;
   double m_calib_heading;

 private: // Configuration variables

 private: // State variables
};

#endif 
