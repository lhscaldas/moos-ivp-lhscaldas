#--------------------------------------------------------
# The CMakeLists.txt for:                       pSimIMU
# Author(s):                              lhscaldas
#--------------------------------------------------------

SET(SRC
  SimIMU.cpp
  SimIMU_Info.cpp
  main.cpp
)

ADD_EXECUTABLE(pSimIMU ${SRC})

TARGET_LINK_LIBRARIES(pSimIMU
   ${MOOS_LIBRARIES}
   apputil
   mbutil
   m
   pthread)

