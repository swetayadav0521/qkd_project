import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import grpc
from concurrent import futures
import time
import uuid

from proto import qkd_pb2, qkd_pb2_grpc

class KeyManagerServicer(qkd_pb2_grpc.KeyManagerServicer):
    def __init__(self):
        self.active_connections = {}  # Store active connections by KSID
        self.keys = {}  # Store generated keys by KSID

    def OpenConnect(self, request, context):
        key_stream_id = request.key_stream_id if request.key_stream_id else str(uuid.uuid4())
        self.active_connections[key_stream_id] = True  # Simulate connection
        print(f"Connection opened for KSID: {key_stream_id}")
        return qkd_pb2.OpenConnectResponse(key_stream_id=key_stream_id, status="SUCCESS")

    def GetKey(self, request, context):
        key_stream_id = request.key_stream_id
        if key_stream_id not in self.active_connections:
            return qkd_pb2.GetKeyResponse(key="", status="ERROR: No connection found")
        
        key = f"Key_{request.index}"  # Mock key generation based on index
        print(f"Generated key for KSID {key_stream_id}: {key}")
        return qkd_pb2.GetKeyResponse(key=key, status="SUCCESS")

    def CloseConnection(self, request, context):
        key_stream_id = request.key_stream_id
        if key_stream_id in self.active_connections:
            del self.active_connections[key_stream_id]
            print(f"Connection closed for KSID: {key_stream_id}")
            return qkd_pb2.CloseConnectionResponse(status="SUCCESS")
        else:
            return qkd_pb2.CloseConnectionResponse(status="ERROR: No connection found")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    qkd_pb2_grpc.add_KeyManagerServicer_to_server(KeyManagerServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()
