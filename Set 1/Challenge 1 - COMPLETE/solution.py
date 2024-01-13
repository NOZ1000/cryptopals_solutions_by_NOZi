from base64 import b64encode
from Crypto.Util.number import long_to_bytes

input_string = 0x49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

output_string = b64encode(long_to_bytes(input_string)).decode()

print(output_string)