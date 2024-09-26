import random

def scramble_word(word):
    """Return a scrambled version of the given word."""
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

def word_guessing_game():
    word_list = ["python", "javascript", "hangman", "programming", "developer"]
    chosen_word = random.choice(word_list)
    scrambled = scramble_word(chosen_word)
    attempts = 3
    
    print("Welcome to the Word Guessing Game!")
    print(f"Here is the scrambled word: {scrambled}")
    print(f"You have {attempts} attempts to guess the word.")

    while attempts > 0:
        guess = input("Guess the word: ").lower()