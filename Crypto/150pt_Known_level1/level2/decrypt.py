decrypt_dect = {}
with open('known.txt') as f:
    data = f.readline().replace('\n','').replace('\r','')
    while data:
        data = f.readline().replace('\n','').replace('\r','')
        if data == '':
            break
        plain = data.split(':')[0]
        cipher = data.split(':')[1]
        for p, c in zip(plain, cipher):
            decrypt_dect[c] = p
print(decrypt_dect)
c_text = 'uAmUXk{jW{Stp{JpMA0spF7OS0SS0aq8'
p_text = ''
for c in c_text:
    p_text = p_text + decrypt_dect[c]
print(p_text)
