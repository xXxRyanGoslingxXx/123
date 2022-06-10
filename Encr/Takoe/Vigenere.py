class Vigenere:
    def __init__(self, alphabet_start, alphabet_end, key):
        self.astart = ord(alphabet_start)
        self.aend = ord(alphabet_end)
        self.alen = self.aend - self.astart+1
        self.key = key

    def get_char(self, i, j):
        return chr(self.astart + (j + i)%self.alen)

    def encode(self, target: str):
        result = ''
        for i in range(len(target)):
            result += self.get_char(
                ord(self.key[i % len(self.key)]) - self.astart,
                ord(target[i]) - self.astart
                )
        return result

permuter = Vigenere('а', 'я', 'дядина')

to_encode = "Учение - изучение пра-вил; опыт - изучение исключений"
print('start:', to_encode)
encoded = permuter.encode(to_encode)
print('encoded:', encoded)
