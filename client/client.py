import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import grpc

from proto import qkd_pb2, qkd_pb2_grpc


def case1(stub):
    """
    Case 1: Undefined KSID in a single-link scenario
    Open a connection, get a key, and close the connection.
    """
    # Step 1: Open a connection without predefined KSID (KSID is None)
    open_response = stub.OpenConnect(qkd_pb2.OpenConnectRequest(source="APP_A", destination="APP_B", key_stream_id=""))
    if open_response.status == "SUCCESS":
        print(f"Case 1: Connection opened with KSID: {open_response.key_stream_id}")

        # Step 2: Retrieve a key
        get_key_response = stub.GetKey(qkd_pb2.GetKeyRequest(key_stream_id=open_response.key_stream_id, index=0))
        if get_key_response.status == "SUCCESS":
            print(f"Case 1: Retrieved key: {get_key_response.key}")
        else:
            print(f"Case 1: Failed to retrieve key: {get_key_response.status}")

        # Step 3: Close the connection
        close_response = stub.CloseConnection(qkd_pb2.CloseConnectionRequest(key_stream_id=open_response.key_stream_id))
        if close_response.status == "SUCCESS":
            print(f"Case 1: Connection closed for KSID: {open_response.key_stream_id}")
    else:
        print("Case 1: Failed to open connection.")


def case2(stub):
    """
    Case 2: Undefined KSID and failed GET_KEY call
    Simulate a failure during key retrieval.
    """
    # Step 1: Open a connection
    open_response = stub.OpenConnect(qkd_pb2.OpenConnectRequest(source="APP_A", destination="APP_B", key_stream_id=""))
    if open_response.status == "SUCCESS":
        print(f"Case 2: Connection opened with KSID: {open_response.key_stream_id}")

        # Step 2: Simulate a failure by using an invalid KSID during GetKey
        invalid_ksid = "invalid-ksid"
        get_key_response = stub.GetKey(qkd_pb2.GetKeyRequest(key_stream_id=invalid_ksid, index=0))
        if get_key_response.status == "SUCCESS":
            print(f"Case 2: Retrieved key: {get_key_response.key}")
        else:
            print(f"Case 2: Error retrieving key: {get_key_response.status}")  # Expect failure

        # Step 3: Close the connection
        close_response = stub.CloseConnection(qkd_pb2.CloseConnectionRequest(key_stream_id=open_response.key_stream_id))
        if close_response.status == "SUCCESS":
            print(f"Case 2: Connection closed for KSID: {open_response.key_stream_id}")
    else:
        print("Case 2: Failed to open connection.")


def case3(stub):
    """
    Case 3: Predefined KSID in a single-link scenario
    Open a connection using a predefined KSID, get a key, and close the connection.
    """
    predefined_ksid = "predefined-ksid-1234"  # Predefined KSID

    # Step 1: Open a connection with the predefined KSID
    open_response = stub.OpenConnect(qkd_pb2.OpenConnectRequest(source="APP_A", destination="APP_B", key_stream_id=predefined_ksid))
    if open_response.status == "SUCCESS":
        print(f"Case 3: Connection opened with predefined KSID: {predefined_ksid}")

        # Step 2: Retrieve a key
        get_key_response = stub.GetKey(qkd_pb2.GetKeyRequest(key_stream_id=predefined_ksid, index=0))
        if get_key_response.status == "SUCCESS":
            print(f"Case 3: Retrieved key: {get_key_response.key}")
        else:
            print(f"Case 3: Failed to retrieve key: {get_key_response.status}")

        # Step 3: Close the connection
        close_response = stub.CloseConnection(qkd_pb2.CloseConnectionRequest(key_stream_id=predefined_ksid))
        if close_response.status == "SUCCESS":
            print(f"Case 3: Connection closed for KSID: {predefined_ksid}")
    else:
        print("Case 3: Failed to open connection.")


def case4(stub):
    """
    Case 4: Predefined KSID and failed GET_KEY call in a single-link scenario
    Simulate a failure during key retrieval with predefined KSID.
    """
    predefined_ksid = "predefined-ksid-1234"  # Predefined KSID

    # Step 1: Open a connection with the predefined KSID
    open_response = stub.OpenConnect(qkd_pb2.OpenConnectRequest(source="APP_A", destination="APP_B", key_stream_id=predefined_ksid))
    if open_response.status == "SUCCESS":
        print(f"Case 4: Connection opened with predefined KSID: {predefined_ksid}")

        # Step 2: Simulate a failure by using an invalid index during GetKey
        invalid_index = 999  # Invalid index to simulate failure
        get_key_response = stub.GetKey(qkd_pb2.GetKeyRequest(key_stream_id=predefined_ksid, index=invalid_index))
        if get_key_response.status == "SUCCESS":
            print(f"Case 4: Retrieved key: {get_key_response.key}")
        else:
            print(f"Case 4: Error retrieving key: {get_key_response.status}")  # Expect failure

        # Step 3: Close the connection
        close_response = stub.CloseConnection(qkd_pb2.CloseConnectionRequest(key_stream_id=predefined_ksid))
        if close_response.status == "SUCCESS":
            print(f"Case 4: Connection closed for KSID: {predefined_ksid}")
    else:
        print("Case 4: Failed to open connection.")


def case5(stub):
    """
    Case 5: Application discovery in a QKD network
    Simulate discovery and key retrieval between APP_A and APP_Z.
    """
    # Step 1: APP_A opens connection (mock discovery)
    open_response = stub.OpenConnect(qkd_pb2.OpenConnectRequest(source="APP_A", destination="QKD_NETWORK", key_stream_id=""))
    if open_response.status == "SUCCESS":
        appa_ksid = open_response.key_stream_id
        print(f"Case 5: APP_A connected to QKD network with KSID: {appa_ksid}")

        # Simulate discovery: APP_Z receives KSID from APP_A
        appz_ksid = appa_ksid  # In a real network, this would be communicated

        # Step 2: APP_Z opens connection using discovered KSID
        open_response = stub.OpenConnect(qkd_pb2.OpenConnectRequest(source="APP_Z", destination="QKD_NETWORK", key_stream_id=appz_ksid))
        if open_response.status == "SUCCESS":
            print(f"Case 5: APP_Z connected to QKD network with KSID: {appz_ksid}")

            # Step 3: Retrieve keys for both applications
            get_key_response = stub.GetKey(qkd_pb2.GetKeyRequest(key_stream_id=appa_ksid, index=0))
            if get_key_response.status == "SUCCESS":
                print(f"Case 5: APP_A retrieved key: {get_key_response.key}")

            get_key_response = stub.GetKey(qkd_pb2.GetKeyRequest(key_stream_id=appz_ksid, index=0))
            if get_key_response.status == "SUCCESS":
                print(f"Case 5: APP_Z retrieved key: {get_key_response.key}")

            # Step 4: Close connection
            close_response = stub.CloseConnection(qkd_pb2.CloseConnectionRequest(key_stream_id=appa_ksid))
            if close_response.status == "SUCCESS":
                print(f"Case 5: Connection closed for KSID: {appa_ksid}")
        else:
            print("Case 5: Failed to open connection for APP_Z.")
    else:
        print("Case 5: Failed to open connection for APP_A.")


def run():
    # Connect to the Key Manager service
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = qkd_pb2_grpc.KeyManagerStub(channel)

        # Run all the cases
        print("\nRunning Case 1:")
        case1(stub)

        print("\nRunning Case 2:")
        case2(stub)

        print("\nRunning Case 3:")
        case3(stub)

        print("\nRunning Case 4:")
        case4(stub)

        print("\nRunning Case 5:")
        case5(stub)


if __name__ == "__main__":
    run()
