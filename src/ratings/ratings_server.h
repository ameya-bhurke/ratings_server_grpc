/**
 * Copyright 2018
 *
 * Licensed under MIT License.
 *
 */

#include "ratings.grpc.pb.h"
#include <grpc/grpc.h>
#include <grpcpp/security/server_credentials.h>
#include <grpcpp/server.h>
#include <grpcpp/server_builder.h>
#include <grpcpp/server_context.h>

namespace ratings {

// A simple implementation of the ratings server.
class ratings_server_impl final : public ratings::Ratings::Service {
public:
  grpc::Status
  RecordBinaryEvents(grpc::ServerContext *ctx,
                     grpc::ServerReader<ratings::BinaryEvent> *reader,
                     ratings::BinaryEventsSummary *summary) override;

  grpc::Status ListBinaryEvents(
      grpc::ServerContext *ctx,
      grpc::ServerReaderWriter<ratings::BinaryEvent, ratings::BinaryEventSource>
          *rw_stream) override;

  grpc::Status VoteBinaryEvent(grpc::ServerContext *ctx,
                               const ratings::BinaryVote *vote,
                               ratings::BinaryVoteSummary *summary) override;

}; // end class ratings_server_impl

void start_async_processor();

void run_server();

} // end namespace ratings