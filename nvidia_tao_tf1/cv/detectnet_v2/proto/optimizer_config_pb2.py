# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nvidia_tao_tf1/cv/detectnet_v2/proto/optimizer_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from nvidia_tao_tf1.cv.detectnet_v2.proto import adam_optimizer_config_pb2 as nvidia__tao__tf1_dot_cv_dot_detectnet__v2_dot_proto_dot_adam__optimizer__config__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='nvidia_tao_tf1/cv/detectnet_v2/proto/optimizer_config.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n;nvidia_tao_tf1/cv/detectnet_v2/proto/optimizer_config.proto\x1a@nvidia_tao_tf1/cv/detectnet_v2/proto/adam_optimizer_config.proto\"D\n\x0fOptimizerConfig\x12$\n\x04\x61\x64\x61m\x18\x01 \x01(\x0b\x32\x14.AdamOptimizerConfigH\x00\x42\x0b\n\toptimizerb\x06proto3')
  ,
  dependencies=[nvidia__tao__tf1_dot_cv_dot_detectnet__v2_dot_proto_dot_adam__optimizer__config__pb2.DESCRIPTOR,])




_OPTIMIZERCONFIG = _descriptor.Descriptor(
  name='OptimizerConfig',
  full_name='OptimizerConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='adam', full_name='OptimizerConfig.adam', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='optimizer', full_name='OptimizerConfig.optimizer',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=129,
  serialized_end=197,
)

_OPTIMIZERCONFIG.fields_by_name['adam'].message_type = nvidia__tao__tf1_dot_cv_dot_detectnet__v2_dot_proto_dot_adam__optimizer__config__pb2._ADAMOPTIMIZERCONFIG
_OPTIMIZERCONFIG.oneofs_by_name['optimizer'].fields.append(
  _OPTIMIZERCONFIG.fields_by_name['adam'])
_OPTIMIZERCONFIG.fields_by_name['adam'].containing_oneof = _OPTIMIZERCONFIG.oneofs_by_name['optimizer']
DESCRIPTOR.message_types_by_name['OptimizerConfig'] = _OPTIMIZERCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OptimizerConfig = _reflection.GeneratedProtocolMessageType('OptimizerConfig', (_message.Message,), dict(
  DESCRIPTOR = _OPTIMIZERCONFIG,
  __module__ = 'nvidia_tao_tf1.cv.detectnet_v2.proto.optimizer_config_pb2'
  # @@protoc_insertion_point(class_scope:OptimizerConfig)
  ))
_sym_db.RegisterMessage(OptimizerConfig)


# @@protoc_insertion_point(module_scope)