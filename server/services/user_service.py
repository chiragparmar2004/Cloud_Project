# import user_service_pb2, user_service_pb2_grpc
from . import user_service_pb2
from . import user_service_pb2_grpc

import uuid

class UserService(user_service_pb2_grpc.UserServiceServicer):
    def __init__(self):
        self.users = {}

    def CreateUser(self, request, context):
        user_id = str(uuid.uuid4())
        self.users[user_id] = {"username": request.username, "email": request.email}
        return user_service_pb2.CreateUserResponse(user_id=user_id, message="User created successfully.")

    def GetUser(self, request, context):
        user = self.users.get(request.user_id)
        if not user:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("User not found.")
            return user_service_pb2.GetUserResponse()
        return user_service_pb2.GetUserResponse(
            user_id=request.user_id,
            username=user["username"],
            email=user["email"]
        )

    def UpdateUser(self, request, context):
        user = self.users.get(request.user_id)
        if not user:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("User not found.")
            return user_service_pb2.UpdateUserResponse()
        user["username"] = request.username
        user["email"] = request.email
        return user_service_pb2.UpdateUserResponse(message="User updated successfully.")
