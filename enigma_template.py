# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: Adriana Ebert
# created: MM.DD.YYYY
# last update:  MM.DD.YYYY
import random

# we'll be using this string for the majority of our translations
alphabet = "abcdefghijklmnopqrstuvwxyz"
key = "..."

# user inputs a message and selects a key (or random), the message is then translated using the cipher
def encode_message():
    let = 0  # Is what letter it's checking
    result = ""  # The encoded message will be result
    message = input("What message?: ")
    print(message)
    key = int(input("Key?: "))
    for x in message:  # repeats code for each letter in the message
        letter = alphabet.index(message[let])  # grabs the number that letter is equal to (Ex: 4 = d so if grabs 4)
        result = result + alphabet[((letter + key) %26)]  # %26 makes it if it at z(25) it goes back to a(0)
        let = let + 1
    print(result)

# encodes a target file, similarly to encode_message, except now targeting a filename
def encode_file():
    let = 0  # Is what letter it's checking
    result = ""  # The encoded file will be result
    filnam = input("What file?: ")
    with open(filnam) as file:
        filmes = file.read().lower()

    key = int(input("Key?: "))
    for enletr in filmes:  # repeats code for each letter in the file
        if enletr.isalpha():  # For (!, spaces, symbols) / not get mixed around in alphabet (Ex: ! becoming r)
            letter = alphabet.index(enletr)  # grabs the number that letter is equal to (Ex: 4 = d so if grabs 4)
            result = result + alphabet[((letter + key) % 26)]  # %26 makes it if it at z(25) it goes back to a(0)
        else:
            result = result + enletr
    print(result)

    contin = int(input("[1] write to another file\n"
                   "[2] Overwrite this file\n"
                   "[3] No\n\n"
                   "Answer: "))

    if contin == 1:
        filnam = input("What file?: ")
        with open(filnam, 'w') as file: #  'w' is writing mode, allows for new file to be created if not already existing
            file.write(result)

    elif contin == 2:
        with open(filnam, 'w') as file: #  'w' is writing mode, allows for new file to be created if not already existing
            file.write(result)




# decodes target file using a user-specified key. If key is unknown, a keypress should
# call decode_unknown_key()
def decode_file():
    let = 0  # Is what letter it's checking
    result = ""  # The encoded file will be result
    filnam = input("What file?: ")
    with open(filnam) as file:
        filmes = file.read().lower()

    key = int(input("Key?: ") or -1)

    if(key == -1):
        decode_unknown_key(filmes)
    else:

        for enletr in filmes:  # repeats code for each letter in the file
            if enletr.isalpha():  # For (!, spaces, symbols) / not get mixed around in alphabet (Ex: ! becoming r)
                letter = alphabet.index(enletr)  # grabs the number that letter is equal to (Ex: 4 = d so if grabs 4)
                result = result + alphabet[((letter - key) % 26)]  # %26 makes it if it at z(25) it goes back to a(0)
            else:
                result = result + enletr
        print(result)

        contin = int(input("[1] write to another file\n"
                       "[2] Overwrite this file\n"
                       "[3] No\n\n"
                       "Answer: "))

        if contin == 1:
            filnam = input("What file?: ")
            with open(filnam, 'w') as file: #  'w' is writing mode, allows for new file to be created if not already existing
                file.write(result)

        elif contin == 2:
            with open(filnam, 'w') as file: #  'w' is writing mode, allows for new file to be created if not already existing
                file.write(result)

# runs if the key is unknown. If this is true, print out all possible decoding combinations.
def decode_unknown_key(filmes):
    result = ""
    for key in range(26):
        for enletr in filmes:  # repeats code for each letter in the file
            if enletr.isalpha():  # For (!, spaces, symbols) / not get mixed around in alphabet (Ex: ! becoming r)
                letter = alphabet.index(enletr)  # grabs the number that letter is equal to (Ex: 4 = d so if grabs 4)
                result = result + alphabet[((letter - key) % 26)]  # %26 makes it if it at z(25) it goes back to a(0)
            else:
                result = result + enletr
    print(f"The decode number is {key}.\n"
          f"{result}\n")


# main method declaration
def main():
    while True:
        print(f"Welcome to the Enigma Machine!\n"
              f"Please select an option:\n"
              f"[1]: Encode a custom message.\n"
              f"[2]: Encode file.\n"
              f"[3]: Decode file.\n"
              f"[4]: Exit.")

        selection = input("Choose an option: ")

        if selection == "1":
            encode_message()
        elif selection == "2":
            encode_file()
        elif selection == "3":
            decode_file()
        elif selection == "4":
            print("Goodbye.")
            exit()
        else:
            print("Invalid choice. Please try again.")

# runs on program start
if __name__ == "__main__":
    main()


