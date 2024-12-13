from random import randint


class Die:
    """Making die for random numbers."""

    def __init__(self, sides=6):
        """Initialize the die."""
        self.sides = sides

    def roll_die(self):
        """Defining a function that return to us a random number between 1 and the number of sides."""
        return randint(1, self.sides)


# Make a 6-sided die, and show the results of 10 rolls.
d6 = Die()

results = list()
for rull_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("\n10 rolls of a 6-sided die:", results)

# Make a 10-sided die, and show the results of 10 rolls.
d10 = Die(10)

results = list()
for rull_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die:", results)

# Make a 20-sided die, and show the results of 10 rolls.
d20 = Die(sides=20)

results = list()
for rull_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sided die:", results)
