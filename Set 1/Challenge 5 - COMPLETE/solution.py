from pwn import xor 

def encrypt(plaintext, key):
    assert type(plaintext) == bytes
    assert type(key) == bytes

    result = b''
    for i in range(len(plaintext)):
        result += xor(plaintext[i], key[i % len(key)])
    return result

def main():
    message1 = b"Burning 'em, if you ain't quick and nimble\n"
    message1 += b"I go crazy when I hear a cymbal"
    key = b"ICE"

    print(encrypt(message1, key).hex())


if __name__ == '__main__':
    main()