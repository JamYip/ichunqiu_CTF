# coding=UTF-8
n = 0xD99E952296A6D960DFC2504ABA545B9442D60A7B9E930AFF451C78EC55D555EB
p = 325045504186436346209877301320131277983
q = 302825536744096741518546212761194311477
e = 0x10001
c1 = 0x0b39cc1b6127d3bbed2bc045148c911d467985a94b147ede80750f95a360d47a
c2 = 0x9afb1cdc1986d3bb53a3425b396c83618efaaa81c14c965c813415e5c54fce4b
c3 = 0x0f04b3b67ef230f80bb518d26ded38af84b6c8d87ba80c09ebf1d865123082fa

import gmpy2
import rsa

d = int(gmpy2.invert(e, (p-1) * (q - 1)))

priv_key = rsa.PrivateKey(n, e, d, p, q)
with open('./attach/encrypted.message1', 'rb') as f:
  data = f.read()
  print(rsa.decrypt(data, priv_key))
with open('./attach/encrypted.message2', 'rb') as f:
  data = f.read()
  print(rsa.decrypt(data, priv_key))
with open('./attach/encrypted.message3', 'rb') as f:
  data = f.read()
  print(rsa.decrypt(data, priv_key))

