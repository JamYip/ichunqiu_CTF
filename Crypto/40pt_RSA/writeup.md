## 题目名称：RSA?

### 题目内容：

John was messing with RSA again... he encrypted our flag! I have a strong feeling he had no idea what he was doing however, can you get the flag for us?flag.txt

### 解题思路
注意到`e=0x1`，因为加密算法为`C % n = M^e % n` (python表达式：`C = pow(M, e, n)`)。当`e=0x1`时，`C % n = M % n`，即`M = C + k * n`，k为非负整数，从0开始遍历k，直至获取明文为可读字符串。

当`k=0`时，有`IceCTF{falls_apart_so_easily_and_reassembled_so_crudely}`