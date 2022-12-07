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


def sign_sha1(msg, key):
    return rsa.sign(msg.encode('ascii'), key, 'SHA-1')

def verify_sha1(msg, signature, key):
    try:
        return rsa.verify(msg.encode('ascii'), signature, key) == 'SHA-1'
    except:
        return False

CreateKey()
public, private = load_keys()
print("#################################################################################################################\n\n\n")

message = input('Enter a message:')

signature = sign_sha1(message, private)

print("#################################################################################################################\n\n\n")


print(f'Signature: {signature}')
print("#################################################################################################################\n\n\n")



if verify_sha1(message, signature, public):
    print('Signature verified!')
else:
    print('Could not verify the message signature.')
