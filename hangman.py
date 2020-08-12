import random as r

# ....
# User has 8 tries to the guess the letters in the word
# The user loses a try after every guess
# Once the user makes a correct guess, uncover all the matching letters in the word
# Once the user makes a wrong guess, display an error message
# Once the user has used up all his tries, show a message

list_of_options = ['python', 'java', 'kotlin', 'javascript']

# Choose a random word from a list of options
selected_word = r.choice(list_of_options)
# blank_spaces = (len(correct_word) - 3) * '_'
# hint = f"{correct_word[:3]}{blank_spaces}"

masked_text = len(selected_word) * '-'

print("H A N G M A N")
print("")
for i in range(8, 0, -1):
    print(masked_text)
    user_guess = input("Input a letter:")
    if user_guess not in selected_word:
        print("No such letter in the word")
    else:
        # Remember strings are immutable, so we need to convert the masked word to 
        # a list of characters so that we can easily (there are other ways sha) replace characters at specific indices
        # We can't use replace either because all the characters are dashes ('-'). Doing this
        # will just affect all the dashes
        char_list = list(masked_text)
        for index, value in enumerate(masked_text):
            if user_guess == selected_word[index]:
                char_list[index] = user_guess
        masked_text = "".join(char_list)
    print("")

print("Thanks for playing!", end='\n')
print("We'll see how well you did in the next stage")




# user_guess = input(f'Guess the word {hint}:')
# if user_guess == selected_option:
#     # print(selected_option)
#     print('You survived!')
# else:
#     # print(selected_option)
#     print('You are hanged!')
