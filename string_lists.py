#
#  .find()
#  .replace()
#  min()
#  max()
#  .sort()
#  len()
# Find and Replace
# In this string: words = "It's thanksgiving day. It's my birthday,too!" print the position of the first instance of
# the word "day". Then create a new string where the word "day" is replaced with the word "month".
words = "It's thanksgiving day. It's my birthday,too!"
words = words.split(" ")
index = words.index("day.")
words[index] = "month."
words = " ".join(words)
print words

# Min and Max
# Print the min and max values in a list like this one: x = [2,54,-2,7,12,98].
# Your code should work for any list.
x = [2,54,-2,7,12,98]
y = [-34,54,-2,7,12,98]
print "max value is ",max(x)
print "min value is ",min(x)
print "max value is ",max(y)
print "min value is ",min(y)
# First and Last
# Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"].
#  Now create a new list containing only the first and last values in the original list.
# Your code should work for any list.
x = ["hello",2,54,-2,7,12,98,"world"]
print "first value:", x[0]
print "last value:", x[-1]
my_list = [x[0], x[-1]]
print my_list
#
# New List
# Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first.
# Then, split your list in half. Push the list created from the first half to position 0 of the list created
 # from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98].
# Stick with it, this one is tough!
x = [19,2,54,-2,7,12,98,32,10,-3,6]
# [-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
x.sort()
print x
length = len(x)
length = length -1
num = length / 2
a, b = [], []
for i in range(0, length):
    if i < num:
        a +=[x[i]]
    else:
        b +=[x[i]]
x = [a]
for i in b:
    x += [i]
print x
