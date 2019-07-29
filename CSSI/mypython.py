import random

'''
roundstring = raw_input("How many rounds do you want to play?")

rounds = int(roundstring)

i = 0

def moves (real_p, comp_p):
     print("Real player chose: " + real_p)
     print("Computer chose: " + comp_p)

    if (real_p == comp_p):
        print ("tie")

    elif (real_p == "paper" and comp_p == "rock") or \
         (real_p == "scissors" and comp_p == "paper") or \
         (real_p == "rock" and comp_p == "scissors"):

        print("Real player wins")

    else:
        print("Computer player wins")

while i < rounds:
    choices = ["rock", "paper", "scissors"]
    move_1 = raw_input("What is your choice?")
    comp_move = choices[random.randint(0,2)]


    moves(move_1, comp_move)

    i = i + 1
    '''

'''
while True:
        randomnumber = (random.randint(1, 10))



        usernumstring = raw_input("Guess a number between 1 and 10?")
        usernum = int(usernumstring)


        print("computer chose: " + str(randomnumber))
        print("You chose: " + str(usernum))

        if  (usernum == randomnumber):
            print("You got it right!")
            break

        elif (usernum < randomnumber):
            print("Too low :((, You are wrong...")

        elif (usernum > randomnumber):
            print("Too high :((, You are wrong...")
'''
