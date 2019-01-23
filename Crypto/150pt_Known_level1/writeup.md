## 题目名称：Known

### 思路

level1：密文是base64编码，解码后与明文异或，发现所有结果都一致，所以密文与明文异或就是key，使用该key解密password.enc，解压压缩包

level2：发现明文的'0'总是对应'{'，所以推出是一一对应的映射关系。

`flag{Y0uG0tKn0wnPl4inT3xt4tt4ck}`


### 参考

https://www.ichunqiu.com/writeup/detail/1769