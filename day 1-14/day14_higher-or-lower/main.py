import random
from game_data import data
import art


def compare_followers(follower_of_a, follower_of_b):
    if follower_of_a > follower_of_b:
        return "a"
    else:
        return "b"


the_score = 0
game_on = True
object_a = {}
object_b = {}

while game_on:

    print(art.logo)

    if the_score < 1:
        object_a = random.choice(data)

    elif the_score > 0:
        object_a = object_b
        print(f"Correct! Your score: {the_score}.")

    name_a = object_a.get("name")
    follower_a = object_a.get("follower_count")
    description_a = object_a.get("description")
    country_a = object_a.get("country")
    print(f"Compare A: {name_a}, a(n) {description_a}, from {country_a}.")

    print(art.vs)

    object_b = random.choice(data)
    while object_b == object_a:
        object_b = random.choice(data)

    name_b = object_b.get("name")
    follower_b = object_b.get("follower_count")
    description_b = object_b.get("description")
    country_b = object_b.get("country")
    print(f"Against B: {name_b}, a(n) {description_b}, from {country_b}.")

    the_answer = input("Who has more Instagram followers. Type 'A' or 'B': ").lower().strip()

    the_winner = compare_followers(follower_a, follower_b)

    if the_answer == the_winner:
        the_score += 1
        print("\n" * 50)
        continue

    else:
        print("\n" * 50)
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {the_score}")
        game_on = False





#TODO-1: import modules art.py and game_data.py ✅
#TODO-2: access information of dictionaries nested in a list ✅
#TODO-3: ask the user to input the answer ✅
#TODO-4: figure out how to make computer understand that who has more follower is the winner ✅
#TODO-5: add conditions, what happen when the player guess wrong and guess right ✅
#TODO-6: figure out how to move object B to object A when the user guess correctly ✅
#TODO-7: restyle the game and check for bugs✅
