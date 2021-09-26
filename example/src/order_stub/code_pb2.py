# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: code.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='code.proto',
  package='code',
  syntax='proto3',
  serialized_options=b'Z\021app/protocol/grpc',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ncode.proto\x12\x04\x63ode*\xae\x07\n\x04\x43ode\x12\x06\n\x02Ok\x10\x00\x12\x16\n\x12UnknownInternalErr\x10\x01\x12\t\n\x05\x44\x42\x45rr\x10\x02\x12\x18\n\x14InvalidRequestParams\x10\x03\x12\x17\n\x12UGUnsupportedGroup\x10\x91N\x12\x19\n\x14OrderStatusNotChange\x10\xf9U\x12\x12\n\rOrderNotFound\x10\xfaU\x12\x15\n\x10OrderStatusError\x10\xfbU\x12\"\n\x1dOrderLogisticsCompanyNotFound\x10\xfcU\x12\x19\n\x14OrderProductNotFound\x10\xfdU\x12\x17\n\x12OrderNotBelongUser\x10\xfeU\x12)\n$OrderPaymentPlatformMethodIdNotFound\x10\xffU\x12(\n#CodOrderNotChangeOtherPaymentMethod\x10\x80V\x12,\n\'OrderNormalProductShouldBelongSameStore\x10\x81V\x12\'\n\"OrderServiceProductShouldPointItem\x10\x82V\x12\x16\n\x11OrderBillNotFound\x10\x83V\x12\x19\n\x14OrderBillStatusError\x10\x84V\x12&\n!OrderBillAmountOrCurrencyNotMatch\x10\x85V\x12,\n\'OrderTransactionShouldBelongSameCountry\x10\x86V\x12\x18\n\x13\x42usinessCodeNoMatch\x10\x87V\x12&\n!OrderPrivilegeProductNoSupportCod\x10\x88V\x12#\n\x1eOrderShippingFeeCalculateError\x10\x89V\x12\x1a\n\x15RebateOrderQueryError\x10\x8aV\x12\"\n\x1dOrderSettlementCalculateError\x10\x8bV\x12\x1c\n\x17\x41PartOfOrderCreateError\x10\x8cV\x12 \n\x1bOrderSettlementConfirmError\x10\x8dV\x12)\n$OrderNoVirtualGoodsNeedDeliveryError\x10\x8eV\x12\x1d\n\x18OrderSettlementLockError\x10\x8fV\x12&\n!OrderOfflineMerchantNotFoundError\x10\x90V\x12\x1c\n\x17OrderSettlementAskError\x10\x91VB\x13Z\x11\x61pp/protocol/grpcb\x06proto3'
)

_CODE = _descriptor.EnumDescriptor(
  name='Code',
  full_name='code.Code',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Ok', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UnknownInternalErr', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DBErr', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='InvalidRequestParams', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UGUnsupportedGroup', index=4, number=10001,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OrderStatusNotChange', index=5, number=11001,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OrderNotFound', index=6, number=11002,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OrderStatusError', index=7, number=11003,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OrderLogisticsCompanyNotFound', index=8, number=11004,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OrderProductNotFound', index=9, number=11005,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OrderNotBelongUser', index=10, number=11006,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OrderPaymentPlatformMethodIdNotFound', index=11, number=11007,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CodOrderNotChangeOtherPaymentMethod', index=12, number=11008,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OrderNormalProductShouldBelongSameStore', index=13, number=11009,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OrderServiceProductShouldPointItem', index=14, number=11010,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OrderBillNotFound', index=15, number=11011,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OrderBillStatusError', index=16, number=11012,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OrderBillAmountOrCurrencyNotMatch', index=17, number=11013,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OrderTransactionShouldBelongSameCountry', index=18, number=11014,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BusinessCodeNoMatch', index=19, number=11015,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OrderPrivilegeProductNoSupportCod', index=20, number=11016,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OrderShippingFeeCalculateError', index=21, number=11017,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RebateOrderQueryError', index=22, number=11018,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OrderSettlementCalculateError', index=23, number=11019,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='APartOfOrderCreateError', index=24, number=11020,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OrderSettlementConfirmError', index=25, number=11021,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OrderNoVirtualGoodsNeedDeliveryError', index=26, number=11022,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OrderSettlementLockError', index=27, number=11023,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OrderOfflineMerchantNotFoundError', index=28, number=11024,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OrderSettlementAskError', index=29, number=11025,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=21,
  serialized_end=963,
)
_sym_db.RegisterEnumDescriptor(_CODE)

Code = enum_type_wrapper.EnumTypeWrapper(_CODE)
Ok = 0
UnknownInternalErr = 1
DBErr = 2
InvalidRequestParams = 3
UGUnsupportedGroup = 10001
OrderStatusNotChange = 11001
OrderNotFound = 11002
OrderStatusError = 11003
OrderLogisticsCompanyNotFound = 11004
OrderProductNotFound = 11005
OrderNotBelongUser = 11006
OrderPaymentPlatformMethodIdNotFound = 11007
CodOrderNotChangeOtherPaymentMethod = 11008
OrderNormalProductShouldBelongSameStore = 11009
OrderServiceProductShouldPointItem = 11010
OrderBillNotFound = 11011
OrderBillStatusError = 11012
OrderBillAmountOrCurrencyNotMatch = 11013
OrderTransactionShouldBelongSameCountry = 11014
BusinessCodeNoMatch = 11015
OrderPrivilegeProductNoSupportCod = 11016
OrderShippingFeeCalculateError = 11017
RebateOrderQueryError = 11018
OrderSettlementCalculateError = 11019
APartOfOrderCreateError = 11020
OrderSettlementConfirmError = 11021
OrderNoVirtualGoodsNeedDeliveryError = 11022
OrderSettlementLockError = 11023
OrderOfflineMerchantNotFoundError = 11024
OrderSettlementAskError = 11025


DESCRIPTOR.enum_types_by_name['Code'] = _CODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)