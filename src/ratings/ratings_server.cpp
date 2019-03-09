/**
 * Copyright 2018
 * 
 * Licensed under MIT License.
 * 
 */
#include "ratings_server.h"

namespace ratings
{

    grpc::Status ratings_server_impl::RecordBinaryEvents(
        grpc::ServerContext* ctx,
        grpc::ServerReader<ratings::BinaryEvent>* reader,
        ratings::BinaryEventsSummary* summary
    ) 
    {
        // TODO: implement me.
        std::cout << "Called RecordBinaryEvents " << std::endl; 
        summary->set_count(0);
        return grpc::Status::OK;      
    } 

    grpc::Status ratings_server_impl::ListBinaryEvents(
        grpc::ServerContext* ctx,
        grpc::ServerReaderWriter<ratings::BinaryEvent, ratings::BinaryEventSource>* rw_stream
    ) 
    {
        std::cout << "Called ListBinaryEvents " << std::endl; 
        return grpc::Status::OK;
    }

    grpc::Status ratings_server_impl::VoteBinaryEvent(
        grpc::ServerContext* ctx,
        const ratings::BinaryVote* vote,
        ratings::BinaryVoteSummary* summary
    ) 
    {
        std::cout << "Called VoteBinaryEvent " << std::endl;
        std::cout << vote->event_id() << std::endl;
        std::cout << vote->when() << std::endl;
        return grpc::Status::OK;
    }
       

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

    void start_async_processor()
    {
        ratings::Ratings::AsyncService* service;
        grpc::ServerCompletionQueue* serverQ;
        grpc::ServerContext ctx;
    }

} // end namespace ratings