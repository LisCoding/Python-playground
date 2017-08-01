# Assignment: Coin Tosses
# Write a function that simulates tossing a coin 5,000 times. Your function should print
 # how many times the head/tail appears.
#
# Sample output should be like the following:

# Starting the program...
# Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
# Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
# Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
# Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
# ...
# Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
# Ending the program, thank you!
import random
num = 5000
def coin_tosses(num):
    head, tails = 0, 0
    print "Starting the program"
    for i in range(1, num+1):
        toss_coin_res = random.random()
        toss_coin_res = round(toss_coin_res)
        if toss_coin_res == 1:
            head += 1
            print "Attempt #" + str(i) + ": Throwing a coin... It's a head! ... Got " + str(head) +  " head(s) so far and "  + str(tails) + " tail(s) so far"
        else:
            tails += 1
            print "Attempt #" + str(i) + ": Throwing a coin... It's a tail! ... Got " + str(head) +  " head(s) so far and "  + str(tails) + " tail(s) so far"
        print

coin_tosses(num)
