import grpc
from concurrent import futures
from services.user_service import UserService
from services.document_service import DocumentService
from services import user_service_pb2_grpc, document_service_pb2_grpc

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    document_service_pb2_grpc.add_DocumentServiceServicer_to_server(DocumentService(), server)
    server.add_insecure_port("[::]:50051")
    print("Server started on port 50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
