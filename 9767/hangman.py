import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "strawberry"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")
            if attempts == 0:
                print("You're out of attempts! The word was:", word)
                break
        else:
            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You guessed the word:", word)
                break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    hangman()
