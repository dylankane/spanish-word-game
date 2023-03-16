import os
import time
import copy
import random
from words import WORDS, WORDS_HARD
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

WIN_TOTAL = 20


class Game():
    '''
    Class to handle game progress (score and lives counters).
    Allowing counters to be updated and printed, at different points.
    '''
    def __init__(self):
        self.score = 0
        self.lives = 3


def clear():
    '''
    Function to clear terminal screen
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def question(x, y):
    '''
    Function to ask the user a [y/n] question, which takes functions as
    parameters. These functions are assigned to the y and n answers.
    '''
    func_1 = x
    func_2 = y
    while True:
        user = input(f" {Fore.YELLOW}[Y/N]{Fore.RESET}\n ").upper()
        if user == "Y":
            os.system('cls' if os.name == 'nt' else 'clear')
            func_1()
        elif user == "N":
            clear()
            func_2()
        else:
            print(f" Invalid entry, please type 'Y' for yes or 'N' for no")


def you_lose(game):
    '''
    Function to handle when the user runs out of lives. Displays scores, and
    directs them back to the game.
    '''
    print(f" {Fore.YELLOW}**********SPANISH WORD GAME**********\n")
    print(f" {Fore.RED}{Style.BRIGHT}GAMEOVER\n")
    print(f" {Fore.RED}{Style.BRIGHT}Good try, but you ran out of lives")
    print(f" {Fore.RED}{Style.BRIGHT}You scored: {game.score}\n")


def you_win(game):
    '''
    Function to handle when the user completes the game.
    Displays, score and lives. Directs them back to the game.
    '''
    print(f" {Fore.YELLOW}**********SPANISH WORD GAME**********\n")
    print(f" {Fore.GREEN}{Style.BRIGHT}CONGRATULATIONS\n")
    print(f" {Fore.GREEN}{Style.BRIGHT}You scored: {game.score}")
    print(f" {Fore.GREEN}{Style.BRIGHT}With {game.lives} lives left")
    print(f" {Fore.GREEN}{Style.BRIGHT}Well done!!!\n")


def finished(game):
    '''
    Function that takes the game class as an argument to decide when game ends,
    where to send them, to the you_win() or you_lose() functions.
    '''
    if game.lives <= 0:
        clear()
        you_lose(game)
    elif game.score >= WIN_TOTAL:
        clear()
        you_win(game)
    time.sleep(1.5)
    print(f" Would you like to start a new game now?")
    game.score = 0
    game.lives = 3
    question(difficulty, start_game)


def rules():
    '''
    Holds print statements for game rules,for user to read.
    Asks user for input to direct them to the game
    '''
    print("")
    print(f" {Fore.YELLOW}**********SPANISH WORD GAME**********\n")
    time.sleep(1.5)
    print(f" {Back.YELLOW}{Fore.BLACK}-----------The Rules-----------\n")
    print(" - First choose your difficulty level, easy or hard")
    print(" - Easy will ask you to translate shorter well known spanish words")
    print(" - Hard will ask you to translate longer more difficult words")
    print(" - Start your game, and you will be given a Spanish word")
    print(" - Just type the english translation for this word")
    print(" - You have 3 lives to complete the game")
    print(" - Each correct translation is 1 point")
    print(" - Score 20 points to win")
    print(" - If your answer is incorrect the correct answer will be shown")
    print(f" - Have fun and learn !!!\n")
    print(f" {Back.YELLOW}{Fore.BLACK}-------------------------------\n\n")
    time.sleep(2)
    print(f" Would you like to start the game now?")
    question(difficulty, start_game)


def main_game(list, level):
    '''
    Creates duplicate list of the specific words list from words.py,
    picked at the difficulty function and shuffles it. Removes a dictionary
    from the list. Prints out the spanish word. Prompts the user to translate
    it and compare their answer to the matching english word. Updates game
    class,to determine the end of game.
    '''
    print("")
    print(f" {Fore.YELLOW}**********SPANISH WORD GAME**********\n")
    time.sleep(1.5)
    print(f" {Fore.RESET}You chose dificulty level: {Fore.YELLOW}{level}\n")
    print(f" Type the translation for the following words\n")
    print(f" OK Here We Go!!!\n")
    print(f" {Fore.YELLOW}-----------------")
    time.sleep(4)
    clear()

    game = Game()
    word_list = copy.deepcopy(list)
    random.shuffle(word_list)

    while game.lives > 0 and game.score < WIN_TOTAL:
        word = word_list.pop(0)
        english_word = word['english']
        spanish_word = word['spanish']
        print(f" {Fore.YELLOW}---------------------")
        print(f" {Fore.YELLOW}lives: {game.lives}    score: {game.score}")
        print(f" {Fore.YELLOW}---------------------\n")
        print(f" {Style.BRIGHT}{spanish_word}")
        answer = input(f"\n ").lower()
        if answer == english_word:
            game.score += 1
            print("")
            print(f" {Fore.GREEN}{Style.BRIGHT}Correct")
            print(f" {Fore.YELLOW}-----------------")
            time.sleep(2)
            clear()
        else:
            game.lives -= 1
            print("")
            print(f" {Fore.RED}{Style.BRIGHT}Incorrect")
            print(f" {Fore.YELLOW}The answer is {Fore.RESET}{english_word}")
            print(f" {Fore.YELLOW}-----------------")
            time.sleep(2.5)
            clear()

    finished(game)


def difficulty():
    '''
    Function that leads to main game function.
    Checks what difficulty level user wants to play game at.
    '''
    print(f" {Fore.YELLOW}**********SPANISH WORD GAME**********\n")
    time.sleep(1.5)
    print(f" What difficulty level would you like to play")
    print(f" Easy or Hard\n")
    time.sleep(1.5)
    print(f" Type {Fore.YELLOW}[E]{Fore.RESET} for Easy")
    print(f" Type {Fore.YELLOW}[H]{Fore.RESET} for Hard\n")

    while True:
        user_dif = input(f" {Fore.YELLOW}[E/H]{Fore.RESET}\n ").upper()
        if user_dif == "E":
            clear()
            main_game(WORDS, "Easy")
        elif user_dif == "H":
            clear()
            main_game(WORDS_HARD, "Hard")
        else:
            print(f" Invalid entry, please type 'E' for Easy or 'H' for Hard")


def start_game():
    '''
    Function to ask user if they are ready to start the game,
    or want to see the set of game rules.
    '''
    clear()
    print("")
    print(f" {Fore.YELLOW}***********WELCOME TO THE************\n")
    time.sleep(1.5)
    print(f" {Fore.YELLOW}**********SPANISH WORD GAME**********\n")
    time.sleep(1.5)
    print(f" {Fore.YELLOW}**Play a game and learn some Spanish**\n")
    time.sleep(1.5)
    print(f" Would you like to see the rules before you start the game?")
    question(rules, difficulty)


start_game()
