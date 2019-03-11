/**
 * Copyright 2018
 *
 * Licensed under MIT License.
 *
 */

#include "ratings_server.h"
#include <algorithm>
#include <unordered_map>
#include <vector>

std::unordered_map<std::string, std::vector<ratings::BinaryEvent>> evt_map;

grpc::Status ratings::ratings_server_impl::RecordBinaryEvents(
    grpc::ServerContext *ctx, grpc::ServerReader<ratings::BinaryEvent> *reader,
    ratings::BinaryEventsSummary *summary) {

  // TODO: implement me.
  std::cout << "Called RecordBinaryEvents " << std::endl;

  ratings::BinaryEvent binary_event;
  uint32_t count{};
  while (reader->Read(&binary_event)) {
    count++;
    std::string event_source = binary_event.event_source();
    auto events = evt_map.find(event_source);
    if (events == evt_map.end()) {
      std::vector<ratings::BinaryEvent> new_events{};
      new_events.push_back(binary_event);
      evt_map[event_source] = new_events;
    } else {
      events->second.push_back(binary_event);
    }
  }

  summary->set_count(count);
  return grpc::Status::OK;
}

grpc::Status ratings::ratings_server_impl::ListBinaryEvents(
    grpc::ServerContext *ctx,
    grpc::ServerReaderWriter<ratings::BinaryEvent, ratings::BinaryEventSource>
        *rw_stream) {
  std::cout << "Called ListBinaryEvents " << std::endl;

  ratings::BinaryEventSource binary_event_source;
  while (rw_stream->Read(&binary_event_source)) {
    uint64_t count{};
    std::string event_source = binary_event_source.event_source();
    auto events = evt_map.find(event_source);
    if (events != evt_map.end()) {
      auto events_v = events->second;
      std::for_each(
          events_v.begin(), events_v.end(),
          [rw_stream, count](const ratings::BinaryEvent &binary_event) mutable {
            rw_stream->Write(binary_event);
            count++;
          });
    }
    std::cout << "Total event count for source: " << event_source << " is "
              << count << ".\n";
  }

  return grpc::Status::OK;
}

grpc::Status ratings::ratings_server_impl::VoteBinaryEvent(
    grpc::ServerContext *ctx, const ratings::BinaryVote *vote,
    ratings::BinaryVoteSummary *summary) {
  std::cout << "Called VoteBinaryEvent " << std::endl;
  std::cout << vote->event_id() << std::endl;
  std::cout << vote->when() << std::endl;
  return grpc::Status::OK;
}

void ratings::run_server() {
  std::string srv_addr("localhost:50051");
  ratings::ratings_server_impl service;

  grpc::ServerBuilder builder;
  builder.AddListeningPort(srv_addr, grpc::InsecureServerCredentials());
  builder.RegisterService(&service);
  std::unique_ptr<grpc::Server> server(builder.BuildAndStart());
  std::cout << "ratings server up and running on: " << srv_addr << std::endl;
  server->Wait();
}

void ratings::start_async_processor() {
  ratings::Ratings::AsyncService *service;
  grpc::ServerCompletionQueue *serverQ;
  grpc::ServerContext ctx;
}
