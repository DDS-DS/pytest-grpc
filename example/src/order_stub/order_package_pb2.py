# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: order_package.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import code_pb2 as code__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='order_package.proto',
  package='order',
  syntax='proto3',
  serialized_options=b'Z\027app/protocol/grpc/order',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13order_package.proto\x12\x05order\x1a\ncode.proto\"q\n\x16OrderPackageListResult\x12!\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x13.order.OrderPackage\x12\r\n\x05total\x18\x02 \x01(\x03\x12\x18\n\x04\x63ode\x18\x03 \x01(\x0e\x32\n.code.Code\x12\x0b\n\x03msg\x18\x04 \x01(\t\"\xa9\x02\n\x0cOrderPackage\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x02 \x01(\t\x12\x10\n\x08order_id\x18\x03 \x01(\t\x12\x0f\n\x07user_id\x18\x04 \x01(\t\x12\x10\n\x08item_ids\x18\x05 \x03(\t\x12\x1c\n\x14logistics_company_id\x18\x06 \x01(\t\x12\x16\n\x0elogistics_code\x18\x07 \x01(\t\x12\x13\n\x0btracking_no\x18\x08 \x01(\t\x12\x14\n\x0ctracking_url\x18\t \x01(\t\x12\x0e\n\x06\x61mount\x18\n \x01(\x03\x12\x10\n\x08\x63urrency\x18\x0b \x01(\t\x12\x11\n\tcreate_at\x18\x0c \x01(\x03\x12\x11\n\tupdate_at\x18\r \x01(\x03\x12\x1e\n\x16logistics_company_name\x18\x0e \x01(\tB\x19Z\x17\x61pp/protocol/grpc/orderb\x06proto3'
  ,
  dependencies=[code__pb2.DESCRIPTOR,])




_ORDERPACKAGELISTRESULT = _descriptor.Descriptor(
  name='OrderPackageListResult',
  full_name='order.OrderPackageListResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='order.OrderPackageListResult.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total', full_name='order.OrderPackageListResult.total', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code', full_name='order.OrderPackageListResult.code', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='order.OrderPackageListResult.msg', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=42,
  serialized_end=155,
)


_ORDERPACKAGE = _descriptor.Descriptor(
  name='OrderPackage',
  full_name='order.OrderPackage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='order.OrderPackage.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='country', full_name='order.OrderPackage.country', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='order.OrderPackage.order_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='order.OrderPackage.user_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='item_ids', full_name='order.OrderPackage.item_ids', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='logistics_company_id', full_name='order.OrderPackage.logistics_company_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='logistics_code', full_name='order.OrderPackage.logistics_code', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tracking_no', full_name='order.OrderPackage.tracking_no', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tracking_url', full_name='order.OrderPackage.tracking_url', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='order.OrderPackage.amount', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='currency', full_name='order.OrderPackage.currency', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create_at', full_name='order.OrderPackage.create_at', index=11,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_at', full_name='order.OrderPackage.update_at', index=12,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='logistics_company_name', full_name='order.OrderPackage.logistics_company_name', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=158,
  serialized_end=455,
)

_ORDERPACKAGELISTRESULT.fields_by_name['data'].message_type = _ORDERPACKAGE
_ORDERPACKAGELISTRESULT.fields_by_name['code'].enum_type = code__pb2._CODE
DESCRIPTOR.message_types_by_name['OrderPackageListResult'] = _ORDERPACKAGELISTRESULT
DESCRIPTOR.message_types_by_name['OrderPackage'] = _ORDERPACKAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OrderPackageListResult = _reflection.GeneratedProtocolMessageType('OrderPackageListResult', (_message.Message,), {
  'DESCRIPTOR' : _ORDERPACKAGELISTRESULT,
  '__module__' : 'order_package_pb2'
  # @@protoc_insertion_point(class_scope:order.OrderPackageListResult)
  })
_sym_db.RegisterMessage(OrderPackageListResult)

OrderPackage = _reflection.GeneratedProtocolMessageType('OrderPackage', (_message.Message,), {
  'DESCRIPTOR' : _ORDERPACKAGE,
  '__module__' : 'order_package_pb2'
  # @@protoc_insertion_point(class_scope:order.OrderPackage)
  })
_sym_db.RegisterMessage(OrderPackage)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
