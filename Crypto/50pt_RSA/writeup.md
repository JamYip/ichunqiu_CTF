## 题目名称：RSA

### 题目内容：
This time John managed to use RSA " correctly "ellipsis; I think he still made some mistakes though。flag.txt

### 解题思路：
已知`n`和`d`等于有私钥，直接解密即可。`m = pow(c, d, n)`
答案：`IceCTF{rsa_is_awesome_when_used_correctly_but_horrible_when_not}`