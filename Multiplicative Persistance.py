# what's special about 277777788888899?
# Multiplicative Persistance
# https://www.youtube.com/watch?v=Wim9WJeDTHQ&t=308s&ab_channel=Numberphile
#
# example: 5428
# 5*4*2*8 = 320
# 3*2*0 = 0
# two steps...

test_number = 277777788888899 # place the test number in here.


#let's make the program. Notice that the counter "steps" is being submitted equal to zero the first time.
def per(n, steps = 0):

    # If we've reached the end of the problem, with no more steps to go, do the following:
    if len(str(n)) ==1:
        print("Total Steps:", str(steps))
        return

    # Create a list of from the input numbers. A list can be easily used to manipulate its contents. int(1) is making
    # sure that the numbers added to the list are stored as integers, as thier source is a string version of the input numbers.
    digits = [int(i) for i in str(n)]

    result = 1
    steps += 1

    # Each digit will be multiplied in order, with the fist number being multiplied by 1 to store as itself (n*1 = n).
    for j in digits:
        result *= j # *= means make the updated counter 'result' = old 'result' * j
    print(result)
    
    # Recursion to allow for multiple steps until termination. Notice that the current step count is being submitted per interation.
    per(result, steps)

per (test_number)