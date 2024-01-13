from Crypto.Util.number import long_to_bytes
from pwn import xor

ENGLISH_WORDS = []
CIPHERS = []

with open('C:\\Users\\nozi\\cryptopals\\Set 1\\Challenge 3 - COMPLETE\\english_wordlist.txt', 'r') as f:
    for line in f:
        line = line.strip()
        ENGLISH_WORDS.append(line)

with open('C:\\Users\\nozi\\cryptopals\\Set 1\\Challenge 4 - COMPLETE\\4.txt', 'r') as f:
    for line in f:
        line = bytes.fromhex(line.strip())
        CIPHERS.append(line.strip())

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
    for cipher in CIPHERS:
        results = {}
        for i in range(256):
            key = bytes([i])
            result = single_byte_xor(cipher, key)
            results[key] = frecuency_analysis(result)

        best_key = max(results, key=results.get)
        
        try:
            print(single_byte_xor(cipher, best_key).decode())
        except UnicodeDecodeError:
            continue
        


if __name__ == '__main__':
    main()