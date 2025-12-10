

def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        if letter not in guesses:
            guesses.append(letter)
        output_value = " ".join([value if value in guesses else "_" for value in secret_word])
        return f"Word So Far: {output_value}"
    return hangman_closure


secret_value = list(input("What is your secret word:").lower())
hang_man = make_hangman(secret_value)

while True:
    letter_value = input("What is your letter guess:").lower()
    print(hang_man(letter_value))

    

