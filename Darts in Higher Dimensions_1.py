"""
Building the testing program from "Darts in Higher Dimensions"


https://www.youtube.com/watch?v=6_yU9eJ0NxA&t=382s&ab_channel=Numberphile

"""
import numpy as np
import sys


sys.setrecursionlimit(10000) # Otherwise the limit would be 1000

first_radius = 500     # How big is the initial radius?
cycle_number = 1000      # How many games do we play before we determine some observed patterns?


final_score_list = [] # An empty list to store the scores we get back.
score_frequency = {} # An empty dictionary that will track the relative frequency of each throw.
# e.g. if we make throw #6, we add a tick to Index 6. 
observed_probabilities = [] # This is where we'll break down the score_frequency/cycle_number

def dartboard(initial_radius, final_score = 1):
    #print(f"%%%%%%%%%%%%%%%%%%%%%% Throw #{final_score} %%%%%%%%%%%%%%%%%%%%%%%%%%")
    #print(f"Current Radius:{round(initial_radius, 2)}")

    # Let's generate a random point where the dart landed
    rand_x = np.random.randint(-1*first_radius, first_radius)
    rand_y = np.random.randint(-1*first_radius, first_radius)
    #print(f"Your throw landed at:({rand_x}, {rand_y})")

    # How far are we from a bullseye?
    distance = np.sqrt((rand_x**2)+(rand_y**2))
    #print(f"Distance from a perfect bullseye: {round(distance, 2)}")

    # Did we lose or do we get to play again?
    if distance <= initial_radius:
        final_score += 1
        score_frequency[final_score] = (score_frequency.get(final_score, 0) +1) #this is how we make the frequency log
        new_radius = np.sqrt((initial_radius**2)-(distance**2))
        dartboard(new_radius, final_score)

    elif distance > initial_radius:
        #print(f"Game Over! Your final score was {final_score}")
        final_score_list.append(final_score)

def repeater(game_counter = 0):

    if game_counter < cycle_number:
        #print(f"Game #{game_counter +1}")
        dartboard(first_radius)
        game_counter += 1
        repeater(game_counter)

repeater()

for score, frequency in score_frequency.items():
    observed_probabilities.append(str(f"{score}: {round((frequency/cycle_number)*100)}%"))

print(f"{len(final_score_list)} Games")   
print(f"High Score: {max(final_score_list)}")
print(f"Frequency Table: {score_frequency}")
print(f"Observed Probabilities: {observed_probabilities}")