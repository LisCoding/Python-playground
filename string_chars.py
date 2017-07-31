# Write a program that takes a list of strings and a string containing a single character, and
# prints a new list of all the strings containing that character.
# test case:
# # input
# word_list = ['hello','world','my','name','is','Anna']
# char = 'o'
# # output
# new_list = ['hello','world']
word_list = ['hello','world','my','name','is','Anna']
char = 'a'
new_list = []
for i in word_list:
    if i.count(char) >= 1:
        new_list += [i]
print new_list
