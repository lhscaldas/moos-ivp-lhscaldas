/************************************************************/
/*    NAME: lhscaldas                                              */
/*    ORGN: MIT, Cambridge MA                               */
/*    FILE: TrajectPID.h                                          */
/*    DATE: December 29th, 1963                             */
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

 private: // Configuration variables

 private: // State variables
};

#endif 
