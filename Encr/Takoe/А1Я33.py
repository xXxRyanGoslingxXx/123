def match(text, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')):
    return not alphabet.isdisjoint(text.lower())

print(match('test')) # False
print(match('тест')) # True
print(match('123Ы')) # True
print(match(''))     # False
