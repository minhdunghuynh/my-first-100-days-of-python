import random
#WORD LIST-----------------------------------------------------
fruit_list = [
    "apricot", "apple", "avocado", "banana", "blackberry", "blackcurrant",
    "blueberry", "cantaloupe", "cherry",
    "clementine", "coconut", "cranberry", "custard apple", "date",
    "dragon fruit", "durian", "elderberry", "fig", "gooseberry", "grape",
    "grapefruit", "guava", "honeydew melon", "jackfruit",
    "kiwi", "kumquat", "lemon", "lime", "longan", "lychee", "mandarin", "mango", "mangosteen", "mulberry",
    "nectarine", "olive", "orange", "papaya", "passion fruit", "peach",
    "pear", "persimmon", "pineapple", "plum", "pomegranate", "pomelo",
    "quince", "rambutan", "raspberry", "redcurrant", "satsuma",
    "soursop", "star fruit", "strawberry", "tamarind", "tangerine", "watermelon", "yuzu",
    "zucchini"
]
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''
]

computer_fruit = random.choice(fruit_list)
print(r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    ''')
print(r'''
  ┌─────────────────┐
  │  fruit edition  │
  └─────────────────┘
''')
#RANDOM ACCESS MEMORY-----------------------------------------------------
health_point = 6
placeholder = ""
chosen_letter = []

for character in computer_fruit:
    placeholder += "_"

print(f"The mysterious fruit is: {placeholder}")
#GAMEPLAY-----------------------------------------------------------------
while health_point > 0:
    printed_screen = ""
    print("+" * 100)
    print("+" * 100)

    guess = input("Guess a letter: \n").lower()
#WHEN GUESS IS CORRECT-----------------------------------------------------
    if guess in computer_fruit:
        health_point += 0
        print(f"You have {health_point} chance(s) left")

        if guess in chosen_letter:
            print(f"You have chosen letter {guess} before.")

        for character in computer_fruit:
            if guess == character:
                printed_screen += guess
                chosen_letter.append(guess)
            elif character in chosen_letter:
                printed_screen += character
            else:
                printed_screen += "_"
        print(f"The mysterious fruit is: {printed_screen}")
        if printed_screen == computer_fruit:
            print(r"""
__   __               __        ___       _
\ \ / /__  _   _      \ \      / (_)_ __ | |
 \ V / _ \| | | |      \ \ /\ / /| | '_ \| |
  | | (_) | |_| |       \ V  V / | | | | |_|
  |_|\___/ \__,_|        \_/\_/  |_|_| |_(_)
""")
            break

# WHEN GUESS IS NOT CORRECT-----------------------------------------------------
    elif guess not in computer_fruit:
        health_point -= 1
        print(f"You have {health_point} chance(s) left")
        for character in computer_fruit:
            if character in chosen_letter:
                printed_screen += character
            else:
                printed_screen += "_"
        print(f"The mysterious fruit is: {printed_screen}")
#PRINT STAGES OF THE HANGMAN-----------------------------------------------------
    if health_point == 6:
        print(stages[0])
    elif health_point == 5:
        print(stages[1])
    elif health_point == 4:
        print(stages[2])
    elif health_point == 3:
        print(stages[3])
    elif health_point == 2:
        print(stages[4])
    elif health_point == 1:
        print(stages[5])
    else:
        print(stages[6])
        print(r'''
        __   __            _               _
        \ \ / /__  _   _  | |    ___  ___ | |_
         \ V / _ \| | | | | |   / _ \/ __|| __|
          | | (_) | |_| | | |__| (_) \__ \| |_
          |_|\___/ \__,_| |_____\___/|___/ \__|
        ''')
        print(f"The word is {computer_fruit}.")
        break
    print("\n" * 1)


