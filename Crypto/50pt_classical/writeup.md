## 题目名称：classical

### 解题思路
替换加密，词频分析
在线解密：https://quipqiup.com/
有部分单词没有匹配，特别是最后一句话，将其复制到搜索引擎搜索，找到结果为
`A quick brown fox jump over the lazy dog`,将其添加到Clues里重新进行词频分析
`Wcuun=Greek ofsr=lazy btlhn=quick veq=fox mtpa=jump`

在明文找到一串字符`LyjtL3fvnSRlo2xvKIjrK2ximSHkJ3ZhJ2Hto3x9`，但不是答案~

试一下凯撒解密，还不是！在这基础上用base64解码：
`flag{classical_cipher_so_easy}`

### 参考
https://www.ichunqiu.com/writeup/detail/21