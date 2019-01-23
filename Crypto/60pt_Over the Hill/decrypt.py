ac = '3EAAAAA56A69AA55A95995A569AA95565556'
bc = '3EAAAAA56A69AA556A965A5999596AA95656'
a =  '8893CA588893CA588893CA588893CA588893'

# for ch1, ch2 in zip(ac, a):
#     xor = (ord(ch1) ^ ord(ch2)) % 0xf
#     print(hex(xor))

key = 'b50920bde10a200d11ca2bbde1092b0eddc5'
for ch1, ch2 in zip(bc, key):
    xor = (ord(ch1) ^ ord(ch2)) % 0xf
    print(hex(xor))