cmake_minimum_required(VERSION 3.16)
project(Cucumber)

set(CMAKE_CXX_STANDARD 17)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)


if(NOT CUCUMBER_ROOT)
    set(CUCUMBER_ROOT $ENV{CUCUMBER_ROOT})
endif()
find_package(GTest REQUIRED)
find_package(CucumberCpp REQUIRED HINTS ${CUCUMBER_ROOT}/lib/cmake)
find_package(Boost REQUIRED regex date_time filesystem thread unit_test_framework program_options)




set(target cucumber_example)

add_executable(${target} 
${PROJECT_SOURCE_DIR}/src/cucumber/step_definitions.cpp
)

target_include_directories(${target} PUBLIC
${Boost_INCLUDE_DIRS}
${PROJECT_SOURCE_DIR}/src
)
target_link_libraries(${target} CucumberCpp::cucumber-cpp ${Boost_LIBRARIES} GTest::GTest)

