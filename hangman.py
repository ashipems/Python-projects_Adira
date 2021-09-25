import random


def get_word():
    words = ["apple", "banana", "mango"]
    choice = random.choice(words)
    return choice


def play(word):
    print("Let's play Hangman!")
    tries = 6
    print(display_man(tries))
    guess_word = "_" * len(word)
    print(guess_word)

    guessed = False
    guessed_letters = []
    guessed_words = []

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                guess_word_list = list(guess_word)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    guess_word_list[index] = guess
                guess_word = "".join(guess_word_list)
                if "_" not in guess_word:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                guess_word = word
        else:
            print("Not a valid guess.")

        print(display_man(tries))
        print(guess_word)

    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_man(tries):
    state = [
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
    return state[tries]


term = get_word()
play(term)
while input("Play Again? (Y/N) ").upper() == "Y":
    term = get_word()
    play(term)
