with open('file.txt', 'r', encoding = "utf-8") as f:
    b= f.read()
RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
key = int(input('шаг шифровки: '))
message = b.upper()
out = ''

for i in message:
    old = RU.find(i)
    shifr = old + key
    if i in RU:
        out += RU[shifr]
    else:
        out += i
print (out)
with open('file2.txt', 'w') as f:
    f.write(out)
