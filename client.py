# client.py
import grpc
import arithmetic_pb2
import arithmetic_pb2_grpc

# Funkcja do uruchamiania klienta
def run():
    channel = grpc.insecure_channel("localhost:50051")  # Klient łączy się z serwerem na porcie 50051
    stub = arithmetic_pb2_grpc.ArithmeticStub(channel)

    num1 = 10.5
    num2 = 2.0

    # Wywołanie operacji dodawania na serwerze
    add_response = stub.Add(arithmetic_pb2.ArithmeticRequest(num1=num1, num2=num2))
    # Wywołanie operacji odejmowania na serwerze
    subtract_response = stub.Subtract(arithmetic_pb2.ArithmeticRequest(num1=num1, num2=num2))
    # Wywołanie operacji mnożenia na serwerze
    multiply_response = stub.Multiply(arithmetic_pb2.ArithmeticRequest(num1=num1, num2=num2))
    # Wywołanie operacji dzielenia na serwerze
    divide_response = stub.Divide(arithmetic_pb2.ArithmeticRequest(num1=num1, num2=num2))

    print(f"Addition result: {add_response.result}")
    print(f"Subtraction result: {subtract_response.result}")
    print(f"Multiplication result: {multiply_response.result}")
    print(f"Division result: {divide_response.result}")

if __name__ == "__main__":
    run()
