/**
 * Copyright 2018
 * 
 * Licensed under MIT License.
 * 
 */

#include <grpc/grpc.h>
#include <grpcpp/server.h>
#include <grpcpp/server_builder.h>
#include <grpcpp/server_context.h>
#include <grpcpp/security/server_credentials.h>
#include "ratings.grpc.pb.h"
#include "ratings_server.h"

namespace ratings{

// A simple implementation of the ratings server.
class ratings_server_impl final : public ratings::Ratings::Service 
{
public:

    grpc::Status RecordBinaryEvents(
        grpc::ServerContext* ctx,
        grpc::ServerReader<ratings::BinaryEvent>* reader,
        ratings::BinaryEventsSummary* summary
    ) override
    {
        // TODO: implement me.
        summary->set_count(0);
        return grpc::Status::OK;      
    } 

    grpc::Status ListBinaryEvents(
        grpc::ServerContext* ctx,
        grpc::ServerReaderWriter<ratings::BinaryEvent, ratings::BinaryEventSource>* rw_stream
    ) override
    {
        return grpc::Status::OK;
    }

    grpc::Status VoteBinaryEvent(
        grpc::ServerContext* ctx,
        const ratings::BinaryVote* vote,
        ratings::BinaryVoteSummary* summary
    ) override
    {
        return grpc::Status::OK;
    }
        
}; // end class ratings_server_impl

void run_server()
{
    std::string srv_addr("localhost:50051");
    ratings_server_impl service;

    grpc::ServerBuilder builder;
    builder.AddListeningPort(srv_addr, grpc::InsecureServerCredentials());
    builder.RegisterService(&service);
    std::unique_ptr<grpc::Server> server(builder.BuildAndStart());
    std::cout << "ratings server up and running on: " << srv_addr << std::endl;   
    server->Wait();
}

} // end namespace ratings