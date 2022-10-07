import screen_info as si
from time import sleep
from math import ceil
import colorama
import sys
import os

def separate_chars(string):
    list = [i for i in string]
    return list

def list2str(list):
    string = " ".join(list)
    return string

def diffconverter(difficulty):
    return -.5*difficulty + 2.5

def delete_last_line():
    "Use this function to delete the last line in the STDOUT"

    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')

width = si.terminal_width()
height = si.terminal_height()

def start_sequence(seconds):
    print(colorama.Fore.RED + "\n"*(ceil(height / 2) - 4) + "Please use fullscreen for best experience.".center(width) + "\n\n\n")
    for i in range(seconds):
        delete_last_line()
        print("|".center(width))
        sleep(.25)
        delete_last_line()
        print("/".center(width))
        sleep(.25)
        delete_last_line()
        print("-".center(width))
        sleep(.25)
        delete_last_line()
        print("\\".center(width))
        sleep(.25)
    os.system('cls')