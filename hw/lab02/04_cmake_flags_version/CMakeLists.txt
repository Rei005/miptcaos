cmake_minimum_required(VERSION 3.15)

project(CalcProject VERSION 1.2.3 LANGUAGES CXX)

add_executable(calculator main.cpp calc.cpp)

configure_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/version.h.in"
    "${CMAKE_CURRENT_BINARY_DIR}/version.h"
)

target_include_directories(calculator
    PRIVATE
        "${CMAKE_CURRENT_BINARY_DIR}"
)

target_compile_definitions(calculator
    PRIVATE
        $<$<CONFIG:Debug>:DEBUG_MODE>
)