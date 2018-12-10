cmake_minimum_required(VERSION 3.10)
project(ratings_server)

#include(FindProtobuf)

find_package(Protobuf REQUIRED)
#include_directories(${Protobuf_INCLUDE_DIR})

set(CMAKE_CPP_FLAGS "${CMAKE_CPP_FLAGS} -std=c++11 pkg-config --cflags --lib protobuf grpc")

include_directories(/usr/local/include)
link_directories(/usr/local/lib)

#set(PROTOBUF_PROTOC_EXECUTABLE "${`which protoc`}")
set(PROTO_PATH "${CMAKE_SOURCE_DIR}/services")
set(RATINGS_PROTO "${PROTO_PATH}/ratings.proto")
set(GENERATED_PROTOBUF_PATH "${CMAKE_BINARY_DIR}/services")

set(RATINGS_PB_CPP_FILE "${GENERATED_PROTOBUF_PATH}/ratings.pb.cc")
set(RATINGS_PB_H_FILE "${GENERATED_PROTOBUF_PATH}/ratings.pb.h")
set(RATINGS_GRPC_PB_CPP_FILE "${GENERATED_PROTOBUF_PATH}/ratings.grpc.pb.cc")
set(RATINGS_GRPC_PB_H_FILE "${GENERATED_PROTOBUF_PATH}/ratings.grpc.pb.h")
add_custom_command(
    OUTPUT "${RATINGS_PB_H_FILE}"
           "${RATINGS_PB_CPP_FILE}"
           "${RATINGS_GRPC_PB_H_FILE}"
           "${RATINGS_GRPC_PB_CPP_FILE}"
    COMMAND ${PROTOBUF_PROTOC_EXECUTABLE}
    ARGS "-I ${PROTO_PATH}}" 
        "--proto_path=${PROTO_PATH}"
        "--grpc_out=${GENERATED_PROTOBUF_PATH}"
        "--plugin=protoc-gen-grpc=/usr/local/bin/grpc_cpp_plugin"
        "${RATINGS_PROTO}"
    COMMAND ${PROTOBUF_PROTOC_EXECUTABLE}
    ARGS "-I ${PROTO_PATH}"
         "--proto_path=${PROTO_PATH}"
         "--cpp_out=${GENERATED_PROTOBUF_PATH}"
         "${RATINGS_PROTO}"

    )

set(GENERATED_PROTOBUF_FILES ${RATINGS_PB_H_FILE} ${RATINGS_PB_CPP_FILE}
    ${RATINGS_GRPC_PB_H_FILE} ${RATINGS_GRPC_PB_CPP_FILE})

file(GLOB_RECURSE INC_FILES src/**/*.h)
file(GLOB_RECURSE SRC_FILES src/**/*.cpp)

add_custom_target(ratings_header ALL DEPENDS ${GENERATED_PROTOBUF_FILES})
include_directories(${GENERATED_PROTOBUF_PATH})


set(SOURCE_FILES src/main.cpp ${GENERATED_PROTOBUF_FILES} ${INC_FILES} ${SRC_FILES})
link_libraries(protoc protobuf grpc++_unsecure gpr grpc++ )
add_executable(ratings_server ${SOURCE_FILES})
