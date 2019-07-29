
# Simplified Battleship!
import random
import sys

SEA_LENGTH = 20
SHIP_LENGTH = 3
SHIP_COUNT = 3
HASHES_STRING = '#' * (SEA_LENGTH+2)
MAX_RETRIES = 1000

def isValidPlacement(sea, index):
    if index < 0 or index > SEA_LENGTH - SHIP_LENGTH:
        return False

    for i in range(SHIP_LENGTH):
        if (sea[index + i] == '*'):
            return False
    return True


def generateShipPlacements(sea_length, ship_length, ship_count):
  # FYI: lines 9-11 can be shortened to a 'list comprehension' via
  # array = [0 for i in range(sea_length)]
  # but we haven't covered this shorthand :)
  sea = []
  for i in range(sea_length):
    sea.append('0')

  # now that we have our sea, let's fill it with a ship
  count = 0
  retries = 0
  while count < SHIP_COUNT and retries < MAX_RETRIES:
      rand_index = random.randint(0, len(sea) - SHIP_LENGTH)
      if isValidPlacement(sea, rand_index):
          count += 1
          for i in range(SHIP_LENGTH):
              sea[rand_index + i] = '*'
      else:
          retries += 1
  return sea

def printSea(sea):
    print(HASHES_STRING)
    sys.stdout.write('#')
    for i in sea:
        sys.stdout.write(i)
    print '#'
    print(HASHES_STRING)

'''
Battleship is a game where you attempt to discover your opponent's ship locations in a hidden sea.

The player has a matching 'sea' where they can track previous attempts to discover a ship.

If a player successfully guesses the location of a ship, the opponent must tell them so that the player can use that information to guess future shots. This is what the player 'sea' board is for.

Objective:
 Continually ask the user to shoot a slot with a missile
 If it is a hit, mark that index in 'player_sea' with a *
 If it is a miss, mark that index in the 'player_sea' with a X so they know not to shoot there again!
 End the game when all 'ships' have been 'sunk' (when all '*'s in the player_sea board map to the '*'s in the 'opponent_sea')
 After each choice, you should reprint the player_sea array using printSea function defined above

 STRETCH: Implement the computer AI to take its turn after each choice you make and see who wins.
'''

########################################
#      YOUR CODE BELOW THIS LINE       #
########################################

'''
Q: What are your milestones?
A:

    1) Make a function thst presents the user with input prompt
    2) Ability to continuallly call a function from #1
    3) Write a function that checks if choice is a hit in the opponent_sea
    4) Befoer each user input, print the current state of the player's see with an "X"
    5) If function from #3 returns False, mark players sea with an X
    6) If function from #3 returns true, mark players sea with a *
    7) Write a function that checks if player's sea has hit all of the ships in the opponent sea
'''
player_sea = ['-' for i in range(SEA_LENGTH)]
opponent_sea = generateShipPlacements(SEA_LENGTH, SHIP_LENGTH, SHIP_COUNT)

# def choice():
#     return int(raw_input("Where do you wanna hit? "))

def outofguesses(numberofguesses):
    return numberofguesses > 20

def choice():
    return int(raw_input("Where do you wanna hit? "))

def didithitornot(didit):
    if "*" in opponent_sea[didit]:
        player_sea[didit] = "*"
        print("you got a hit")

    else:
        player_sea[didit] = "X"
        print("you didnt")

        printSea(opponent_sea)
        numberofguesses=0

while True:
    hittarget = choice()
    didithitornot(hittarget)
    printSea(player_sea)
    outofguesses(numberofguesses)
    numberofguesses = numberofguesses +1

    if outofguesses == True:
        break







# this represents the 'hidden' board that you are attempting to shoot


# this represents the players board which tracks where you
# have previously attempted to shoot
