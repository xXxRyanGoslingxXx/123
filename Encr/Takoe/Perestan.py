def decode(s:str, k:int=1):
    d = {x+1:'' for x in range(k)}
    c=0
    v=1
    h=(len(s)-(len(s)//k)*k)
    while(v<=h):
        for j in range((len(s)//k)+1): 
            d[v] += s[j+c]
        c +=(len(s)//k)+1
        v +=1
    while(v<k+1):
        for j in range((len(s)//k)):
            d[v] += s[j+c]
        c +=(len(s)//k)
        v +=1
    x = []
    c=0
    while(c<(len(s)//k)):
        for j in d.values():
            x.append(j[c])
        c+=1
    for i in range(h):
        x.append(d[i+1][-1])
    return ''.join(x)
 
def encode(s:str, k:int=1):
    d = {x+1:'' for x in range(k)}
    for i in [s[0+x:k+x] for x in range(0, len(s), k)]:
        c = 1
        for j in i:
            d[c] += j
            c += 1
    return ''.join([x for x in d.values()])
 
strtocode = input()
keycode = int(input())
 
print('Исходная строка:',strtocode,'Ключ:',keycode)
print('Кодируем:',encode(strtocode,keycode))
print('Декодируем:',decode(encode(strtocode,keycode),keycode))
