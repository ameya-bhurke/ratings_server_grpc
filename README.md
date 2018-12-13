#Ratings server

* This is a B2B service. This service doesn't provide user management.
* 

#Ratings client

```python
python -m grpc_tools.protoc -I ../../services --python_out=. --grpc_python_out=. ../../services/ratings.proto
```