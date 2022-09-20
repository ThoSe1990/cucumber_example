cmake_minimum_required(VERSION 3.16)
project(Cucumber)

set(CMAKE_CXX_STANDARD 17)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

if(MSVC)
    add_compile_options(
        $<$<CONFIG:>:/MT> 
        $<$<CONFIG:Debug>:/MTd>
        $<$<CONFIG:Release>:/MT>
    )
endif()


include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(target cucumber_example)

add_executable(${target} 
${PROJECT_SOURCE_DIR}/features/step_definitions/step_definitions.cpp
)

target_include_directories(${target} PUBLIC
${PROJECT_SOURCE_DIR}/src
)
target_link_libraries(${target} ${CONAN_LIBS})

