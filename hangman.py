import random
import sys
from words import WORDS


def get_word() -> str:
    return random.choice(WORDS)


def play(word):
    word_completion = "_" * len(word)
    guessed_letters = []
    tries = 6
    print(get_scaffold(tries))
    print(word_completion)
    while tries >= 0:
        letter = input('Wpisz literę do wisielca: ')
        if letter in word:
            guessed_letters.append(letter)
            found_letter_pos = word.find(letter)
            word_completion = word_completion[:found_letter_pos] + letter + word_completion[found_letter_pos+1:]
            print('Brawo udało ci się odgadnąć literę!')
            print(word_completion)
            print(get_scaffold(tries))
        else:
            print(f'Nie udało się odgadnąć litery\n pozostało {tries} prób')
            tries -= 1
            print(get_scaffold(tries))
        if not '_' in word_completion:
            print('Gratulacje zgadłeś hasło!!!')
            while True:
                print('Zagraj jeszcze raz (wpisz 1), wyjdź z programu (wpisz 2)')
                choice = input()
                if choice == '1':
                    word = get_word()
                    play(word)
                elif choice == '2':
                    sys.exit(0)
                else:
                    print('Wpisane zły znak, wpisz 1 lub 2')
                    continue
    print('Nie udało się zgadnąć hasła, spróbuj ponownie')




def get_scaffold(tries):
    hangman = [
        """
        --------
        |      |
        |      O
        |     \\//
        |      |
        |     /\\
        - 
        """,
        """
        --------
        |      |
        |      O
        |     \\//
        |      |
        |     /
        - 
        """,
        """
        --------
        |      |
        |      O
        |     \\//
        |      |
        |
        - 
        """,
        """
        --------
        |      |
        |      O
        |     \\/
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