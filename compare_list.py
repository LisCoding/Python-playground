# Write a program that compares two lists and prints a message depending on if the inputs are
# identical or not.
# Your program should be able to accept and compare two lists: list_one and list_two. If both
# lists are identical print "The lists are the same". If they are not identical print
# "The lists are not the same." Try the following test cases for lists one and two:
# test cases:
list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
#
# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]
#
# list_one = [1,2,5,6,5,16]
# list_two = [1,2,5,6,5]
# list_one = ['celery','carrots','bread','milk']
# list_two = ['celery','carrots','bread','cream']


i = 0
not_same = "false"
while i < len(list_one):
    if list_one[i] != list_two[i]:
        print "The list are not the same"
        not_same = "true"
    i += 1
if not_same != "true":
    print "The list are the same"
