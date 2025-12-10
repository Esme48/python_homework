

def make_hangman(secret_word):
    secret_value = input("What is your word:")
    guesses = []

    def hangman_closure(letter):
        guess_value = input("What is the letter that you are guessing:")
        guesses.append(letter)
        return hangman_closure
    return 