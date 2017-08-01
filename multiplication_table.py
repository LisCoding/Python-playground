# Create a program that prints a multiplication table in your console.
numbers = ["x", 1, 2,3,4,5,6,7,8,9,10,11,12]
for i in numbers:
    print i,
print "*"

result = []
for i in range(1, 13):
    for j in range(1, 13):
        result += [i * j]
    for i in result:
        print i,
    result = []
    print "*"
