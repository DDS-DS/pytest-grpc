# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: merchant_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2
import data_pb2 as data__pb2
import offline_order_pb2 as offline__order__pb2
import manager_backend_pb2 as manager__backend__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='merchant_service.proto',
  package='merchant',
  syntax='proto3',
  serialized_options=b'Z\032app/protocol/grpc/merchant',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16merchant_service.proto\x12\x08merchant\x1a\x0c\x63ommon.proto\x1a\ndata.proto\x1a\x13offline_order.proto\x1a\x15manager_backend.proto2\xe8\x0e\n\x0fMerchantService\x12/\n\tQueryShop\x12\x11.common.QueryInfo\x1a\x0f.merchant.Shops\x12\x37\n\rQuerySupplier\x12\x11.common.QueryInfo\x1a\x13.merchant.Suppliers\x12/\n\tQueryUser\x12\x11.common.QueryInfo\x1a\x0f.merchant.Users\x12\x38\n\rQueryCategory\x12\x11.common.QueryInfo\x1a\x14.merchant.Categories\x12\x35\n\x0cQueryComment\x12\x11.common.QueryInfo\x1a\x12.merchant.Comments\x12\x38\n\nUpsertShop\x12\x17.merchant.UpdateShopReq\x1a\x11.merchant.ShopRsb\x12\x44\n\x0eUpsertSupplier\x12\x1b.merchant.UpdateSupplierReq\x1a\x15.merchant.SupplierRsb\x12;\n\rUpsertAccount\x12\x17.merchant.UpdateUserReq\x1a\x11.merchant.UserRsb\x12;\n\rDeleteAccount\x12\x17.merchant.DeleteUserReq\x1a\x11.merchant.UserRsb\x12\x35\n\x0e\x44\x65leteSupplier\x12\x14.merchant.DeleteById\x1a\r.common.Empty\x12\x31\n\nDeleteShop\x12\x14.merchant.DeleteById\x1a\r.common.Empty\x12\x41\n\x0b\x43ounterShop\x12\x18.merchant.CounterShopReq\x1a\x18.merchant.CounterShopRsb\x12\x44\n\x15\x43reateBrandCollection\x12\x1c.merchant.BrandCollectionReq\x1a\r.common.Empty\x12\x44\n\x15UpdateBrandCollection\x12\x1c.merchant.BrandCollectionReq\x1a\r.common.Empty\x12\\\n\x14QueryBrandCollection\x12!.merchant.QueryBrandCollectionReq\x1a!.merchant.QueryBrandCollectionRsb\x12J\n\x0eUpsertComments\x12\x1b.merchant.UpdateCommentsReq\x1a\x1b.merchant.UpdateCommentsRsb\x12\x34\n\rDeleteComment\x12\x14.merchant.DeleteById\x1a\r.common.Empty\x12G\n\x11QueryOfflineOrder\x12\x11.common.QueryInfo\x1a\x1f.merchant.QueryOfflineOrderResp\x12\x44\n\x12ReviewOfflineOrder\x12\x1f.merchant.ReviewOfflineOrderReq\x1a\r.common.Empty\x12P\n\x18UpdateOfflineOrderAmount\x12%.merchant.UpdateOfflineOrderAmountReq\x1a\r.common.Empty\x12\x65\n QueryOfflineOrderOperationRecord\x12\x11.common.QueryInfo\x1a..merchant.QueryOfflineOrderOperationRecordResp\x12\\\n\x1e\x41\x64\x64OfflineOrderOperationRecord\x12+.merchant.AddOfflineOrderOperationRecordReq\x1a\r.common.Empty\x12/\n\x05Login\x12\x12.merchant.LoginReq\x1a\x12.merchant.LoginRes\x12\x34\n\nCheckToken\x12\x17.merchant.CheckTokenReq\x1a\r.common.Empty\x12\x45\n\x10QueryApplyRecord\x12\x11.common.QueryInfo\x1a\x1e.merchant.QueryApplyRecordResp\x12?\n\rQueryDistrict\x12\x11.common.QueryInfo\x1a\x1b.merchant.QueryDistrictResp\x12T\n\x11UpsertApplyRecord\x12\x1e.merchant.UpsertApplyRecordReq\x1a\x1f.merchant.UpsertApplyRecordResp\x12K\n\x0eUpsertDistrict\x12\x1b.merchant.UpsertDistrictReq\x1a\x1c.merchant.UpsertDistrictRespB\x1cZ\x1a\x61pp/protocol/grpc/merchantb\x06proto3'
  ,
  dependencies=[common__pb2.DESCRIPTOR,data__pb2.DESCRIPTOR,offline__order__pb2.DESCRIPTOR,manager__backend__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_MERCHANTSERVICE = _descriptor.ServiceDescriptor(
  name='MerchantService',
  full_name='merchant.MerchantService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=107,
  serialized_end=2003,
  methods=[
  _descriptor.MethodDescriptor(
    name='QueryShop',
    full_name='merchant.MerchantService.QueryShop',
    index=0,
    containing_service=None,
    input_type=common__pb2._QUERYINFO,
    output_type=data__pb2._SHOPS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='QuerySupplier',
    full_name='merchant.MerchantService.QuerySupplier',
    index=1,
    containing_service=None,
    input_type=common__pb2._QUERYINFO,
    output_type=data__pb2._SUPPLIERS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='QueryUser',
    full_name='merchant.MerchantService.QueryUser',
    index=2,
    containing_service=None,
    input_type=common__pb2._QUERYINFO,
    output_type=data__pb2._USERS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='QueryCategory',
    full_name='merchant.MerchantService.QueryCategory',
    index=3,
    containing_service=None,
    input_type=common__pb2._QUERYINFO,
    output_type=data__pb2._CATEGORIES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='QueryComment',
    full_name='merchant.MerchantService.QueryComment',
    index=4,
    containing_service=None,
    input_type=common__pb2._QUERYINFO,
    output_type=data__pb2._COMMENTS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpsertShop',
    full_name='merchant.MerchantService.UpsertShop',
    index=5,
    containing_service=None,
    input_type=data__pb2._UPDATESHOPREQ,
    output_type=data__pb2._SHOPRSB,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpsertSupplier',
    full_name='merchant.MerchantService.UpsertSupplier',
    index=6,
    containing_service=None,
    input_type=data__pb2._UPDATESUPPLIERREQ,
    output_type=data__pb2._SUPPLIERRSB,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpsertAccount',
    full_name='merchant.MerchantService.UpsertAccount',
    index=7,
    containing_service=None,
    input_type=data__pb2._UPDATEUSERREQ,
    output_type=data__pb2._USERRSB,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteAccount',
    full_name='merchant.MerchantService.DeleteAccount',
    index=8,
    containing_service=None,
    input_type=data__pb2._DELETEUSERREQ,
    output_type=data__pb2._USERRSB,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteSupplier',
    full_name='merchant.MerchantService.DeleteSupplier',
    index=9,
    containing_service=None,
    input_type=data__pb2._DELETEBYID,
    output_type=common__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteShop',
    full_name='merchant.MerchantService.DeleteShop',
    index=10,
    containing_service=None,
    input_type=data__pb2._DELETEBYID,
    output_type=common__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CounterShop',
    full_name='merchant.MerchantService.CounterShop',
    index=11,
    containing_service=None,
    input_type=data__pb2._COUNTERSHOPREQ,
    output_type=data__pb2._COUNTERSHOPRSB,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateBrandCollection',
    full_name='merchant.MerchantService.CreateBrandCollection',
    index=12,
    containing_service=None,
    input_type=data__pb2._BRANDCOLLECTIONREQ,
    output_type=common__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateBrandCollection',
    full_name='merchant.MerchantService.UpdateBrandCollection',
    index=13,
    containing_service=None,
    input_type=data__pb2._BRANDCOLLECTIONREQ,
    output_type=common__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='QueryBrandCollection',
    full_name='merchant.MerchantService.QueryBrandCollection',
    index=14,
    containing_service=None,
    input_type=data__pb2._QUERYBRANDCOLLECTIONREQ,
    output_type=data__pb2._QUERYBRANDCOLLECTIONRSB,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpsertComments',
    full_name='merchant.MerchantService.UpsertComments',
    index=15,
    containing_service=None,
    input_type=data__pb2._UPDATECOMMENTSREQ,
    output_type=data__pb2._UPDATECOMMENTSRSB,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteComment',
    full_name='merchant.MerchantService.DeleteComment',
    index=16,
    containing_service=None,
    input_type=data__pb2._DELETEBYID,
    output_type=common__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='QueryOfflineOrder',
    full_name='merchant.MerchantService.QueryOfflineOrder',
    index=17,
    containing_service=None,
    input_type=common__pb2._QUERYINFO,
    output_type=offline__order__pb2._QUERYOFFLINEORDERRESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReviewOfflineOrder',
    full_name='merchant.MerchantService.ReviewOfflineOrder',
    index=18,
    containing_service=None,
    input_type=offline__order__pb2._REVIEWOFFLINEORDERREQ,
    output_type=common__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateOfflineOrderAmount',
    full_name='merchant.MerchantService.UpdateOfflineOrderAmount',
    index=19,
    containing_service=None,
    input_type=offline__order__pb2._UPDATEOFFLINEORDERAMOUNTREQ,
    output_type=common__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='QueryOfflineOrderOperationRecord',
    full_name='merchant.MerchantService.QueryOfflineOrderOperationRecord',
    index=20,
    containing_service=None,
    input_type=common__pb2._QUERYINFO,
    output_type=offline__order__pb2._QUERYOFFLINEORDEROPERATIONRECORDRESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddOfflineOrderOperationRecord',
    full_name='merchant.MerchantService.AddOfflineOrderOperationRecord',
    index=21,
    containing_service=None,
    input_type=offline__order__pb2._ADDOFFLINEORDEROPERATIONRECORDREQ,
    output_type=common__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Login',
    full_name='merchant.MerchantService.Login',
    index=22,
    containing_service=None,
    input_type=manager__backend__pb2._LOGINREQ,
    output_type=manager__backend__pb2._LOGINRES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CheckToken',
    full_name='merchant.MerchantService.CheckToken',
    index=23,
    containing_service=None,
    input_type=manager__backend__pb2._CHECKTOKENREQ,
    output_type=common__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='QueryApplyRecord',
    full_name='merchant.MerchantService.QueryApplyRecord',
    index=24,
    containing_service=None,
    input_type=common__pb2._QUERYINFO,
    output_type=data__pb2._QUERYAPPLYRECORDRESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='QueryDistrict',
    full_name='merchant.MerchantService.QueryDistrict',
    index=25,
    containing_service=None,
    input_type=common__pb2._QUERYINFO,
    output_type=data__pb2._QUERYDISTRICTRESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpsertApplyRecord',
    full_name='merchant.MerchantService.UpsertApplyRecord',
    index=26,
    containing_service=None,
    input_type=data__pb2._UPSERTAPPLYRECORDREQ,
    output_type=data__pb2._UPSERTAPPLYRECORDRESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpsertDistrict',
    full_name='merchant.MerchantService.UpsertDistrict',
    index=27,
    containing_service=None,
    input_type=data__pb2._UPSERTDISTRICTREQ,
    output_type=data__pb2._UPSERTDISTRICTRESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MERCHANTSERVICE)

DESCRIPTOR.services_by_name['MerchantService'] = _MERCHANTSERVICE

# @@protoc_insertion_point(module_scope)