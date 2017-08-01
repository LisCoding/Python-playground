# Assignment: Names
# Write the following function.
# Part I
# Given the following list:
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# output :
# Michael Jordan
# John Rosales
# Mark Guillen
# KB Tonel

def students_list(students):
    for student in students:
        name = [ ]
        for val in student.itervalues():
            name += [val]
        print " ".join(name)
students_list(students)

# Now, given the following dictionary:
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
#  output:
#  Students
# 1 - MICHAEL JORDAN - 13
# 2 - JOHN ROSALES - 11
# 3 - MARK GUILLEN - 11
# 4 - KB TONEL - 7
# Instructors
# 1 - MICHAEL CHOI - 11
# 2 - MARTIN PURYEAR - 13

def names(users):
    for key in users.iterkeys():
        print key
        for i in range(0, len(users[key])):
            info = users[key][i]
            name = []
            for val in info.itervalues():
                name += [val]
            name = " ".join(name)
            length = len(name) - 1
            num = i + 1
            print num, "-",name, "-", length

names(users)
