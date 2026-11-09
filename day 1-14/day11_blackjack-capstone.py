import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
#++++++++++++++++++++++---FUNCTIONS---+++++++++++++++++++++++++++++++++++++++++++++++++++
def withdraw_card(someone_card):
    """Withdraw a random card from the card deck to someone's hand"""
    someone_card.append(random.choice(deck_of_card))

def win_or_lost(player_1, status_1, status_2, p1_value, p2_value):
    if status_1 == "blackjack":
        if status_2 == "blackjack":
            return f"😢😢😢{player_1} LOSE this round😢😢😢"
        elif status_2 == "bust" or 17 <= p2_value:
            return f"{player_1} WINS this round.🏆🏆🏆"

    elif p1_value <= 21:
        if status_2 == "blackjack":
            return f"😢😢😢{player_1} LOSE this round.😢😢😢"
        elif status_2 == "bust":
            return f"{player_1} WINS this round.🏆🏆🏆"
        elif 17 <= p2_value <= 21:
            if p1_value > p2_value:
                return f"{player_1} WINS this round.🏆🏆🏆"
            elif p1_value < p2_value:
                return f"😢😢😢{player_1} LOSE this round😢😢😢"
            elif p1_value == p2_value:
                return "🤝This round ends with a PUSH."
    return None

def check_bust_with_ace(hand_of_card):
    while sum(hand_of_card) > 21 and 11 in hand_of_card:
        if 11 in hand_of_card:
            hand_of_card.remove(11)
            hand_of_card.append(1)
    return sum(hand_of_card[0:])

#++++++++++++++++++++++---GAMEPLAY---+++++++++++++++++++++++++++++++++++++++++++++++++++
game_on = True
play_or_not = input("+++Press Enter to start a new game of Blackjack+++\n")

while game_on:
# ++++++++++++++++++++++---RAM---+++++++++++++++++++++++++++++++++++++++++++++++++++
    deck_of_card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    player_card = random.choices(deck_of_card, k=2)
    player_card_number = len(player_card)
    player_value = sum(player_card[0:])
    player_status = ""

    computer_card = random.choices(deck_of_card, k=1)
    computer_card_number = len(computer_card)
    computer_value = sum(computer_card[0:])
    computer_status = ""

    print(logo)
    print(f'Your hand for this game: {player_card}, and its value is {player_value}.')
    print(f'Dealer\'s first card is {computer_card}.')

    # ++++++++++++++++++++++---WHEN A PLAYER GETS A BLACK JACK STRAIGHT UP---+++++++++++++++++++++++++++++++++++++++++++++++++++
    if player_value == 21 and player_card_number == 2:
        print("♠️ ♥️ ♦️ ♣️You got a BLACKJACK ♠️ ♥️ ♦️ ♣️!")
        player_status += "blackjack"

        while computer_value < 17:

            withdraw_card(computer_card)

            computer_value = sum(computer_card[0:])
            computer_card_number = len(computer_card)

            if computer_value == 21 and computer_card_number == 2:
                print("♠️ ♥️ ♦️ ♣️Dealer got a BLACKJACK!♠️ ♥️ ♦️ ♣️")
                computer_status += "blackjack"
                break

            elif computer_value > 21:

                computer_value = check_bust_with_ace(computer_card)

                if computer_value > 21:
                    print("Dealer went BUST!")
                    computer_status += "bust"
                    break

                elif computer_value < 17:
                    print(f"The Ace counted as 1 instead. Your card value now is {computer_value}. ")
                    continue

        print(f'Dealer\'s cards are now: {computer_card}, and the new value is {sum(computer_card)}.')
        game_result = win_or_lost("You", player_status, computer_status, player_value, computer_value)
        print(game_result)
# ++++++++++++++++++++++---WHEN PLAYER DONT GET A BLACK JACK---+++++++++++++++++++++++++++++++++++++++++++++++++++
    else:

        while not player_value > 21:

            hit_or_stand = input("Type 'y' to HIT or 'n' to STAND: \n")

            if hit_or_stand == "y":

                withdraw_card(player_card)

                player_value = sum(player_card[0:])
                player_card_number = len(player_card)
                print(f"This is your hand now: {player_card}, and the value is now {player_value}.")

                if player_value > 21:

                    player_value = check_bust_with_ace(player_card)

                    if player_value > 21:
                        print("😢😢😢BUST! You lost to the dealer. Game over.😢😢😢\n")
                        player_status += "bust"
                        break
                    else:
                        print(f"The Ace counted as 1 instead. Your card value now is {player_value}. ")
                        continue


            elif hit_or_stand == "n":

                while computer_value < 17:

                    withdraw_card(computer_card)

                    computer_value = sum(computer_card[0:])
                    computer_card_number = len(computer_card)

                    if computer_value == 21 and computer_card_number == 2:
                        print("♠️ ♥️ ♦️ ♣️Dealer got a BLACKJACK!♠️ ♥️ ♦️ ♣️")
                        computer_status += "blackjack"

                    elif computer_value > 21:

                        computer_value = check_bust_with_ace(computer_card)

                        if computer_value > 21:
                            print("Dealer went BUST!")
                            computer_status += "bust"
                            break

                        elif computer_value < 17:
                            print(f"The Ace counted as 1 instead. Dealer card value now is {computer_value}. ")
                            continue

                print(f'Dealer\'s cards are now: {computer_card}, and its new value is {sum(computer_card)}.')
                game_result = win_or_lost("You", player_status, computer_status, player_value, computer_value)
                print(game_result)
                break


    another_game = input("Would you like to play another round of Blackjack?"
                             "Type 'y' to play, 'n' to escape. \n").lower()
    if another_game == "y":
        print("\n" * 20)
        continue
    else:
        game_on = False
