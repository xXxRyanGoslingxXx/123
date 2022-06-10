def atbash(s):
    abc = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    return s.translate(str.maketrans(
        abc + abc.upper(), abc[::-1] + abc.upper()[::-1]))

print(atbash("КРИПТОСТОЙКОСТЬ"))
