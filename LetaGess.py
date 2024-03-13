#!/usr/bin/python3

import random

# Function to choose a random word from words.txt
def choose_word():
    with open("words.txt", "r") as file:
        words = file.readlines()
    return random.choice(words).strip().lower()

# Function to check the guessed word and provide feedback
def check_guess(word, guess):
    correct_letters = []
    misplaced_letters = []
    incorrect_letters = []
    
    for i in range(len(word)):
        if guess[i] == word[i]:
            correct_letters.append(guess[i])
        elif guess[i] in word:
            misplaced_letters.append(guess[i])
        else:
            incorrect_letters.append(guess[i])
    
    return correct_letters, misplaced_letters, incorrect_letters

# Main game function
def letter_guess_game():
    print("Welcome to LetterGuess!")
    print("Try to guess the 5-letter word.")

    # Choose a random word
    word_to_guess = choose_word()
    # Initialize variables
    attempts = 0
    max_attempts = 5
    guessed_word = "_____"  # Placeholder for guessed letters

    while attempts < max_attempts:
        print("\nWord to guess:", guessed_word)
        guess = input("Enter your guess: ").lower()

        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue

        attempts += 1
        correct, misplaced, incorrect = check_guess(word_to_guess, guess)

        if correct:
            for letter in correct:
                position = word_to_guess.index(letter)
                guessed_word = guessed_word[:position] + letter + guessed_word[position+1:]

        print("Correct letters:", correct)
        print("Misplaced letters:", misplaced)
        print("Incorrect letters:", incorrect)

        if guessed_word == word_to_guess:
            print("\nCongratulations! You guessed the word:", word_to_guess)
            break
    else:
        print("\nSorry, you're out of attempts. The word was:", word_to_guess)

# Start the game
letter_guess_game()

