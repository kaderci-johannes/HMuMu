#
# build everything with cmake
#

# min version for cmake
cmake_minimum_required(VERSION 2.8.0)

#	project name
project (Analysis)

message (SOURCE DIRECTORY = ${PROJECT_SOURCE_DIR})
message (BUILD DIRECTORY = ${PROJECT_BINARY_DIR})

#
#	Compiler flags and some definitions
#
set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++1y")
add_definitions(-DSTANDALONE=1)

#
#	project's versions and some other env vars to pass
#
set (Analysis_VERSION_MAJOR 1)
set (Analysis_VERSION_MINOR 0)
configure_file(
	"${PROJECT_SOURCE_DIR}/config/config.h.in"
	"${PROJECT_BINARY_DIR}/config/config.h"
)

#
#	add the config.h to the search include path and enable
#
include_directories("${PROJECT_BINARY_DIR}/config")
option (STANDALONE
	"Compile and build in standalone mode without CMSSW" ON
)

#	
#	find and add ROOT
#
set (CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/config)
find_package(ROOT REQUIRED COMPONENTS RHTTP)
include_directories("${ROOT_INCLUDE_DIR}")
add_definitions(${ROOT_CXX_FLAGS})

#
#	add ROOT to the eet of libraries to link against
#
set (EXTRA_LIBS ${EXTRA_LIBS} ${ROOT_LIBRARIES})

#
#	add the includes to the search path
#
include_directories ("${PROJECT_SOURCE_DIR}/Core/interface")

#
#	Generate ROOT Dictionary and Shared Lib
#
ROOT_GENERATE_DICTIONARY(G__Core 
	${PROJECT_SOURCE_DIR}/Core/interface/Object.h
	${PROJECT_SOURCE_DIR}/Core/interface/Track.h
	${PROJECT_SOURCE_DIR}/Core/interface/Muon.h
	${PROJECT_SOURCE_DIR}/Core/interface/GenJet.h
	${PROJECT_SOURCE_DIR}/Core/interface/Jet.h
	${PROJECT_SOURCE_DIR}/Core/interface/GenParticle.h
	${PROJECT_SOURCE_DIR}/Core/interface/MET.h
	${PROJECT_SOURCE_DIR}/Core/interface/Vertex.h
	${PROJECT_SOURCE_DIR}/Core/interface/Event.h
	${PROJECT_SOURCE_DIR}/Core/interface/MetaHiggs.h
    ${PROJECT_SOURCE_DIR}/Core/interface/Electron.h
    ${PROJECT_SOURCE_DIR}/Core/interface/Tau.h
	LINKDEF ${PROJECT_SOURCE_DIR}/config/LinkDef.h
	OPTIONS -DSTANDALONE=1 -inlineInputHeader
)
add_library(AnalysisCore SHARED G__Core.cxx)
target_link_libraries(AnalysisCore ${ROOT_LIBRARIES})
set (EXTRA_LIBS ${EXTRA_LIBS} AnalysisCore)
