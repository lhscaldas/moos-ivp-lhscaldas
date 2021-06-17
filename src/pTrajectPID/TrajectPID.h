/************************************************************/
/*    NAME: lhscaldas                                       */
/*    ORGN: USP, São Paulo SP                               */
/*    FILE: TrajectPID.h                                    */
/*    DATE: 17/06/2021                                      */
/************************************************************/

#ifndef TrajectPID_HEADER
#define TrajectPID_HEADER

#include "MOOS/libMOOS/Thirdparty/AppCasting/AppCastingMOOSApp.h"

class TrajectPID : public AppCastingMOOSApp
{
 public:
   TrajectPID();
   ~TrajectPID();

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
   void speedPID(double y);
   void coursePID(double y);
   double m_desired_speed;
   double m_desired_heading;
   double m_nav_speed;
   double m_nav_heading;
   double m_desired_rudder;
   double m_desired_rotation;
   double m_speed_kp;
   double m_speed_ki;
   double m_speed_kd;
   double m_course_kp;
   double m_course_ki;
   double m_course_kd;
   double m_dt;
   double m_speed_int_err;
   double m_speed_prev_err;
   double m_speed_setpoint;
   double m_speed_maxout;
   double m_speed_saturated;
   double m_course_int_err;
   double m_course_prev_err;
   double m_course_setpoint;
   double m_course_maxout;
   double m_course_saturated;
   



 private: // Configuration variables

 private: // State variables
};

#endif 
