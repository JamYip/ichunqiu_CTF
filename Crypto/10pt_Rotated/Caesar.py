# coding=UTF-8
# 凯撒解密

class Caesar:
    def decrypt(self, chiper, offset):
        plain = ''
        for ch in chiper:
            if ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
                tmp = ord(ch) - offset
                if tmp < ord('A'): tmp = tmp + 26
                plain = plain + chr(tmp)
            elif ord(ch) >= ord('a') and ord(ch) <= ord('z'):
                tmp = ord(ch) - offset
                if tmp < ord('a'): tmp = tmp + 26
                plain = plain + chr(tmp)
            else:
                plain = plain + ch
        return plain

def main():
    chiper = input('Input the chiper: ')
    for i in range(1, 26):
        print('offset: %d. ' + Caesar().decrypt(chiper, i), i)

if __name__ == "__main__":
    main()
