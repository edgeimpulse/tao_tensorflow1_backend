# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nvidia_tao_tf1/cv/detectnet_v2/proto/evaluation_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='nvidia_tao_tf1/cv/detectnet_v2/proto/evaluation_config.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n<nvidia_tao_tf1/cv/detectnet_v2/proto/evaluation_config.proto\"\xbe\x05\n\x10\x45valuationConfig\x12)\n!validation_period_during_training\x18\x01 \x01(\r\x12\x1e\n\x16\x66irst_validation_epoch\x18\x02 \x01(\r\x12%\n\x1d\x65\x61rly_stopping_patience_steps\x18\x06 \x01(\r\x12i\n&minimum_detection_ground_truth_overlap\x18\x03 \x03(\x0b\x32\x39.EvaluationConfig.MinimumDetectionGroundTruthOverlapEntry\x12I\n\x15\x65valuation_box_config\x18\x04 \x03(\x0b\x32*.EvaluationConfig.EvaluationBoxConfigEntry\x12\x39\n\x16\x61verage_precision_mode\x18\x05 \x01(\x0e\x32\x19.EvaluationConfig.AP_MODE\x1aI\n\'MinimumDetectionGroundTruthOverlapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\x1as\n\x13\x45valuationBoxConfig\x12\x16\n\x0eminimum_height\x18\x01 \x01(\x05\x12\x16\n\x0emaximum_height\x18\x02 \x01(\x05\x12\x15\n\rminimum_width\x18\x03 \x01(\x05\x12\x15\n\rmaximum_width\x18\x04 \x01(\x05\x1a\x61\n\x18\x45valuationBoxConfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.EvaluationConfig.EvaluationBoxConfig:\x02\x38\x01\"$\n\x07\x41P_MODE\x12\n\n\x06SAMPLE\x10\x00\x12\r\n\tINTEGRATE\x10\x01\x62\x06proto3')
)



_EVALUATIONCONFIG_AP_MODE = _descriptor.EnumDescriptor(
  name='AP_MODE',
  full_name='EvaluationConfig.AP_MODE',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SAMPLE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTEGRATE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=731,
  serialized_end=767,
)
_sym_db.RegisterEnumDescriptor(_EVALUATIONCONFIG_AP_MODE)


_EVALUATIONCONFIG_MINIMUMDETECTIONGROUNDTRUTHOVERLAPENTRY = _descriptor.Descriptor(
  name='MinimumDetectionGroundTruthOverlapEntry',
  full_name='EvaluationConfig.MinimumDetectionGroundTruthOverlapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='EvaluationConfig.MinimumDetectionGroundTruthOverlapEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='EvaluationConfig.MinimumDetectionGroundTruthOverlapEntry.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=440,
  serialized_end=513,
)

_EVALUATIONCONFIG_EVALUATIONBOXCONFIG = _descriptor.Descriptor(
  name='EvaluationBoxConfig',
  full_name='EvaluationConfig.EvaluationBoxConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='minimum_height', full_name='EvaluationConfig.EvaluationBoxConfig.minimum_height', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maximum_height', full_name='EvaluationConfig.EvaluationBoxConfig.maximum_height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minimum_width', full_name='EvaluationConfig.EvaluationBoxConfig.minimum_width', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maximum_width', full_name='EvaluationConfig.EvaluationBoxConfig.maximum_width', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=515,
  serialized_end=630,
)

_EVALUATIONCONFIG_EVALUATIONBOXCONFIGENTRY = _descriptor.Descriptor(
  name='EvaluationBoxConfigEntry',
  full_name='EvaluationConfig.EvaluationBoxConfigEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='EvaluationConfig.EvaluationBoxConfigEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='EvaluationConfig.EvaluationBoxConfigEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=632,
  serialized_end=729,
)

_EVALUATIONCONFIG = _descriptor.Descriptor(
  name='EvaluationConfig',
  full_name='EvaluationConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='validation_period_during_training', full_name='EvaluationConfig.validation_period_during_training', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_validation_epoch', full_name='EvaluationConfig.first_validation_epoch', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='early_stopping_patience_steps', full_name='EvaluationConfig.early_stopping_patience_steps', index=2,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minimum_detection_ground_truth_overlap', full_name='EvaluationConfig.minimum_detection_ground_truth_overlap', index=3,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='evaluation_box_config', full_name='EvaluationConfig.evaluation_box_config', index=4,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='average_precision_mode', full_name='EvaluationConfig.average_precision_mode', index=5,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EVALUATIONCONFIG_MINIMUMDETECTIONGROUNDTRUTHOVERLAPENTRY, _EVALUATIONCONFIG_EVALUATIONBOXCONFIG, _EVALUATIONCONFIG_EVALUATIONBOXCONFIGENTRY, ],
  enum_types=[
    _EVALUATIONCONFIG_AP_MODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=767,
)

_EVALUATIONCONFIG_MINIMUMDETECTIONGROUNDTRUTHOVERLAPENTRY.containing_type = _EVALUATIONCONFIG
_EVALUATIONCONFIG_EVALUATIONBOXCONFIG.containing_type = _EVALUATIONCONFIG
_EVALUATIONCONFIG_EVALUATIONBOXCONFIGENTRY.fields_by_name['value'].message_type = _EVALUATIONCONFIG_EVALUATIONBOXCONFIG
_EVALUATIONCONFIG_EVALUATIONBOXCONFIGENTRY.containing_type = _EVALUATIONCONFIG
_EVALUATIONCONFIG.fields_by_name['minimum_detection_ground_truth_overlap'].message_type = _EVALUATIONCONFIG_MINIMUMDETECTIONGROUNDTRUTHOVERLAPENTRY
_EVALUATIONCONFIG.fields_by_name['evaluation_box_config'].message_type = _EVALUATIONCONFIG_EVALUATIONBOXCONFIGENTRY
_EVALUATIONCONFIG.fields_by_name['average_precision_mode'].enum_type = _EVALUATIONCONFIG_AP_MODE
_EVALUATIONCONFIG_AP_MODE.containing_type = _EVALUATIONCONFIG
DESCRIPTOR.message_types_by_name['EvaluationConfig'] = _EVALUATIONCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EvaluationConfig = _reflection.GeneratedProtocolMessageType('EvaluationConfig', (_message.Message,), dict(

  MinimumDetectionGroundTruthOverlapEntry = _reflection.GeneratedProtocolMessageType('MinimumDetectionGroundTruthOverlapEntry', (_message.Message,), dict(
    DESCRIPTOR = _EVALUATIONCONFIG_MINIMUMDETECTIONGROUNDTRUTHOVERLAPENTRY,
    __module__ = 'nvidia_tao_tf1.cv.detectnet_v2.proto.evaluation_config_pb2'
    # @@protoc_insertion_point(class_scope:EvaluationConfig.MinimumDetectionGroundTruthOverlapEntry)
    ))
  ,

  EvaluationBoxConfig = _reflection.GeneratedProtocolMessageType('EvaluationBoxConfig', (_message.Message,), dict(
    DESCRIPTOR = _EVALUATIONCONFIG_EVALUATIONBOXCONFIG,
    __module__ = 'nvidia_tao_tf1.cv.detectnet_v2.proto.evaluation_config_pb2'
    # @@protoc_insertion_point(class_scope:EvaluationConfig.EvaluationBoxConfig)
    ))
  ,

  EvaluationBoxConfigEntry = _reflection.GeneratedProtocolMessageType('EvaluationBoxConfigEntry', (_message.Message,), dict(
    DESCRIPTOR = _EVALUATIONCONFIG_EVALUATIONBOXCONFIGENTRY,
    __module__ = 'nvidia_tao_tf1.cv.detectnet_v2.proto.evaluation_config_pb2'
    # @@protoc_insertion_point(class_scope:EvaluationConfig.EvaluationBoxConfigEntry)
    ))
  ,
  DESCRIPTOR = _EVALUATIONCONFIG,
  __module__ = 'nvidia_tao_tf1.cv.detectnet_v2.proto.evaluation_config_pb2'
  # @@protoc_insertion_point(class_scope:EvaluationConfig)
  ))
_sym_db.RegisterMessage(EvaluationConfig)
_sym_db.RegisterMessage(EvaluationConfig.MinimumDetectionGroundTruthOverlapEntry)
_sym_db.RegisterMessage(EvaluationConfig.EvaluationBoxConfig)
_sym_db.RegisterMessage(EvaluationConfig.EvaluationBoxConfigEntry)


_EVALUATIONCONFIG_MINIMUMDETECTIONGROUNDTRUTHOVERLAPENTRY._options = None
_EVALUATIONCONFIG_EVALUATIONBOXCONFIGENTRY._options = None
# @@protoc_insertion_point(module_scope)
