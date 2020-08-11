import random as r

list_of_options = ['python', 'java', 'kotlin', 'javascript']


correct_word: str = r.choice(list_of_options)


blank_spaces = (len(correct_word) - 3) * '-'
# hint = f"{correct_word[:3]}{blank_spaces}"
hint = correct_word.replace(correct_word[3:], blank_spaces)

# TODO:Get the hint to show the user. The hint should the first 3 letters
# of the correct word. The remaining letters should be hypens

# Currently, the I'm thinking of getting the length of the correct word, the first letters, 
# ans then subtracting 3 from the length of the word to get the number of hyphens to show

print("H A N G M A N")

user_guess = input(f'Guess the word {hint}:')
if user_guess == correct_word:
    print(correct_word)
    print('You survived!')
else:
    print(correct_word)
    print('You are hanged!')




    




# whitespace_string = '         hey    '
# normal_string = 'incomprehensibilties'

# modded_string = normal_string.strip('i')
# print(f'"{modded_string}"')


# sentence = "London is the capital of Great Britain."
# sentence = sentence.lower()
# sentence.upper()
# sentence = sentence.replace("a", "x", 2)
# print(sentence.capitalize())


# print(sentence.replace('x', ''))