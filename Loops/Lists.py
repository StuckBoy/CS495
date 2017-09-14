print("Make a list of numbers 1-10")
a = []
for x in range(1,11):
    a.append(x)
for x in a:
    print(x)
print("Make a list of even numbers 1-50")
b = []
for x in range(2,52,2):
    b.append(x)

b.append(5)

for x in b:
    print(x)

print("Use List Comprehension")
evens = [x for x in range(1,51) if x % 2 == 0]
print(list(evens))

print("Compute a+b")
c = a + b
print(list(c))

print("Size of c (a+b)")
length = len(c)
print(length)

print("Find the number of fives in c")
count = 0
for x in c:
    if x == 5:
        count+=1
print(count)

print("Find the number of 5's in a+b using a sinlge line")
print(c.count(5))

print("Compute the sum of all elements in b")
sum = 0
for x in a:
    sum += x
print(sum)

print("Change the 3rd element to 99")
a[3] = 99
for x in a:
    print(x)

print("Use slices, print the 3rd through 5th element")
print(a[3:6])

print("Print the last two elements")
print(a[-2:])

print("Make a list of perfect squares")
squares = []
for x in range (1,11):
    squares.append(x*x)

print(list(squares))

print("Differences between a+b, a.insert(0,b), and a.extend(b)")
print("a+b combines the two lists by linking the end of a to the front of b")
print("a.insert(0,b) would insert the contents of b into the given position")
print("a.extend(b) is similar to a+b, except a.extend(b) actually modifies a")