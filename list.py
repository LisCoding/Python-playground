# Assignment: Type List
# Write a program that takes a list and prints a message for each element in the list, based on
# that element's data type.
# Your program input will always be a list. For each item in the list, test its data type.
# If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.
#
# Here are a couple of test cases. Think of some of your own, too. What kind of
#  unexpected input could you get?
# #input
# l = ['magical unicorns',19,'hello',98.98,'world']
# #output
# "The list you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"
l = ['magical unicorns',19,'hello',98.98,'world']
# l = ["hello", "there", "ye"]
# l = []
integer_type = ""
string_type = ""
string = []
sum_result = 0
for i in l:
    if type(i) is int or type(i) is float:
        integer_type = "integer"
        sum_result += i
    elif type(i) is str:
        string_type = "string"
        string += [i]
if integer_type and string_type:
    print "the list you entered is of mixed type"
    print "String:", " ".join(string)
    print "Sum:", sum_result
elif string_type:
    print "the list you entered is of string type"
    print "String:", " ".join(string)
# check if the list is empty
elif l == []:
    print "Upss You entered a empty list"
else:
    print "the list you entered is of integer type"
    print "Sum:", sum_result
