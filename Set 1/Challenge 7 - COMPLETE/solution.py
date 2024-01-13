import base64
from Crypto.Cipher import AES

cipher = ''

with open('C:\\Users\\nozi\\cryptopals\\Set 1\\Challenge 7\\7.txt', 'r') as f:
    for line in f:
        cipher += line.strip()

cipher = base64.b64decode(cipher)

key = b'YELLOW SUBMARINE'

aes = AES.new(key, AES.MODE_ECB)

print(aes.decrypt(cipher).decode())