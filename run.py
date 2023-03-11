import os
import copy
import random
from words import WORDS
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def question(x, y):
    '''
    Function to ask the user a [y/n] question, which takes functions as
    parameters. These functions are assigned to the y and n answers.
    '''
    func_1 = x
    func_2 = y
    while True:
        user = input(f"{Fore.YELLOW}[Y/N]{Fore.RESET}\n").upper()
        if user == "Y":
            os.system('cls' if os.name == 'nt' else 'clear')
            func_1()
        elif user == "N":
            os.system('cls' if os.name == 'nt' else 'clear')
            func_2()
        else:
            print(f"Invalid entry, please type 'Y' for yes or 'N' for no")


def you_lose(x, y):
    '''
    Function to handle when the user runs out of lives. Displays scores, and
    directs them back to the game.
    '''
    lives = x
    score = y
    print(f'{Fore.RED}GAMEOVER')
    print(f"Good try but you ran out of lives")
    print(f'{Fore.GREEN}You scored {score}')
    print(f"Would you like to start a new game now?")
    question(main_game, start_game)


def you_win(x, y):
    '''
    Function to handle when the user completes the game.
    Displays, score and lives. Directs them back to the game.
    '''
    lives = x
    score = y
    print(f"{Fore.GREEN}CONGRATULATIONS\n")
    print(f'{Fore.GREEN}You scored {score}')
    print(f"With {lives} lives left")
    print(f"Well done!!!\n")
    print(f"Would you like to start a new game now?")
    question(main_game, start_game)


def finished(x, y):
    '''
    Function to handle the score vs lives counters, when game ends, to decide
    where to send them,to the you_win or you_lose functions
    '''
    lives = x
    score = y
    if x <= 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        you_lose(lives, score)
    elif y >= 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        you_win(lives, score)


def rules():
    '''
    Holds set of game rules, can be accessed from different areasof the game,
    for user to read. Asks user for input to direct them to the game
    '''
    print("")
    print(f"{Fore.YELLOW}**********SPANISH WORD GAME**********\n")
    print(f"{Back.YELLOW}-----------The Rules-----------")
    print("-Start your game, and you will be given a Spanish word")
    print("-Just type the english translation for this word")
    print("-You have 3 lives to complete the game")
    print("-Each correct translation is 1 point")
    print("-Score 20 points to win")
    print("-If your answer is incorrect the correct answer will be shown")
    print(f"-Have fun and learn !!!\n\n")
    print(f"Would you like to start the game now?")
    question(main_game, start_game)


def main_game():
    '''
    Gets a random set of translations from a list of dictionaries in words.py.
    Prints out one spanish word using its dictionary key. Prompts the user to
    translate it and compare their answer to the matching english word.
    Keeps score count and lives counter, to determine the end of game
    '''
    lives = 3
    score = 0
    word_list = copy.deepcopy(WORDS)
    print("")
    print(f"{Fore.YELLOW}**********SPANISH WORD GAME**********\n")
    print(f"{Fore.MAGENTA} OK Here We Go!!!\n\n")
    print(f"Type the translation to the following words\n")
    print(Fore.YELLOW + "-----------------")

    while lives > 0 and score < 3:
        random.shuffle(word_list)
        word = word_list.pop(0)
        english_word = word['english']
        spanish_word = word['spanish']
        print(f"{Style.BRIGHT}{spanish_word}")
        answer = input().lower()
        if answer == english_word:
            print("")
            print(f"{Fore.GREEN}Correct")
            score += 1
            print(f'lives: {lives}')
            print(f'score: {score}')
            print(Fore.YELLOW + "-----------------")
        else:
            print("")
            print(f'{Fore.RED}Incorrect')
            print(f"The answer is {Fore.YELLOW}{english_word}")
            lives -= 1
            print(f'lives: {lives}')
            print(f'score: {score}')
            print(Fore.YELLOW + "-----------------")

    finished(lives, score)


def start_game():
    '''
    Function to ask user if they are ready to start the game,
    or want to see the set of game rules.
    '''
    print("")
    print(f"{Fore.YELLOW}***********WELCOME TO THE************\n")
    print(f"{Fore.YELLOW}**********SPANISH WORD GAME**********\n")
    print(f"Have fun and learn!!!\n")
    print(f"Would you like to see the rules before you start the game?")
    question(rules, main_game)


start_game()
