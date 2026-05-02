from cryptography.fernet import Fernet

key = Fernet.generate_key()
print("KEY:")
print(key.decode())

cipher = Fernet(key)

api = input("输入你的API Key: ")

enc = cipher.encrypt(api.encode())

print("\nENCRYPTED_API:")
print(enc.decode())
