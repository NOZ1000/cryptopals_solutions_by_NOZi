from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64decode
from pwn import xor

ciphers = b''
key = b'YELLOW SUBMARINE'
iv = b'\x00' * 16

with open('C:\\Users\\nozi\\cryptopals\\Set 2\\Challenge 10 - COMPLETE\\10.txt', 'r') as f:
    for line in f:
        ciphers += b64decode(line.strip())

def encrpyt(plaintext, key, iv):
    assert type(plaintext) == bytes
    assert type(key) == bytes
    assert type(iv) == bytes

    aes = AES.new(key, AES.MODE_ECB)
    blocks = []

    for i in range(0, len(plaintext), 16):
        blocks.append(plaintext[i:i+16])

    cipher = b''
    prev = iv

    for i, block in enumerate(blocks):
        if i == len(blocks) - 1:
            block = pad(block, 16)
        prev = aes.encrypt(xor(prev, block))
        cipher += prev

    return cipher


def decrypt(cipher, key, iv):
    assert type(cipher) == bytes
    assert type(key) == bytes
    assert type(iv) == bytes

    aes = AES.new(key, AES.MODE_ECB)

    blocks = []

    for i in range(0, len(cipher), 16):
        blocks.append(cipher[i:i+16])

    plaintext = b''
    prev = iv

    for i, block in enumerate(blocks):
        if i == len(blocks) - 1:
            block = unpad(block, 16)
        plaintext += xor(aes.decrypt(block), prev)
        prev = block
    
    return plaintext

enc = encrpyt(b'Hello Worlds@', key, iv)
dec = decrypt(enc, key, iv)

print(enc)
print(dec)
