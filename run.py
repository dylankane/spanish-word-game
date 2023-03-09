import random
from words import WORDS


def you_lose():
    print('gameover')


def restart():
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
            print(lives)
    else:
        if lives < 0:
            you_lose()


def start_game():
    '''
    Function to ask user if they are ready to start the game
    '''
    print("Type Y for yes to the start game")
    inp = input().lower()
    if inp == "y":
        main_game()
    else:
        print("You must type 'y' or 'n' ")
        restart()


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
