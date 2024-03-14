cmake_minimum_required(VERSION 3.16.3)

set(app_name hello_world_2)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY      "${CMAKE_BINARY_DIR}/bin")

project(${app_name})

file(GLOB SOURCES "*.c")

add_definitions(-DJOB_ID_BUILD=${JOB_ID})

add_executable(${app_name} ${SOURCES})