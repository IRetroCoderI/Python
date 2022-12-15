from random import randint

x = randint(1,6)



from random import choice
players = ['joey','charles','billy','florence','daisy']
nextPlayer = choice(players)
#print(f"Next player is {nextPlayer.title()}")

class Die:
    def __init__(self, sides = 6):
        self.sides = sides
    
    def roll(self, times = 1):
        while times!=0:
            print(f"Rolled a {randint(1, self.sides)}!")
            times = times - 1





