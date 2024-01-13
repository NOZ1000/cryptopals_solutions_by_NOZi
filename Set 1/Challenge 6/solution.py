from Crypto.Util.number import bytes_to_long, long_to_bytes


def hamming_distance(str1, str2):
    assert len(str1) == len(str2)
    assert type(str1) == type(str2) == bytes

    return sum([bin(a ^ b).count('1') for a, b in zip(str1, str2)])

