# SPANISH WORD GAME


![screenshot](documentation/mockup.png)


Welcome to the Spanish Word Game.

This is a game written in the Python programming language, it is a terminal-based language word game. Its main purpose is to aid in the learning of new Spanish words while playing a game. Adding competitiveness, and gaming aspects to learning. It helps to increase general vocabulary knowledge, not testing on the specifics of grammar.

A perfect tool for language schools to add to their curriculum. Giving their students some light relief from traditional learning techniques, and a simple way to introduce them to new vocabulary and test what has already been taught. With an easily edited word list, to update for students at different stages of their education.
Also, easily edited into other languages.


It is aimed at anyone of any age starting to learn Spanish as a new language. Ideal for kids, once they are of reading and writing ages, with the bonus of improving their typing skills, or even as their first introduction to hard typing. As it is a terminal-based game the display output and styling are minimalist and simple. This leaves it equally appealing to adults of all ages.

The gameplay is straightforward. The user is asked if they want to see the rules of the game before the game begins. Once the user decides to start the game, they are asked what difficulty level they want to play. With two levels easy or hard, easy being short simple well-known words and hard being longer less well-known words. With the difficulty level chosen, the game will begin. A Spanish word is shown, and the user is prompted to type the English translation. Users will be told if correct or incorrect, with the translation shown for the incorrect guesses. Once the user scores 20 points or gets 3 incorrect answers the game ends. Their score will be displayed. The next option will be to start a new game or return to the opening section.

The player is kept in a loop, with each section/page, there is a 2 option question, where the user can decide what to do next by typing a single letter. Creating a simply navigated game with a clear path through.


## UX

The idea for this game is a quick word learning game, it is simple to navigate and self explanitary. The navigation is circular, with a very clear path through the application. Being a terminal based game the scope for design features are limited. However to make this as user friendly as possible I implemented a few features, to the game.

The most obvious is colour. By imorting a module called "colorama" I was able to style specific pieces of text with colour. This helps the UX of the application, by emphasisng certain information, e.g. notifing the user for a correct answer with the word "correct" in green and when wrong, "incorrect" in red. Using colour to make information clearer. The yellow, is the main colour used throughout for the title texts and input prompt text, creating a reckonisable theme throughout the appication.

Another two features that greatly increases the user experience is the clear terminal screen function, along with the text ouput delay function. This means that after every move or navigation to a different section by the user the terminal screen will clear. This prevents the terminal becoming too overcrowded with previous arts of the game. than as the terminal is re-populated with the output text of the new section, it is printed with differnet delay times. 

Each section is finished with a question,e.g "do you want to start a new game", "do you want to see the gae rules". These are all 2 otion questions, with a click of a single letter key, the desion is made.
the text appeares at time intervals, giving the flowing feel of the game.


## Features

### Existing Features

- **Landing Area**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/feature01.png)

- **Game Rules**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/feature02.png)

- **Difficulty Level**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/feature03.png)

- **Main game**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/feature03.png)

- ****

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/feature03.png)

- **Score and Lives Counters**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/feature03.png)


- **Question Function**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/feature03.png)

- **Game Class**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/feature03.png)

- **Difficulty Level**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/feature03.png)


### Future Features

Below is a list of some future features that could be implemented to the application.

- Additional lists of words
    - Any additional notes about this feature.
- Catogaories of words
    - Any additional notes about this feature.
- Reverse eglish to spanish
    - Any additional notes about this feature.
- Cool new feature #3
    - Any additional notes about this feature.


## Tools & Technologies Used

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

In this section, you should explain the various tools and technologies used to develop the project.
Make sure to put a link (where applicable) to the source, and explain what each was used for.
Some examples have been provided, but this is just a sample only, your project might've used others.
Feel free to delete any unused items below as necessary.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑



- [Python](https://www.python.org) used as the main programming language in this project.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Markdown Builder by Tim Nelson](https://traveltimn.github.io/markdown-builder) used to help generate the Markdown files.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.


## Data Model

### Flowchart

To follow best practice, a flowchart was created for the app's logic,
and mapped out before coding began using a free version of
[Lucidchart](https://www.lucidchart.com/pages/ER-diagram-symbols-and-meaning) and/or [Draw.io](https://www.draw.io).

Below is the flowchart of the main process of this Python program. It shows the entire cycle of the program.

![screenshot](documentation/flowchart.png)

### Classes & Functions

The program uses one class to handle game progress, (the score and lives counters), allowing them to be updated at different stages troughout the code

```python
class Game():
    '''
    Class to handle game progress (score and lives counters).
    Allowing counters to be updated and printed, at different points.
    '''
    def __init__(self):
        self.score = 0
        self.lives = 3

```

The primary functions used on this application are:

- `question()`
    - Function to ask the user a y/n question, which takes functions as parameters. These functions are then called depending on the users answer, leading them to different places. This way the code doesn't have to be repeated every time the user is asked a question to get to the next step.

- `start_game()`
    - Function to ask user if they are ready to start the game, or want to see the set of game rules.
- `rules()`
    - Holds print statements for game rules,for user to read. Asks user for input to direct them to the game
- `difficulty()`
    - Function that leads to main game function. Checks what difficulty level user wants to play game at.
- `main_game()`
    - Creates duplicate list of the specific words list from words.py, picked at the difficulty function and shuffles it. Removes a dictionary from the list. Prints out the spanish word. Prompts the user to translate it and compare their answer to the matching english word. Updates game class, to determine the end of game.
- `finished()`
    - Function that takes the game class as an argument to decide when game ends, where to send them, to the you_win() or you_lose() functions
- `you_win()`
    -  Function to handle when the user completes the game. Displays, score and lives. Directs them back to the game.
- `you_lose()`
    - Function to handle when the user runs out of lives. Displays scores, and
    directs them back to the game.

- `clear()`
    - Function to clear terminal screen, to be called at multiple points.

- `question()`
    - Function to ask the user a y/n question, which takes functions as parameters. These functions are then called depending on the users answer, leading them to different places. This way the code doesn't have to be repeated every time the user is asked a question to get to the next step.

### Imports

I've used the following Python packages and/or external imported packages.

- `time`: used for adding time delays to text outputs
- `copy`: used for creating a shuffled list of words, to prevent words being repeated in game
- `random`: used to get a random randomly shuffle word list
- `os`: used for adding a `clear()` function, to clear the terminal screen
- `colorama`: used for including color in the terminal

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

Code Institute has provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of this backend application in a modern web browser.
This is to improve the accessibility of the project to others.

The live deployed application can be found deployed on [Heroku](https://spanish-word-game.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- If using any confidential credentials, such as CREDS.JSON, then these should be pasted in the Config Variables as well.
- Further down, to support dependencies, select **Add Buildpack**.
- The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs to be updated using:
- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:
- `echo web: node index.js > Procfile`

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select **Automatic Deployment** or **Manual Deployment** from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The frontend terminal should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.

If using any confidential credentials, such as `CREDS.json` or `env.py` data, these will need to be manually added to your own newly created project as well.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/dylankane/spanish-word-game) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/dylankane/spanish-word-game.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/dylankane/spanish-word-game)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/dylankane/spanish-word-game)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

The only notable difference between the local and live version of this application that I am aware of, is the colours. The live deployed version seems to have rendered the colours darker and duller than the local version I developed. It doesn't seem to have any effect on the UX. 

⚠️⚠️⚠️⚠️⚠️
## Credits

### Content

| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder by Tim Nelson](https://traveltimn.github.io/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [W3Schools](https://www.w3schools.com/howto/howto_js_topnav_responsive.asp) | entire site | responsive HTML/CSS/JS navbar |
| [W3Schools](https://www.w3schools.com/howto/howto_css_modals.asp) | contact page | interactive pop-up (modal) |
| [W3Schools](https://www.w3schools.com/css/css3_variables.asp) | entire site | how to use CSS :root variables |
| [Flexbox Froggy](https://flexboxfroggy.com/) | entire site | modern responsive layouts |
| [Grid Garden](https://cssgridgarden.com) | entire site | modern responsive layouts |
| [StackOverflow](https://stackoverflow.com/a/2450976) | quiz page | Fisher-Yates/Knuth shuffle in JS |
| [YouTube](https://www.youtube.com/watch?v=YL1F4dCUlLc) | leaderboard | using `localStorage()` in JS for high scores |
| [YouTube](https://www.youtube.com/watch?v=u51Zjlnui4Y) | PP3 terminal | tutorial for adding color to the Python terminal |
| [strftime](https://strftime.org) | CRUD functionality | helpful tool to format date/time from string |
| [WhiteNoise](http://whitenoise.evans.io) | entire site | hosting static files on Heroku temporarily |

⚠️⚠️⚠️⚠️⚠️
### Media

| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [Pexels](https://www.pexels.com) | entire site | image | favicon on all pages |
| [Lorem Picsum](https://picsum.photos) | home page | image | hero image background |


### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://traveltimn.github.io) for his support and advice throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) tutor team for their assistance with troubleshooting.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support.
- I would like to thank my partner (Isabel), all the support and for helping with the spanish translations.
