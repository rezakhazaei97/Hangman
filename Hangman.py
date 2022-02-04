import random
import os
import HangmanArt
import HangmanWord

# choose a word randomly from wordList
choosenWord = random.choice(HangmanWord.wordList)

# creat blanks
display = []

for i in range(1, len(choosenWord)+1):
    display.append('-')

lifs = 0
while lifs <= 6:
    # user guesses
    print(HangmanArt.stages[lifs])
    if lifs == 6:
      print("you losed... :(")
      print(f"word was: {choosenWord}")
      break
    elif not '-' in display:
      print("you won... :)")
      break
    guess = input("Guess a letter... ").lower()
    os.system('cls')
    # check user guesses
    i = 0
    if choosenWord.find(guess) >= 0 and choosenWord.find(guess) < len(choosenWord):
        for ch in choosenWord:
            if ch == guess:
                display.pop(i)
                display.insert(i, ch)
            i += 1
        print(''.join(display))
    else:
        lifs += 1
        print(''.join(display))
        print(f"{guess} is not in the word, you lose a life!! :(")

