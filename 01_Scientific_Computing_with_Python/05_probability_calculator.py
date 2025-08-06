# Solution to "Build a Probability Counter Project", 08/06/2025

# INSTRUCTIONS: Suppose there is a hat containing 5 blue balls, 4 red balls,
# and 2 green balls. What is the probability that a random draw of 4 balls
# will contain at least 1 red ball and 2 green balls? While it would be
# possible to calculate the probability using advanced mathematics, an easier
# way is to write a program to perform a large number of experiments to
# estimate an approximate probability. For this project, you will write a
# program to determine the approximate probability of drawing certain balls
# randomly from a hat.

# MORE INFO: https://www.freecodecamp.org/learn/scientific-computing-with-python/build-a-probability-calculator-project/build-a-probability-calculator-project



import copy
import random

class Hat:
    def __init__(self, **args):
        # create self.contents, then fill with balls
        self.contents = []
        for color, amount in args.items():
            for i in range(amount):
                self.contents.append(f'{color}')
        # max value for first draw in each trial
        self.total = len(self.contents)

    def draw(self, num):
        # check for enough balls to draw from and return the emptied hat
        if num >= len(self.contents):
            drawn = self.contents[:]
            self.contents.clear()
            return drawn

        # create random draw of balls and remove from original hat
        sample = random.sample(self.contents, num)
        for ball in sample:
            self.contents.remove(ball)
        return sample

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # initiate successful trial count
    win = 0

    for run in range(num_experiments):
        # create hat unique to trial
        hat_copy = copy.deepcopy(hat)
        sample = hat_copy.draw(num_balls_drawn)

        # create dictionary to record data and fill
        data = {}
        for ball in sample:
            if ball in data:
                data[ball] += 1
            else:
                data[ball] = 1

        # null hypothesis is that trial is successful
        success = True
        # check for alternative hypothesis
        for color, amount in expected_balls.items():
            if color not in data or data[color] < amount:
                success = False
                break

        # update successful trial count
        if success:
            win += 1

    # calculate and return probability
    probability = round(win/num_experiments, 3)
    return probability

