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
include src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/depend.make

# Include the progress variables for this target.
include src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/progress.make

# Include the compile flags for this target's objects.
include src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/flags.make

src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/CMAlert.cpp.o: src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/flags.make
src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/CMAlert.cpp.o: ../src/pContactMgrMod/CMAlert.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/lhscaldas/moos-ivp-lhscaldas/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/CMAlert.cpp.o"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pContactMgrMod && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/pContactMgrMod.dir/CMAlert.cpp.o -c /home/lhscaldas/moos-ivp-lhscaldas/src/pContactMgrMod/CMAlert.cpp

src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/CMAlert.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/pContactMgrMod.dir/CMAlert.cpp.i"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pContactMgrMod && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/lhscaldas/moos-ivp-lhscaldas/src/pContactMgrMod/CMAlert.cpp > CMakeFiles/pContactMgrMod.dir/CMAlert.cpp.i

src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/CMAlert.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/pContactMgrMod.dir/CMAlert.cpp.s"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pContactMgrMod && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/lhscaldas/moos-ivp-lhscaldas/src/pContactMgrMod/CMAlert.cpp -o CMakeFiles/pContactMgrMod.dir/CMAlert.cpp.s

src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/ContactMgrV20.cpp.o: src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/flags.make
src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/ContactMgrV20.cpp.o: ../src/pContactMgrMod/ContactMgrV20.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/lhscaldas/moos-ivp-lhscaldas/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/ContactMgrV20.cpp.o"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pContactMgrMod && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/pContactMgrMod.dir/ContactMgrV20.cpp.o -c /home/lhscaldas/moos-ivp-lhscaldas/src/pContactMgrMod/ContactMgrV20.cpp

src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/ContactMgrV20.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/pContactMgrMod.dir/ContactMgrV20.cpp.i"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pContactMgrMod && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/lhscaldas/moos-ivp-lhscaldas/src/pContactMgrMod/ContactMgrV20.cpp > CMakeFiles/pContactMgrMod.dir/ContactMgrV20.cpp.i

src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/ContactMgrV20.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/pContactMgrMod.dir/ContactMgrV20.cpp.s"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pContactMgrMod && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/lhscaldas/moos-ivp-lhscaldas/src/pContactMgrMod/ContactMgrV20.cpp -o CMakeFiles/pContactMgrMod.dir/ContactMgrV20.cpp.s

src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/ContactMgrV20_Info.cpp.o: src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/flags.make
src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/ContactMgrV20_Info.cpp.o: ../src/pContactMgrMod/ContactMgrV20_Info.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/lhscaldas/moos-ivp-lhscaldas/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/ContactMgrV20_Info.cpp.o"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pContactMgrMod && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/pContactMgrMod.dir/ContactMgrV20_Info.cpp.o -c /home/lhscaldas/moos-ivp-lhscaldas/src/pContactMgrMod/ContactMgrV20_Info.cpp

src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/ContactMgrV20_Info.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/pContactMgrMod.dir/ContactMgrV20_Info.cpp.i"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pContactMgrMod && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/lhscaldas/moos-ivp-lhscaldas/src/pContactMgrMod/ContactMgrV20_Info.cpp > CMakeFiles/pContactMgrMod.dir/ContactMgrV20_Info.cpp.i

src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/ContactMgrV20_Info.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/pContactMgrMod.dir/ContactMgrV20_Info.cpp.s"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pContactMgrMod && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/lhscaldas/moos-ivp-lhscaldas/src/pContactMgrMod/ContactMgrV20_Info.cpp -o CMakeFiles/pContactMgrMod.dir/ContactMgrV20_Info.cpp.s

src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/MOOSGeodesy.cpp.o: src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/flags.make
src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/MOOSGeodesy.cpp.o: ../src/pContactMgrMod/MOOSGeodesy.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/lhscaldas/moos-ivp-lhscaldas/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/MOOSGeodesy.cpp.o"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pContactMgrMod && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/pContactMgrMod.dir/MOOSGeodesy.cpp.o -c /home/lhscaldas/moos-ivp-lhscaldas/src/pContactMgrMod/MOOSGeodesy.cpp

src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/MOOSGeodesy.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/pContactMgrMod.dir/MOOSGeodesy.cpp.i"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pContactMgrMod && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/lhscaldas/moos-ivp-lhscaldas/src/pContactMgrMod/MOOSGeodesy.cpp > CMakeFiles/pContactMgrMod.dir/MOOSGeodesy.cpp.i

src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/MOOSGeodesy.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/pContactMgrMod.dir/MOOSGeodesy.cpp.s"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pContactMgrMod && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/lhscaldas/moos-ivp-lhscaldas/src/pContactMgrMod/MOOSGeodesy.cpp -o CMakeFiles/pContactMgrMod.dir/MOOSGeodesy.cpp.s

src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/PlatformAlertRecord.cpp.o: src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/flags.make
src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/PlatformAlertRecord.cpp.o: ../src/pContactMgrMod/PlatformAlertRecord.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/lhscaldas/moos-ivp-lhscaldas/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building CXX object src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/PlatformAlertRecord.cpp.o"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pContactMgrMod && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/pContactMgrMod.dir/PlatformAlertRecord.cpp.o -c /home/lhscaldas/moos-ivp-lhscaldas/src/pContactMgrMod/PlatformAlertRecord.cpp

src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/PlatformAlertRecord.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/pContactMgrMod.dir/PlatformAlertRecord.cpp.i"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pContactMgrMod && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/lhscaldas/moos-ivp-lhscaldas/src/pContactMgrMod/PlatformAlertRecord.cpp > CMakeFiles/pContactMgrMod.dir/PlatformAlertRecord.cpp.i

src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/PlatformAlertRecord.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/pContactMgrMod.dir/PlatformAlertRecord.cpp.s"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pContactMgrMod && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/lhscaldas/moos-ivp-lhscaldas/src/pContactMgrMod/PlatformAlertRecord.cpp -o CMakeFiles/pContactMgrMod.dir/PlatformAlertRecord.cpp.s

src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/RangeMark.cpp.o: src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/flags.make
src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/RangeMark.cpp.o: ../src/pContactMgrMod/RangeMark.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/lhscaldas/moos-ivp-lhscaldas/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building CXX object src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/RangeMark.cpp.o"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pContactMgrMod && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/pContactMgrMod.dir/RangeMark.cpp.o -c /home/lhscaldas/moos-ivp-lhscaldas/src/pContactMgrMod/RangeMark.cpp

src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/RangeMark.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/pContactMgrMod.dir/RangeMark.cpp.i"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pContactMgrMod && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/lhscaldas/moos-ivp-lhscaldas/src/pContactMgrMod/RangeMark.cpp > CMakeFiles/pContactMgrMod.dir/RangeMark.cpp.i

src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/RangeMark.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/pContactMgrMod.dir/RangeMark.cpp.s"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pContactMgrMod && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/lhscaldas/moos-ivp-lhscaldas/src/pContactMgrMod/RangeMark.cpp -o CMakeFiles/pContactMgrMod.dir/RangeMark.cpp.s

src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/main.cpp.o: src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/flags.make
src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/main.cpp.o: ../src/pContactMgrMod/main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/lhscaldas/moos-ivp-lhscaldas/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Building CXX object src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/main.cpp.o"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pContactMgrMod && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/pContactMgrMod.dir/main.cpp.o -c /home/lhscaldas/moos-ivp-lhscaldas/src/pContactMgrMod/main.cpp

src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/pContactMgrMod.dir/main.cpp.i"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pContactMgrMod && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/lhscaldas/moos-ivp-lhscaldas/src/pContactMgrMod/main.cpp > CMakeFiles/pContactMgrMod.dir/main.cpp.i

src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/pContactMgrMod.dir/main.cpp.s"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pContactMgrMod && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/lhscaldas/moos-ivp-lhscaldas/src/pContactMgrMod/main.cpp -o CMakeFiles/pContactMgrMod.dir/main.cpp.s

# Object files for target pContactMgrMod
pContactMgrMod_OBJECTS = \
"CMakeFiles/pContactMgrMod.dir/CMAlert.cpp.o" \
"CMakeFiles/pContactMgrMod.dir/ContactMgrV20.cpp.o" \
"CMakeFiles/pContactMgrMod.dir/ContactMgrV20_Info.cpp.o" \
"CMakeFiles/pContactMgrMod.dir/MOOSGeodesy.cpp.o" \
"CMakeFiles/pContactMgrMod.dir/PlatformAlertRecord.cpp.o" \
"CMakeFiles/pContactMgrMod.dir/RangeMark.cpp.o" \
"CMakeFiles/pContactMgrMod.dir/main.cpp.o"

# External object files for target pContactMgrMod
pContactMgrMod_EXTERNAL_OBJECTS =

../bin/pContactMgrMod: src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/CMAlert.cpp.o
../bin/pContactMgrMod: src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/ContactMgrV20.cpp.o
../bin/pContactMgrMod: src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/ContactMgrV20_Info.cpp.o
../bin/pContactMgrMod: src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/MOOSGeodesy.cpp.o
../bin/pContactMgrMod: src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/PlatformAlertRecord.cpp.o
../bin/pContactMgrMod: src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/RangeMark.cpp.o
../bin/pContactMgrMod: src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/main.cpp.o
../bin/pContactMgrMod: src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/build.make
../bin/pContactMgrMod: /home/lhscaldas/moos-ivp/build/MOOS/MOOSCore/lib/libMOOS.a
../bin/pContactMgrMod: /lib/libmbutil.a
../bin/pContactMgrMod: /lib/libmbutil.a
../bin/pContactMgrMod: src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/lhscaldas/moos-ivp-lhscaldas/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_8) "Linking CXX executable ../../../bin/pContactMgrMod"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pContactMgrMod && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/pContactMgrMod.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/build: ../bin/pContactMgrMod

.PHONY : src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/build

src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/clean:
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pContactMgrMod && $(CMAKE_COMMAND) -P CMakeFiles/pContactMgrMod.dir/cmake_clean.cmake
.PHONY : src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/clean

src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/depend:
	cd /home/lhscaldas/moos-ivp-lhscaldas/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/lhscaldas/moos-ivp-lhscaldas /home/lhscaldas/moos-ivp-lhscaldas/src/pContactMgrMod /home/lhscaldas/moos-ivp-lhscaldas/build /home/lhscaldas/moos-ivp-lhscaldas/build/src/pContactMgrMod /home/lhscaldas/moos-ivp-lhscaldas/build/src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/pContactMgrMod/CMakeFiles/pContactMgrMod.dir/depend

