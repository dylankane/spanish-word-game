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
    print(f"Would you like to start the game now?")
    user = input(f"{Fore.YELLOW} [Y/N]\n ").upper()
    while user != "Y" and "N":
        print(f"Invalid entry, please type 'y' or 'N'")
        user = input(Fore.YELLOW + "[Y/N] ").upper()

    os.system('cls' if os.name == 'nt' else 'clear')
    main_game()


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
            print(f'{Fore.RED}Incorrect')
            print(f"the answer is {Fore.YELLOW}{english_word}")
            lives -= 1
            print(f'lives = {lives}')
            print(f'score = {score}')
            print(Fore.YELLOW + "-----------------")

    finished(lives, score)


def start_game():
    '''
    Function to ask user if they are ready to start the game
    '''
    print("")
    print(Fore.YELLOW + "**********SPANISH WORD GAME**********")
    print("")
    print("Would you like to see the rules before you start the game?")
    inp = input(f"{Fore.YELLOW}[Y/N]\n").upper()
    while inp != "Y" and "N":
        print(f"Invalid entry, please type 'y' or 'N'")
        inp = input(f"{Fore.YELLOW}[Y/N]\n").upper()
    if inp == "Y":
        rules()
    elif inp == "N":
        main_game()


print("")
print(Fore.YELLOW + "***********WELCOME TO THE************")

start_game()
