def encrypt(original_text, shift_amount):
    # --find the index of the original text
    original_index = []
    for letter in original_text:
        if letter in alphabet:
            original_index.append(alphabet.index(letter))
        elif letter not in alphabet:
            original_index.append(letter)
   #--find the new index in a form of a list
    new_index = []
    k = shift_amount // 26
    for coordinate in original_index:
        if type(coordinate) != int:
            new_index.append(coordinate)
        elif coordinate + shift_amount in range(0,26):
            new_index.append(coordinate + shift_amount)
        elif k == 0 and coordinate + shift_amount not in range(0,26):
            new_index.append(coordinate + shift_amount - 26)
        elif k > 0:
            new_index.append((coordinate + (shift_amount % 26) - 26))
    # --add encrypted letters to a list and then to a string
    new_text_list = []
    for x in new_index:
        if type(x) != int:
            new_text_list.append(x)
        else:
            new_text_list.append(alphabet[x])
    encrypted_text = "".join(new_text_list)
    print(f'Your encrypted message is: {encrypted_text}')

def decrypt(original_text, shift_amount):
    original_index = []
    new_index = []
    decrypted_text = ""
    #find coordinate of the original text in alphabet:
    for letter in original_text:
        if letter in alphabet:
            original_index.append(alphabet.index(letter))
        elif letter not in alphabet:
            original_index.append(letter)

    #find new index after the shift
    for coordinate in original_index:
        if type(coordinate) != int:
            new_index.append(coordinate)
        elif type(coordinate) == int:
            new_index.append(coordinate - (shift_amount % 26))
    #convert new index to new text
    for new_coordinate in new_index:
        if type(new_coordinate) != int:
            decrypted_text += new_coordinate
        elif type(new_coordinate) == int:
            decrypted_text += alphabet[new_coordinate]
    print(f'Your decrypted massage is: {decrypted_text}')

def caesar(user_direction):
    user_direction = user_direction.lower()
    if user_direction == "encode":
        encrypt(original_text=text, shift_amount=shift)
    elif user_direction == "decode":
        decrypt(original_text=text, shift_amount=shift)
    elif user_direction != "encode" and user_direction != "decode":
        print("Invalid cipher method")

#-----------------------------------------------------------------------------------------------------------
print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")
while True:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(user_direction=direction)
    end_program = input("Restart the Caesar Cipher?. Type 'yes' or 'no'\n")
    end_program = end_program.lower()
    if end_program == "no":
        print("Goodbye")
        break
    elif end_program == "yes":
        continue
    else:
        print("Goodbye")
        break
