# Optional Assignment: Foo and Bar
# Write a program that prints all the prime numbers and all the perfect squares for
#  all numbers between 100 and 100000.
# For all numbers between 100 and 100000 test that number for whether it is prime or a perfect square.
# If it is a prime number print "Foo". If it is a perfect square print "Bar".
 # If it is neither print "FooBar".
# Do not use the python math library for this exercise. For example, if the number you are evaluating is 25, you will
# have to figure out if it is a perfect square. It is, so print "Bar".
#
#1...10 print if the prime numbers:
def is_prime(num): #2 => true, 3=> true 6=> false
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True

print is_prime(4)
# print is_prime(5)
# print is_prime(7)
# print is_prime(9)
# print is_prime(10)

def is_square(num): # 4 => true 9 => true, 12=> false
    number = num/ 2
    while number > 0:
        if number * number == num:
            return True
        number -= 1
    return False

print is_square(2)
# print is_square(4)
# print is_square(9)
# print is_square(10)
# print is_square(100)

def foo_bar():
    for i in range(100, 100001):
        if is_prime(i):
            print i, "foo"
        elif is_square(i):
            print i, "bar"
        else:
            print i , "foobar"

foo_bar()
