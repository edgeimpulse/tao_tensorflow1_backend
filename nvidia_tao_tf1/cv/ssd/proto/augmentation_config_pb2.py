# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nvidia_tao_tf1/cv/ssd/proto/augmentation_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='nvidia_tao_tf1/cv/ssd/proto/augmentation_config.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n5nvidia_tao_tf1/cv/ssd/proto/augmentation_config.proto\"\xcd\x03\n\x12\x41ugmentationConfig\x12\x14\n\x0coutput_width\x18\x01 \x01(\x05\x12\x15\n\routput_height\x18\x02 \x01(\x05\x12\x16\n\x0eoutput_channel\x18\x03 \x01(\x05\x12\x1d\n\x15random_crop_min_scale\x18\x04 \x01(\x02\x12\x1d\n\x15random_crop_max_scale\x18\x05 \x01(\x02\x12\x1a\n\x12random_crop_min_ar\x18\x06 \x01(\x02\x12\x1a\n\x12random_crop_max_ar\x18\x07 \x01(\x02\x12\x1a\n\x12zoom_out_min_scale\x18\x08 \x01(\x02\x12\x1a\n\x12zoom_out_max_scale\x18\t \x01(\x02\x12\x12\n\nbrightness\x18\n \x01(\x05\x12\x10\n\x08\x63ontrast\x18\x0b \x01(\x02\x12\x12\n\nsaturation\x18\x0c \x01(\x02\x12\x0b\n\x03hue\x18\r \x01(\x05\x12\x13\n\x0brandom_flip\x18\x0e \x01(\x02\x12\x36\n\nimage_mean\x18\x0f \x03(\x0b\x32\".AugmentationConfig.ImageMeanEntry\x1a\x30\n\x0eImageMeanEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\x62\x06proto3')
)




_AUGMENTATIONCONFIG_IMAGEMEANENTRY = _descriptor.Descriptor(
  name='ImageMeanEntry',
  full_name='AugmentationConfig.ImageMeanEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='AugmentationConfig.ImageMeanEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='AugmentationConfig.ImageMeanEntry.value', index=1,
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
  serialized_start=471,
  serialized_end=519,
)

_AUGMENTATIONCONFIG = _descriptor.Descriptor(
  name='AugmentationConfig',
  full_name='AugmentationConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='output_width', full_name='AugmentationConfig.output_width', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_height', full_name='AugmentationConfig.output_height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_channel', full_name='AugmentationConfig.output_channel', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='random_crop_min_scale', full_name='AugmentationConfig.random_crop_min_scale', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='random_crop_max_scale', full_name='AugmentationConfig.random_crop_max_scale', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='random_crop_min_ar', full_name='AugmentationConfig.random_crop_min_ar', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='random_crop_max_ar', full_name='AugmentationConfig.random_crop_max_ar', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zoom_out_min_scale', full_name='AugmentationConfig.zoom_out_min_scale', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zoom_out_max_scale', full_name='AugmentationConfig.zoom_out_max_scale', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='brightness', full_name='AugmentationConfig.brightness', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contrast', full_name='AugmentationConfig.contrast', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='saturation', full_name='AugmentationConfig.saturation', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hue', full_name='AugmentationConfig.hue', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='random_flip', full_name='AugmentationConfig.random_flip', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_mean', full_name='AugmentationConfig.image_mean', index=14,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_AUGMENTATIONCONFIG_IMAGEMEANENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=519,
)

_AUGMENTATIONCONFIG_IMAGEMEANENTRY.containing_type = _AUGMENTATIONCONFIG
_AUGMENTATIONCONFIG.fields_by_name['image_mean'].message_type = _AUGMENTATIONCONFIG_IMAGEMEANENTRY
DESCRIPTOR.message_types_by_name['AugmentationConfig'] = _AUGMENTATIONCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AugmentationConfig = _reflection.GeneratedProtocolMessageType('AugmentationConfig', (_message.Message,), dict(

  ImageMeanEntry = _reflection.GeneratedProtocolMessageType('ImageMeanEntry', (_message.Message,), dict(
    DESCRIPTOR = _AUGMENTATIONCONFIG_IMAGEMEANENTRY,
    __module__ = 'nvidia_tao_tf1.cv.ssd.proto.augmentation_config_pb2'
    # @@protoc_insertion_point(class_scope:AugmentationConfig.ImageMeanEntry)
    ))
  ,
  DESCRIPTOR = _AUGMENTATIONCONFIG,
  __module__ = 'nvidia_tao_tf1.cv.ssd.proto.augmentation_config_pb2'
  # @@protoc_insertion_point(class_scope:AugmentationConfig)
  ))
_sym_db.RegisterMessage(AugmentationConfig)
_sym_db.RegisterMessage(AugmentationConfig.ImageMeanEntry)


_AUGMENTATIONCONFIG_IMAGEMEANENTRY._options = None
# @@protoc_insertion_point(module_scope)