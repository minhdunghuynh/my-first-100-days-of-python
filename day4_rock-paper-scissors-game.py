import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#HUMAN INPUT
human_input = int(input('What do you choose? Type 0 for "Rock", 1 for "Paper" or 2 for "Scissors".\n'))
random_number = [0, 1, 2]
computer_input = random.choice(random_number)
if human_input == 0:
    print("You chose ROCK")
    print(rock)
# COMPUTER INPUT
    if computer_input == 0:
        print(rock)
        print("Computer chose ROCK")
    elif computer_input == 1:
        print(paper)
        print("Computer chose PAPER")
    elif computer_input == 2:
        print(scissors)
        print("Computer chose SCISSORS")
elif human_input == 1:
    print("You chose PAPER")
    print(paper)
    if computer_input == 0:
        print(rock)
        print("Computer chose ROCK")
    elif computer_input == 1:
        print(paper)
        print("Computer chose PAPER")
    elif computer_input == 2:
        print(scissors)
        print("Computer chose SCISSORS")
elif human_input == 2:
    print("You chose SCISSORS")
    print(scissors)
#COMPUTER INPUT
    if computer_input == 0:
        print(rock)
        print("Computer chose ROCK")
    elif computer_input == 1:
        print(paper)
        print("Computer chose PAPER")
    elif computer_input == 2:
        print(scissors)
        print("Computer chose SCISSORS")
else:
    print("You choose an invalid number. You lose the game.")
#GAME RULE
#DRAW
if human_input == computer_input:
    print("It's a draw between you and the computer")
#LOSE
elif human_input == 0 and computer_input == 1:
    print("You lost")
elif human_input == 1 and computer_input == 2:
    print("You lost")
elif human_input == 2 and computer_input == 0:
    print("You lost")
#WIN
elif human_input == 0 and computer_input == 2:
    print("You win")
elif human_input == 1 and computer_input == 0:
    print("You win")
elif human_input == 2 and computer_input == 1:
    print("You win")

