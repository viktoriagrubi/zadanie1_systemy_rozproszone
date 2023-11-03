# server.py
import math
from concurrent import futures
import grpc
import arithmetic_pb2
import arithmetic_pb2_grpc

# Klasa implementująca usługi mikroserwisu
class ArithmeticService(arithmetic_pb2_grpc.ArithmeticServicer):
    def Add(self, request, context):
        # Implementacja operacji dodawania
        result = request.num1 + request.num2
        return arithmetic_pb2.Result(result=result)

    def Subtract(self, request, context):
        # Implementacja operacji odejmowania
        result = request.num1 - request.num2
        return arithmetic_pb2.Result(result=result)

    def Multiply(self, request, context):
        # Implementacja operacji mnożenia
        result = request.num1 * request.num2
        return arithmetic_pb2.Result(result=result)

    def Divide(self, request, context):
        # Implementacja operacji dzielenia
        if request.num2 == 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Cannot divide by zero")
            return arithmetic_pb2.Result()
        result = request.num1 / request.num2
        return arithmetic_pb2.Result(result=result)

# Funkcja do uruchamiania serwera gRPC
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    arithmetic_pb2_grpc.add_ArithmeticServicer_to_server(ArithmeticService(), server)
    server.add_insecure_port("[::]:50051")  # Serwer działa na porcie 50051
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()

