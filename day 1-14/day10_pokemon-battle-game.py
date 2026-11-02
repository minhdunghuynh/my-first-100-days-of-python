import random
escape_image = ('''

                  ▄█████▄
                 █▓▓▓▓▓▓████
                 █░░█░░░█
                  ▀█░░▀█▀
          ▄██▄   ▄██▓▓██▄
  ░░▒▒▓▓ █▓▓▓████▓█▓▓█░░██
          ▀██▀ ▀██▓▓▓█ ▀▀
  ░░▒▒▓▓       ▄██████▄
           ▄███▀    ▀█░██
          ███▀        ▀███

''')

catch_image = '''

                    ▄█████▄
                  ▄██▓▓▓▓▓██▄
       ░░▒▒▓▓    ██▓▓▓▓▓▓▓▓▓██
                 █▓▓▓▓▓▓▓▓▓▓▓█
  ░░▒▒▓▓████    ██████▀▀▀██████
                █░░░░█░█░█░░░░█
       ░░▒▒▓▓    ██░░░▀▀▀░░░██
                  ██░░░░░░░██
                   ▀██░░░██▀
                     ▀███▀

'''

cyndaquil_turn_image = '''
               
                    ▒     ▒
                 ▒▒▓▒  ▒▓▒
               ▒▓▓░▓▒▒▓░▓▓▒
              ▒▓░░░░▓▓░░░▓▒
             ▒▓▓████████▓▓▒
         ▄██████▓▓▓▓▓▓▓██▄
     ▄███░░▀▀░░░░▓▓▓▓▓▓▓▓██
   ▄█░░░░░░░░░░░░░▓▓▓▓▓▓▓█
   ▀██████░░░░░░░░░░░░░░██
          ▀██▄▄██▀▀██▄▄██▀'''

pikachu_turn_image = '''
 
     ██▄       ▄██
     █▓░█▄   ▄█░▓█
      █░░░███░░░█       ▄█████
      █░░░░░░░░░█      █░░░░█
     █░░█░░░░█░░░█   ▄██░░██
     █▒▒░░▄░░░▒▒░█   █░░██
      █░░▀▀▀░░░░█  ▄██░█
     █░█░░░░░░█░███░░██
     ▀█░░░░░░░░█▀▀██▀
      ▀██▀    ▀██▀'''

print('''
                ██    ██
                  █░█  █░█                ▓ ▓
                   █░██░█               ▓▒▓▒▓▒▓
                  █░░░░░░█              ▓▒███▒▓
                  █░█░░█░█            ██░░░░░██
                  █▒░▀▀░▒█         ███░▀░░░░░█
                 █ █░░░░█         █░░░░░░░░░█
                █░██░░░░█          ███░░░░░█
                 ██░█░░█░█            █░█░█
                    ██ ██              ██ ██
==============================================================
                       POKEMON BATTLE
==============================================================
''')

#++++++++++++++++++++++++++++++++++  RAM  +++++++++++++++++++++++++++++++++
pikachu_hp = 100
cyndaquil_hp = 100
pokeball_inventory = 2
battle = True
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#++++++++++++++++++++++++++++++++++  FUNCTIONS  +++++++++++++++++++++++++++++++++
def damage_generator():
    return random.randint(0, 70)

def hp_calculator(hp, damage):
    hp_result = hp - damage
    if hp_result >= 0:
        hp_result = hp_result
    if hp_result < 0:
        hp_result = 0
    return hp_result

def attack(attacking_pokemon, defending_pokemon, skills, damage):
    if 1 <= damage <= 50:
        print(f"{attacking_pokemon} uses {skills} and deals {damage} damage on {defending_pokemon}")
    elif 50 < damage <= 70:
        print(f"{attacking_pokemon} uses {skills} and deals {damage} CRITICAL damage on {defending_pokemon} \n"
              f"{defending_pokemon} is vulnerable.")
    elif damage == 0:
        print(f"{attacking_pokemon} misses")
def catch_pokemon(caught_pokemon, number_of_pokeball):
    print(f"You attempt to catch {caught_pokemon} using Poke Ball. You have {number_of_pokeball} left")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
player_name = input("Type in your Pokemon trainer's name: \n")
print(f"Okay {player_name}! You and Pikachu encounter a wild Cyndaquil. Choose what you want to do: \n")

while battle == True:

    play_decision = input("\nChoose to proceed [--ATTACK--][--CATCH--][--ESCAPE--]\n").lower().strip()

    if play_decision == "escape":
        print(escape_image)
        escape_yn = input("Are you sure you want to escape this battle? Y/N?").lower().strip()

        if escape_yn == "y" or escape_yn == "yes":
            print("You successfully ran away from the Cyndaquil.")
            break
        elif escape_yn == "n" or escape_yn == "no":
            print("You continue the battle.")
            continue
        else:
            continue

    elif play_decision == "attack":
        print(pikachu_turn_image)

        pikachu_damage = damage_generator()
        pikachu_skill = random.choice(["Tail whip", "Thunder Shock", "Spark"])
        cyndaquil_hp = hp_calculator(cyndaquil_hp,pikachu_damage)

        attack("Pikachu", "Cyndaquil",pikachu_skill, pikachu_damage)
        if 0 < cyndaquil_hp < 100:
            print(f"Pikachu HP is: {pikachu_hp}. Cyndaquil HP is: {cyndaquil_hp}")
        elif cyndaquil_hp <= 0:
            print("Pikachu has defeated Cyndaquil. Battle over.")
            break

    elif play_decision == "catch":
        if pokeball_inventory ==  0:
            print("You have ran out of Poke Ball.")
            continue
        elif pokeball_inventory > 0:
            pokeball_inventory -= 1

            print(catch_image)

            catch_pokemon("Cyndaquil", pokeball_inventory)

            if cyndaquil_hp > 65:
                print("Darn! Cyndaquil broke free!")
            elif 20 < cyndaquil_hp <= 65:
                catching_odd = random.choices((0, 1),[2,1], k=1)
                if catching_odd == [0]:
                    print("Arrgh! Almost got it.")
                elif catching_odd == [1]:
                    print("Aww. It appeared to be caught. Congratulations! Battle over.")
                    break
            elif 0 < cyndaquil_hp <= 20:
                print("You have successfully captured Cyndaquil. Congratulations! Battle over.")
                break
    else:
        print("Hmm..?")
        continue

    game_continue = input("\nPress Enter to end your turn.")

    print(cyndaquil_turn_image)
    cyndaquil_damage = damage_generator()
    cyndaquil_skill = random.choice(["Quick Attack","Flame Wheel","Tackle"])
    attack("Cyndaquil","Pikachu",cyndaquil_skill, cyndaquil_damage)
    pikachu_hp = hp_calculator(pikachu_hp,cyndaquil_damage)
    if 0 < pikachu_hp < 100:
        print(f"Pikachu HP is: {pikachu_hp}. Cyndaquil HP is: {cyndaquil_hp}")
    elif pikachu_hp <= 0:
        print("Your Pikachu is defeated against the wild Cyndaquil. Battle over.")
        break



















