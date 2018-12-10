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
} // end namespace ratings