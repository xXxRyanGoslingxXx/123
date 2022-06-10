with open('file.txt', 'r', encoding = "utf-8") as f:
    b= f.read()
strcode = b
key = int(input('ключ:'))
def encode(s:str, k:int=1):
    d = {x+1:'' for x in range(k)}
    for i in [s[0+x:k+x] for x in range(0, len(s), k)]:
        c = 1
        for j in i:
            d[c] += j
            c += 1
    return ''.join([x for x in d.values()])
print('начальное сообщение:',strcode)
print('Шифрованное сообщение:',encode(strcode,key))
with open('file2.txt', 'w') as f:
    f.write(encode(strcode,key))
