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
include src/pSimGyro/CMakeFiles/pSimGyro.dir/depend.make

# Include the progress variables for this target.
include src/pSimGyro/CMakeFiles/pSimGyro.dir/progress.make

# Include the compile flags for this target's objects.
include src/pSimGyro/CMakeFiles/pSimGyro.dir/flags.make

src/pSimGyro/CMakeFiles/pSimGyro.dir/SimGyro.cpp.o: src/pSimGyro/CMakeFiles/pSimGyro.dir/flags.make
src/pSimGyro/CMakeFiles/pSimGyro.dir/SimGyro.cpp.o: ../src/pSimGyro/SimGyro.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/lhscaldas/moos-ivp-lhscaldas/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/pSimGyro/CMakeFiles/pSimGyro.dir/SimGyro.cpp.o"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGyro && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/pSimGyro.dir/SimGyro.cpp.o -c /home/lhscaldas/moos-ivp-lhscaldas/src/pSimGyro/SimGyro.cpp

src/pSimGyro/CMakeFiles/pSimGyro.dir/SimGyro.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/pSimGyro.dir/SimGyro.cpp.i"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGyro && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/lhscaldas/moos-ivp-lhscaldas/src/pSimGyro/SimGyro.cpp > CMakeFiles/pSimGyro.dir/SimGyro.cpp.i

src/pSimGyro/CMakeFiles/pSimGyro.dir/SimGyro.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/pSimGyro.dir/SimGyro.cpp.s"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGyro && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/lhscaldas/moos-ivp-lhscaldas/src/pSimGyro/SimGyro.cpp -o CMakeFiles/pSimGyro.dir/SimGyro.cpp.s

src/pSimGyro/CMakeFiles/pSimGyro.dir/SimGyro_Info.cpp.o: src/pSimGyro/CMakeFiles/pSimGyro.dir/flags.make
src/pSimGyro/CMakeFiles/pSimGyro.dir/SimGyro_Info.cpp.o: ../src/pSimGyro/SimGyro_Info.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/lhscaldas/moos-ivp-lhscaldas/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object src/pSimGyro/CMakeFiles/pSimGyro.dir/SimGyro_Info.cpp.o"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGyro && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/pSimGyro.dir/SimGyro_Info.cpp.o -c /home/lhscaldas/moos-ivp-lhscaldas/src/pSimGyro/SimGyro_Info.cpp

src/pSimGyro/CMakeFiles/pSimGyro.dir/SimGyro_Info.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/pSimGyro.dir/SimGyro_Info.cpp.i"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGyro && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/lhscaldas/moos-ivp-lhscaldas/src/pSimGyro/SimGyro_Info.cpp > CMakeFiles/pSimGyro.dir/SimGyro_Info.cpp.i

src/pSimGyro/CMakeFiles/pSimGyro.dir/SimGyro_Info.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/pSimGyro.dir/SimGyro_Info.cpp.s"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGyro && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/lhscaldas/moos-ivp-lhscaldas/src/pSimGyro/SimGyro_Info.cpp -o CMakeFiles/pSimGyro.dir/SimGyro_Info.cpp.s

src/pSimGyro/CMakeFiles/pSimGyro.dir/main.cpp.o: src/pSimGyro/CMakeFiles/pSimGyro.dir/flags.make
src/pSimGyro/CMakeFiles/pSimGyro.dir/main.cpp.o: ../src/pSimGyro/main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/lhscaldas/moos-ivp-lhscaldas/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object src/pSimGyro/CMakeFiles/pSimGyro.dir/main.cpp.o"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGyro && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/pSimGyro.dir/main.cpp.o -c /home/lhscaldas/moos-ivp-lhscaldas/src/pSimGyro/main.cpp

src/pSimGyro/CMakeFiles/pSimGyro.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/pSimGyro.dir/main.cpp.i"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGyro && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/lhscaldas/moos-ivp-lhscaldas/src/pSimGyro/main.cpp > CMakeFiles/pSimGyro.dir/main.cpp.i

src/pSimGyro/CMakeFiles/pSimGyro.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/pSimGyro.dir/main.cpp.s"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGyro && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/lhscaldas/moos-ivp-lhscaldas/src/pSimGyro/main.cpp -o CMakeFiles/pSimGyro.dir/main.cpp.s

# Object files for target pSimGyro
pSimGyro_OBJECTS = \
"CMakeFiles/pSimGyro.dir/SimGyro.cpp.o" \
"CMakeFiles/pSimGyro.dir/SimGyro_Info.cpp.o" \
"CMakeFiles/pSimGyro.dir/main.cpp.o"

# External object files for target pSimGyro
pSimGyro_EXTERNAL_OBJECTS =

../bin/pSimGyro: src/pSimGyro/CMakeFiles/pSimGyro.dir/SimGyro.cpp.o
../bin/pSimGyro: src/pSimGyro/CMakeFiles/pSimGyro.dir/SimGyro_Info.cpp.o
../bin/pSimGyro: src/pSimGyro/CMakeFiles/pSimGyro.dir/main.cpp.o
../bin/pSimGyro: src/pSimGyro/CMakeFiles/pSimGyro.dir/build.make
../bin/pSimGyro: /home/lhscaldas/moos-ivp/build/MOOS/MOOSCore/lib/libMOOS.a
../bin/pSimGyro: /lib/libmbutil.a
../bin/pSimGyro: src/pSimGyro/CMakeFiles/pSimGyro.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/lhscaldas/moos-ivp-lhscaldas/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX executable ../../../bin/pSimGyro"
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGyro && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/pSimGyro.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/pSimGyro/CMakeFiles/pSimGyro.dir/build: ../bin/pSimGyro

.PHONY : src/pSimGyro/CMakeFiles/pSimGyro.dir/build

src/pSimGyro/CMakeFiles/pSimGyro.dir/clean:
	cd /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGyro && $(CMAKE_COMMAND) -P CMakeFiles/pSimGyro.dir/cmake_clean.cmake
.PHONY : src/pSimGyro/CMakeFiles/pSimGyro.dir/clean

src/pSimGyro/CMakeFiles/pSimGyro.dir/depend:
	cd /home/lhscaldas/moos-ivp-lhscaldas/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/lhscaldas/moos-ivp-lhscaldas /home/lhscaldas/moos-ivp-lhscaldas/src/pSimGyro /home/lhscaldas/moos-ivp-lhscaldas/build /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGyro /home/lhscaldas/moos-ivp-lhscaldas/build/src/pSimGyro/CMakeFiles/pSimGyro.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/pSimGyro/CMakeFiles/pSimGyro.dir/depend

