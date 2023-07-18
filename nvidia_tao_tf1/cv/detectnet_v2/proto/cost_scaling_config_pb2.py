# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nvidia_tao_tf1/cv/detectnet_v2/proto/cost_scaling_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='nvidia_tao_tf1/cv/detectnet_v2/proto/cost_scaling_config.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n>nvidia_tao_tf1/cv/detectnet_v2/proto/cost_scaling_config.proto\"d\n\x11\x43ostScalingConfig\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x18\n\x10initial_exponent\x18\x02 \x01(\x01\x12\x11\n\tincrement\x18\x03 \x01(\x01\x12\x11\n\tdecrement\x18\x04 \x01(\x01\x62\x06proto3')
)




_COSTSCALINGCONFIG = _descriptor.Descriptor(
  name='CostScalingConfig',
  full_name='CostScalingConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='CostScalingConfig.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initial_exponent', full_name='CostScalingConfig.initial_exponent', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='increment', full_name='CostScalingConfig.increment', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='decrement', full_name='CostScalingConfig.decrement', index=3,
      number=4, type=1, cpp_type=5, label=1,
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
  serialized_start=66,
  serialized_end=166,
)

DESCRIPTOR.message_types_by_name['CostScalingConfig'] = _COSTSCALINGCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CostScalingConfig = _reflection.GeneratedProtocolMessageType('CostScalingConfig', (_message.Message,), dict(
  DESCRIPTOR = _COSTSCALINGCONFIG,
  __module__ = 'nvidia_tao_tf1.cv.detectnet_v2.proto.cost_scaling_config_pb2'
  # @@protoc_insertion_point(class_scope:CostScalingConfig)
  ))
_sym_db.RegisterMessage(CostScalingConfig)


# @@protoc_insertion_point(module_scope)