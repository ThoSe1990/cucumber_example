cmake_minimum_required(VERSION 3.1.0)
project(cmake_wrapper)

if(EXISTS "${CMAKE_BINARY_DIR}/conanbuildinfo.cmake")
  include("${CMAKE_BINARY_DIR}/conanbuildinfo.cmake")
else()
  include(conanbuildinfo.cmake)
endif()
conan_basic_setup()

link_libraries(${CONAN_LIBS})
include_directories(source_subfolder/include)

add_subdirectory("source_subfolder")

