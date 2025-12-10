

def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        return hangman_closure
    return make_hangman

secret_value = input("What is your secret word:").lower().split()
hang_man = make_hangman(secret_value)

while True:
    letter_value = input("What is your letter guess:").lower()
    hang_man(letter_value)
    break

