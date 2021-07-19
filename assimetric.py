import rsa
#ДВа ключа открыттый и закрытый
(pubkey, privkey) = rsa.newkeys(512)

message = b'I am password'

# шифруем
crypto = rsa.encrypt(message, pubkey)
print(crypto)
# расшифровываем
message = rsa.decrypt(crypto, privkey)
print(message)


