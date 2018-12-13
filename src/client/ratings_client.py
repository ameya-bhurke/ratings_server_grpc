#
# Copyright 2018
#
# MIT License
#

""" A simple python client for ratings """

import grpc

import ratings_pb2
import ratings_pb2_grpc

import time
from datetime import datetime

def run():
    print(datetime.now())
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = ratings_pb2_grpc.RatingsStub(channel)
        bv = ratings_pb2.BinaryVote()
        bv.event_id = 123456789
        bv.key = b'0'
        bv.type = ratings_pb2.BinaryVote.up
        bv.when = int(round(time.time() * 1000))
        stub.VoteBinaryEvent(bv)
    print(datetime.now())


if __name__ == '__main__':
    run()