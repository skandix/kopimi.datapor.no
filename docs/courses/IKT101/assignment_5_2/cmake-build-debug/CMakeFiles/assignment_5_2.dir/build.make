# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.14

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

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = C:\Users\Paal\AppData\Local\JetBrains\Toolbox\apps\CLion\ch-0\192.6262.62\bin\cmake\win\bin\cmake.exe

# The command to remove a file.
RM = C:\Users\Paal\AppData\Local\JetBrains\Toolbox\apps\CLion\ch-0\192.6262.62\bin\cmake\win\bin\cmake.exe -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = C:\Users\Paal\ikt101g19h\assignments\solutions\assignment_5_2

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = C:\Users\Paal\ikt101g19h\assignments\solutions\assignment_5_2\cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/assignment_5_2.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/assignment_5_2.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/assignment_5_2.dir/flags.make

CMakeFiles/assignment_5_2.dir/main.c.obj: CMakeFiles/assignment_5_2.dir/flags.make
CMakeFiles/assignment_5_2.dir/main.c.obj: ../main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:\Users\Paal\ikt101g19h\assignments\solutions\assignment_5_2\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/assignment_5_2.dir/main.c.obj"
	C:\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles\assignment_5_2.dir\main.c.obj   -c C:\Users\Paal\ikt101g19h\assignments\solutions\assignment_5_2\main.c

CMakeFiles/assignment_5_2.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/assignment_5_2.dir/main.c.i"
	C:\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E C:\Users\Paal\ikt101g19h\assignments\solutions\assignment_5_2\main.c > CMakeFiles\assignment_5_2.dir\main.c.i

CMakeFiles/assignment_5_2.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/assignment_5_2.dir/main.c.s"
	C:\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S C:\Users\Paal\ikt101g19h\assignments\solutions\assignment_5_2\main.c -o CMakeFiles\assignment_5_2.dir\main.c.s

CMakeFiles/assignment_5_2.dir/Student_t.c.obj: CMakeFiles/assignment_5_2.dir/flags.make
CMakeFiles/assignment_5_2.dir/Student_t.c.obj: ../Student_t.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:\Users\Paal\ikt101g19h\assignments\solutions\assignment_5_2\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object CMakeFiles/assignment_5_2.dir/Student_t.c.obj"
	C:\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles\assignment_5_2.dir\Student_t.c.obj   -c C:\Users\Paal\ikt101g19h\assignments\solutions\assignment_5_2\Student_t.c

CMakeFiles/assignment_5_2.dir/Student_t.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/assignment_5_2.dir/Student_t.c.i"
	C:\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E C:\Users\Paal\ikt101g19h\assignments\solutions\assignment_5_2\Student_t.c > CMakeFiles\assignment_5_2.dir\Student_t.c.i

CMakeFiles/assignment_5_2.dir/Student_t.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/assignment_5_2.dir/Student_t.c.s"
	C:\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S C:\Users\Paal\ikt101g19h\assignments\solutions\assignment_5_2\Student_t.c -o CMakeFiles\assignment_5_2.dir\Student_t.c.s

# Object files for target assignment_5_2
assignment_5_2_OBJECTS = \
"CMakeFiles/assignment_5_2.dir/main.c.obj" \
"CMakeFiles/assignment_5_2.dir/Student_t.c.obj"

# External object files for target assignment_5_2
assignment_5_2_EXTERNAL_OBJECTS =

assignment_5_2.exe: CMakeFiles/assignment_5_2.dir/main.c.obj
assignment_5_2.exe: CMakeFiles/assignment_5_2.dir/Student_t.c.obj
assignment_5_2.exe: CMakeFiles/assignment_5_2.dir/build.make
assignment_5_2.exe: CMakeFiles/assignment_5_2.dir/linklibs.rsp
assignment_5_2.exe: CMakeFiles/assignment_5_2.dir/objects1.rsp
assignment_5_2.exe: CMakeFiles/assignment_5_2.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=C:\Users\Paal\ikt101g19h\assignments\solutions\assignment_5_2\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking C executable assignment_5_2.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\assignment_5_2.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/assignment_5_2.dir/build: assignment_5_2.exe

.PHONY : CMakeFiles/assignment_5_2.dir/build

CMakeFiles/assignment_5_2.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\assignment_5_2.dir\cmake_clean.cmake
.PHONY : CMakeFiles/assignment_5_2.dir/clean

CMakeFiles/assignment_5_2.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" C:\Users\Paal\ikt101g19h\assignments\solutions\assignment_5_2 C:\Users\Paal\ikt101g19h\assignments\solutions\assignment_5_2 C:\Users\Paal\ikt101g19h\assignments\solutions\assignment_5_2\cmake-build-debug C:\Users\Paal\ikt101g19h\assignments\solutions\assignment_5_2\cmake-build-debug C:\Users\Paal\ikt101g19h\assignments\solutions\assignment_5_2\cmake-build-debug\CMakeFiles\assignment_5_2.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/assignment_5_2.dir/depend

