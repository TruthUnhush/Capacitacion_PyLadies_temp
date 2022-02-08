import hangman_art as art
import random

words = ["python", "ruby", "javaScript", "java", "rust"]
n_stages = len(art.stages)
lives = 7
word = random.choice(words)
word_hidden = list("-" * len(word))
game_on = True

print(art.logo)

while game_on:
    letter = input("Guess a letter: ").lower()

    if letter not in word:
        lives -= 1
        print(f"You guessed {letter}, that's not in the word. You lose a life!")
        if lives == 1:
            print("The game is over!")
            print(f"The word was {word}")
            game_on = False
    elif letter in word_hidden:
        print(f"You alredy guessed {letter}!")

    for i in range(len(word)):

        if word[i] == letter:
            word_hidden[i] = letter

    if "-" not in word_hidden:
        print("You win!")
        game_on = False
    
    print(" ".join(word_hidden))
    print(art.stages[n_stages - lives])

    