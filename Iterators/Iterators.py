class Twelve:
    "Prints 12 forever."
    def __init__(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            print(12)

class Hello:
    "Returns 1 letter at a time of 'hello'."
    def __init__(self):
        self.word = ['h', 'e', 'l', 'l', 'o']
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.word:
            return self.word.pop
        else:
            raise StopIteration


print("\n\nShould be hello")
for x in Hello():
    print(x)

print("Should be 12 12 12 12 12 ...")
#for x in Twelve():
 #   print(x, end=" ")

