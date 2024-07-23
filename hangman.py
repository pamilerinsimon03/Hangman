import random
import hangman_art
import hangman_word

stages = hangman_art.stages
rand_word = random.choice(hangman_word.wordList)

display = []
lives = 6

print(hangman_art.logo)

for i in range(len(rand_word)):
    display.append("_")
print(display)
while lives > 0:
    guess = input("Guess a letter: ").lower()
    if guess in rand_word:
        for i in range(len(rand_word)):
            if guess == rand_word[i]:
                display[i] = guess
        print("Letter in rand word")
    else:
        lives -= 1
        print(f"{guess} not in word")
        print(f"{lives} lives remaining")
    if lives == 6:
        print(stages[6])
    elif lives == 5:
        print(stages[5])
    elif lives == 4:
        print(stages[4])
    elif lives == 3:
        print(stages[3])
    elif lives == 2:
        print(stages[2])
    elif lives == 1:
        print(stages[1])
    elif lives == 0:
        print(stages[0])
        print("You Lose")
    print(display)
    if "_" not in display:
        print("You Win!")
        break
