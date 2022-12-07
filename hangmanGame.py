# Hangman for Final
# CIT-95 Fall 2022
# Ashley Hayburn

import random
import requests
import colorama
from colorama import init, Fore
init()


def wordGetter():
    word = requests.get("https://raw.githubusercontent.com/adambom/dictionary/master/dictionary.json").json()
    word, definition = random.choice(list(word.items()))
    return word.upper()


def playingGame(word):
    completion = "_" * len(word)
    guessed = False
    lettersGuessed = []
    wordsGuessed = []
    attempt = 8
    print(Fore.BLUE + "Want to playing a round of Hangman with me?")
    print(Fore.RED + hangmanBodyParts(attempt))
    print(completion)
    print("\n")
    while not guessed and attempt > 0:
        guess = input(Fore.BLUE + "What is your guess? Type a letter or even a word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in lettersGuessed:
                print(Fore.YELLOW + "You have already tried ", guess, ". Try again!")
            elif guess not in word:
                print(Fore.YELLOW + guess, "isn't in it, sorry.")
                attempt -= 1
                lettersGuessed.append(guess)
            else:
                print(Fore.WHITE + "Nice!", guess, "IS in this word!")
                lettersGuessed.append(guess)
                listOfWords = list(completion)
                ind = [i for i, letter in enumerate(word) if letter == guess]
                for indexes in ind:
                    listOfWords[indexes] = guess
                completion = "".join(listOfWords)
                if "_" not in completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in wordsGuessed:
                print(Fore.BLUE +"You already guessed that one. Try again!", guess)
            elif guess != word:
                print(Fore.YELLOW + guess, "isn't in this word, sorry.")
                attempt -= 1
                wordsGuessed.append(guess)
            else:
                guessed = True
                completion = word
        else:
            print(Fore.YELLOW + "Try again with a valid guess.")
        print(Fore.RED + hangmanBodyParts(attempt))
        print(completion)
        print("\n")
    if guessed:
        print(Fore.WHITE + "Heck yeah! You guessed the right word! You win!")
    else:
        print(Fore.YELLOW + "Sorry, you ran out of guesses. The word was " + word + ". Try again!")


def hangmanBodyParts(tries):
    body_parts = [

                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |   _ / \\_
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |   _ / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
# beginning
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return body_parts[tries]


def body():
    word = wordGetter()
    playingGame(word)
    while input(Fore.GREEN + "Do you want to try another round? (Y/N) ").upper() == "Y":
        word = wordGetter()
        playingGame(word)


if __name__ == "__main__":
    body()
