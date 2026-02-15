import sys
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

def sign_file(file_path, pvt_key_path):
    with open(pvt_key_path,"rb") as key_file:
        pvt_key = serialization.load_pem_private_key(key_file.read(), password=None)
        
    with open(file_path,"rb") as f:
        file_data = f.read()
        
    signature = pvt_key.sign(
        file_data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    
    sig_filename = file_path + ".sig"
    with open(sig_filename,"wb") as f:
        f.write(signature)
        
    print(f"Signature save in {sig_filename}")
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        sign_file(sys.argv[1],"pvt_key.pem")