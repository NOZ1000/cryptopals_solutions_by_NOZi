'''
Fixed XOR
Write a function that takes two equal-length buffers and produces their XOR combination.
'''

from pwn import xor
from Crypto.Util.number import long_to_bytes

buffer1 = 0x1c0111001f010100061a024b53535009181c
buffer2 = 0x686974207468652062756c6c277320657965

buffer1 = long_to_bytes(buffer1)
buffer2 = long_to_bytes(buffer2)

result = xor(buffer1, buffer2)
result_hex = result.hex()

print(result_hex)