import random

# Define the computer's possible choices
computer_choices = [-1, 1, 0]  # -1 for paper, 1 for rock, 0 for scissor

# Let the computer make a random choice
computer = random.choice(computer_choices)

youstr=input("Enter your choice (r for rock, p for paper, s for scissor):").lower()

youDict={"r":1, "p":-1, "s":0}

you=youDict[youstr]

if(computer==you):
    print("It's a draw")

else:
    if (computer==-1 and you==0):
        print("You win")

    elif (computer==-1 and you==1):
        print("You lose")

    elif (computer==1 and you==0):
        print("You lose")

    elif (computer==1 and you==-1):
        print("You win")

    elif (computer==0 and you==1):
        print("You win")

    elif (computer==0 and you==-1):
        print("You lose")

    else:
        print("Something is wrong")