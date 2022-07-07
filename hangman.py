import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word.upper())
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    print('Choose a difficulty: ')
    difficulty = input('Easy (E), Medium (M), or Hard (H): ')
    while difficulty != 'E' and difficulty != 'M' and difficulty != 'H':
        print('Invalid input. Choose a difficulty')
        difficulty = input('Easy (E), Medium (M), or Hard (H): ')

    if (difficulty == 'E'):
        from hangman_visual import easy_lives_visual
        visual = easy_lives_visual
        lives = 10
    elif (difficulty == 'M'):
        from hangman_visual import medium_lives_visual
        visual = medium_lives_visual
        lives = 9
    else:
        from hangman_visual import hard_lives_visual_dict
        visual = hard_lives_visual_dict
        lives = 6

    # get user input
    while len(word_letters) > 0 and lives > 0:
        # print used letters 
        print()
        print(visual[lives])
        print(f'You have {lives} lives left.')
        print('You have used these letters: ', ' '.join(used_letters))

        # print guessed letters + underscores
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        # instantly guess
        guess_now = input('Would you like to guess the word now (Y/N)?: ').upper()
        while guess_now != 'N' and guess_now != 'Y':
            guess_now = input("Invalid input. Please input 'Y' or 'N': ").upper()
        if (guess_now == 'Y'):
            user_word = input('Guess a word: ').upper()
            if (user_word != word):
                lives = 0
            break

        # guess letter
        else:
            user_letter = input('Guess a letter: ').upper()
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                else:
                    lives = lives - 1
                    print('Letter is not in this word.')
                    print()
            elif user_letter in used_letters:
                print('You have already used this character. Please try again.')
                print()
            elif user_letter not in alphabet:
                print('Invalid input. Please try again.')
                print()

    print()
    if lives == 0:
        print(visual[0])
        print('Sorry, you lost. The word was', word)
    else:
        print(f'You guessed the word {word}! Congratulations!')

    play_again = input('Would you like to play again (Y/N)? ').upper()
    while play_again != 'N' and play_again != 'Y':
        play_again = input("Invalid input. Please input 'Y' or 'N': ").upper()
    if play_again == 'Y':
        print()
        hangman()
    else:
        print()
        print('Thank you for playing HANGMAN')

hangman()
