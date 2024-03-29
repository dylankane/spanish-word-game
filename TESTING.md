# Testing

Return back to the [README.md](README.md) file.

Here is all the testing I have put the application through and the results of these tests.

## Code Validation

### Python

I have used the recommended [CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| run.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/dylankane/spanish-word-game/main/run.py) | ![screenshot](documentation/validation-run.py.png) | All clear, no errors found |
| words.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/dylankane/spanish-word-game/main/words.py) | ![screenshot](documentation/validation-words.py.png) | All clear, no errors found |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Spanish Word Game | Large monitor | ![screenshot](documentation/lighthouse-monitor.png) | Slightly lower than optimal on the SEO category |
| Spanish Word Game | Laptop | ![screenshot](documentation/lighthouse-laptop.png) | Same issue with SEO |
| Spanish Word Game | Tablet | ![screenshot](documentation/lighthouse-tablet.png) | Same issue with SEO |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Section | User Action | Expected Result | Pass/Fail |
| --- | --- | --- | --- |
| Start Game | | | |
| | Type "Y" | Redirection to game rules | Pass |
| | Type "N" | Redirection to difficulty choice | Pass |
| | Type neither Y/N or type non letter key | Invalid entry message, ask user to answer again | Pass |
| Rules | | | |
| | Type "Y" | Redirection to difficulty choice | Pass |
| | Type "N" | Redirection back to start game | Pass |
| | Type neither Y/N or type non letter key | Invalid entry message, ask user to answer again | Pass |
| Difficulty level | | | |
| | Type "E" | Redirection to main game with easy level choosen | Pass |
| | Type "H" | Redirection to main game with hard level choosen | Pass |
| | Type neither E/H or type non letter key | Invalid entry message, ask user to answer again | Pass |
| Main Game | | | |
| | Type translation | Correct | Pass |
| | Type translation | Incorrect  | Pass |
| Win game | | | |
| | Type "Y" | Redirection to main game | Pass |
| | Type "N" | Redirection back to start game | Pass |
| | Type neither Y/N or type non letter key | Invalid entry message, ask user to answer again | Pass |
| Loose game | | | |
| | Type "Y" | Redirection to main game | Pass |
| | Type "N" | Redirection back to start game | Pass |
| | Type neither Y/N or type non letter key | Invalid entry message, ask user to answer again | Pass |

## Browser Compatibility

I have tested the deployed application on 3 browsers to check for compatibility. Below are the results.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documentation/chrome-screenshot.png) | All working as expected |
| Firefox | ![screenshot](documentation/firefox-screenshot.png) | All working as expected |
| Edge | ![screenshot](documentation/edge-screenshot.png) | All working as expected |

## Bugs

While developing this project I came up against a few issues and bugs, below is a list of some issues I had.


- While loop in the `main_game()`. This piece of code threw up a few different issues/ bugs while I was developing it. When first written I had created an infinite loop by not having a condition to break or stop it. I also had a problem getting the conditions to end it at the right points. Also retrieving the Spanish word to be displayed and a corresponding English word to compare to the user input, without the word being repeated in a game caused issues. It went through a few different stages of evolution until finally getting it all to work correctly. Finished product is below.

    ```python
        game = Game()
        word_list = copy.deepcopy(list)
        random.shuffle(word_list)

        while game.lives > 0 and game.score < 20:
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
    ```

    - To fix this, I put the condition of the while loop in the while statement at the beginning, and realized that I didn't need `>=` and only needed `>` to get the breakpoints of the while loop to stop at the right places. To output the Spanish word, a copy of the list of dictionaries was created inside the game function but outside the while loop, the while loop then contained a method to `pop()` out one entry from the list giving it one Spanish word to print and its corresponding English word to compare to the users' input.

- Y/N. Where the user is prompted to type one of two letters as an answer to a question, I needed it to recognize upper and lowercase letters, to make the navigation as simple as possible. It didn't work with lowercase letters and the beginning. As I had checked the user input against a capital letter.

    ```python
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
    ```

    - To fix this, I added a `.upper()` method to the user input field, transforming all the input to upper case. I then used this method for all user input in the application, including in the main game, but here I used the `.lower()` method as all the words in the list are in lowercase.


- Function parameters. Building up the flow through the application, calling different functions depending on users' input and game results, I came across a few bugs/errors 

    - To fix this I had to work on the appropriate arguments/parameters being called in a function, to then use that data within the next function.


- Line too long. This was a reoccurring issue/bug with the print statements in particular. With a max of 80 characters, I found the output text exceeded this maximum often.

    ![screenshot](documentation/line-too-long.png)

    - To fix this, I had to split the text into different print statements and add new lines.

## Unfixed Bugs / Issues

- One issue outstanding is in the main gameplay, where the user has to type the English translation of the word displayed. It currently just checks to see if the answer is right or wrong. I have not yet implemented an error check when the player types a non-letter key. To have a message telling them "that is not a valid entry and possibly a typo", giving them a chance to retry that word, without being marked as incorrect.

    - Possible solution is to use the `isalpha()` method to check if the answer is only alphabetic entries.

There are no remaining bugs that I am aware of.
