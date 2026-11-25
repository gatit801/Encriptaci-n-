import hashlib
from simplecrypt import encrypt, decrypt

value = "Jade, caza pajaros"
def SHA256():
    result= hashlib.sha256( value.encode() )
    print("Datos encriptados por sha256:", result.hexdigest())
SHA256()

def MD5():
    result = hashlib.md5( value.encode())
    print("Datos encriptados por MD5", result.hexdigest())
MD5()

message = "Jade, caza pajaros"
hex_string = " "

def encryption():
    global hex_string
    ciphercode = encrypt('AIM', message)
    hex_string = ciphercode.hex()
    print("Encriptacion: ", hex_string)

def decryption():
    global hex_string
    byte_str = bytes.fromhex(hex_string)
    original = decrypt('AIM', byte_str)
    final_message = original.decode("utf-8")
    print("Desifrado: ", final_message)

encryption()
decryption()