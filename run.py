import os
import random
from words import WORDS
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def you_lose():
    print(f'{Fore.RED} GAMEOVER \n')
    print(f"{Fore.WHITE}Type {Fore.YELLOW}C {Fore.WHITE}to contimue")
    contin = input().upper()
    while contin != "C":
        print("Please enter C to continue")
        contin = input().upper()

    os.system('cls' if os.name == 'nt' else 'clear')
    start_game()


def you_win():
    print(Fore.GREEN + 'CONGRATULATIONS')
    print(f'{Fore.GREEN}You scored {score}')
    print(f"{Fore.WHITE}Type {Fore.YELLOW}C {Fore.WHITE}to contimue")
    contin = input().upper()
    while contin != "C":
        print("Please enter C to continue")
        contin = input().upper()

    os.system('cls' if os.name == 'nt' else 'clear')
    start_game()


def finished(x, y):
    if x <= 0:
        you_lose()
    elif y >= 3:
        you_win()


def rules():
    print("")
    print(Fore.YELLOW + "**********SPANISH WORD GAME**********")
    print("")
    print(f"{Back.YELLOW}-----------The Rules-----------")
    print("-Start your game, and you will be given a word-")
    print("-Just type the english translation for this word-")
    print("-You have 3 lives to make 20 correct answers to win the game-")
    print("")
    print("")
    print(f"{Fore.WHITE}Type {Fore.YELLOW}C {Fore.WHITE}to contimue")
    contin = input().upper()
    while contin != "C":
        print("Please enter C to continue")
        contin = input().upper()

    os.system('cls' if os.name == 'nt' else 'clear')
    start_game()


def main_game():
    '''
    Get a dictionary from the list in words.py,
    and print out one spanish word, from it.
    Ask user to translate the spainish word.
    Check if the answer is correct
    '''
    lives = 3
    score = 0
    print("")
    print(Fore.YELLOW + "**********SPANISH WORD GAME**********")
    print("")
    print("Type the translation to the following words")
    print(Fore.YELLOW + "-----------------")

    while lives > 0 and score < 3:
        word = random.choice(WORDS)
        english_word = word['english']
        spanish_word = word['spanish']
        print(spanish_word)
        answer = input().lower()
        if answer == english_word:
            print(Fore.GREEN + "Correct")
            score += 1
            print(f'lives = {lives}')
            print(f'score = {score}')
            print(Fore.YELLOW + "-----------------")
        else:
            print(f'{Fore.RED}Incorrect,\n the answer is {Fore.YELLOW}{english_word}')
            lives -= 1
            print(f'lives = {lives}')
            print(f'score = {score}')
            print(Fore.YELLOW + "-----------------")

    finished(lives, score)
    # else:
    #     if lives < 0:
    #         you_lose()

    #     elif score > 3:
    #         win()


def start_game():
    '''
    Function to ask user if they are ready to start the game
    '''
    print("")
    print(Fore.YELLOW + "**********SPANISH WORD GAME**********")
    print("")
    print(f"{Fore.WHITE}Type {Fore.YELLOW}G {Fore.WHITE}to the start game")
    print(f"{Fore.WHITE}Type {Fore.YELLOW}R {Fore.WHITE}to see the game rules")
    inp = input().upper()

    if inp == "G":
        os.system('cls' if os.name == 'nt' else 'clear')
        main_game()

    elif inp == "R":
        os.system('cls' if os.name == 'nt' else 'clear')
        rules()

    else:
        print("You must type 'G' or 'R' ")
        inp = input().upper()


print("")
print(Fore.YELLOW + "***********WELCOME TO THE************")
print("")

start_game()
