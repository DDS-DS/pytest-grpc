# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: offline_order.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='offline_order.proto',
  package='merchant',
  syntax='proto3',
  serialized_options=b'Z\032app/protocol/grpc/merchant',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13offline_order.proto\x12\x08merchant\"L\n\x15QueryOfflineOrderResp\x12\r\n\x05total\x18\x01 \x01(\x05\x12$\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x16.merchant.OfflineOrder\"w\n\x15ReviewOfflineOrderReq\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12\x15\n\rreview_status\x18\x02 \x01(\t\x12\x0e\n\x06remark\x18\x03 \x01(\t\x12\x10\n\x08operator\x18\x04 \x01(\t\x12\x13\n\x0boperator_id\x18\x05 \x01(\t\"f\n\x1bUpdateOfflineOrderAmountReq\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\x12\x10\n\x08operator\x18\x03 \x01(\t\x12\x13\n\x0boperator_id\x18\x04 \x01(\t\"j\n$QueryOfflineOrderOperationRecordResp\x12\r\n\x05total\x18\x01 \x01(\x05\x12\x33\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32%.merchant.OfflineOrderOperationRecord\"c\n!AddOfflineOrderOperationRecordReq\x12>\n\x0foperationRecord\x18\x01 \x01(\x0b\x32%.merchant.OfflineOrderOperationRecord\"\x9a\x04\n\x0cOfflineOrder\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x02 \x01(\t\x12\x10\n\x08\x63urrency\x18\x03 \x01(\t\x12\x14\n\x0ctotal_amount\x18\x04 \x01(\x03\x12\x0e\n\x06status\x18\x05 \x01(\t\x12\x15\n\rrebate_amount\x18\x06 \x01(\x03\x12\x13\n\x0brebate_rate\x18\x07 \x01(\x01\x12\x15\n\rrebate_status\x18\x08 \x01(\t\x12,\n\x03tag\x18\t \x03(\x0b\x32\x1f.merchant.OfflineOrder.TagEntry\x12\x0f\n\x07user_id\x18\n \x01(\t\x12\x18\n\x10merchant_user_id\x18\x0b \x01(\t\x12\x10\n\x08store_id\x18\x0c \x01(\t\x12\x11\n\treview_at\x18\r \x01(\x03\x12\x11\n\tcreate_at\x18\x0e \x01(\x03\x12\x11\n\tupdate_at\x18\x0f \x01(\x03\x12&\n\x1emerchant_apportion_rebate_rate\x18\x10 \x01(\x01\x12&\n\x1eplatform_apportion_rebate_rate\x18\x11 \x01(\x01\x12(\n merchant_apportion_rebate_amount\x18\x12 \x01(\x03\x12(\n platform_apportion_rebate_amount\x18\x13 \x01(\x03\x1a*\n\x08TagEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb2\x01\n\x1bOfflineOrderOperationRecord\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\toperation\x18\x02 \x01(\t\x12\x0e\n\x06remark\x18\x03 \x01(\t\x12\x10\n\x08operator\x18\x04 \x01(\t\x12\x15\n\roperator_type\x18\x05 \x01(\t\x12\x10\n\x08order_id\x18\x06 \x01(\t\x12\x13\n\x0boperator_id\x18\x07 \x01(\t\x12\x14\n\x0coperation_at\x18\x08 \x01(\x03\x42\x1cZ\x1a\x61pp/protocol/grpc/merchantb\x06proto3'
)




_QUERYOFFLINEORDERRESP = _descriptor.Descriptor(
  name='QueryOfflineOrderResp',
  full_name='merchant.QueryOfflineOrderResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='total', full_name='merchant.QueryOfflineOrderResp.total', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='merchant.QueryOfflineOrderResp.data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=33,
  serialized_end=109,
)


_REVIEWOFFLINEORDERREQ = _descriptor.Descriptor(
  name='ReviewOfflineOrderReq',
  full_name='merchant.ReviewOfflineOrderReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='order_id', full_name='merchant.ReviewOfflineOrderReq.order_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='review_status', full_name='merchant.ReviewOfflineOrderReq.review_status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remark', full_name='merchant.ReviewOfflineOrderReq.remark', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operator', full_name='merchant.ReviewOfflineOrderReq.operator', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operator_id', full_name='merchant.ReviewOfflineOrderReq.operator_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=111,
  serialized_end=230,
)


_UPDATEOFFLINEORDERAMOUNTREQ = _descriptor.Descriptor(
  name='UpdateOfflineOrderAmountReq',
  full_name='merchant.UpdateOfflineOrderAmountReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='order_id', full_name='merchant.UpdateOfflineOrderAmountReq.order_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='merchant.UpdateOfflineOrderAmountReq.amount', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operator', full_name='merchant.UpdateOfflineOrderAmountReq.operator', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operator_id', full_name='merchant.UpdateOfflineOrderAmountReq.operator_id', index=3,
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
  serialized_start=232,
  serialized_end=334,
)


_QUERYOFFLINEORDEROPERATIONRECORDRESP = _descriptor.Descriptor(
  name='QueryOfflineOrderOperationRecordResp',
  full_name='merchant.QueryOfflineOrderOperationRecordResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='total', full_name='merchant.QueryOfflineOrderOperationRecordResp.total', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='merchant.QueryOfflineOrderOperationRecordResp.data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=336,
  serialized_end=442,
)


_ADDOFFLINEORDEROPERATIONRECORDREQ = _descriptor.Descriptor(
  name='AddOfflineOrderOperationRecordReq',
  full_name='merchant.AddOfflineOrderOperationRecordReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operationRecord', full_name='merchant.AddOfflineOrderOperationRecordReq.operationRecord', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=444,
  serialized_end=543,
)


_OFFLINEORDER_TAGENTRY = _descriptor.Descriptor(
  name='TagEntry',
  full_name='merchant.OfflineOrder.TagEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='merchant.OfflineOrder.TagEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='merchant.OfflineOrder.TagEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1042,
  serialized_end=1084,
)

_OFFLINEORDER = _descriptor.Descriptor(
  name='OfflineOrder',
  full_name='merchant.OfflineOrder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='merchant.OfflineOrder.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='country', full_name='merchant.OfflineOrder.country', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='currency', full_name='merchant.OfflineOrder.currency', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_amount', full_name='merchant.OfflineOrder.total_amount', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='merchant.OfflineOrder.status', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rebate_amount', full_name='merchant.OfflineOrder.rebate_amount', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rebate_rate', full_name='merchant.OfflineOrder.rebate_rate', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rebate_status', full_name='merchant.OfflineOrder.rebate_status', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tag', full_name='merchant.OfflineOrder.tag', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='merchant.OfflineOrder.user_id', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='merchant_user_id', full_name='merchant.OfflineOrder.merchant_user_id', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='store_id', full_name='merchant.OfflineOrder.store_id', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='review_at', full_name='merchant.OfflineOrder.review_at', index=12,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create_at', full_name='merchant.OfflineOrder.create_at', index=13,
      number=14, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_at', full_name='merchant.OfflineOrder.update_at', index=14,
      number=15, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='merchant_apportion_rebate_rate', full_name='merchant.OfflineOrder.merchant_apportion_rebate_rate', index=15,
      number=16, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='platform_apportion_rebate_rate', full_name='merchant.OfflineOrder.platform_apportion_rebate_rate', index=16,
      number=17, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='merchant_apportion_rebate_amount', full_name='merchant.OfflineOrder.merchant_apportion_rebate_amount', index=17,
      number=18, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='platform_apportion_rebate_amount', full_name='merchant.OfflineOrder.platform_apportion_rebate_amount', index=18,
      number=19, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_OFFLINEORDER_TAGENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=546,
  serialized_end=1084,
)


_OFFLINEORDEROPERATIONRECORD = _descriptor.Descriptor(
  name='OfflineOrderOperationRecord',
  full_name='merchant.OfflineOrderOperationRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='merchant.OfflineOrderOperationRecord.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operation', full_name='merchant.OfflineOrderOperationRecord.operation', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remark', full_name='merchant.OfflineOrderOperationRecord.remark', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operator', full_name='merchant.OfflineOrderOperationRecord.operator', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operator_type', full_name='merchant.OfflineOrderOperationRecord.operator_type', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='merchant.OfflineOrderOperationRecord.order_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operator_id', full_name='merchant.OfflineOrderOperationRecord.operator_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operation_at', full_name='merchant.OfflineOrderOperationRecord.operation_at', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1087,
  serialized_end=1265,
)

_QUERYOFFLINEORDERRESP.fields_by_name['data'].message_type = _OFFLINEORDER
_QUERYOFFLINEORDEROPERATIONRECORDRESP.fields_by_name['data'].message_type = _OFFLINEORDEROPERATIONRECORD
_ADDOFFLINEORDEROPERATIONRECORDREQ.fields_by_name['operationRecord'].message_type = _OFFLINEORDEROPERATIONRECORD
_OFFLINEORDER_TAGENTRY.containing_type = _OFFLINEORDER
_OFFLINEORDER.fields_by_name['tag'].message_type = _OFFLINEORDER_TAGENTRY
DESCRIPTOR.message_types_by_name['QueryOfflineOrderResp'] = _QUERYOFFLINEORDERRESP
DESCRIPTOR.message_types_by_name['ReviewOfflineOrderReq'] = _REVIEWOFFLINEORDERREQ
DESCRIPTOR.message_types_by_name['UpdateOfflineOrderAmountReq'] = _UPDATEOFFLINEORDERAMOUNTREQ
DESCRIPTOR.message_types_by_name['QueryOfflineOrderOperationRecordResp'] = _QUERYOFFLINEORDEROPERATIONRECORDRESP
DESCRIPTOR.message_types_by_name['AddOfflineOrderOperationRecordReq'] = _ADDOFFLINEORDEROPERATIONRECORDREQ
DESCRIPTOR.message_types_by_name['OfflineOrder'] = _OFFLINEORDER
DESCRIPTOR.message_types_by_name['OfflineOrderOperationRecord'] = _OFFLINEORDEROPERATIONRECORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryOfflineOrderResp = _reflection.GeneratedProtocolMessageType('QueryOfflineOrderResp', (_message.Message,), {
  'DESCRIPTOR' : _QUERYOFFLINEORDERRESP,
  '__module__' : 'offline_order_pb2'
  # @@protoc_insertion_point(class_scope:merchant.QueryOfflineOrderResp)
  })
_sym_db.RegisterMessage(QueryOfflineOrderResp)

ReviewOfflineOrderReq = _reflection.GeneratedProtocolMessageType('ReviewOfflineOrderReq', (_message.Message,), {
  'DESCRIPTOR' : _REVIEWOFFLINEORDERREQ,
  '__module__' : 'offline_order_pb2'
  # @@protoc_insertion_point(class_scope:merchant.ReviewOfflineOrderReq)
  })
_sym_db.RegisterMessage(ReviewOfflineOrderReq)

UpdateOfflineOrderAmountReq = _reflection.GeneratedProtocolMessageType('UpdateOfflineOrderAmountReq', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEOFFLINEORDERAMOUNTREQ,
  '__module__' : 'offline_order_pb2'
  # @@protoc_insertion_point(class_scope:merchant.UpdateOfflineOrderAmountReq)
  })
_sym_db.RegisterMessage(UpdateOfflineOrderAmountReq)

QueryOfflineOrderOperationRecordResp = _reflection.GeneratedProtocolMessageType('QueryOfflineOrderOperationRecordResp', (_message.Message,), {
  'DESCRIPTOR' : _QUERYOFFLINEORDEROPERATIONRECORDRESP,
  '__module__' : 'offline_order_pb2'
  # @@protoc_insertion_point(class_scope:merchant.QueryOfflineOrderOperationRecordResp)
  })
_sym_db.RegisterMessage(QueryOfflineOrderOperationRecordResp)

AddOfflineOrderOperationRecordReq = _reflection.GeneratedProtocolMessageType('AddOfflineOrderOperationRecordReq', (_message.Message,), {
  'DESCRIPTOR' : _ADDOFFLINEORDEROPERATIONRECORDREQ,
  '__module__' : 'offline_order_pb2'
  # @@protoc_insertion_point(class_scope:merchant.AddOfflineOrderOperationRecordReq)
  })
_sym_db.RegisterMessage(AddOfflineOrderOperationRecordReq)

OfflineOrder = _reflection.GeneratedProtocolMessageType('OfflineOrder', (_message.Message,), {

  'TagEntry' : _reflection.GeneratedProtocolMessageType('TagEntry', (_message.Message,), {
    'DESCRIPTOR' : _OFFLINEORDER_TAGENTRY,
    '__module__' : 'offline_order_pb2'
    # @@protoc_insertion_point(class_scope:merchant.OfflineOrder.TagEntry)
    })
  ,
  'DESCRIPTOR' : _OFFLINEORDER,
  '__module__' : 'offline_order_pb2'
  # @@protoc_insertion_point(class_scope:merchant.OfflineOrder)
  })
_sym_db.RegisterMessage(OfflineOrder)
_sym_db.RegisterMessage(OfflineOrder.TagEntry)

OfflineOrderOperationRecord = _reflection.GeneratedProtocolMessageType('OfflineOrderOperationRecord', (_message.Message,), {
  'DESCRIPTOR' : _OFFLINEORDEROPERATIONRECORD,
  '__module__' : 'offline_order_pb2'
  # @@protoc_insertion_point(class_scope:merchant.OfflineOrderOperationRecord)
  })
_sym_db.RegisterMessage(OfflineOrderOperationRecord)


DESCRIPTOR._options = None
_OFFLINEORDER_TAGENTRY._options = None
# @@protoc_insertion_point(module_scope)
