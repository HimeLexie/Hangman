import colorama
from source_code.extend import separate_chars
from source_code.extend import list2str
from source_code.extend import diffconverter
from source_code.words import random_word
from math import ceil

print(colorama.Fore.GREEN + """\nWelcome to:\n
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                        Creator: Alex J.\n""")

while True:
    input1 = random_word()
    difficulty = diffconverter(int(input("Difficulty 1 - 3: ")))
    listed_input = separate_chars(input1)
    fill_list = separate_chars("_" * len(listed_input))
    guess_amount = ceil(len(input1) * diffconverter(difficulty))
    while_count = 0

    print("\nYou have " + str(guess_amount) + " guesses.\nOnly guess lowercase letters.\n")

    for i in range(guess_amount):
        guess = input("Guess: ")
        guess_num = 0
        while_count = while_count + 1

        for i in range(listed_input.count(guess)):
            # print("in: " + str(listed_input)) <-- for testing purposes
            
            fill_list[listed_input.index(guess)] = guess
            listed_input[listed_input.index(guess)] = "_"
            guess_num = guess_num + 1

        print("\n" + list2str(fill_list))

        if guess_amount - while_count == 1:
            a = " guess"
        else:
            a = " guesses"
        if guess_num == 0:
            print("No " + guess + "'s found. ;w;  " + str(guess_amount - while_count) + a + " left.\n")

        if guess_num == 1:
            print("1 " + guess + " found! " + str(guess_amount - while_count) + a + " left.\n")

        if guess_num > 1:
            print(str(guess_num) + " " + guess + "'s found! " + str(guess_amount - while_count) + a + " left.\n")

        if fill_list == separate_chars(input1):
            print("Congrats, you win!")
            break

        if guess_amount - while_count == 0:
            print("You lose. I am crying.\nWord was: " + input1 + "\n")
            break
    
    play = input("Would you like to play again (y/n)? ")

    if play == "n":
        print()
        break
    elif play == "y":
        print("\nAlright, let's play again!\n")
    elif play != "y" and play != "n":
        print("Not y or n, continuing anyways.")