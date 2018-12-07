mkdir build
protoc -I ../services --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_cpp_plugin` ../services/ratings.proto
protoc -I ../services --cpp_out=. ../services/ratings.proto