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
        if self.count == len(self.word):
            raise StopIteration
        self.count = self.count + 1
        return self.word[self.count-1]

class doubleIt:
    "Returns the double of the input sequence"
    def __init__(self):


    def __iter__(self):


    def __next__(self):


print("\n\nShould be hello")
for x in Hello():
    print(x)

print("Should be 12 12 12 12 12 ...")
#for x in Twelve():
 #   print(x, end=" ")

