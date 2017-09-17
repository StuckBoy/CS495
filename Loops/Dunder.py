class Interval:
    def __init__(self, first=0, second=0):
        "Constructor"
        self.numOne = first
        self.numTwo = second

    def __str__(self):
        "Used by print"
        if(self.numTwo != 0):
            return str(self.numOne) + " ... " + str(self.numTwo)
        else:
            return str(self.numOne) + " ... " + str(self.numTwo)

    def __add__(self, other):
        "Overloads '+' symbol"
        if(str(other).isnumeric()):
            return Interval(self.numTwo+other,self.numOne+other)
        else:
            if(self.numOne > other.numTwo):
                return Interval(other.numTwo,self.numTwo+other.numOne)
            else:
                return Interval(self.numOne,self.numTwo+other.numOne)

    def __radd__(self, other):
        "Does right '+' stuff"
        return self + other

    def __mul__(self, other):
        "Does multiplication stuff"
        if(str(other).isnumeric()):
            return Interval(self.numOne * other,self.numTwo * other)
        else:
            return Interval(self.numOne * other.numTwo,self.numTwo * other.numOne)

    def __eq__(self, other):
        "Overrides eq to check for interval equality"
        if (self.numOne == other.numOne and self.numTwo == other.numTwo):
            return True
        else:
            return False


a = Interval(2,3)     # The interval from 2 ... 3
b = Interval(4)       # the interval from 0 ... 4
c = Interval()	      # The interval 0 ... 0
aa = Interval(2,3)    # Also the interval 2 ... 3

print("Should be 2...3 ", a)		# Needs __str__() to work
print("Should be 0...7 ", a+b)		# Needs __add__() to work
print("Should be 10...14 ", 10+b)	# Needs __radd__() to work
print("Should be 0...12 ", a*b)		# Needs __mul__() to work
print("Should be 4...6 ", a*2)		# Needs __mul__() with an int to work


print("should be true ", a==a)		# Needs __eq__() to work
print("Should be true ", a==aa)		# ditto
