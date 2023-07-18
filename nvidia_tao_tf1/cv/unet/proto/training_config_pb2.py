# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nvidia_tao_tf1/cv/unet/proto/training_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from nvidia_tao_tf1.cv.unet.proto import optimizer_config_pb2 as nvidia__tao__tf1_dot_cv_dot_unet_dot_proto_dot_optimizer__config__pb2
from nvidia_tao_tf1.cv.unet.proto import regularizer_config_pb2 as nvidia__tao__tf1_dot_cv_dot_unet_dot_proto_dot_regularizer__config__pb2
from nvidia_tao_tf1.cv.unet.proto import visualizer_config_pb2 as nvidia__tao__tf1_dot_cv_dot_unet_dot_proto_dot_visualizer__config__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='nvidia_tao_tf1/cv/unet/proto/training_config.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n2nvidia_tao_tf1/cv/unet/proto/training_config.proto\x1a\x33nvidia_tao_tf1/cv/unet/proto/optimizer_config.proto\x1a\x35nvidia_tao_tf1/cv/unet/proto/regularizer_config.proto\x1a\x34nvidia_tao_tf1/cv/unet/proto/visualizer_config.proto\"\xd9\x06\n\x0eTrainingConfig\x12\x12\n\nbatch_size\x18\x01 \x01(\r\x12\x12\n\nnum_epochs\x18\x02 \x01(\r\x12\'\n\x0bregularizer\x18\x04 \x01(\x0b\x32\x12.RegularizerConfig\x12#\n\toptimizer\x18\x05 \x01(\x0b\x32\x10.OptimizerConfig\x12\x1b\n\x13\x63heckpoint_interval\x18\x07 \x01(\r\x12\x11\n\tmax_steps\x18\x08 \x01(\r\x12\x0e\n\x06\x65pochs\x18\x13 \x01(\r\x12\x19\n\x11log_summary_steps\x18\t \x01(\r\x12\x0f\n\x07\x61ugment\x18\n \x01(\x08\x12\x0f\n\x07use_xla\x18\x0b \x01(\x08\x12\x14\n\x0cwarmup_steps\x18\x0c \x01(\r\x12\x0f\n\x07use_amp\x18\r \x01(\x08\x12\x15\n\rlearning_rate\x18\x0e \x01(\x02\x12\x14\n\x0cweight_decay\x18\x0f \x01(\x02\x12\x0f\n\x07use_trt\x18\x10 \x01(\x08\x12\x1b\n\x13\x63rossvalidation_idx\x18\x11 \x01(\x08\x12\x0c\n\x04loss\x18\x12 \x01(\t\x12\x17\n\x0fweights_monitor\x18\x17 \x01(\x08\x12\x37\n\x0clr_scheduler\x18\x19 \x01(\x0b\x32!.TrainingConfig.LRSchedulerConfig\x12%\n\nvisualizer\x18\x1b \x01(\x0b\x32\x11.VisualizerConfig\x12\x13\n\x0b\x62uffer_size\x18\x1c \x01(\r\x12\x14\n\x0c\x64\x61ta_options\x18\x1d \x01(\x08\x1a\x37\n\x11\x43osineDecayConfig\x12\r\n\x05\x61lpha\x18\x01 \x01(\x02\x12\x13\n\x0b\x64\x65\x63\x61y_steps\x18\x02 \x01(\x05\x1a\x41\n\x16\x45xponentialDecayConfig\x12\x12\n\ndecay_rate\x18\x01 \x01(\x02\x12\x13\n\x0b\x64\x65\x63\x61y_steps\x18\x02 \x01(\x05\x1a\xa3\x01\n\x11LRSchedulerConfig\x12\x43\n\x11\x65xponential_decay\x18\x01 \x01(\x0b\x32&.TrainingConfig.ExponentialDecayConfigH\x00\x12\x39\n\x0c\x63osine_decay\x18\x02 \x01(\x0b\x32!.TrainingConfig.CosineDecayConfigH\x00\x42\x0e\n\x0clr_schedulerb\x06proto3')
  ,
  dependencies=[nvidia__tao__tf1_dot_cv_dot_unet_dot_proto_dot_optimizer__config__pb2.DESCRIPTOR,nvidia__tao__tf1_dot_cv_dot_unet_dot_proto_dot_regularizer__config__pb2.DESCRIPTOR,nvidia__tao__tf1_dot_cv_dot_unet_dot_proto_dot_visualizer__config__pb2.DESCRIPTOR,])




_TRAININGCONFIG_COSINEDECAYCONFIG = _descriptor.Descriptor(
  name='CosineDecayConfig',
  full_name='TrainingConfig.CosineDecayConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='alpha', full_name='TrainingConfig.CosineDecayConfig.alpha', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='decay_steps', full_name='TrainingConfig.CosineDecayConfig.decay_steps', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=786,
  serialized_end=841,
)

_TRAININGCONFIG_EXPONENTIALDECAYCONFIG = _descriptor.Descriptor(
  name='ExponentialDecayConfig',
  full_name='TrainingConfig.ExponentialDecayConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='decay_rate', full_name='TrainingConfig.ExponentialDecayConfig.decay_rate', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='decay_steps', full_name='TrainingConfig.ExponentialDecayConfig.decay_steps', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=843,
  serialized_end=908,
)

_TRAININGCONFIG_LRSCHEDULERCONFIG = _descriptor.Descriptor(
  name='LRSchedulerConfig',
  full_name='TrainingConfig.LRSchedulerConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='exponential_decay', full_name='TrainingConfig.LRSchedulerConfig.exponential_decay', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cosine_decay', full_name='TrainingConfig.LRSchedulerConfig.cosine_decay', index=1,
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
    _descriptor.OneofDescriptor(
      name='lr_scheduler', full_name='TrainingConfig.LRSchedulerConfig.lr_scheduler',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=911,
  serialized_end=1074,
)

_TRAININGCONFIG = _descriptor.Descriptor(
  name='TrainingConfig',
  full_name='TrainingConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='TrainingConfig.batch_size', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_epochs', full_name='TrainingConfig.num_epochs', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='regularizer', full_name='TrainingConfig.regularizer', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='optimizer', full_name='TrainingConfig.optimizer', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkpoint_interval', full_name='TrainingConfig.checkpoint_interval', index=4,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_steps', full_name='TrainingConfig.max_steps', index=5,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='epochs', full_name='TrainingConfig.epochs', index=6,
      number=19, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_summary_steps', full_name='TrainingConfig.log_summary_steps', index=7,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='augment', full_name='TrainingConfig.augment', index=8,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_xla', full_name='TrainingConfig.use_xla', index=9,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='warmup_steps', full_name='TrainingConfig.warmup_steps', index=10,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_amp', full_name='TrainingConfig.use_amp', index=11,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='learning_rate', full_name='TrainingConfig.learning_rate', index=12,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight_decay', full_name='TrainingConfig.weight_decay', index=13,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_trt', full_name='TrainingConfig.use_trt', index=14,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='crossvalidation_idx', full_name='TrainingConfig.crossvalidation_idx', index=15,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loss', full_name='TrainingConfig.loss', index=16,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weights_monitor', full_name='TrainingConfig.weights_monitor', index=17,
      number=23, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lr_scheduler', full_name='TrainingConfig.lr_scheduler', index=18,
      number=25, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visualizer', full_name='TrainingConfig.visualizer', index=19,
      number=27, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buffer_size', full_name='TrainingConfig.buffer_size', index=20,
      number=28, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_options', full_name='TrainingConfig.data_options', index=21,
      number=29, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TRAININGCONFIG_COSINEDECAYCONFIG, _TRAININGCONFIG_EXPONENTIALDECAYCONFIG, _TRAININGCONFIG_LRSCHEDULERCONFIG, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=217,
  serialized_end=1074,
)

_TRAININGCONFIG_COSINEDECAYCONFIG.containing_type = _TRAININGCONFIG
_TRAININGCONFIG_EXPONENTIALDECAYCONFIG.containing_type = _TRAININGCONFIG
_TRAININGCONFIG_LRSCHEDULERCONFIG.fields_by_name['exponential_decay'].message_type = _TRAININGCONFIG_EXPONENTIALDECAYCONFIG
_TRAININGCONFIG_LRSCHEDULERCONFIG.fields_by_name['cosine_decay'].message_type = _TRAININGCONFIG_COSINEDECAYCONFIG
_TRAININGCONFIG_LRSCHEDULERCONFIG.containing_type = _TRAININGCONFIG
_TRAININGCONFIG_LRSCHEDULERCONFIG.oneofs_by_name['lr_scheduler'].fields.append(
  _TRAININGCONFIG_LRSCHEDULERCONFIG.fields_by_name['exponential_decay'])
_TRAININGCONFIG_LRSCHEDULERCONFIG.fields_by_name['exponential_decay'].containing_oneof = _TRAININGCONFIG_LRSCHEDULERCONFIG.oneofs_by_name['lr_scheduler']
_TRAININGCONFIG_LRSCHEDULERCONFIG.oneofs_by_name['lr_scheduler'].fields.append(
  _TRAININGCONFIG_LRSCHEDULERCONFIG.fields_by_name['cosine_decay'])
_TRAININGCONFIG_LRSCHEDULERCONFIG.fields_by_name['cosine_decay'].containing_oneof = _TRAININGCONFIG_LRSCHEDULERCONFIG.oneofs_by_name['lr_scheduler']
_TRAININGCONFIG.fields_by_name['regularizer'].message_type = nvidia__tao__tf1_dot_cv_dot_unet_dot_proto_dot_regularizer__config__pb2._REGULARIZERCONFIG
_TRAININGCONFIG.fields_by_name['optimizer'].message_type = nvidia__tao__tf1_dot_cv_dot_unet_dot_proto_dot_optimizer__config__pb2._OPTIMIZERCONFIG
_TRAININGCONFIG.fields_by_name['lr_scheduler'].message_type = _TRAININGCONFIG_LRSCHEDULERCONFIG
_TRAININGCONFIG.fields_by_name['visualizer'].message_type = nvidia__tao__tf1_dot_cv_dot_unet_dot_proto_dot_visualizer__config__pb2._VISUALIZERCONFIG
DESCRIPTOR.message_types_by_name['TrainingConfig'] = _TRAININGCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TrainingConfig = _reflection.GeneratedProtocolMessageType('TrainingConfig', (_message.Message,), dict(

  CosineDecayConfig = _reflection.GeneratedProtocolMessageType('CosineDecayConfig', (_message.Message,), dict(
    DESCRIPTOR = _TRAININGCONFIG_COSINEDECAYCONFIG,
    __module__ = 'nvidia_tao_tf1.cv.unet.proto.training_config_pb2'
    # @@protoc_insertion_point(class_scope:TrainingConfig.CosineDecayConfig)
    ))
  ,

  ExponentialDecayConfig = _reflection.GeneratedProtocolMessageType('ExponentialDecayConfig', (_message.Message,), dict(
    DESCRIPTOR = _TRAININGCONFIG_EXPONENTIALDECAYCONFIG,
    __module__ = 'nvidia_tao_tf1.cv.unet.proto.training_config_pb2'
    # @@protoc_insertion_point(class_scope:TrainingConfig.ExponentialDecayConfig)
    ))
  ,

  LRSchedulerConfig = _reflection.GeneratedProtocolMessageType('LRSchedulerConfig', (_message.Message,), dict(
    DESCRIPTOR = _TRAININGCONFIG_LRSCHEDULERCONFIG,
    __module__ = 'nvidia_tao_tf1.cv.unet.proto.training_config_pb2'
    # @@protoc_insertion_point(class_scope:TrainingConfig.LRSchedulerConfig)
    ))
  ,
  DESCRIPTOR = _TRAININGCONFIG,
  __module__ = 'nvidia_tao_tf1.cv.unet.proto.training_config_pb2'
  # @@protoc_insertion_point(class_scope:TrainingConfig)
  ))
_sym_db.RegisterMessage(TrainingConfig)
_sym_db.RegisterMessage(TrainingConfig.CosineDecayConfig)
_sym_db.RegisterMessage(TrainingConfig.ExponentialDecayConfig)
_sym_db.RegisterMessage(TrainingConfig.LRSchedulerConfig)


# @@protoc_insertion_point(module_scope)