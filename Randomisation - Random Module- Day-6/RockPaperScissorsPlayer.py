import random
import rockPaperScicersGame


user_Choice = int(input("Let's Play Rock,Paper,Scissors ,Type 0 for Rock, 1 for paper,2 for Scissors"));
# print(user_Choice)
if user_Choice == 0:
    print(rockPaperScicersGame.rock)
elif user_Choice == 1:
    print(rockPaperScicersGame.paper)
elif user_Choice == 2:
    print(rockPaperScicersGame.scissors)

computer_Choice = random.randint(0,2)

if computer_Choice == 0:
    print(rockPaperScicersGame.rock)
elif computer_Choice == 1:
    print(rockPaperScicersGame.paper)
elif computer_Choice == 2:
    print(rockPaperScicersGame.scissors)

if user_Choice > computer_Choice:
    print(" You Win the Game")
elif user_Choice == computer_Choice:
    print("Game Draw!!")
else:
    print("Computer Has Won the Game")


# program_Choice = random.choice(rockPaperScicersGame)
# print(program_Choice)
