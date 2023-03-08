import random
from words import WORDS


def get_word():
    word = random.choice(WORDS)
    print(word)


def start_game():
    '''
    Function to ask user if they are ready to start the game
    '''
    print("Type Y for yes to the start game")
    inp = input().lower()
    if inp == "y":
        get_word()
    else:
        print("You must type 'y' or 'n' ")


print("")
print("****SPANISH WORD GAME****")
print("")
print("-----------The Rules-----------")
print("-Start your game, and you will be given a word-")
print("-Just type the english translation for this word-")
print("-You have 3 lives to make 20 correct answers to win the game-")
print("")
print("")

start_game()

# word = random.choice(WORDS)
# print(word)
# python3 run.py
