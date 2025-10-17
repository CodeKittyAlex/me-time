from cryptography.fernet import Fernet

print("is de or encription needed")
cry = input()


key = Fernet.generate_key()
fernet = Fernet(key)

if (cry.lower == 'encrypt'):
    message = input("what is the message")
    encMessage = fernet.encrypt(message.encode())

elif (cry.lower == 'decrypt'):
    message = input("what needs decrypting")
    decMessage = fernet.decrypt(message.decode())
else:
    print(cry)
