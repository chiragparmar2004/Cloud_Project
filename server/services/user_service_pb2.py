# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proto/user_service.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'proto/user_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18proto/user_service.proto\x12\x04user\"4\n\x11\x43reateUserRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\"6\n\x12\x43reateUserResponse\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"!\n\x0eGetUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"C\n\x0fGetUserResponse\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"E\n\x11UpdateUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"%\n\x12UpdateUserResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xc7\x01\n\x0bUserService\x12?\n\nCreateUser\x12\x17.user.CreateUserRequest\x1a\x18.user.CreateUserResponse\x12\x36\n\x07GetUser\x12\x14.user.GetUserRequest\x1a\x15.user.GetUserResponse\x12?\n\nUpdateUser\x12\x17.user.UpdateUserRequest\x1a\x18.user.UpdateUserResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.user_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CREATEUSERREQUEST']._serialized_start=34
  _globals['_CREATEUSERREQUEST']._serialized_end=86
  _globals['_CREATEUSERRESPONSE']._serialized_start=88
  _globals['_CREATEUSERRESPONSE']._serialized_end=142
  _globals['_GETUSERREQUEST']._serialized_start=144
  _globals['_GETUSERREQUEST']._serialized_end=177
  _globals['_GETUSERRESPONSE']._serialized_start=179
  _globals['_GETUSERRESPONSE']._serialized_end=246
  _globals['_UPDATEUSERREQUEST']._serialized_start=248
  _globals['_UPDATEUSERREQUEST']._serialized_end=317
  _globals['_UPDATEUSERRESPONSE']._serialized_start=319
  _globals['_UPDATEUSERRESPONSE']._serialized_end=356
  _globals['_USERSERVICE']._serialized_start=359
  _globals['_USERSERVICE']._serialized_end=558
# @@protoc_insertion_point(module_scope)
