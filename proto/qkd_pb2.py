# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: qkd.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'qkd.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tqkd.proto\x12\x03qkd\"P\n\x12OpenConnectRequest\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x02 \x01(\t\x12\x15\n\rkey_stream_id\x18\x03 \x01(\t\"<\n\x13OpenConnectResponse\x12\x15\n\rkey_stream_id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\"5\n\rGetKeyRequest\x12\x15\n\rkey_stream_id\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\x05\"-\n\x0eGetKeyResponse\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\"/\n\x16\x43loseConnectionRequest\x12\x15\n\rkey_stream_id\x18\x01 \x01(\t\")\n\x17\x43loseConnectionResponse\x12\x0e\n\x06status\x18\x01 \x01(\t2\xcf\x01\n\nKeyManager\x12@\n\x0bOpenConnect\x12\x17.qkd.OpenConnectRequest\x1a\x18.qkd.OpenConnectResponse\x12\x31\n\x06GetKey\x12\x12.qkd.GetKeyRequest\x1a\x13.qkd.GetKeyResponse\x12L\n\x0f\x43loseConnection\x12\x1b.qkd.CloseConnectionRequest\x1a\x1c.qkd.CloseConnectionResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'qkd_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_OPENCONNECTREQUEST']._serialized_start=18
  _globals['_OPENCONNECTREQUEST']._serialized_end=98
  _globals['_OPENCONNECTRESPONSE']._serialized_start=100
  _globals['_OPENCONNECTRESPONSE']._serialized_end=160
  _globals['_GETKEYREQUEST']._serialized_start=162
  _globals['_GETKEYREQUEST']._serialized_end=215
  _globals['_GETKEYRESPONSE']._serialized_start=217
  _globals['_GETKEYRESPONSE']._serialized_end=262
  _globals['_CLOSECONNECTIONREQUEST']._serialized_start=264
  _globals['_CLOSECONNECTIONREQUEST']._serialized_end=311
  _globals['_CLOSECONNECTIONRESPONSE']._serialized_start=313
  _globals['_CLOSECONNECTIONRESPONSE']._serialized_end=354
  _globals['_KEYMANAGER']._serialized_start=357
  _globals['_KEYMANAGER']._serialized_end=564
# @@protoc_insertion_point(module_scope)
