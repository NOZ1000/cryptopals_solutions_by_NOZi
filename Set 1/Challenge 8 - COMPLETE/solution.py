ciphers = []

with open('8.txt', 'r') as f:
    for line in f:
        for i in range(0, len(line.strip()), 32):
            ciphers.append(line.strip()[i:i+32])


for cipher in ciphers:
    if ciphers.count(cipher) > 1:
        print(cipher, ' detected ', ciphers.count(cipher), ' times')
        break