from cryptography.fernet import Fernet

# 生成合法 KEY
key = Fernet.generate_key()
print("KEY =", key)

# 用这个 KEY 加密 API
cipher = Fernet(key)
encrypted = cipher.encrypt(b"youapi-key")

print("ENCRYPTED_API =", encrypted)
