# Install script for directory: /home/lhscaldas/moos-ivp-lhscaldas/src

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "None")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/lhscaldas/moos-ivp-lhscaldas/build/src/lib_behaviors-test/cmake_install.cmake")
  include("/home/lhscaldas/moos-ivp-lhscaldas/build/src/lib_mbutil/cmake_install.cmake")
  include("/home/lhscaldas/moos-ivp-lhscaldas/build/src/pExampleApp/cmake_install.cmake")
  include("/home/lhscaldas/moos-ivp-lhscaldas/build/src/pXRelayTest/cmake_install.cmake")
  include("/home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimIMU/cmake_install.cmake")
  include("/home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGPS/cmake_install.cmake")
  include("/home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimDVL/cmake_install.cmake")
  include("/home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGyro/cmake_install.cmake")
  include("/home/lhscaldas/moos-ivp-lhscaldas/build/src/uSimRadar/cmake_install.cmake")
  include("/home/lhscaldas/moos-ivp-lhscaldas/build/src/pContactMgrMod/cmake_install.cmake")
  include("/home/lhscaldas/moos-ivp-lhscaldas/build/src/uSimLidar/cmake_install.cmake")
  include("/home/lhscaldas/moos-ivp-lhscaldas/build/src/pTrajectPID/cmake_install.cmake")
  include("/home/lhscaldas/moos-ivp-lhscaldas/build/src/pSensor/cmake_install.cmake")
  include("/home/lhscaldas/moos-ivp-lhscaldas/build/src/iRemoteMod/cmake_install.cmake")

endif()

