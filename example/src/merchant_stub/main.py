import grpc

import merchant_service_pb2_grpc
import data_pb2

import pymongo

uri = "mongodb://root:8DNsidknweoRGwSbWgDN@localhost:27017"
database = "sms"
shop = "shop"

myclient = pymongo.MongoClient(uri)
shop_table = myclient[database][shop]


channel = grpc.insecure_channel('localhost:9000')
client = merchant_service_pb2_grpc.MerchantServiceStub(channel)


for item in shop_table.find():
    response = client.UpsertShop(
        data_pb2.UpdateShopReq(shop_id=item["shop_id"]))
