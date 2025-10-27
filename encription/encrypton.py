from cryptography.fernet import Fernet

print("is en(1) or decription(2) needed")
cry = int(input())


key = Fernet.generate_key()
fernet = Fernet(key)

if (cry == 1):
    message = input("what is the message ")
    encMessage = fernet.encrypt(message.encode())
    print(encMessage)

elif (cry == 2):
    message = input("what needs decrypting ")
    decMessage = fernet.decrypt(message).decode()
    print(decMessage)

else:
    print('err')
