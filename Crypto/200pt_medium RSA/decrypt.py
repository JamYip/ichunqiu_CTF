#coding=UTF-8
import gmpy2
import rsa

n = 0xC2636AE5C3D8E43FFB97AB09028F1AAC6C0BF6CD3D70EBCA281BFFE97FBE30DD
e = 0x10001
p = 275127860351348928173285174381581152299
q = 319576316814478949870590164193048041239

d = int(gmpy2.invert(e, (p-1) * (q -1)))

pri_key = rsa.PrivateKey(n, e, d, p, q)
with open('flag.enc', 'rb') as f:
    print(rsa.decrypt(f.read(), pri_key).decode())