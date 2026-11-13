import random
logo = '''
▄▄▄▄  █  ▐▌▄▄▄▄  ▗▖   ▗▞▀▚▖ ▄▄▄        █  ▐▌▗▞▀▚▖ ▄▄▄  ▄▄▄ ▄ ▄▄▄▄    
█   █ ▀▄▄▞▘█ █ █ ▐▌   ▐▛▀▀▘█           ▀▄▄▞▘▐▛▀▀▘▀▄▄  ▀▄▄  ▄ █   █   
█   █      █   █ ▐▛▀▚▖▝▚▄▄▖█                ▝▚▄▄▖▄▄▄▀ ▄▄▄▀ █ █   █   
                 ▐▙▄▞▘               ▗▄▖                   █     ▗▄▖ 
                                    ▐▌ ▐▌                       ▐▌ ▐▌
                                     ▝▀▜▌                        ▝▀▜▌
                                    ▐▙▄▞▘                       ▐▙▄▞▘
'''
print(logo)
print("Welcome to The Number Guessing Game!\n"
      "I'm thinking of a number between 1 and 100. Guess what the number is.\n ")

computer_number = random.randint(1, 100)
player_lives = 0
game_level = input("Choose a difficulty. Type 'easy' or 'hard': \n ").lower().strip()

if game_level == "easy":
    player_lives = 10

else:
    player_lives = 5

#+++++++++++++++++++++++++++FUNCTIONS+++++++++++++++++++++++++++++
def lives_calculator(guess_number, chosen_number, lives):
    if guess_number > chosen_number:
        return lives - 1

    elif guess_number < chosen_number:
        return lives -1

    return lives

def guess_result(guess_number, chosen_number, lives):
        if guess_number < chosen_number:
            return f"Too low. You have {lives} attempts remaining. "
        elif guess_number > chosen_number:
            return f"Too high. You have {lives} attempts remaining. "
        else:
            return f"You got it. The number was {chosen_number}. "



#+++++++++++++++++++++++++++GAMEPLAY+++++++++++++++++++++++++++++
print(f"You have {player_lives} attempts remaining to guess the number. ")

game_on = True
while game_on:

    player_guess = int(input("Make a guess: "))

    player_lives = lives_calculator(player_guess, computer_number, player_lives)

    result = guess_result(player_guess, computer_number, player_lives)

    print(result)

    if player_lives <= 0:
        print("You ran out of lives. Game over.")
        game_on = False

    elif result == f"You got it. The number was {computer_number}. ":
        game_on = False

    else:
        continue






