from cryptography.fernet import Fernet
#один ключ
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"Meet me at 9pm. The bus stop. Bring the case.")
print(token)
print(f.decrypt(token))