#!/bin/sh
cd src/client
python3 -m grpc_tools.protoc -I ../../services --python_out=. --grpc_python_out=. ../../services/ratings.proto
python3 ratings_client.py
cd ../..