letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# Easy version: password with a sequence: letter ->symbol --> number
import random
pass_letter = random.choices(letters,weights=None, cum_weights=None, k= nr_letters)
pass_symbol = random.choices(symbols,weights=None, cum_weights=None, k= nr_symbols)
pass_number = random.choices(numbers,weights=None, cum_weights=None, k= nr_numbers)
final_password = pass_letter + pass_symbol + pass_number
print(final_password)
delimiter_space = ""
print("Your sequence password is" + " "+  delimiter_space.join(final_password))
#Hard version: password with no sequence: all characters are random
random.shuffle(final_password)
print("Your complex password is" + " " + delimiter_space.join(final_password))


