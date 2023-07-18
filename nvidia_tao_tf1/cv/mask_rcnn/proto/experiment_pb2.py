# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nvidia_tao_tf1/cv/mask_rcnn/proto/experiment.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from nvidia_tao_tf1.cv.mask_rcnn.proto import maskrcnn_config_pb2 as nvidia__tao__tf1_dot_cv_dot_mask__rcnn_dot_proto_dot_maskrcnn__config__pb2
from nvidia_tao_tf1.cv.mask_rcnn.proto import data_config_pb2 as nvidia__tao__tf1_dot_cv_dot_mask__rcnn_dot_proto_dot_data__config__pb2
from nvidia_tao_tf1.cv.common.proto import clearml_config_pb2 as nvidia__tao__tf1_dot_cv_dot_common_dot_proto_dot_clearml__config__pb2
from nvidia_tao_tf1.cv.common.proto import wandb_config_pb2 as nvidia__tao__tf1_dot_cv_dot_common_dot_proto_dot_wandb__config__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='nvidia_tao_tf1/cv/mask_rcnn/proto/experiment.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n2nvidia_tao_tf1/cv/mask_rcnn/proto/experiment.proto\x1a\x37nvidia_tao_tf1/cv/mask_rcnn/proto/maskrcnn_config.proto\x1a\x33nvidia_tao_tf1/cv/mask_rcnn/proto/data_config.proto\x1a\x33nvidia_tao_tf1/cv/common/proto/clearml_config.proto\x1a\x31nvidia_tao_tf1/cv/common/proto/wandb_config.proto\"\x9d\x06\n\nExperiment\x12(\n\x0fmaskrcnn_config\x18\x01 \x01(\x0b\x32\x0f.MaskRCNNConfig\x12 \n\x0b\x64\x61ta_config\x18\x02 \x01(\x0b\x32\x0b.DataConfig\x12!\n\x19skip_checkpoint_variables\x18\x03 \x01(\t\x12\x18\n\x10train_batch_size\x18\x05 \x01(\r\x12\x1e\n\x16save_checkpoints_steps\x18\x06 \x01(\r\x12\x1a\n\x12num_steps_per_eval\x18\x07 \x01(\r\x12\x10\n\x08momentum\x18\x08 \x01(\x02\x12\x17\n\x0fl2_weight_decay\x18\n \x01(\x02\x12\x1c\n\x14warmup_learning_rate\x18\x0b \x01(\x02\x12\x1a\n\x12init_learning_rate\x18\x0c \x01(\x02\x12\"\n\x1aglobal_gradient_clip_ratio\x18\r \x01(\x02\x12\x13\n\x0btotal_steps\x18\x0e \x01(\r\x12 \n\x18visualize_images_summary\x18\x0f \x01(\x08\x12\x12\n\ncheckpoint\x18\x13 \x01(\t\x12\x17\n\x0f\x65val_batch_size\x18\x14 \x01(\r\x12\x14\n\x0cwarmup_steps\x18\x15 \x01(\r\x12\x1b\n\x13learning_rate_steps\x18\x16 \x01(\t\x12\"\n\x1alearning_rate_decay_levels\x18\x17 \x01(\t\x12\x0c\n\x04seed\x18\x18 \x01(\r\x12\x18\n\x10report_frequency\x18\x19 \x01(\r\x12\x0f\n\x07use_amp\x18\x1a \x01(\x08\x12\x19\n\x11pruned_model_path\x18\x1b \x01(\t\x12\x17\n\x0fl1_weight_decay\x18\x1c \x01(\x02\x12\x12\n\nnum_epochs\x18\x1d \x01(\r\x12\x1e\n\x16num_examples_per_epoch\x18\x1e \x01(\r\x12\x19\n\x11logging_frequency\x18\x1f \x01(\r\x12\"\n\x0cwandb_config\x18  \x01(\x0b\x32\x0c.WandBConfig\x12&\n\x0e\x63learml_config\x18! \x01(\x0b\x32\x0e.ClearMLConfigb\x06proto3')
  ,
  dependencies=[nvidia__tao__tf1_dot_cv_dot_mask__rcnn_dot_proto_dot_maskrcnn__config__pb2.DESCRIPTOR,nvidia__tao__tf1_dot_cv_dot_mask__rcnn_dot_proto_dot_data__config__pb2.DESCRIPTOR,nvidia__tao__tf1_dot_cv_dot_common_dot_proto_dot_clearml__config__pb2.DESCRIPTOR,nvidia__tao__tf1_dot_cv_dot_common_dot_proto_dot_wandb__config__pb2.DESCRIPTOR,])




_EXPERIMENT = _descriptor.Descriptor(
  name='Experiment',
  full_name='Experiment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='maskrcnn_config', full_name='Experiment.maskrcnn_config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_config', full_name='Experiment.data_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='skip_checkpoint_variables', full_name='Experiment.skip_checkpoint_variables', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='train_batch_size', full_name='Experiment.train_batch_size', index=3,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='save_checkpoints_steps', full_name='Experiment.save_checkpoints_steps', index=4,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_steps_per_eval', full_name='Experiment.num_steps_per_eval', index=5,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='momentum', full_name='Experiment.momentum', index=6,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='l2_weight_decay', full_name='Experiment.l2_weight_decay', index=7,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='warmup_learning_rate', full_name='Experiment.warmup_learning_rate', index=8,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='init_learning_rate', full_name='Experiment.init_learning_rate', index=9,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='global_gradient_clip_ratio', full_name='Experiment.global_gradient_clip_ratio', index=10,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_steps', full_name='Experiment.total_steps', index=11,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visualize_images_summary', full_name='Experiment.visualize_images_summary', index=12,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkpoint', full_name='Experiment.checkpoint', index=13,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eval_batch_size', full_name='Experiment.eval_batch_size', index=14,
      number=20, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='warmup_steps', full_name='Experiment.warmup_steps', index=15,
      number=21, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='learning_rate_steps', full_name='Experiment.learning_rate_steps', index=16,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='learning_rate_decay_levels', full_name='Experiment.learning_rate_decay_levels', index=17,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seed', full_name='Experiment.seed', index=18,
      number=24, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='report_frequency', full_name='Experiment.report_frequency', index=19,
      number=25, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_amp', full_name='Experiment.use_amp', index=20,
      number=26, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pruned_model_path', full_name='Experiment.pruned_model_path', index=21,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='l1_weight_decay', full_name='Experiment.l1_weight_decay', index=22,
      number=28, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_epochs', full_name='Experiment.num_epochs', index=23,
      number=29, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_examples_per_epoch', full_name='Experiment.num_examples_per_epoch', index=24,
      number=30, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logging_frequency', full_name='Experiment.logging_frequency', index=25,
      number=31, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wandb_config', full_name='Experiment.wandb_config', index=26,
      number=32, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clearml_config', full_name='Experiment.clearml_config', index=27,
      number=33, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=269,
  serialized_end=1066,
)

_EXPERIMENT.fields_by_name['maskrcnn_config'].message_type = nvidia__tao__tf1_dot_cv_dot_mask__rcnn_dot_proto_dot_maskrcnn__config__pb2._MASKRCNNCONFIG
_EXPERIMENT.fields_by_name['data_config'].message_type = nvidia__tao__tf1_dot_cv_dot_mask__rcnn_dot_proto_dot_data__config__pb2._DATACONFIG
_EXPERIMENT.fields_by_name['wandb_config'].message_type = nvidia__tao__tf1_dot_cv_dot_common_dot_proto_dot_wandb__config__pb2._WANDBCONFIG
_EXPERIMENT.fields_by_name['clearml_config'].message_type = nvidia__tao__tf1_dot_cv_dot_common_dot_proto_dot_clearml__config__pb2._CLEARMLCONFIG
DESCRIPTOR.message_types_by_name['Experiment'] = _EXPERIMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Experiment = _reflection.GeneratedProtocolMessageType('Experiment', (_message.Message,), dict(
  DESCRIPTOR = _EXPERIMENT,
  __module__ = 'nvidia_tao_tf1.cv.mask_rcnn.proto.experiment_pb2'
  # @@protoc_insertion_point(class_scope:Experiment)
  ))
_sym_db.RegisterMessage(Experiment)


# @@protoc_insertion_point(module_scope)