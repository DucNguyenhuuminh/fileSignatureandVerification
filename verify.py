import sys
import hashlib
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

def verify_file(file_path, sign_path, pbl_key_path):
    with open(pbl_key_path,"rb") as key_file:
        pbl_key = serialization.load_pem_public_key(key_file.read())
        
    with open(file_path,"rb") as f:
        file_data = f.read()
        
    with open(sign_path,"rb") as f:
        signature = f.read()
        
    file_hash = hashlib.sha256(file_data).hexdigest()
    print(f"\nFile: {file_path}")
    print(f"SHA-256:{file_hash}")
    
    try:
        pbl_key.verify(
            signature,
            file_data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("Verification success")
    except Exception:
        print("Verification fail!!!")
        
if __name__ == "__main__":
    if len(sys.argv) > 2:
        verify_file(sys.argv[1], sys.argv[2], "pbl_key.pem")
    else:
        print("Usage: python verify.py <original_file> <signature_file>")