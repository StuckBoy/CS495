def count(num):
    "Takes the given number and counts up to it while printing."
    if(num >= 1):
        count(num-1)
        print(num)

def fac(n):
    "Takes in a given number and calculates the factorial of it"
    if(n == 1):
        return 1
    else:
        return n * fac(n-1)

def spacer(count, character):
    """Takes in count and character, then recursively prints count # of spaces
        before printing the given character."""
    if(count == 0):
        return character
    else:
        return (" " + str(spacer(count-1, character)))

def smallest(aList):
    "Given a list, this function recursively scans for the largest element & returns it."
    if(not aList):
        return "This is an empty list bruh."
    elif (len(aList) == 1):
        return aList[0]
    else:
        biggest = smallest(aList[1:])
        if(biggest > aList[0]):
            return biggest
        else:
            return aList[0]

def power(base, exp):
    """Takes in 2 numbers, a base and a power. It recursively computes the base to the exp,
        then returns it."""
    if(exp == 1):
        return base
    else:
        return base * power(base, exp-1)

def backwards(aStr):
    """Takes in a string, then recursively prints it backwards."""
    if(aStr == ""):
        return aStr
    else:
        return backwards(aStr[1:]) + aStr[0]

count(5)

print(fac(5))

print(spacer(5, '@'))

someList = [1,2,5,3,4]

print(smallest(someList))
emptyList = []
print(smallest(emptyList))

print(power(8,3))

empty = ""
word = "Spaghetti"
print(backwards(word))
print(backwards(empty))