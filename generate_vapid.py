import base64
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

def b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("utf-8")

private_key = ec.generate_private_key(ec.SECP256R1())

private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption(),
).decode("utf-8")

public_key = private_key.public_key()
nums = public_key.public_numbers()
x = nums.x.to_bytes(32, "big")
y = nums.y.to_bytes(32, "big")
public_raw = b"\x04" + x + y
public_b64 = b64url(public_raw)

print("=== COPY THESE ===")
print("VAPID_PUBLIC_KEY:")
print(public_b64)
print("\nVAPID_PRIVATE_KEY_PEM:")
print(private_pem)
