import os
import random
from words import WORDS
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def you_lose():
    print('gameover')


def restart():
    start_game()


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
    if inp == "C":
        os.system('cls' if os.name == 'nt' else 'clear')
        start_game()

    else:
        print("Unidentified entry")
        print(f"{Fore.WHITE}Type {Fore.YELLOW}C {Fore.WHITE}to contimue")


def main_game():
    '''
    Get a dictionary from the list in words.py,
    and print out one spanish word, from it.
    Ask user to translate the spainish word.
    Check if the answer is correct
    '''
    lives = 3
    score = 0

    while lives >= 0 or score <= 3:
        word = random.choice(WORDS)
        english_word = word['english']
        spanish_word = word['spanish']
        print(spanish_word)
        answer = input().lower()
        if answer == english_word:
            print("Correct")
            score += 1
            print(f'You have {lives} lives left')
            print(f'Your score is {score}')
        else:
            print(f'Incorrect, the answer is {english_word}')
            lives -= 1
            print(f'you have {lives} lives left')
            print(f'Your score is {score}')
    else:
        if lives < 0:
            you_lose()


def start_game():
    '''
    Function to ask user if they are ready to start the game
    '''
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
print(Fore.YELLOW + "**********SPANISH WORD GAME**********")
print("")

start_game()
