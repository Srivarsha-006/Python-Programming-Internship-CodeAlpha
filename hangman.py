import random
# STEP 1: List of words to choose from
word_list = ['python', 'keyboard', 'hangman', 'eclipse', 'puzzle']

# Pick a random word from the list
secret_word = random.choice(word_list)

# STEP 2: Set up the game variables
guessed_letters = []   # letters the player has tried
wrong_guesses   = 0    # how many wrong guesses so far
max_wrong       = 6    # player loses after 6 wrong guesses

print("Welcome to Hangman!")
print(f"The word has {len(secret_word)} letters.")
print("You have 6 chances to guess wrong before you lose.\n")

# STEP 3: Keep playing until win or lose
while True:

    # --- Show the word with blanks ---
    # For each letter in the secret word:
    #   show the letter if guessed, else show '_'
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("Word: ", display)
    print("Wrong guesses left:", max_wrong - wrong_guesses)
    print("Letters tried:", guessed_letters)
    print()

    # --- Check if the player WON ---
    # Win = every letter in the word has been guessed
    all_guessed = True
    for letter in secret_word:
        if letter not in guessed_letters:
            all_guessed = False

    if all_guessed:
        print("You WIN! The word was:", secret_word)
        break

    # --- Check if the player LOST ---
    if wrong_guesses == max_wrong:
        print("You LOSE! The word was:", secret_word)
        break

    # --- Ask the player for a guess ---
    guess = input("Guess a letter: ").lower()

    # Make sure it's a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue

    # Make sure they haven't tried it already
    if guess in guessed_letters:
        print("You already tried that letter!\n")
        continue

    # Add the letter to the tried list
    guessed_letters.append(guess)

    # --- Check if the guess is correct ---
    if guess in secret_word:
        print("Correct!\n")
    else:
        wrong_guesses += 1
        print(f"Wrong! ({wrong_guesses}/{max_wrong})\n")
