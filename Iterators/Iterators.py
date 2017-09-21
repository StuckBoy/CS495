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
        while self.word:
            return self.word.pop(0)
        else:
            raise StopIteration

class DoubleIt:
    "Makes an iterator that returns the double of an inputted sequence"
    def __init__(self, *args):
        self.entries = list(args[0])

    def __iter__(self):
        return self

    def __next__(self):
        if self.entries:
            return self.entries.pop(0) * 2
        else:
            raise StopIteration

class SecondDoubleIt:
    "Makes an iterator that returns the double of multiple inputted arguments"
    def __init__(self, *kwargs):
        self.input = list(kwargs)

    def __iter__(self):
        return self

    def __next__(self):
        if self.input:
            return self.input.pop(0) *2
        else:
            raise StopIteration

class JustLetters:
    "Takes in both letters and numbers, but only returns the letters of the input."
    def __init__(self, *args):
        self.input = list(args[0])
        self.letters = []
        length = len(self.input)
        while(length != 0):
            if self.input:
                thing = self.input.pop(0)
                if str(thing).isalpha():
                    self.letters.append(thing)
                else:
                    continue
                length = length - 1
            else:
                break

    def __iter__(self):
        return self

    def __next__(self):
        if self.letters:
            return self.letters.pop(0)
        else:
            raise StopIteration

class Words:
    "Takes in a string and separates out words based on whitespace."
    def __init__(self, *args):
        sentence = str(*args)
        self.sWords = sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.sWords:
            return self.sWords.pop(0)
        else:
            raise StopIteration

print("Should be 12 12 12 12 12 ...")
#for x in Twelve():
 #   print(x, end=" ")
#It does, but obviously loops to infinity.

print("\n\nShould be hello")
for x in Hello():
    print(x)

print("\n\nShould be 2 6 4 8")
for x in DoubleIt([1,3,2,4]):
    print(x, end = " ")
print("\n\nShould be empty")
for x in DoubleIt([]):
    print(x)

print("\n\nShould be 2 6 4 8")
for x in SecondDoubleIt(1,3,2,4):
    print(x, end = " ")
print("\nShould be 2 2 2 2 2 4 4 8 8 8 8 ")
for x in SecondDoubleIt(1,1,1,1,1,2,2,4,4,4,4):
    print(x, end = " ")

print("\n\nShould be empty")
for x in SecondDoubleIt([]):
    print(x)

print("\n\nShould be a b c d")
for letter in JustLetters(["a", 4, 5, "b", "c", 2, "d"]):
    print(letter, end = " ")
print("\n\nShould be a b c")
for letter in JustLetters(["a", 4, 5, "b", "c", 2]):
    print(letter, end = " ")

print("\n\nShould be I, Love, Cheese,")
for word in Words("I Love Cheese"):
    print(word, end=",")
print("\n\nShould be empty")
for word in Words(""):
    print(word, end=",")