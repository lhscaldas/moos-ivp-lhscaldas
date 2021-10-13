#--------------------------------------------------------
# The CMakeLists.txt for:                  pContactMgrV20
# Author(s):                                Mike Benjamin
#--------------------------------------------------------

FILE(GLOB SRC
     ContactMgrV20.cpp
     ContactMgrV20_Info.cpp
     ContactRecord.cpp
     CMAlert.cpp
     RangeMark.cpp
     PlatformAlertRecord.cpp
     main.cpp
     MOOSGeodesy.cpp
)

ADD_EXECUTABLE(pContactMgrMod ${SRC})

# Set System Specific Libraries
if (${WIN32})
  SET(SYSTEM_LIBS wsock32)
else (${WIN32})
  SET(SYSTEM_LIBS m pthread)
endif (${WIN32})


TARGET_LINK_LIBRARIES(pContactMgrMod
   ${MOOS_LIBRARIES}
   ${MOOSGeodesy_LIBRARIES}
   mbutil
   bhvutil
   apputil
   geometry
   contacts
   ${SYSTEM_LIBS}
)

