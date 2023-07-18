# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nvidia_tao_tf1/cv/makenet/proto/experiment.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from nvidia_tao_tf1.cv.makenet.proto import model_config_pb2 as nvidia__tao__tf1_dot_cv_dot_makenet_dot_proto_dot_model__config__pb2
from nvidia_tao_tf1.cv.makenet.proto import training_config_pb2 as nvidia__tao__tf1_dot_cv_dot_makenet_dot_proto_dot_training__config__pb2
from nvidia_tao_tf1.cv.makenet.proto import eval_config_pb2 as nvidia__tao__tf1_dot_cv_dot_makenet_dot_proto_dot_eval__config__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='nvidia_tao_tf1/cv/makenet/proto/experiment.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n0nvidia_tao_tf1/cv/makenet/proto/experiment.proto\x1a\x32nvidia_tao_tf1/cv/makenet/proto/model_config.proto\x1a\x35nvidia_tao_tf1/cv/makenet/proto/training_config.proto\x1a\x31nvidia_tao_tf1/cv/makenet/proto/eval_config.proto\"v\n\nExperiment\x12 \n\x0b\x65val_config\x18\x01 \x01(\x0b\x32\x0b.EvalConfig\x12\"\n\x0cmodel_config\x18\x02 \x01(\x0b\x32\x0c.ModelConfig\x12\"\n\x0ctrain_config\x18\x03 \x01(\x0b\x32\x0c.TrainConfigb\x06proto3')
  ,
  dependencies=[nvidia__tao__tf1_dot_cv_dot_makenet_dot_proto_dot_model__config__pb2.DESCRIPTOR,nvidia__tao__tf1_dot_cv_dot_makenet_dot_proto_dot_training__config__pb2.DESCRIPTOR,nvidia__tao__tf1_dot_cv_dot_makenet_dot_proto_dot_eval__config__pb2.DESCRIPTOR,])




_EXPERIMENT = _descriptor.Descriptor(
  name='Experiment',
  full_name='Experiment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='eval_config', full_name='Experiment.eval_config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_config', full_name='Experiment.model_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='train_config', full_name='Experiment.train_config', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=210,
  serialized_end=328,
)

_EXPERIMENT.fields_by_name['eval_config'].message_type = nvidia__tao__tf1_dot_cv_dot_makenet_dot_proto_dot_eval__config__pb2._EVALCONFIG
_EXPERIMENT.fields_by_name['model_config'].message_type = nvidia__tao__tf1_dot_cv_dot_makenet_dot_proto_dot_model__config__pb2._MODELCONFIG
_EXPERIMENT.fields_by_name['train_config'].message_type = nvidia__tao__tf1_dot_cv_dot_makenet_dot_proto_dot_training__config__pb2._TRAINCONFIG
DESCRIPTOR.message_types_by_name['Experiment'] = _EXPERIMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Experiment = _reflection.GeneratedProtocolMessageType('Experiment', (_message.Message,), dict(
  DESCRIPTOR = _EXPERIMENT,
  __module__ = 'nvidia_tao_tf1.cv.makenet.proto.experiment_pb2'
  # @@protoc_insertion_point(class_scope:Experiment)
  ))
_sym_db.RegisterMessage(Experiment)


# @@protoc_insertion_point(module_scope)
