

def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        if letter in secret_word:
            print("You guessed a letter!")
        else:
            print("Please try again!")
        guesses.append(letter)
        return hangman_closure
    return hangman_closure


secret_value = list(input("What is your secret word:").lower())
hang_man = make_hangman(secret_value)

while True:
    letter_value = input("What is your letter guess:").lower()
    hang_man(letter_value)
    

