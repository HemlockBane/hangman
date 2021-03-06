# Print "Type "play" to play the game, "exit" to quit:" when game starts
# - Start game if user types "play"
# - Do nothing if user types "exit"
# - Print message again if user types anything else
# Print "Type "play" to play the game, "exit" to quit:" when game end

import random as r


def play_game():

    list_of_options = ['python', 'java', 'kotlin', 'javascript']

    previous_guesses = []

    selected_word = r.choice(list_of_options)

    masked_text = len(selected_word) * '-'

    # print(selected_word)
    print("H A N G M A N")
    print("")
    remaining_lives = 8
    while remaining_lives > 0:
        print(masked_text)
        guessed_letter = input("Input a letter:")

        islower = guessed_letter.islower()
        isenglishalpha = guessed_letter.isalpha() and guessed_letter.isascii()

        if len(guessed_letter) != 1:
            print("Please input a single letter")
            if remaining_lives != 0:
                print("")
            continue

        elif not(islower and isenglishalpha):
            print("Please enter a lowercase English letter")
            if remaining_lives != 0:
                print("")
            continue

        elif guessed_letter in previous_guesses:
            print("You've already guessed this letter")

            if remaining_lives != 0:
                print("")
            continue

        elif guessed_letter not in selected_word:
            print("That letter doesn't appear in the word")
            remaining_lives -= 1

            if remaining_lives != 0:
                previous_guesses.append(guessed_letter)
                print("")
            continue

        else:
            char_list = list(masked_text)
            for index, value in enumerate(masked_text):
                if guessed_letter == selected_word[index]:
                    char_list[index] = guessed_letter
            masked_text = "".join(char_list)
            if '-' not in masked_text:
                break

            if remaining_lives != 0:
                previous_guesses.append(guessed_letter)
                print("")

    if '-' not in masked_text:
        print(f"You guessed the word {masked_text}!")
        print("You survived!")

    if '-' in masked_text:
        print("You lost!")


user_input = ""

while True:
    user_input = input('Type "play" to play the game, "exit" to quit:')
    if user_input == "play":
        play_game()
        print("")
    elif user_input == "exit":
        break
    else:
        pass
