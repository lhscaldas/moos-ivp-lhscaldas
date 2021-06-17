#--------------------------------------------------------
# The CMakeLists.txt for:                       pTrajectPID
# Author(s):                              lhscaldas
#--------------------------------------------------------

SET(SRC
  TrajectPID.cpp
  TrajectPID_Info.cpp
  main.cpp
)

ADD_EXECUTABLE(pTrajectPID ${SRC})

TARGET_LINK_LIBRARIES(pTrajectPID
   ${MOOS_LIBRARIES}
   apputil
   mbutil
   m
   pthread)

