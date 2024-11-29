import grpc
import threading
import sys
import time
import os
import tkinter as tk
from tkinter import simpledialog, messagebox
import queue

# Add the root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'E:\\Cloud final_Google_Docs')))

from server.services import user_service_pb2
from server.services import user_service_pb2_grpc
from server.services import document_service_pb2, document_service_pb2_grpc


class RealTimeEditorClient:
    def __init__(self):
        print("Initializing RealTimeEditorClient...")
        self.channel = grpc.insecure_channel('localhost:50051')
        self.document_stub = document_service_pb2_grpc.DocumentServiceStub(self.channel)
        self.user_stub = user_service_pb2_grpc.UserServiceStub(self.channel)

        self.user_id = None
        self.document_id = None
        self.edit_queue = queue.Queue()
        self.stop_listening = threading.Event()

        self.root = None
        self.text_widget = None
        self.user_name = None
        print("Client initialized successfully.")

    def create_user(self):
        print("Creating user...")
        root = tk.Tk()
        root.withdraw()

        self.user_name = simpledialog.askstring("User Registration", "Enter your username:")
        if not self.user_name:
            messagebox.showerror("Error", "Username is required")
            return False

        email = simpledialog.askstring("User Registration", "Enter your email:")
        if not email:
            messagebox.showerror("Error", "Email is required")
            return False

        try:
            request = user_service_pb2.CreateUserRequest(username=self.user_name, email=email)
            response = self.user_stub.CreateUser(request)
            self.user_id = response.user_id
            print(f"User created successfully: {self.user_name}, User ID: {self.user_id}")
            return True
        except grpc.RpcError as e:
            print(f"Error creating user: {e.details()}")
            return False

    def create_or_join_document(self):
        print("Creating or joining document...")
        root = tk.Tk()
        root.withdraw()

        choice = messagebox.askyesno("Document", "Do you want to create a new document? (No = Join existing)")

        if choice:
            title = simpledialog.askstring("New Document", "Enter document title:")
            initial_content = simpledialog.askstring("New Document", "Enter initial content:")

            request = document_service_pb2.CreateDocumentRequest(
                user_id=self.user_id,
                title=title,
                initial_content=initial_content
            )
            response = self.document_stub.CreateDocument(request)
            self.document_id = response.document_id
            print(f"Document created successfully: ID={self.document_id}, Title={title}")
            return initial_content
        else:
            document_id = simpledialog.askstring("Join Document", "Enter document ID to join:")
            request = document_service_pb2.JoinDocumentRequest(
                user_id=self.user_id,
                document_id=document_id
            ) 
            response = self.document_stub.JoinDocument(request)

            request2 = document_service_pb2.AddEditorStreamRequest(user_id=self.user_id, document_id=document_id)
            
            print("Joined  reqeust  ",request2)

            response2 = self.document_stub.AddEditorStream(request2)
            print("Joined editor stream for document, response2 ",response2)
            print(f"Joined editor stream for document {document_id}")

           
            self.document_id = response.document_id
            print(f"Joined document: ID={self.document_id}, Title={response.title}")
            return response.content

    def create_document_ui(self, initial_content):
        print("Creating document UI...")
        self.root = tk.Tk()
        self.root.title(f"Real-Time Document Editor - {self.user_name}")

        self.text_widget = tk.Text(self.root, wrap=tk.WORD)
        self.text_widget.pack(expand=True, fill='both')
        self.text_widget.insert(tk.END, initial_content)
        print("UI initialized with initial content.")

        self.text_widget.bind('<KeyRelease>', self.on_key_release)
        self.text_widget.edit_modified(False)

        update_thread = threading.Thread(target=self.listen_for_updates, daemon=True)
        update_thread.start()
        print("Update listening thread started.")

    def on_key_release(self, event=None):
        print("Key released, queuing edit...")
        self.send_edit()

    def send_edit(self):
        content = self.text_widget.get('1.0', tk.END)
        print(f"Queuing edit: {content.strip()}")
        self.edit_queue.put(content)

    def send_edits(self):
        print("Sending edits to server...")
        while not self.stop_listening.is_set():
            try:
                content_change = self.edit_queue.get(timeout=1)
                timestamp = str(time.time())
                print(f"Sending edit: {content_change.strip()}")
                yield document_service_pb2.EditDocumentRequest(
                    user_id=self.user_id,
                    document_id=self.document_id,
                    content_change=content_change,
                    timestamp=timestamp
                )
            except queue.Empty:
                continue

    def listen_for_updates(self):
        print("Listening for updates from server...")
        try:
            responses = self.document_stub.EditDocument(self.send_edits())
            print("Listening for updates from server ...",responses)

            for response in responses:
                print("Listening for updates from server response...",response)
                if response.user_id != self.user_id:
                    print(f"Received update: {response.updated_content.strip()}")
                    self.root.after(0, self.update_text_widget, response.updated_content)
        except grpc.RpcError as e:
            print(f"Error receiving updates: {e.details()}")
            messagebox.showerror("Connection Error", "Lost connection to server")

    def update_text_widget(self, content):
        print(f"Updating text widget with new content: {content.strip()}")
        current_pos = self.text_widget.index(tk.INSERT)
        self.text_widget.delete('1.0', tk.END)
        self.text_widget.insert('1.0', content)
        self.text_widget.mark_set(tk.INSERT, current_pos)

    def start(self):
        print("Starting client...")
        if not self.create_user():
            return

        initial_content = self.create_or_join_document()
        self.create_document_ui(initial_content)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def on_closing(self):
        print("Closing client...")
        self.stop_listening.set()
        self.root.destroy()
        print("Client closed.")

if __name__ == "__main__":
    client = RealTimeEditorClient()
    client.start()
