#--------------------------------------------------------
# The CMakeLists.txt for:                       pSensor
# Author(s):                              lhscaldas
#--------------------------------------------------------

SET(SRC
  Sensor.cpp
  Sensor_Info.cpp
  main.cpp
)

ADD_EXECUTABLE(pSensor ${SRC})

TARGET_LINK_LIBRARIES(pSensor
   ${MOOS_LIBRARIES}
   apputil
   mbutil
   m
   pthread)

