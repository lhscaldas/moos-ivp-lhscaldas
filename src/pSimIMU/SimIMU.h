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
   double m_real_heading;
   double m_nav_heading;

 private: // Configuration variables

 private: // State variables
};

#endif 
