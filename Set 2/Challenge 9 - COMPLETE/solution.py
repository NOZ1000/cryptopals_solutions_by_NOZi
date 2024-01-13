from Crypto.Util.Padding import pad

message = b"YELLOW SUBMARINE"

print(pad(message, 20))