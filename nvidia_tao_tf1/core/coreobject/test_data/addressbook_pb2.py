# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nvidia_tao_tf1/core/coreobject/test_data/addressbook.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='nvidia_tao_tf1/core/coreobject/test_data/addressbook.proto',
  package='modulus.modulusobject',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n:nvidia_tao_tf1/core/coreobject/test_data/addressbook.proto\x12\x15modulus.modulusobject\"\x9e\x02\n\x0cMaglevPerson\x12\x11\n\tfull_name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x45\n\x06phones\x18\x04 \x03(\x0b\x32\x35.modulus.modulusobject.MaglevPerson.MaglevPhoneNumber\x1a\x66\n\x11MaglevPhoneNumber\x12\x0e\n\x06number\x18\x01 \x01(\t\x12\x41\n\x04type\x18\x02 \x01(\x0e\x32\x33.modulus.modulusobject.MaglevPerson.MaglevPhoneType\"1\n\x0fMaglevPhoneType\x12\n\n\x06MOBILE\x10\x00\x12\x08\n\x04HOME\x10\x01\x12\x08\n\x04WORK\x10\x02\"H\n\x11MaglevAddressBook\x12\x33\n\x06people\x18\x01 \x03(\x0b\x32#.modulus.modulusobject.MaglevPersonb\x06proto3')
)



_MAGLEVPERSON_MAGLEVPHONETYPE = _descriptor.EnumDescriptor(
  name='MaglevPhoneType',
  full_name='modulus.modulusobject.MaglevPerson.MaglevPhoneType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MOBILE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOME', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORK', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=323,
  serialized_end=372,
)
_sym_db.RegisterEnumDescriptor(_MAGLEVPERSON_MAGLEVPHONETYPE)


_MAGLEVPERSON_MAGLEVPHONENUMBER = _descriptor.Descriptor(
  name='MaglevPhoneNumber',
  full_name='modulus.modulusobject.MaglevPerson.MaglevPhoneNumber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='modulus.modulusobject.MaglevPerson.MaglevPhoneNumber.number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='modulus.modulusobject.MaglevPerson.MaglevPhoneNumber.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=219,
  serialized_end=321,
)

_MAGLEVPERSON = _descriptor.Descriptor(
  name='MaglevPerson',
  full_name='modulus.modulusobject.MaglevPerson',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='full_name', full_name='modulus.modulusobject.MaglevPerson.full_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='modulus.modulusobject.MaglevPerson.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='modulus.modulusobject.MaglevPerson.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phones', full_name='modulus.modulusobject.MaglevPerson.phones', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MAGLEVPERSON_MAGLEVPHONENUMBER, ],
  enum_types=[
    _MAGLEVPERSON_MAGLEVPHONETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=372,
)


_MAGLEVADDRESSBOOK = _descriptor.Descriptor(
  name='MaglevAddressBook',
  full_name='modulus.modulusobject.MaglevAddressBook',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='people', full_name='modulus.modulusobject.MaglevAddressBook.people', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=374,
  serialized_end=446,
)

_MAGLEVPERSON_MAGLEVPHONENUMBER.fields_by_name['type'].enum_type = _MAGLEVPERSON_MAGLEVPHONETYPE
_MAGLEVPERSON_MAGLEVPHONENUMBER.containing_type = _MAGLEVPERSON
_MAGLEVPERSON.fields_by_name['phones'].message_type = _MAGLEVPERSON_MAGLEVPHONENUMBER
_MAGLEVPERSON_MAGLEVPHONETYPE.containing_type = _MAGLEVPERSON
_MAGLEVADDRESSBOOK.fields_by_name['people'].message_type = _MAGLEVPERSON
DESCRIPTOR.message_types_by_name['MaglevPerson'] = _MAGLEVPERSON
DESCRIPTOR.message_types_by_name['MaglevAddressBook'] = _MAGLEVADDRESSBOOK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MaglevPerson = _reflection.GeneratedProtocolMessageType('MaglevPerson', (_message.Message,), dict(

  MaglevPhoneNumber = _reflection.GeneratedProtocolMessageType('MaglevPhoneNumber', (_message.Message,), dict(
    DESCRIPTOR = _MAGLEVPERSON_MAGLEVPHONENUMBER,
    __module__ = 'nvidia_tao_tf1.core.coreobject.test_data.addressbook_pb2'
    # @@protoc_insertion_point(class_scope:modulus.modulusobject.MaglevPerson.MaglevPhoneNumber)
    ))
  ,
  DESCRIPTOR = _MAGLEVPERSON,
  __module__ = 'nvidia_tao_tf1.core.coreobject.test_data.addressbook_pb2'
  # @@protoc_insertion_point(class_scope:modulus.modulusobject.MaglevPerson)
  ))
_sym_db.RegisterMessage(MaglevPerson)
_sym_db.RegisterMessage(MaglevPerson.MaglevPhoneNumber)

MaglevAddressBook = _reflection.GeneratedProtocolMessageType('MaglevAddressBook', (_message.Message,), dict(
  DESCRIPTOR = _MAGLEVADDRESSBOOK,
  __module__ = 'nvidia_tao_tf1.core.coreobject.test_data.addressbook_pb2'
  # @@protoc_insertion_point(class_scope:modulus.modulusobject.MaglevAddressBook)
  ))
_sym_db.RegisterMessage(MaglevAddressBook)


# @@protoc_insertion_point(module_scope)