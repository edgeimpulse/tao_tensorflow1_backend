# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nvidia_tao_tf1/cv/common/proto/soft_start_cosine_annealing_schedule_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='nvidia_tao_tf1/cv/common/proto/soft_start_cosine_annealing_schedule_config.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nPnvidia_tao_tf1/cv/common/proto/soft_start_cosine_annealing_schedule_config.proto\"r\n&SoftStartCosineAnnealingScheduleConfig\x12\x19\n\x11max_learning_rate\x18\x01 \x01(\x02\x12\x12\n\nsoft_start\x18\x02 \x01(\x02\x12\x19\n\x11min_learning_rate\x18\x03 \x01(\x02\x62\x06proto3')
)




_SOFTSTARTCOSINEANNEALINGSCHEDULECONFIG = _descriptor.Descriptor(
  name='SoftStartCosineAnnealingScheduleConfig',
  full_name='SoftStartCosineAnnealingScheduleConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_learning_rate', full_name='SoftStartCosineAnnealingScheduleConfig.max_learning_rate', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='soft_start', full_name='SoftStartCosineAnnealingScheduleConfig.soft_start', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_learning_rate', full_name='SoftStartCosineAnnealingScheduleConfig.min_learning_rate', index=2,
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
  serialized_start=84,
  serialized_end=198,
)

DESCRIPTOR.message_types_by_name['SoftStartCosineAnnealingScheduleConfig'] = _SOFTSTARTCOSINEANNEALINGSCHEDULECONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SoftStartCosineAnnealingScheduleConfig = _reflection.GeneratedProtocolMessageType('SoftStartCosineAnnealingScheduleConfig', (_message.Message,), dict(
  DESCRIPTOR = _SOFTSTARTCOSINEANNEALINGSCHEDULECONFIG,
  __module__ = 'nvidia_tao_tf1.cv.common.proto.soft_start_cosine_annealing_schedule_config_pb2'
  # @@protoc_insertion_point(class_scope:SoftStartCosineAnnealingScheduleConfig)
  ))
_sym_db.RegisterMessage(SoftStartCosineAnnealingScheduleConfig)


# @@protoc_insertion_point(module_scope)
