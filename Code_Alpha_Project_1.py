import random

def hangman():
    # Predefined list of words
    words = ["python", "hangman", "computer", "program", "game"]
    
    # Select a random word from the list
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6
    
    print("Welcome to Hangman!")
    print("Guess the word one letter at a time. You have 6 incorrect attempts allowed.")
    
    while attempts > 0:
        # Display the current state of the word
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print("\n" + display_word)
        
        # Check if the player has won
        if "_" not in display_word:
            print(f"Congratulations! You guessed the word: {secret_word}")
            break
        
        # Get player's guess
        guess = input("Guess a letter: ").lower()
        
        # Validate the input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        # Check if the letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue
        
        # Add the guess to the list of guessed letters
        guessed_letters.append(guess)
        
        # Check if the guess is correct
        if guess not in secret_word:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
        
    else:
        # This runs if the while loop completes (no more attempts)
        print(f"\nGame over! The word was: {secret_word}")

# Start the game
hangman()