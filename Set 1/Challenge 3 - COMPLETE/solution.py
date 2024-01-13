'''
Single-byte XOR cipher
'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
... has been XOR'd against a single character. Find the key, decrypt the message.
'''

from Crypto.Util.number import long_to_bytes
from pwn import xor

cipher = 0x1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
cipher = long_to_bytes(cipher)

ENGLISH_WORDS = []

with open('C:\\Users\\nozi\\cryptopals\\Set 1\\Challenge 3 - COMPLETE\\english_wordlist.txt', 'r') as f:
    for line in f:
        ENGLISH_WORDS.append(line.strip())

def single_byte_xor(cipher, key):
    assert len(key) == 1
    assert type(key) == bytes
    assert type(cipher) == bytes

    result = b''
    for byte in cipher:
        result += xor(byte, key)
    return result


def frecuency_analysis(text):
    assert type(text) == bytes

    try:
        text = text.decode().upper()

    except UnicodeDecodeError:
        return 0
    score = 0
    for word in ENGLISH_WORDS:
        if word in text:
            score += 1
    return score


def main():
    results = {}
    for i in range(256):
        key = bytes([i])
        result = single_byte_xor(cipher, key)
        results[key] = frecuency_analysis(result)

    best_key = max(results, key=results.get)
    print(best_key)

    print(single_byte_xor(cipher, best_key))


if __name__ == '__main__':
    main()