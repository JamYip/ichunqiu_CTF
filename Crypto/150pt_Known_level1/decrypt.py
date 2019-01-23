import base64
# ciphertext = 'IB8hBnIHFQkRBAERABwFCDsPe0AadDEZJVkIbWMyFzo='
# plaintext = 'jYj0ApA8korwFrDKhkBsyAfcklX81hYr'
ciphertext = 'KSgufn8uOVcdLCEBNDomchISdlIwQh9JJgUSZGQfDzk='
plaintext = 'cneHLYmfgGRgrTg1AvOaSwH3h0B16EAq'
ciphertext_b64 = base64.b64decode(ciphertext)
key = ''
for c1, c2 in zip(plaintext, ciphertext_b64):
    key = key + chr(ord(c1) ^ ord(c2))
print(key)

pwd_ciphertext = 'CzVrT1wCdFoUBARGMgYgN3McVkFDQzIINxUjPD8qIi0='

pwd_plain = ''
for c1, c2 in zip(key, base64.b64decode(pwd_ciphertext)):
    pwd_plain = pwd_plain + chr(ord(c1) ^ ord(c2))
print(pwd_plain)
#As you know that xor very simple
