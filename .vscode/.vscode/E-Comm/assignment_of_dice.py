import random
class Dice:
    
    def roll(self):
        a=random.randint(1,6)
        b=random.randint(1,6)
        return a,b   #automatically interpretted as tuple, could have used paranthesis too
    
    

print(Dice.roll())
        
        