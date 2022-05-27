import random
import sys

from pkg_resources import working_set
from words import WORDS


def get_word() -> str:
    return random.choice(WORDS).upper()


def play(word):
    word_completion = "_" * len(word)
    guessed_letters = []
    guessed_word = []
    guessed = False
    tries = 6
    print('Zagraj w wisielca.')
    print(get_scaffold(tries))
    print(word_completion)
    while not guessed and tries > 0:
        guess = input('Wpisz literę lub hasło do wisielca: ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f'Już zgadłeś tą literę, {guess}')
            elif guess not in word:
                print(f'{guess} nie ma w słowie')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f'Dobra robota, {guess} jest w słowie')
                guessed_letters.append(guess)
                found_letter_pos = word.find(guess)
                word_completion = word_completion[:found_letter_pos] + guess + word_completion[found_letter_pos+1:]
                if not '_' in word_completion:
                    print('Gratulacje zgadłeś hasło!!!')
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_word:
                print(f'Już odgadywałeś to słowo {guess}')
            if guess != word:
                print(f'{guess} nie jest poprawnym słowem')
                tries -= 1
                guessed_word.append(guess)
            else:
                guessed = True
                word_completion = guess

        else:
            print('nie poprawna odpowiedź.')
        print(get_scaffold(tries))
        print(word_completion)
        print('\n')
    if guessed:
        print('Gratulacje zgadłeś hasło!!!')
    else:
        print('Wykorzystałeś limit szans.')


def get_scaffold(tries):
    hangman = [
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
    return hangman[tries]


if __name__ == "__main__":
    word = get_word()
    play(word=word)
    while input("Chcesz zagrać jeszcze raz? Y/N: ").upper() == 'Y':
        word = get_word()
        play(word=word)
