cmake_minimum_required(VERSION 3.15)

project(CalcProject LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(FetchContent)

FetchContent_Declare(
    googletest
    GIT_REPOSITORY https://github.com/google/googletest.git
    GIT_TAG        v1.14.0
)

set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)

FetchContent_MakeAvailable(googletest)

add_library(math_lib STATIC calc.cpp calc.h)

target_include_directories(math_lib
    PUBLIC
        "${CMAKE_CURRENT_SOURCE_DIR}"
)

add_executable(calc_tests tests.cpp)

target_link_libraries(calc_tests
    PRIVATE
        math_lib
        gtest_main
)

include(CTest)
enable_testing()

include(GoogleTest)
gtest_discover_tests(calc_tests)