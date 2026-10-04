print('''
.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           '.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'   |
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
go = input("Where would you like to go next? Type in left or right.")
go1 = go.lower()
if go1 == "left":
    print("You survived")
#this separate the first condition
    swim = input("Now you have encountered a river. Would you like to swim or wait? Type in swim or wait.")
    swim1 = swim.lower()
    if swim1 == "wait":
        print("You survived again. Somebody came and pick you up with a boat")
        print("Now you reached a house with 3 doors: red, yellow and blue.")
        # this separate the second condition
        color = input("Type in the door color that you would enter")
        color1 = color.lower()
        if color1 == "red":
            print("You are killed by an assassin. Game over")
        elif color1 == "blue":
            print("You are shot by a thieve bow trap. Game over")
        elif color1 == "yellow":
            print("You found the treasure. You have won the game. Congratulations! ")
        else:
            print("Game over")
    elif swim1 == "swim":
        print("You cant swim and died. Game over")
    else:
        print("Game over")
else:
    print("Game over")

