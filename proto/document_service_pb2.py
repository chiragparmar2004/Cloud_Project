# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proto/document_service.proto
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
    'proto/document_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cproto/document_service.proto\x12\x08\x64ocument\"P\n\x15\x43reateDocumentRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x17\n\x0finitial_content\x18\x03 \x01(\t\">\n\x16\x43reateDocumentResponse\x12\x13\n\x0b\x64ocument_id\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\";\n\x13JoinDocumentRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x13\n\x0b\x64ocument_id\x18\x02 \x01(\t\"K\n\x14JoinDocumentResponse\x12\x13\n\x0b\x64ocument_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\"f\n\x13\x45\x64itDocumentRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x13\n\x0b\x64ocument_id\x18\x02 \x01(\t\x12\x16\n\x0e\x63ontent_change\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\t\"h\n\x14\x45\x64itDocumentResponse\x12\x13\n\x0b\x64ocument_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x17\n\x0fupdated_content\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\t\">\n\x16\x41\x64\x64\x45\x64itorStreamRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x13\n\x0b\x64ocument_id\x18\x02 \x01(\t\"*\n\x17\x41\x64\x64\x45\x64itorStreamResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xe0\x02\n\x0f\x44ocumentService\x12S\n\x0e\x43reateDocument\x12\x1f.document.CreateDocumentRequest\x1a .document.CreateDocumentResponse\x12M\n\x0cJoinDocument\x12\x1d.document.JoinDocumentRequest\x1a\x1e.document.JoinDocumentResponse\x12Q\n\x0c\x45\x64itDocument\x12\x1d.document.EditDocumentRequest\x1a\x1e.document.EditDocumentResponse(\x01\x30\x01\x12V\n\x0f\x41\x64\x64\x45\x64itorStream\x12 .document.AddEditorStreamRequest\x1a!.document.AddEditorStreamResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.document_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CREATEDOCUMENTREQUEST']._serialized_start=42
  _globals['_CREATEDOCUMENTREQUEST']._serialized_end=122
  _globals['_CREATEDOCUMENTRESPONSE']._serialized_start=124
  _globals['_CREATEDOCUMENTRESPONSE']._serialized_end=186
  _globals['_JOINDOCUMENTREQUEST']._serialized_start=188
  _globals['_JOINDOCUMENTREQUEST']._serialized_end=247
  _globals['_JOINDOCUMENTRESPONSE']._serialized_start=249
  _globals['_JOINDOCUMENTRESPONSE']._serialized_end=324
  _globals['_EDITDOCUMENTREQUEST']._serialized_start=326
  _globals['_EDITDOCUMENTREQUEST']._serialized_end=428
  _globals['_EDITDOCUMENTRESPONSE']._serialized_start=430
  _globals['_EDITDOCUMENTRESPONSE']._serialized_end=534
  _globals['_ADDEDITORSTREAMREQUEST']._serialized_start=536
  _globals['_ADDEDITORSTREAMREQUEST']._serialized_end=598
  _globals['_ADDEDITORSTREAMRESPONSE']._serialized_start=600
  _globals['_ADDEDITORSTREAMRESPONSE']._serialized_end=642
  _globals['_DOCUMENTSERVICE']._serialized_start=645
  _globals['_DOCUMENTSERVICE']._serialized_end=997
# @@protoc_insertion_point(module_scope)
