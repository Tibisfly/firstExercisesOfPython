import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

#  DON'T CHANGE THE CODE ABOVE
def fire_gun():
	# YOUR CODE HERE
    x = spin_chamber()
    print(x)

    if(bullet_position == x):
        print("You're dead")
    else:
        print( "Keep Playing!")
    


fire_gun()