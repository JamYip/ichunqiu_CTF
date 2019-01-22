## 题目名称：medium RSA

### 题目内容：

你没看错，这还真是密码学系列了，相信你已经解出前两题了，那么继续看这题吧。

文件：mediumRSA.rar

flag格式：PCTF{flag}

### 解题思路
1. 用OpenSSL提取 `n` 和 `e`

```shell
root@kali:~/CTF# openssl rsa -pubin -text -modulus -in warmup -in pubkey.pem
Public-Key: (256 bit)
Modulus:
    00:c2:63:6a:e5:c3:d8:e4:3f:fb:97:ab:09:02:8f:
    1a:ac:6c:0b:f6:cd:3d:70:eb:ca:28:1b:ff:e9:7f:
    be:30:dd
Exponent: 65537 (0x10001)
Modulus=C2636AE5C3D8E43FFB97AB09028F1AAC6C0BF6CD3D70EBCA281BFFE97FBE30DD
writing RSA key
-----BEGIN PUBLIC KEY-----
MDwwDQYJKoZIhvcNAQEBBQADKwAwKAIhAMJjauXD2OQ/+5erCQKPGqxsC/bNPXDr
yigb/+l/vjDdAgMBAAE=
-----END PUBLIC KEY-----
```

2. http://www.factordb.com 用`n`求出`p` `q`

3. python 解出  

### 参考
https://www.ichunqiu.com/writeup/detail/577