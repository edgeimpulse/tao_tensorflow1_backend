# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nvidia_tao_tf1/cv/detectnet_v2/proto/adam_optimizer_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='nvidia_tao_tf1/cv/detectnet_v2/proto/adam_optimizer_config.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n@nvidia_tao_tf1/cv/detectnet_v2/proto/adam_optimizer_config.proto\"D\n\x13\x41\x64\x61mOptimizerConfig\x12\x0f\n\x07\x65psilon\x18\x01 \x01(\x02\x12\r\n\x05\x62\x65ta1\x18\x02 \x01(\x02\x12\r\n\x05\x62\x65ta2\x18\x03 \x01(\x02\x62\x06proto3')
)




_ADAMOPTIMIZERCONFIG = _descriptor.Descriptor(
  name='AdamOptimizerConfig',
  full_name='AdamOptimizerConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='epsilon', full_name='AdamOptimizerConfig.epsilon', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='beta1', full_name='AdamOptimizerConfig.beta1', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='beta2', full_name='AdamOptimizerConfig.beta2', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=68,
  serialized_end=136,
)

DESCRIPTOR.message_types_by_name['AdamOptimizerConfig'] = _ADAMOPTIMIZERCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdamOptimizerConfig = _reflection.GeneratedProtocolMessageType('AdamOptimizerConfig', (_message.Message,), dict(
  DESCRIPTOR = _ADAMOPTIMIZERCONFIG,
  __module__ = 'nvidia_tao_tf1.cv.detectnet_v2.proto.adam_optimizer_config_pb2'
  # @@protoc_insertion_point(class_scope:AdamOptimizerConfig)
  ))
_sym_db.RegisterMessage(AdamOptimizerConfig)


# @@protoc_insertion_point(module_scope)