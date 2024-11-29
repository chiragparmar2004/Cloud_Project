import grpc
from concurrent import futures
import uuid
from threading import Lock
from . import document_service_pb2, document_service_pb2_grpc


class DocumentService(document_service_pb2_grpc.DocumentServiceServicer):
    def __init__(self):
        self.documents = {}  # Stores document data
        self.lock = Lock()
        self.active_editors = {}  # Maps document_id to active editor streams
        print("DocumentService initialized.")

    def CreateDocument(self, request, context):
        document_id = str(uuid.uuid4())
        with self.lock:
            self.documents[document_id] = {
                "title": request.title,
                "content": request.initial_content
            }
            # Initialize active editors for the document and add the creator
            self.active_editors[document_id] = {request.user_id: context}

        print(f"Document created: {document_id} with title: {request.title} by user: {request.user_id}")
        
        return document_service_pb2.CreateDocumentResponse(
            document_id=document_id,
            message="Document created successfully."
        )

    def JoinDocument(self, request, context):
        with self.lock:
            document = self.documents.get(request.document_id)
            if not document:
                print(f"Document not found: {request.document_id}")
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("Document not found.")
                return document_service_pb2.JoinDocumentResponse()

            # Add user to active editors
            self.active_editors[request.document_id][request.user_id] = context
            print(f"User {request.user_id} joined document {request.document_id}.")

        return document_service_pb2.JoinDocumentResponse(
            document_id=request.document_id,
            title=document["title"],
            content=document["content"]
        )

    def EditDocument(self, request_iterator, context):
        print("EditDocument called. Listening for incoming edits...")

        user_id = None
        document_id = None

        try:
            for edit_request in request_iterator:
                user_id = edit_request.user_id
                document_id = edit_request.document_id
                print(f"Received edit from user {user_id} for document {document_id}")

                with self.lock:
                    document = self.documents.get(document_id)
                    if not document:
                        print(f"Document not found during edit: {document_id}")
                        context.set_code(grpc.StatusCode.NOT_FOUND)
                        context.set_details("Document not found.")
                        return

                    # Update the document content
                    document["content"] = edit_request.content_change
                    print(f"Updated document {document_id} content: {document['content']}")

                    # Broadcast the update to all active editors
                    active_editors = self.active_editors.get(document_id, {})
                    for editor_id, editor_context in active_editors.items():
                        if editor_context == context:
                            # The sender already receives updates automatically
                            continue

                        try:
                            # Yield the update to other connected editors
                            print(f"Broadcasting update to user {editor_id} for document {document_id}")
                            yield document_service_pb2.EditDocumentResponse(
                                document_id=document_id,
                                user_id=user_id,
                                updated_content=document["content"],
                                timestamp=edit_request.timestamp
                            )
                        except Exception as e:
                            print(f"Failed to send update to user {editor_id}: {e}")
        except Exception as e:
            print(f"Error in EditDocument: {e}")
        finally:
            print(f"EditDocument stream for user {user_id} on document {document_id} has ended.")

    def AddEditorStream(self, request, context):
        with self.lock:
            if request.document_id not in self.active_editors:
                self.active_editors[request.document_id] = {}
            self.active_editors[request.document_id][request.user_id] = context
        print(f"Added user {request.user_id} to active editors for document {request.document_id}.")
        return document_service_pb2.AddEditorStreamResponse(message="User added to active editors.")
