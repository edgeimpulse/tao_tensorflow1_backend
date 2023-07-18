# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nvidia_tao_tf1/cv/makenet/proto/model_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='nvidia_tao_tf1/cv/makenet/proto/model_config.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n2nvidia_tao_tf1/cv/makenet/proto/model_config.proto\"4\n\x0f\x42\x61tchNormConfig\x12\x10\n\x08momentum\x18\x01 \x01(\x02\x12\x0f\n\x07\x65psilon\x18\x02 \x01(\x02\"\xa8\x01\n\nActivation\x12\x17\n\x0f\x61\x63tivation_type\x18\x01 \x01(\t\x12\x44\n\x15\x61\x63tivation_parameters\x18\x02 \x03(\x0b\x32%.Activation.ActivationParametersEntry\x1a;\n\x19\x41\x63tivationParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\"\x8c\x03\n\x0bModelConfig\x12\x0c\n\x04\x61rch\x18\x01 \x01(\t\x12\x18\n\x10input_image_size\x18\x02 \x01(\t\x12\x39\n\x1bresize_interpolation_method\x18\x0c \x01(\x0e\x32\x14.InterpolationMethod\x12\x10\n\x08n_layers\x18\x03 \x01(\r\x12\x13\n\x0bretain_head\x18\x04 \x01(\x08\x12\x16\n\x0euse_batch_norm\x18\x05 \x01(\x08\x12\x10\n\x08use_bias\x18\x06 \x01(\x08\x12\x13\n\x0buse_pooling\x18\x07 \x01(\x08\x12\x17\n\x0f\x61ll_projections\x18\x08 \x01(\x08\x12\x11\n\tfreeze_bn\x18\t \x01(\x08\x12\x15\n\rfreeze_blocks\x18\n \x03(\r\x12\x0f\n\x07\x64ropout\x18\x0b \x01(\x02\x12+\n\x11\x62\x61tch_norm_config\x18\r \x01(\x0b\x32\x10.BatchNormConfig\x12\x1f\n\nactivation\x18\x0e \x01(\x0b\x32\x0b.Activation\x12\x12\n\nbyom_model\x18\x0f \x01(\t*0\n\x13InterpolationMethod\x12\x0c\n\x08\x42ILINEAR\x10\x00\x12\x0b\n\x07\x42ICUBIC\x10\x01\x62\x06proto3')
)

_INTERPOLATIONMETHOD = _descriptor.EnumDescriptor(
  name='InterpolationMethod',
  full_name='InterpolationMethod',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BILINEAR', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BICUBIC', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=678,
  serialized_end=726,
)
_sym_db.RegisterEnumDescriptor(_INTERPOLATIONMETHOD)

InterpolationMethod = enum_type_wrapper.EnumTypeWrapper(_INTERPOLATIONMETHOD)
BILINEAR = 0
BICUBIC = 1



_BATCHNORMCONFIG = _descriptor.Descriptor(
  name='BatchNormConfig',
  full_name='BatchNormConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='momentum', full_name='BatchNormConfig.momentum', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='epsilon', full_name='BatchNormConfig.epsilon', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=106,
)


_ACTIVATION_ACTIVATIONPARAMETERSENTRY = _descriptor.Descriptor(
  name='ActivationParametersEntry',
  full_name='Activation.ActivationParametersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Activation.ActivationParametersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='Activation.ActivationParametersEntry.value', index=1,
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
  serialized_start=218,
  serialized_end=277,
)

_ACTIVATION = _descriptor.Descriptor(
  name='Activation',
  full_name='Activation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='activation_type', full_name='Activation.activation_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activation_parameters', full_name='Activation.activation_parameters', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ACTIVATION_ACTIVATIONPARAMETERSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=277,
)


_MODELCONFIG = _descriptor.Descriptor(
  name='ModelConfig',
  full_name='ModelConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='arch', full_name='ModelConfig.arch', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input_image_size', full_name='ModelConfig.input_image_size', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resize_interpolation_method', full_name='ModelConfig.resize_interpolation_method', index=2,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n_layers', full_name='ModelConfig.n_layers', index=3,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retain_head', full_name='ModelConfig.retain_head', index=4,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_batch_norm', full_name='ModelConfig.use_batch_norm', index=5,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_bias', full_name='ModelConfig.use_bias', index=6,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_pooling', full_name='ModelConfig.use_pooling', index=7,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='all_projections', full_name='ModelConfig.all_projections', index=8,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='freeze_bn', full_name='ModelConfig.freeze_bn', index=9,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='freeze_blocks', full_name='ModelConfig.freeze_blocks', index=10,
      number=10, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dropout', full_name='ModelConfig.dropout', index=11,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch_norm_config', full_name='ModelConfig.batch_norm_config', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activation', full_name='ModelConfig.activation', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='byom_model', full_name='ModelConfig.byom_model', index=14,
      number=15, type=9, cpp_type=9, label=1,
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
  serialized_start=280,
  serialized_end=676,
)

_ACTIVATION_ACTIVATIONPARAMETERSENTRY.containing_type = _ACTIVATION
_ACTIVATION.fields_by_name['activation_parameters'].message_type = _ACTIVATION_ACTIVATIONPARAMETERSENTRY
_MODELCONFIG.fields_by_name['resize_interpolation_method'].enum_type = _INTERPOLATIONMETHOD
_MODELCONFIG.fields_by_name['batch_norm_config'].message_type = _BATCHNORMCONFIG
_MODELCONFIG.fields_by_name['activation'].message_type = _ACTIVATION
DESCRIPTOR.message_types_by_name['BatchNormConfig'] = _BATCHNORMCONFIG
DESCRIPTOR.message_types_by_name['Activation'] = _ACTIVATION
DESCRIPTOR.message_types_by_name['ModelConfig'] = _MODELCONFIG
DESCRIPTOR.enum_types_by_name['InterpolationMethod'] = _INTERPOLATIONMETHOD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BatchNormConfig = _reflection.GeneratedProtocolMessageType('BatchNormConfig', (_message.Message,), dict(
  DESCRIPTOR = _BATCHNORMCONFIG,
  __module__ = 'nvidia_tao_tf1.cv.makenet.proto.model_config_pb2'
  # @@protoc_insertion_point(class_scope:BatchNormConfig)
  ))
_sym_db.RegisterMessage(BatchNormConfig)

Activation = _reflection.GeneratedProtocolMessageType('Activation', (_message.Message,), dict(

  ActivationParametersEntry = _reflection.GeneratedProtocolMessageType('ActivationParametersEntry', (_message.Message,), dict(
    DESCRIPTOR = _ACTIVATION_ACTIVATIONPARAMETERSENTRY,
    __module__ = 'nvidia_tao_tf1.cv.makenet.proto.model_config_pb2'
    # @@protoc_insertion_point(class_scope:Activation.ActivationParametersEntry)
    ))
  ,
  DESCRIPTOR = _ACTIVATION,
  __module__ = 'nvidia_tao_tf1.cv.makenet.proto.model_config_pb2'
  # @@protoc_insertion_point(class_scope:Activation)
  ))
_sym_db.RegisterMessage(Activation)
_sym_db.RegisterMessage(Activation.ActivationParametersEntry)

ModelConfig = _reflection.GeneratedProtocolMessageType('ModelConfig', (_message.Message,), dict(
  DESCRIPTOR = _MODELCONFIG,
  __module__ = 'nvidia_tao_tf1.cv.makenet.proto.model_config_pb2'
  # @@protoc_insertion_point(class_scope:ModelConfig)
  ))
_sym_db.RegisterMessage(ModelConfig)


_ACTIVATION_ACTIVATIONPARAMETERSENTRY._options = None
# @@protoc_insertion_point(module_scope)
