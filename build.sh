mkdir build
mkdir -p build/services
cd build
protoc -I ../services --grpc_out=./services/. --plugin=protoc-gen-grpc=`which grpc_cpp_plugin` ../services/ratings.proto
protoc -I ../services --cpp_out=./services/. ../services/ratings.proto