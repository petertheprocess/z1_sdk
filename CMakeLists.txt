cmake_minimum_required(VERSION 3.0)
project(z1_sdk)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3 -std=c++14 -pthread")

include_directories(
  include
)

link_directories(lib)

set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/lib)
find_package(pybind11 QUIET)
find_package(Eigen3 REQUIRED)
include_directories(${EIGEN3_INCLUDE_DIR})

pybind11_add_module(unitree_arm_interface examples_py/arm_python_interface.cpp)
target_link_libraries(unitree_arm_interface PRIVATE Z1_SDK_${CMAKE_SYSTEM_PROCESSOR})
