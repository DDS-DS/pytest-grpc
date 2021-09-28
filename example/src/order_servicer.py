# from stub.test_pb2 import EchoRequest, EchoResponse, Empty
# from stub.test_pb2_grpc import EchoServiceServicer
# import threading

from order_stub.order_pb2 import OrderCreateReq,OrderCreateResult
from order_stub.order_service_pb2_grpc import OrderServiceServicer
import threading



class Servicer(OrderServiceServicer):
    def __init__(self):
        self.barrier = threading.Barrier(2)

    def CreateOrder(self, request, context) -> OrderCreateResult:
        return OrderCreateResult(name=f'test-{request.name}')

    def error_handler(self, request: OrderCreateReq, context) -> OrderCreateResult:
        raise RuntimeError('Some error')

    def blocking(self, request_stream, context):
        for i in range(2):
            yield OrderCreateResult(name=str(i))
            self.barrier.wait()

    def unblock(self, _, context):
        self.barrier.wait()
        pass
        # return Empty()


