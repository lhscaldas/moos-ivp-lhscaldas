# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.18

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/lhscaldas/moos-ivp-lhscaldas

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/lhscaldas/moos-ivp-lhscaldas/build

# Include any dependencies generated for this target.
include src/pSimGPS/CMakeFiles/pSimGPS.dir/depend.make

# Include the progress variables for this target.
include src/pSimGPS/CMakeFiles/pSimGPS.dir/progress.make

# Include the compile flags for this target's objects.
include src/pSimGPS/CMakeFiles/pSimGPS.dir/flags.make

src/pSimGPS/CMakeFiles/pSimGPS.dir/SimGPS.cpp.o: src/pSimGPS/CMakeFiles/pSimGPS.dir/flags.make
src/pSimGPS/CMakeFiles/pSimGPS.dir/SimGPS.cpp.o: ../src/pSimGPS/SimGPS.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/lhscaldas/moos-ivp-lhscaldas/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/pSimGPS/CMakeFiles/pSimGPS.dir/SimGPS.cpp.o"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGPS && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/pSimGPS.dir/SimGPS.cpp.o -c /home/lhscaldas/moos-ivp-lhscaldas/src/pSimGPS/SimGPS.cpp

src/pSimGPS/CMakeFiles/pSimGPS.dir/SimGPS.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/pSimGPS.dir/SimGPS.cpp.i"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGPS && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/lhscaldas/moos-ivp-lhscaldas/src/pSimGPS/SimGPS.cpp > CMakeFiles/pSimGPS.dir/SimGPS.cpp.i

src/pSimGPS/CMakeFiles/pSimGPS.dir/SimGPS.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/pSimGPS.dir/SimGPS.cpp.s"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGPS && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/lhscaldas/moos-ivp-lhscaldas/src/pSimGPS/SimGPS.cpp -o CMakeFiles/pSimGPS.dir/SimGPS.cpp.s

src/pSimGPS/CMakeFiles/pSimGPS.dir/MOOSGeodesy.cpp.o: src/pSimGPS/CMakeFiles/pSimGPS.dir/flags.make
src/pSimGPS/CMakeFiles/pSimGPS.dir/MOOSGeodesy.cpp.o: ../src/pSimGPS/MOOSGeodesy.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/lhscaldas/moos-ivp-lhscaldas/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object src/pSimGPS/CMakeFiles/pSimGPS.dir/MOOSGeodesy.cpp.o"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGPS && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/pSimGPS.dir/MOOSGeodesy.cpp.o -c /home/lhscaldas/moos-ivp-lhscaldas/src/pSimGPS/MOOSGeodesy.cpp

src/pSimGPS/CMakeFiles/pSimGPS.dir/MOOSGeodesy.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/pSimGPS.dir/MOOSGeodesy.cpp.i"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGPS && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/lhscaldas/moos-ivp-lhscaldas/src/pSimGPS/MOOSGeodesy.cpp > CMakeFiles/pSimGPS.dir/MOOSGeodesy.cpp.i

src/pSimGPS/CMakeFiles/pSimGPS.dir/MOOSGeodesy.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/pSimGPS.dir/MOOSGeodesy.cpp.s"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGPS && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/lhscaldas/moos-ivp-lhscaldas/src/pSimGPS/MOOSGeodesy.cpp -o CMakeFiles/pSimGPS.dir/MOOSGeodesy.cpp.s

src/pSimGPS/CMakeFiles/pSimGPS.dir/SimGPS_Info.cpp.o: src/pSimGPS/CMakeFiles/pSimGPS.dir/flags.make
src/pSimGPS/CMakeFiles/pSimGPS.dir/SimGPS_Info.cpp.o: ../src/pSimGPS/SimGPS_Info.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/lhscaldas/moos-ivp-lhscaldas/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object src/pSimGPS/CMakeFiles/pSimGPS.dir/SimGPS_Info.cpp.o"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGPS && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/pSimGPS.dir/SimGPS_Info.cpp.o -c /home/lhscaldas/moos-ivp-lhscaldas/src/pSimGPS/SimGPS_Info.cpp

src/pSimGPS/CMakeFiles/pSimGPS.dir/SimGPS_Info.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/pSimGPS.dir/SimGPS_Info.cpp.i"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGPS && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/lhscaldas/moos-ivp-lhscaldas/src/pSimGPS/SimGPS_Info.cpp > CMakeFiles/pSimGPS.dir/SimGPS_Info.cpp.i

src/pSimGPS/CMakeFiles/pSimGPS.dir/SimGPS_Info.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/pSimGPS.dir/SimGPS_Info.cpp.s"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGPS && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/lhscaldas/moos-ivp-lhscaldas/src/pSimGPS/SimGPS_Info.cpp -o CMakeFiles/pSimGPS.dir/SimGPS_Info.cpp.s

src/pSimGPS/CMakeFiles/pSimGPS.dir/main.cpp.o: src/pSimGPS/CMakeFiles/pSimGPS.dir/flags.make
src/pSimGPS/CMakeFiles/pSimGPS.dir/main.cpp.o: ../src/pSimGPS/main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/lhscaldas/moos-ivp-lhscaldas/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object src/pSimGPS/CMakeFiles/pSimGPS.dir/main.cpp.o"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGPS && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/pSimGPS.dir/main.cpp.o -c /home/lhscaldas/moos-ivp-lhscaldas/src/pSimGPS/main.cpp

src/pSimGPS/CMakeFiles/pSimGPS.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/pSimGPS.dir/main.cpp.i"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGPS && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/lhscaldas/moos-ivp-lhscaldas/src/pSimGPS/main.cpp > CMakeFiles/pSimGPS.dir/main.cpp.i

src/pSimGPS/CMakeFiles/pSimGPS.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/pSimGPS.dir/main.cpp.s"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGPS && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/lhscaldas/moos-ivp-lhscaldas/src/pSimGPS/main.cpp -o CMakeFiles/pSimGPS.dir/main.cpp.s

# Object files for target pSimGPS
pSimGPS_OBJECTS = \
"CMakeFiles/pSimGPS.dir/SimGPS.cpp.o" \
"CMakeFiles/pSimGPS.dir/MOOSGeodesy.cpp.o" \
"CMakeFiles/pSimGPS.dir/SimGPS_Info.cpp.o" \
"CMakeFiles/pSimGPS.dir/main.cpp.o"

# External object files for target pSimGPS
pSimGPS_EXTERNAL_OBJECTS =

../bin/pSimGPS: src/pSimGPS/CMakeFiles/pSimGPS.dir/SimGPS.cpp.o
../bin/pSimGPS: src/pSimGPS/CMakeFiles/pSimGPS.dir/MOOSGeodesy.cpp.o
../bin/pSimGPS: src/pSimGPS/CMakeFiles/pSimGPS.dir/SimGPS_Info.cpp.o
../bin/pSimGPS: src/pSimGPS/CMakeFiles/pSimGPS.dir/main.cpp.o
../bin/pSimGPS: src/pSimGPS/CMakeFiles/pSimGPS.dir/build.make
../bin/pSimGPS: /home/lhscaldas/moos-ivp/build/MOOS/MOOSCore/lib/libMOOS.a
../bin/pSimGPS: /lib/libmbutil.a
../bin/pSimGPS: src/pSimGPS/CMakeFiles/pSimGPS.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/lhscaldas/moos-ivp-lhscaldas/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Linking CXX executable ../../../bin/pSimGPS"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGPS && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/pSimGPS.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/pSimGPS/CMakeFiles/pSimGPS.dir/build: ../bin/pSimGPS

.PHONY : src/pSimGPS/CMakeFiles/pSimGPS.dir/build

src/pSimGPS/CMakeFiles/pSimGPS.dir/clean:
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGPS && $(CMAKE_COMMAND) -P CMakeFiles/pSimGPS.dir/cmake_clean.cmake
.PHONY : src/pSimGPS/CMakeFiles/pSimGPS.dir/clean

src/pSimGPS/CMakeFiles/pSimGPS.dir/depend:
	cd /home/lhscaldas/moos-ivp-lhscaldas/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/lhscaldas/moos-ivp-lhscaldas /home/lhscaldas/moos-ivp-lhscaldas/src/pSimGPS /home/lhscaldas/moos-ivp-lhscaldas/build /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGPS /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGPS/CMakeFiles/pSimGPS.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/pSimGPS/CMakeFiles/pSimGPS.dir/depend

