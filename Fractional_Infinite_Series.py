"""
A robot with an axe is about to start chopping wood incrementally faster, to infinite speed. Each swing will be 2x faster than the previous,
in other words the next swing will take exactly half as long as the last one. This will continue until the robot is chopping wood infinately fast.
Approximately how long will it take the robot to reach infinately fast chopping?

In order to answer that, we need to know the initial swing time, since the rules of the prompt (2x incriments) are based on an inital swing time. 
If we start at 1 min (slow robot), then the next swing would take 30 seconds. If we start as 10 seconds, then the next move would take 5.

So what's the answer?

2*intial_interval

proof?

let's only do it for the first 6 "chops", even though we know it will continue to infinity:

let's try starting with 1 min(60 seconds):
60 + 30 + 15 + 7.5 + 3.75 + 1.875 = 118 seconds, just 2 seconds shy of two minutes. 

let's try starting with 10 seconds:
10 + 5 + 2.5 + 1.25 + 0.625 + 0.3125 = 19.6875 seconds, less than 0.5 seconds shy of 20.

Each additional step adds an increasingly smaller figure to the total sum, to the extent that it approaches a limit of 2.
Technically it never gets to two, however, as the robot can keep moving infinately faster, adding infinately smaller numbers to our sum.
"""
# Update these input values
first_interval = 60  # Value for the first swing.
number_of_steps = 10  # How many "chops" into our infinite series should we calculate?
incrementation = 2   # How much is each following interval divided by? (1/2 = 2x faster, 1/3 = 3, etc)
decimal_dust = 5     # To how many places do we want to round our approximated limit? Larger incrementation values will yield limits closer to 1.

# The calculating program 
def fract_limit(n, output = [], steps = 0):
    if steps < number_of_steps:
        output.append(n)
        steps += 1
        fract_limit(n/incrementation, output, steps)
    
    else:
        print((output), "Total:", (sum(output)))

        if number_of_steps < 5:
            print("Increase number of steps above 5; we need a bigger sample size to approximate the limit")
        else:
            print("The limit of this series is approaching", round((sum(output)/first_interval), decimal_dust))

fract_limit(first_interval)