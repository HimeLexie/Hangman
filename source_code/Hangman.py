from functions import separate_chars, list2str, diffconverter, delete_last_line, start_sequence
from screen_info import terminal_width, terminal_height, center_input, center_print
from words import random_word
from math import ceil
from time import sleep
import colorama
import os


colorama.init()
os.system('cls')

width = terminal_width()
height = terminal_height()

start_sequence(10)

width = terminal_width()
height = terminal_height()

print(colorama.Fore.GREEN + "\n"*(ceil(height / 2) - 11) + "Welcome to:".center(width) + "\n\n" + "██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗".center(width) + "\n" + "██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║".center(width) + "\n" + "███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║".center(width) + "\n" + "██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║".center(width) + "\n" + "██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║".center(width)  + "\n" + "╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝".center(width)  + "\n" + "Creator: Alex J.".center(width))

start_bool = True
ready = input("\n" + " "*(ceil(width / 2) - 14) + "Are you ready to play (y/n)? ")

if ready == "n":
    os.system("exit")
else:
    if ready != "n" and ready != "y":
        print("Not y or n, continuing anyways.".center(width))
        sleep(3)
        delete_last_line()
    while True:
        word = random_word()
        delete_last_line()
        while start_bool == True:
            difficulty = input(" "*(ceil(width / 2) - 10) + "Difficulty 1 - 3: ")
            
            try:
                diffconverter(int(difficulty))
            except:
                print("Input conversion error, try a number?".center(width))
                sleep(2)
                delete_last_line()
                delete_last_line()
            else:
                difficulty = diffconverter(int(difficulty))

                if difficulty <= 2 and difficulty >= 1:
                    delete_last_line()
                    print("Difficulty set.".center(width) + "\n" + "Word set.".center(width) + "\n" + "Have fun!".center(width))
                    sleep(3)
                    os.system('cls')
                    print("""
    ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
    ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
    ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
    ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
    ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝\n\n""")
                    line_count = 9
                    start_bool = False
                else:
                    print("Difficulty not in range.".center(width))
                    sleep(3)
                    delete_last_line()
                    delete_last_line()
        listed_input = separate_chars(word)
        fill_list = separate_chars("_" * len(listed_input))
        guess_amount = ceil(len(word) * diffconverter(difficulty))
        while_count = 0

        print("   You have " + str(guess_amount) + " guesses.")
        line_count = line_count + 1

        for i in range(guess_amount):
            guess_bool = True
            
            sleep(1)
            while guess_bool == True:
                guess_input = input("\n   Guess: ")
                guess = guess_input.lower()
                alphabet = "a/b/c/d/e/f/g/h/i/j/k/l/m/n/o/p/q/r/s/t/u/v/w/x/y/z".split('/')
                line_count = line_count + 2

                try:
                    alphabet.index(guess)
                except:
                    if len(guess) > 1:
                        print("   Guess has too many characters.")
                        line_count = line_count + 1
                    else:
                        print("   Guess is not a letter, try again.")
                        line_count = line_count + 1
                else:
                    guess_bool = False

            guess_num = 0
            while_count = while_count + 1

            for i in range(listed_input.count(guess)):
                # print("in: " + str(listed_input)) <-- for testing purposes
                
                fill_list[listed_input.index(guess)] = guess
                listed_input[listed_input.index(guess)] = "_"
                guess_num = guess_num + 1

            print("\n   " + list2str(fill_list) + "\n")
            line_count = line_count + 3

            if guess_amount - while_count == 1:
                a = " guess"
            else:
                a = " guesses"

            if guess_num == 0:
                print("   No " + guess + "'s found. ;w;  " + str(guess_amount - while_count) + a + " left.")
                line_count = line_count + 1
            if guess_num == 1:
                print("   1 " + guess + " found! " + str(guess_amount - while_count) + a + " left.")
                line_count = line_count + 1
            if guess_num > 1:
                print("   " + str(guess_num) + " " + guess + "'s found! " + str(guess_amount - while_count) + a + " left.")
                line_count = line_count + 1
            if fill_list == separate_chars(word):
                print("   Congrats, you win!")
                line_count = line_count + 1
                break
            if guess_amount - while_count == 0:
                print("   You lose. I am crying.\n   Word was: " + word + "\n")
                line_count = line_count + 3
                break
            if (line_count - height) == 0 or 9 > (height - line_count) > 0:
                sleep(2)
                os.system('cls')
                print("""
    ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
    ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
    ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
    ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
    ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝\n\n""")
                print("   " + list2str(fill_list))
                line_count = 10
        play = input("Would you like to play again (y/n)? ")
        line_count = line_count + 1

        if play == "n":
            print("   Thanks for playing!" + colorama.Fore.RESET)
            line_count = line_count + 1
            break
        elif play == "y":
            print("\n   Alright, let's play again!\n")
            line_count = line_count + 3
        elif play != "y" and play != "n":
            print("   Not y or n, continuing anyways.")
            line_count = line_count + 1
        os.system('cls')
        print("""
    ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
    ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
    ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
    ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
    ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝\n\n""")