from random import randint

class Die():
    """docstring for Die"""
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        print(str(x))


# ten_sides_die = Die(10)
# for x in range(1,11):
#     ten_sides_die.roll_die()
twenty_sides_die = Die(20)
for x in range(1,21):
    twenty_sides_die.roll_die()