#--------------------------------------------------------
# The CMakeLists.txt for:                       pSimGyro
# Author(s):                              lhscaldas
#--------------------------------------------------------

SET(SRC
  SimGyro.cpp
  SimGyro_Info.cpp
  main.cpp
)

ADD_EXECUTABLE(pSimGyro ${SRC})

TARGET_LINK_LIBRARIES(pSimGyro
   ${MOOS_LIBRARIES}
   apputil
   mbutil
   m
   pthread)

