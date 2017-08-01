# Write a program that prints a 'checkerboard' pattern to the console.
# Your program should require no input and produce console output that looks like so:
# * * * *
#  * * * *
# * * * *
#  * * * *
# * * * *
#  * * * *
# * * * *
#  * * * *
row_1 = "* * * *"
row_2 = " * * * *"
print row_1
for i in range(1, 8):
    if i % 2 != 0:
        print row_2
    else:
        print row_1
