# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ratings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ratings.proto',
  package='ratings',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rratings.proto\x12\x07ratings\"\xf8\x01\n\x0b\x42inaryEvent\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\x04\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x12\x12\n\nevent_data\x18\x03 \x01(\x0c\x12\x14\n\x0c\x65vent_source\x18\x04 \x01(\t\x12\x12\n\nratings_up\x18\x05 \x01(\x04\x12\x14\n\x0cratings_down\x18\x06 \x01(\x04\x12\x34\n\x07ratings\x18\x07 \x03(\x0b\x32#.ratings.BinaryEvent.UserRatingPair\x1a@\n\x0eUserRatingPair\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12!\n\x04vote\x18\x02 \x01(\x0b\x32\x13.ratings.BinaryVote\")\n\x11\x42inaryEventSource\x12\x14\n\x0c\x65vent_source\x18\x01 \x01(\t\"{\n\nBinaryVote\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\x04\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x12&\n\x04type\x18\x03 \x01(\x0e\x32\x18.ratings.BinaryVote.Type\x12\x0c\n\x04when\x18\x04 \x01(\x04\"\x18\n\x04Type\x12\x06\n\x02up\x10\x00\x12\x08\n\x04\x64own\x10\x01\"$\n\x13\x42inaryEventsSummary\x12\r\n\x05\x63ount\x18\x01 \x01(\x04\"4\n\x11\x42inaryVoteSummary\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2\xe9\x01\n\x07Ratings\x12L\n\x12RecordBinaryEvents\x12\x14.ratings.BinaryEvent\x1a\x1c.ratings.BinaryEventsSummary\"\x00(\x01\x12J\n\x10ListBinaryEvents\x12\x1a.ratings.BinaryEventSource\x1a\x14.ratings.BinaryEvent\"\x00(\x01\x30\x01\x12\x44\n\x0fVoteBinaryEvent\x12\x13.ratings.BinaryVote\x1a\x1a.ratings.BinaryVoteSummary\"\x00\x62\x06proto3')
)



_BINARYVOTE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='ratings.BinaryVote.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='up', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='down', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=419,
  serialized_end=443,
)
_sym_db.RegisterEnumDescriptor(_BINARYVOTE_TYPE)


_BINARYEVENT_USERRATINGPAIR = _descriptor.Descriptor(
  name='UserRatingPair',
  full_name='ratings.BinaryEvent.UserRatingPair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ratings.BinaryEvent.UserRatingPair.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vote', full_name='ratings.BinaryEvent.UserRatingPair.vote', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=275,
)

_BINARYEVENT = _descriptor.Descriptor(
  name='BinaryEvent',
  full_name='ratings.BinaryEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_id', full_name='ratings.BinaryEvent.event_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='ratings.BinaryEvent.key', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_data', full_name='ratings.BinaryEvent.event_data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_source', full_name='ratings.BinaryEvent.event_source', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ratings_up', full_name='ratings.BinaryEvent.ratings_up', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ratings_down', full_name='ratings.BinaryEvent.ratings_down', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ratings', full_name='ratings.BinaryEvent.ratings', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BINARYEVENT_USERRATINGPAIR, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=275,
)


_BINARYEVENTSOURCE = _descriptor.Descriptor(
  name='BinaryEventSource',
  full_name='ratings.BinaryEventSource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_source', full_name='ratings.BinaryEventSource.event_source', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=277,
  serialized_end=318,
)


_BINARYVOTE = _descriptor.Descriptor(
  name='BinaryVote',
  full_name='ratings.BinaryVote',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_id', full_name='ratings.BinaryVote.event_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='ratings.BinaryVote.key', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='ratings.BinaryVote.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='when', full_name='ratings.BinaryVote.when', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BINARYVOTE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=320,
  serialized_end=443,
)


_BINARYEVENTSSUMMARY = _descriptor.Descriptor(
  name='BinaryEventsSummary',
  full_name='ratings.BinaryEventsSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='ratings.BinaryEventsSummary.count', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=445,
  serialized_end=481,
)


_BINARYVOTESUMMARY = _descriptor.Descriptor(
  name='BinaryVoteSummary',
  full_name='ratings.BinaryVoteSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ratings.BinaryVoteSummary.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='ratings.BinaryVoteSummary.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=483,
  serialized_end=535,
)

_BINARYEVENT_USERRATINGPAIR.fields_by_name['vote'].message_type = _BINARYVOTE
_BINARYEVENT_USERRATINGPAIR.containing_type = _BINARYEVENT
_BINARYEVENT.fields_by_name['ratings'].message_type = _BINARYEVENT_USERRATINGPAIR
_BINARYVOTE.fields_by_name['type'].enum_type = _BINARYVOTE_TYPE
_BINARYVOTE_TYPE.containing_type = _BINARYVOTE
DESCRIPTOR.message_types_by_name['BinaryEvent'] = _BINARYEVENT
DESCRIPTOR.message_types_by_name['BinaryEventSource'] = _BINARYEVENTSOURCE
DESCRIPTOR.message_types_by_name['BinaryVote'] = _BINARYVOTE
DESCRIPTOR.message_types_by_name['BinaryEventsSummary'] = _BINARYEVENTSSUMMARY
DESCRIPTOR.message_types_by_name['BinaryVoteSummary'] = _BINARYVOTESUMMARY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BinaryEvent = _reflection.GeneratedProtocolMessageType('BinaryEvent', (_message.Message,), dict(

  UserRatingPair = _reflection.GeneratedProtocolMessageType('UserRatingPair', (_message.Message,), dict(
    DESCRIPTOR = _BINARYEVENT_USERRATINGPAIR,
    __module__ = 'ratings_pb2'
    # @@protoc_insertion_point(class_scope:ratings.BinaryEvent.UserRatingPair)
    ))
  ,
  DESCRIPTOR = _BINARYEVENT,
  __module__ = 'ratings_pb2'
  # @@protoc_insertion_point(class_scope:ratings.BinaryEvent)
  ))
_sym_db.RegisterMessage(BinaryEvent)
_sym_db.RegisterMessage(BinaryEvent.UserRatingPair)

BinaryEventSource = _reflection.GeneratedProtocolMessageType('BinaryEventSource', (_message.Message,), dict(
  DESCRIPTOR = _BINARYEVENTSOURCE,
  __module__ = 'ratings_pb2'
  # @@protoc_insertion_point(class_scope:ratings.BinaryEventSource)
  ))
_sym_db.RegisterMessage(BinaryEventSource)

BinaryVote = _reflection.GeneratedProtocolMessageType('BinaryVote', (_message.Message,), dict(
  DESCRIPTOR = _BINARYVOTE,
  __module__ = 'ratings_pb2'
  # @@protoc_insertion_point(class_scope:ratings.BinaryVote)
  ))
_sym_db.RegisterMessage(BinaryVote)

BinaryEventsSummary = _reflection.GeneratedProtocolMessageType('BinaryEventsSummary', (_message.Message,), dict(
  DESCRIPTOR = _BINARYEVENTSSUMMARY,
  __module__ = 'ratings_pb2'
  # @@protoc_insertion_point(class_scope:ratings.BinaryEventsSummary)
  ))
_sym_db.RegisterMessage(BinaryEventsSummary)

BinaryVoteSummary = _reflection.GeneratedProtocolMessageType('BinaryVoteSummary', (_message.Message,), dict(
  DESCRIPTOR = _BINARYVOTESUMMARY,
  __module__ = 'ratings_pb2'
  # @@protoc_insertion_point(class_scope:ratings.BinaryVoteSummary)
  ))
_sym_db.RegisterMessage(BinaryVoteSummary)



_RATINGS = _descriptor.ServiceDescriptor(
  name='Ratings',
  full_name='ratings.Ratings',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=538,
  serialized_end=771,
  methods=[
  _descriptor.MethodDescriptor(
    name='RecordBinaryEvents',
    full_name='ratings.Ratings.RecordBinaryEvents',
    index=0,
    containing_service=None,
    input_type=_BINARYEVENT,
    output_type=_BINARYEVENTSSUMMARY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListBinaryEvents',
    full_name='ratings.Ratings.ListBinaryEvents',
    index=1,
    containing_service=None,
    input_type=_BINARYEVENTSOURCE,
    output_type=_BINARYEVENT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='VoteBinaryEvent',
    full_name='ratings.Ratings.VoteBinaryEvent',
    index=2,
    containing_service=None,
    input_type=_BINARYVOTE,
    output_type=_BINARYVOTESUMMARY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RATINGS)

DESCRIPTOR.services_by_name['Ratings'] = _RATINGS

# @@protoc_insertion_point(module_scope)