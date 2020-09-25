# Hangman Game


# Keep on looping if user still has lives (total lives count is 8)
# During the loop:
# - If user meets win condition #1, react accordingly
# - if user meets a life loss condition, react accordingly
# At the end of the loop, check for fail condition #1 & win condition #2



# Life loss conditions:
# 1. If a letter doesn't occur in the word:
# - Print "That letter does'nt appear in the word"
# - Reduce the number of remaining attempts

# 2. If a letter occurs in the word but has been guessed by the user,
# - print "No improvements"
# - Reduce the number of remaining attempts


# Fail conditions
# 1. remaining attempts is 0 and user has not guessed all the words
# - print "You lost!"


# Win conditions
# 1. If remaining attempts is greater than or equal to 1 (i.e. during the loop)
# after printing masked text, if all the letters have been guessed
# - print "You guessed the word!"
# - print "You survived!"
# break out of loop

# 2. If remaining attempts is 0 and all the letters have been guessed
# - print "You guessed the word!"
# - print "You survived!"


import random as r

list_of_options = ['python', 'java', 'kotlin', 'javascript']

selected_word = r.choice(list_of_options)

masked_text = len(selected_word) * '-'


# print(selected_word)

print("H A N G M A N")
print("")
remaining_lives = 8
while remaining_lives > 0:
    print(masked_text)
    if '-' not in masked_text:
        break

    user_guess = input("Input a letter:")
    if user_guess not in selected_word:
        print("That letter doesn't appear in the word")
        remaining_lives -= 1
        
        if remaining_lives != 0:
            print("")
        continue
    else:
        if user_guess in masked_text:
            print("No improvements")
            remaining_lives -= 1

            if remaining_lives != 0:
                print("")
            continue
        else:
            char_list = list(masked_text)
            for index, value in enumerate(masked_text):
                if user_guess == selected_word[index]:
                    char_list[index] = user_guess
            masked_text = "".join(char_list)
            print("")

if '-' not in masked_text:
    print("You guessed the word!")
    print("You survived!")

if '-' in masked_text:
    print("You lost!")
