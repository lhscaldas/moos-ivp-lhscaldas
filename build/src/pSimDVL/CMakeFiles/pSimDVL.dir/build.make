# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
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
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/luiz_caldas/moos-ivp-lhscaldas

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/luiz_caldas/moos-ivp-lhscaldas/build

# Include any dependencies generated for this target.
include src/pSimDVL/CMakeFiles/pSimDVL.dir/depend.make

# Include the progress variables for this target.
include src/pSimDVL/CMakeFiles/pSimDVL.dir/progress.make

# Include the compile flags for this target's objects.
include src/pSimDVL/CMakeFiles/pSimDVL.dir/flags.make

src/pSimDVL/CMakeFiles/pSimDVL.dir/SimDVL.cpp.o: src/pSimDVL/CMakeFiles/pSimDVL.dir/flags.make
src/pSimDVL/CMakeFiles/pSimDVL.dir/SimDVL.cpp.o: ../src/pSimDVL/SimDVL.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/luiz_caldas/moos-ivp-lhscaldas/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/pSimDVL/CMakeFiles/pSimDVL.dir/SimDVL.cpp.o"
	cd /home/luiz_caldas/moos-ivp-lhscaldas/build/src/pSimDVL && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/pSimDVL.dir/SimDVL.cpp.o -c /home/luiz_caldas/moos-ivp-lhscaldas/src/pSimDVL/SimDVL.cpp

src/pSimDVL/CMakeFiles/pSimDVL.dir/SimDVL.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/pSimDVL.dir/SimDVL.cpp.i"
	cd /home/luiz_caldas/moos-ivp-lhscaldas/build/src/pSimDVL && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/luiz_caldas/moos-ivp-lhscaldas/src/pSimDVL/SimDVL.cpp > CMakeFiles/pSimDVL.dir/SimDVL.cpp.i

src/pSimDVL/CMakeFiles/pSimDVL.dir/SimDVL.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/pSimDVL.dir/SimDVL.cpp.s"
	cd /home/luiz_caldas/moos-ivp-lhscaldas/build/src/pSimDVL && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/luiz_caldas/moos-ivp-lhscaldas/src/pSimDVL/SimDVL.cpp -o CMakeFiles/pSimDVL.dir/SimDVL.cpp.s

src/pSimDVL/CMakeFiles/pSimDVL.dir/SimDVL_Info.cpp.o: src/pSimDVL/CMakeFiles/pSimDVL.dir/flags.make
src/pSimDVL/CMakeFiles/pSimDVL.dir/SimDVL_Info.cpp.o: ../src/pSimDVL/SimDVL_Info.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/luiz_caldas/moos-ivp-lhscaldas/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object src/pSimDVL/CMakeFiles/pSimDVL.dir/SimDVL_Info.cpp.o"
	cd /home/luiz_caldas/moos-ivp-lhscaldas/build/src/pSimDVL && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/pSimDVL.dir/SimDVL_Info.cpp.o -c /home/luiz_caldas/moos-ivp-lhscaldas/src/pSimDVL/SimDVL_Info.cpp

src/pSimDVL/CMakeFiles/pSimDVL.dir/SimDVL_Info.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/pSimDVL.dir/SimDVL_Info.cpp.i"
	cd /home/luiz_caldas/moos-ivp-lhscaldas/build/src/pSimDVL && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/luiz_caldas/moos-ivp-lhscaldas/src/pSimDVL/SimDVL_Info.cpp > CMakeFiles/pSimDVL.dir/SimDVL_Info.cpp.i

src/pSimDVL/CMakeFiles/pSimDVL.dir/SimDVL_Info.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/pSimDVL.dir/SimDVL_Info.cpp.s"
	cd /home/luiz_caldas/moos-ivp-lhscaldas/build/src/pSimDVL && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/luiz_caldas/moos-ivp-lhscaldas/src/pSimDVL/SimDVL_Info.cpp -o CMakeFiles/pSimDVL.dir/SimDVL_Info.cpp.s

src/pSimDVL/CMakeFiles/pSimDVL.dir/main.cpp.o: src/pSimDVL/CMakeFiles/pSimDVL.dir/flags.make
src/pSimDVL/CMakeFiles/pSimDVL.dir/main.cpp.o: ../src/pSimDVL/main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/luiz_caldas/moos-ivp-lhscaldas/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object src/pSimDVL/CMakeFiles/pSimDVL.dir/main.cpp.o"
	cd /home/luiz_caldas/moos-ivp-lhscaldas/build/src/pSimDVL && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/pSimDVL.dir/main.cpp.o -c /home/luiz_caldas/moos-ivp-lhscaldas/src/pSimDVL/main.cpp

src/pSimDVL/CMakeFiles/pSimDVL.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/pSimDVL.dir/main.cpp.i"
	cd /home/luiz_caldas/moos-ivp-lhscaldas/build/src/pSimDVL && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/luiz_caldas/moos-ivp-lhscaldas/src/pSimDVL/main.cpp > CMakeFiles/pSimDVL.dir/main.cpp.i

src/pSimDVL/CMakeFiles/pSimDVL.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/pSimDVL.dir/main.cpp.s"
	cd /home/luiz_caldas/moos-ivp-lhscaldas/build/src/pSimDVL && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/luiz_caldas/moos-ivp-lhscaldas/src/pSimDVL/main.cpp -o CMakeFiles/pSimDVL.dir/main.cpp.s

# Object files for target pSimDVL
pSimDVL_OBJECTS = \
"CMakeFiles/pSimDVL.dir/SimDVL.cpp.o" \
"CMakeFiles/pSimDVL.dir/SimDVL_Info.cpp.o" \
"CMakeFiles/pSimDVL.dir/main.cpp.o"

# External object files for target pSimDVL
pSimDVL_EXTERNAL_OBJECTS =

../bin/pSimDVL: src/pSimDVL/CMakeFiles/pSimDVL.dir/SimDVL.cpp.o
../bin/pSimDVL: src/pSimDVL/CMakeFiles/pSimDVL.dir/SimDVL_Info.cpp.o
../bin/pSimDVL: src/pSimDVL/CMakeFiles/pSimDVL.dir/main.cpp.o
../bin/pSimDVL: src/pSimDVL/CMakeFiles/pSimDVL.dir/build.make
../bin/pSimDVL: /home/luiz_caldas/moos-ivp/build/MOOS/MOOSCore/lib/libMOOS.a
../bin/pSimDVL: /lib/libmbutil.a
../bin/pSimDVL: src/pSimDVL/CMakeFiles/pSimDVL.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/luiz_caldas/moos-ivp-lhscaldas/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX executable ../../../bin/pSimDVL"
	cd /home/luiz_caldas/moos-ivp-lhscaldas/build/src/pSimDVL && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/pSimDVL.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/pSimDVL/CMakeFiles/pSimDVL.dir/build: ../bin/pSimDVL

.PHONY : src/pSimDVL/CMakeFiles/pSimDVL.dir/build

src/pSimDVL/CMakeFiles/pSimDVL.dir/clean:
	cd /home/luiz_caldas/moos-ivp-lhscaldas/build/src/pSimDVL && $(CMAKE_COMMAND) -P CMakeFiles/pSimDVL.dir/cmake_clean.cmake
.PHONY : src/pSimDVL/CMakeFiles/pSimDVL.dir/clean

src/pSimDVL/CMakeFiles/pSimDVL.dir/depend:
	cd /home/luiz_caldas/moos-ivp-lhscaldas/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/luiz_caldas/moos-ivp-lhscaldas /home/luiz_caldas/moos-ivp-lhscaldas/src/pSimDVL /home/luiz_caldas/moos-ivp-lhscaldas/build /home/luiz_caldas/moos-ivp-lhscaldas/build/src/pSimDVL /home/luiz_caldas/moos-ivp-lhscaldas/build/src/pSimDVL/CMakeFiles/pSimDVL.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/pSimDVL/CMakeFiles/pSimDVL.dir/depend

