print(r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
print("Welcome to The Secret Auction Program\n")
bidder_dict = {}
winner_bidder = None
winner_bid_amount = 0
while True:
    users_name = input("Enter your name to start bidding:\n")
    money_amount = float(input("Enter your bid amount: €"))
    bidder_dict.update({users_name : money_amount})

    new_bidder = input("Is there another bidder? "
                       "Type 'yes' or 'no'\n")
    new_bidder = new_bidder.lower()

    if new_bidder == "yes":
        print("\n" * 30)
    elif new_bidder == "no":
        for bidder, money in bidder_dict.items():
            if money > winner_bid_amount:
                winner_bid_amount = money
                winner_bidder = bidder
        print(f"The winner of this auction is: {winner_bidder} at €{winner_bid_amount}")
        break
    else:
        continue

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


