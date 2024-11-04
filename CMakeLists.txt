# Require CMake 3.15+ (matching scikit-build-core) Use new versions of all
# policies up to CMake 3.27
cmake_minimum_required(VERSION 3.15...3.27)

# Scikit-build-core sets these values for you, or you can just hard-code the
# name and version.
project(
  ${SKBUILD_PROJECT_NAME}
  VERSION ${SKBUILD_PROJECT_VERSION}
  LANGUAGES CXX)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3 -std=c++14 -pthread")

# Find the module development requirements (requires FindPython from 3.17 or
# scikit-build-core's built-in backport)
find_package(Python REQUIRED COMPONENTS Interpreter Development.Module)
find_package(pybind11 CONFIG REQUIRED)

find_package(Eigen3 REQUIRED)
link_directories(lib)
include_directories(include ${EIGEN3_INCLUDE_DIR})

# Add a library using FindPython's tooling (pybind11 also provides a helper like
# this)
pybind11_add_module(unitree_arm_interface src/arm_python_interface.cpp)
target_link_libraries(unitree_arm_interface PRIVATE pybind11::headers Z1_SDK_${CMAKE_SYSTEM_PROCESSOR})

# This is passing in the version as a define just as an example
target_compile_definitions(unitree_arm_interface PRIVATE VERSION_INFO=${PROJECT_VERSION})

# Set RPATH to the same place as target's
set_target_properties(unitree_arm_interface PROPERTIES
    INSTALL_RPATH "$ORIGIN"
    BUILD_WITH_INSTALL_RPATH TRUE
)

# The install directory is the output (wheel) directory
install(TARGETS unitree_arm_interface DESTINATION z1_sdk)
install(FILES lib/libZ1_SDK_${CMAKE_SYSTEM_PROCESSOR}.so DESTINATION z1_sdk)
