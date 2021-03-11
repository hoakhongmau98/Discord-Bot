import codecs
import base64
from sys import argv
str_out = {}
"""
len_argv = int(len(argv[4]))
if len_argv < 6:
    z = []
    z.append(int(argv[4][1:-1]))
    [z.append(int(x[:-1])) for x in argv[5:-1]]
    z.append(int(argv[-1][:-2]))
    str_in = {argv[1][1:-1]: argv[2][:-1], argv[3][:-1]: z}
    print('here')
else:
    print('not here')
    str_in = {argv[1][1:-1]: argv[2][:-1], argv[3][:-1]: str(argv[4][:-1])}
print(str_in)
print(type(str_in))
"""


def decode(text):
    text = text.split(' ')
    len_argv = int(len(text[3]))
    if len_argv < 6:
        z = []
        z.append(int(text[0][1:-1]))
        [z.append(int(x[:-1])) for x in text[4:-1]]
        z.append(int(text[-1][:-2]))
        str_in = {text[1][1:-1]: text[2][:-1], text[3][:-1]: z}
        print('here')
        print(str_in)
    else:
        print('not here')
        str_in = {argv[1][1:-1]: argv[2][:-1], argv[3][:-1]: str(argv[4][:-1])}
        
    if str_in['type'] == "base64":
        encoded = base64.b64decode(str_in['encoded'])  # wow so encode
        encoded = str(encoded)
        encoded = encoded[2:-1]
    elif str_in['type'] == "hex":
        encoded = bytes.fromhex(str_in['encoded']).decode('utf-8')
    elif str_in['type'] == "rot13":
        encoded = codecs.encode(str_in['encoded'], 'rot_13')
    elif str_in['type'] == "bigint":
        str_hex = str_in['encoded']
        str_hex = str_hex[2:]
        encoded = bytes.fromhex(str_hex).decode('utf-8')
        # encoded = long_to_bytes(encoded)
    elif str_in['type'] == "utf-8":
        encoded = ''
        for b in str_in['encoded']:
            encoded = encoded + chr(b)
    str_out["decoded"] = encoded
    return str_out


print(decode('{"type": "utf-8", "encoded": [70, 117, 107, 117, 121, 97, 109, 97, 95, 87, 97, 108, 100, 111, 114, 102, 95, 97, 112, 101, 115]}'))



