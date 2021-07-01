#--------------------------------------------------------
# The CMakeLists.txt for:                       pSimDVL
# Author(s):                              lhscaldas
#--------------------------------------------------------

SET(SRC
  SimDVL.cpp
  SimDVL_Info.cpp
  main.cpp
)

ADD_EXECUTABLE(pSimDVL ${SRC})

TARGET_LINK_LIBRARIES(pSimDVL
   ${MOOS_LIBRARIES}
   apputil
   mbutil
   m
   pthread)

