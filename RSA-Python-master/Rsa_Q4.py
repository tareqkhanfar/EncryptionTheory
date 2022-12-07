import rsa

def CreateKey():
    (public, private) = rsa.newkeys(1024)

    print(public)
    print("#################################################################################################################\n\n\n")
    print(private)


    with open('./publickey.txt', 'wb') as f:
        f.write(public.save_pkcs1('PEM'))

    with open('./privatekey.txt', 'wb') as f:
        f.write(private.save_pkcs1('PEM'))

def load_keys():
    with open('./publickey.txt', 'rb') as f:
        public = rsa.PublicKey.load_pkcs1(f.read())

    with open('./privatekey.txt', 'rb') as f:
        private = rsa.PrivateKey.load_pkcs1(f.read())

    return public, private

def encrypt(msg, key):
    return rsa.encrypt(msg.encode('ascii'), key)

def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False


CreateKey()
public, private = load_keys()
print("#################################################################################################################\n\n\n")

message = input('Enter a message:')
ciphertext = encrypt(message, public)



plaintext = decrypt(ciphertext, private)

print("#################################################################################################################\n\n\n")

print(f'Cipher text: {ciphertext}')
print("#################################################################################################################\n\n\n")

if plaintext:
    print(f'The Plain text After Decryption : {plaintext}')
else:
    print('Could not decrypt the message.')
