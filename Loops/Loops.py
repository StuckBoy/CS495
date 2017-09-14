#Counts up to 10 including 1 and 10
numbers = [1,2,3,4,5,6,7,8,9,10]
for x in numbers:
    print(x)

print(" ")

#Count backwards from 30 by 3's
x = 30
while(x != 3 ):
    print(x)
    x = x-3

print(" ")

#Loop that prints pairs of numbers
for x in range(1,3):
    for y in range(1,4):
        print (str(x) + ", " + str(y))

print(" ")

#Print star pyramid thing
for x in range(1,8):
    print ("*" * x)

print(" ")

#Infinite Loop
while(1):
    print("Reeeeeeeeeeeeeeee")
    break

#Follow the rules
a=1
print(a)
for x in range(1,21):
    if a % 2 == 0:
        a = a//2
        print(a)
    else:
        a = 3*a+a//2
        print(a)

print(" ")

#Do it 1000 times
a=1
print(a)
for x in range(1,1001):
    if a % 2 == 0:
        a = a//2
        print(a)
    else:
        a = 3*a+a//2
        print(a)
