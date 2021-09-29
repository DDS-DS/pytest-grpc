from merchant_stub.data_pb2 import UpdateSupplierReq,SupplierRsb
from merchant_stub.merchant_service_pb2_grpc import MerchantServiceServicer
import threading



class Servicer(MerchantServiceServicer):
    def __init__(self):
        self.barrier = threading.Barrier(2)

    def UpsertSupplier(self, request: UpdateSupplierReq , context) -> SupplierRsb:
        return SupplierRsb(name=f'test-{request.name}')
    #
    # def error_handler(self, request: OrderCreateReq, context) -> OrderCreateResult:
    #     raise RuntimeError('Some error')
    #
    # def blocking(self, request_stream, context):
    #     for i in range(2):
    #         yield OrderCreateResult(name=str(i))
    #         self.barrier.wait()

    def unblock(self, _, context):
        self.barrier.wait()
        pass
        # return Empty()
