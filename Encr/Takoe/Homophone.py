import random
from prettytable import PrettyTable

class Homophone:
    def __init__(self, alphabet_start, alphabet_end, count, seed):
        self.homocodes = {}
        self.codes = count
        self.seed = seed
        random.seed(seed)
        self.ptable = PrettyTable()
        nums = set()
        cols = ['char']
        for j in range(count):
            cols.append('c'+str(j))
        self.ptable.field_names = cols

        for i in range(ord(alphabet_start), ord(alphabet_end)):
            lst = []
            plst = [chr(i)]

            for j in range(count):
                r = random.randint(0, ((ord(alphabet_end) - ord(alphabet_start))*10*count))
                while r in nums:
                    r = random.randint(0, ((ord(alphabet_end) - ord(alphabet_start))*10*count))
                nums.add(r)
                lst.append(r)
                plst.append(r)
            self.ptable.add_row(plst)
            self.homocodes[chr(i)] = lst

    def print(self):
        
        print(self.ptable)

    def encode(self, target: str):
        random.seed(self.seed)
        result = ''
        for i in range(len(target)):
            index = random.randint(0, self.codes-1)
            result += str(self.homocodes[target[i]][index]) + ' '

        return result
