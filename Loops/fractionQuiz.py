from functools import *
from random import randint

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n


@total_ordering
class Fraction(object):
     def __init__(self,top,bottom):
         " constructor"
         self.num = top
         self.den = bottom

     def __str__(self):
         " used by print "
         return str(self.num)+"/"+str(self.den)

     @lru_cache(maxsize=1024)
     def __add__(self,other):
         " Overload operator +"
         if isinstance(other, int):
            return Fraction(self.num + other*self.den, self.den)
         elif isinstance(other, Fraction):
           newnum = self.num*other.den + self.den*other.num
           newden = self.den * other.den
           common = gcd(newnum,newden)
           return Fraction(newnum//common,newden//common)
         else:
           raise ValueError("Tried to __add__ with a bad right hand side type")

     def __hash__(self):
         " Needed so that cache can work "
         return hash(self.__str__())

     def __eq__(self, other):
         "overload operator =="
         firstnum = self.num * other.den
         secondnum = other.num * self.den
         return firstnum == secondnum

     def __lt__(self,other):
         "Overloaded operator <"
         firstnum = self.num * other.den
         secondnum = other.num * self.den
         return firstnum < secondnum

     def __mul__(self, other):
         "Overload operator *"
         if str(other).isnumeric():
             return Fraction(self.num * other,self.den)

     def __rmul__(self, other):
         return self * other

     def __getitem__(self, item):
         "Overloads index searching"
         if (item == 0):
             return self.num
         else:
             return self.den

     def __iadd__(self, other):
         "Overloads operator +="
         return self + other

     def __pow__(self, power, modulo=None):
         "Overloads operator **"
         return Fraction(pow(self.num,power), pow(self.den,power))

if __name__=='__main__':

	onefifth = Fraction(1,5)
	twothirds = Fraction(2,3)

	#
	# Make this work
	#
	print("Should be 4/3: {}".format(twothirds * 2))
	print("Should be 2/5: {}".format(onefifth * 2))

	#
	# Make this work
	#
	print("Should be 4/3: {}".format(2 * twothirds))
	print("Should be 2/5: {}".format(2 * onefifth))

	#
	# Make this work
	#
	print("Should print the numerator 2 : {}".format(twothirds[0]))
	print("Should print the denominator 5 : {} ".format(onefifth[1]))

	#
	# make this work
	#
	tmp = Fraction(0,1)
	tmp += onefifth
	tmp += twothirds
	print("Should be 13/15: {}".format(tmp))

	#
	# make this work
	#
	print("Should be 8/27: {}".format(twothirds ** 3))