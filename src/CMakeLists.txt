##############################################################################
# FILE:        moos-ivp-extend/src/CMakeLists.txt
# DATE:        2010/09/07
#              2020/05/09 minor mods
# DESCRIPTION: CMakeLists.txt file for the moos-ivp-extend source directory
##############################################################################

#---------------------------------------------------------------------
#  Build the Libraries
#---------------------------------------------------------------------

SET(IVP_NON_GUI_LIBS
   lib_behaviors
   lib_behaviors-marine
   lib_behaviors-colregs
   lib_bhvutil
   lib_genutil
   lib_geometry
   lib_helmivp
   lib_ivpbuild
   lib_ivpcore
   lib_ivpsolve
   lib_logic
   lib_evalutil
   lib_encounters
   lib_apputil
   lib_realm
   lib_contacts
   lib_obstacles
   lib_ufield
   lib_logutils
   lib_mbutil
   lib_manifest
   )

IF (${WIN32})
  SET(TIFF_SRC_DIR lib_tiff/tiff-3.8.2/libtiff)
  # For Windows use the preconfigure headers provided by libtiff
  # Use CONFIGURE_FILE to copy the supplied files to their approtiate
  # locations.
  CONFIGURE_FILE(${TIFF_SRC_DIR}/tif_config.h.vc 
    ${TIFF_SRC_DIR}/tif_config.h COPYONLY)
  CONFIGURE_FILE(${TIFF_SRC_DIR}/tiffconf.h.vc 
    ${TIFF_SRC_DIR}/tiffconf.h COPYONLY)
  # Add the libtiff headers directory
  INCLUDE_DIRECTORIES( AFTER ${TIFF_SRC_DIR} )
  # Set the IVP GUI libraries for Windows
  SET(IVP_GUI_LIBS lib_ipfview lib_marineview lib_tiff lib_zaicview lib_ucommand)
  
ELSE (${WIN32})
  # Linux, Mac
  SET(IVP_GUI_LIBS lib_ipfview lib_marineview lib_zaicview lib_ucommand)
ENDIF (${WIN32})

#============================================================================
# Add the libraries in the current directory to the include path
#============================================================================
FILE(GLOB LOCAL_LIBRARY_DIRS ./lib_*)
INCLUDE_DIRECTORIES(${LOCAL_LIBRARY_DIRS})

#============================================================================
# List the subdirectories to build...
#============================================================================
ADD_SUBDIRECTORY(lib_behaviors-test)
ADD_SUBDIRECTORY(lib_mbutil)
ADD_SUBDIRECTORY(pExampleApp)
ADD_SUBDIRECTORY(pXRelayTest)
ADD_SUBDIRECTORY(pSimIMU)
ADD_SUBDIRECTORY(pSimGPS)
ADD_SUBDIRECTORY(pSimDVL)
ADD_SUBDIRECTORY(pSimGyro)
ADD_SUBDIRECTORY(uSimRadar)
ADD_SUBDIRECTORY(uSimLidar)
ADD_SUBDIRECTORY(pTrajectPID)
ADD_SUBDIRECTORY(pSensor)
ADD_SUBDIRECTORY(iRemoteMod)

##############################################################################
#                           END of CMakeLists.txt
##############################################################################
