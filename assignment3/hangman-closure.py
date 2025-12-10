

def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        return hangman_closure
    return make_hangman

hang_man = make_hangman(print(input("What is your secret word:").lower().split()))

