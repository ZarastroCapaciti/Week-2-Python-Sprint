import random

#variable initialization
game_run = True
roll1 = 0
roll2 = 0

#processing start
while game_run:
    game = input('Do you wanna roll a dice? type y/n') #user input
    if game[0].lower() == 'y':
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        print('Dice 1: ' + str(roll1))
        print('Dice 2: ' + str(roll2))
        print('Total: ' + str(roll1 + roll2))
    else:
        print('Thank you for playing, come back soon.') #if the user types "n"
        game_run = False
