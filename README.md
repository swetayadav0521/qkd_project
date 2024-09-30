# QKD
This project simulates a Quantum Key Distribution (QKD) Application Interface using gRPC and Protocol Buffers (protobuf). The application acts as a client that communicates with a Key Management System (KMS) server using gRPC calls.

---

### Prerequisites

- Python 3.6+
- pip for managing Python packages
- virtualenv (optional, recommended for environment isolation)

### Setup Instructions

```
# Create virtual environment
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

#### Install Dependencies

```
pip install -r requirements.txt
```

 #### Running the gRPC Server
```
python server/server.py
```

#### Running the gRPC Client
```
python client/client.py
```
