import os
from cryptography.fernet import Fernet
from openai import OpenAI

# 运行前替换
KEY = b''
ENCRYPTED_API = b''

def get_client():
    api_key = os.getenv("OPENAI_API_KEY")

    # 优先环境变量
    if api_key:
        return OpenAI(api_key=api_key)

    # 如果没填加密key
    if not KEY or not ENCRYPTED_API:
        raise ValueError("请配置 API Key")

    try:
        cipher = Fernet(KEY)
        api_key = cipher.decrypt(ENCRYPTED_API).decode()
        return OpenAI(api_key=api_key)

    except Exception as e:
        raise ValueError(f"API解密失败: {e}")
