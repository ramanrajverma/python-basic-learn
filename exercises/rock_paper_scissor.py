import random
options = ("rock", "paper", "scissors")
player =  None
computer = random.choice(options)
player = input("Enter a choice(rock, paper, scissor): ")


while player not in options:
    player = input("Please enter a valid choice(rock, paper, scissor): ")

"""print(computer)
print(player)
"""

running = True

while running:
    if player == computer:
        print("Its a ties")

    elif player == "rock" and computer == "scissors":
        print("You win")
    elif player == "paper" and computer == "rock":
        print("you win")
    else:
        print("You Loose")
    
    if not input("Play again?  y/n: ").lower() == "y":
        running = False
print("Thank You")



print("______ More yet to be done in this __________--")