from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

pvt_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

with open("pvt_key.pem","wb") as f:
    f.write(pvt_key.private_bytes(encoding=serialization.Encoding.PEM,
                                  format=serialization.PrivateFormat.PKCS8,
                                  encryption_algorithm=serialization.NoEncryption()))
    
pbl_key = pvt_key.public_key()
with open("pbl_key.pem","wb") as f:
    f.write(pbl_key.public_bytes(encoding=serialization.Encoding.PEM,
                                 format=serialization.PublicFormat.SubjectPublicKeyInfo))
    
print("Initialize key pair: pvt_key.pem and pbl_key.pem")