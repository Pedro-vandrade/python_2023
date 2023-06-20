import random

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

endgame = False
lives = 6

from hangman_logo import logo
print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not endgame:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed: {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lost a life.")
        lives -= 1
        if lives == 0:
            endgame = True
            print("You lose")

    if "_" not in display:
        endgame = True
        print("You win.")

    from hangman_module import stages
    print(stages[lives])