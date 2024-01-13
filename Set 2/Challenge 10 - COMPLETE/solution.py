from Crypto.Cipher import AES
from base64 import b64decode
from pwn import xor

key = b'YELLOW SUBMARINE'
iv = b'\x00' * 16
ciphers = b''

with open("C:\\Users\\nozi\\cryptopals\\Set 2\\Challenge 10\\10.txt", 'r') as f:
    for line in f:
        ciphers += b64decode(line.strip())

def encrypt(plaintext, key, iv):
    assert type(plaintext) == bytes
    assert type(key) == bytes
    assert type(iv) == bytes

    aes = AES.new(key, AES.MODE_ECB)
    
    blocks = []

    for i in range(0, len(plaintext), 16):
        blocks.append(plaintext[i:i+16])
    
    ciphertext = b''
    prev = iv

    for block in blocks:
        prev = aes.encrypt(xor(block, prev))
        ciphertext += prev
    
    return ciphertext

def decrypt(ciphertext, key, iv):
    assert type(ciphertext) == bytes
    assert type(key) == bytes
    assert type(iv) == bytes

    aes = AES.new(key, AES.MODE_ECB)
    
    blocks = []

    for i in range(0, len(ciphertext), 16):
        blocks.append(ciphertext[i:i+16])
    
    plaintext = b''
    prev = iv

    for block in blocks:
        plaintext += xor(aes.decrypt(block), prev)
        prev = block
    
    return plaintext


print(decrypt(ciphers, key, iv).decode())
