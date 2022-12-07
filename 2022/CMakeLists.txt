cmake_minimum_required (VERSION 3.16.3)
project(advent2022)

SUBDIRLIST(SUBDIRS ${CMAKE_CURRENT_LIST_DIR})

FOREACH(subdir ${SUBDIRS})
  if(EXISTS "${CMAKE_CURRENT_LIST_DIR}/${subdir}/CMakeLists.txt")
    ADD_SUBDIRECTORY(${subdir})
  endif()
ENDFOREACH()