# import random

# word_list=['hello','pacewisdom','python','name']

# random_word=random.choice(word_list)

# try_count=0

# print("Welcome to Hangman!")
# print("-------------------")
# print("Guess the Word. You have 6 chance to Guess!")

# def get_letter(prompt):
#     return input(prompt)
# res_str=""

# while try_count<=6:
#    letter= get_letter("Guess the letter: ")
   
#    if letter not in random_word:
#         print("Incorrect")
#         try_count +=1
#         print(f"You have only {6-try_count} chances left")
#    else:
#        for char in random_word:
#            if char==letter:
#                res_str += char
#            else:
#                res_str += "_"
#    print(res_str)

import random

word_list = ['hello', 'pacewisdom', 'python', 'name']
random_word = random.choice(word_list)

try_count = 0
max_attempts = 6
guessed_letters = set()

print("Welcome to Hangman!")
print("-------------------")
print("Guess the Word. You have 6 chances to Guess!")

def get_letter(prompt):
    return input(prompt)

while try_count < max_attempts:
    guessed_word = ''.join([char if char in guessed_letters else '_' for char in random_word])
    print(f"Word: {guessed_word}")
    
    if '_' not in guessed_word:
        print(f"Congratulations! You guessed the word '{random_word}'")
        break
    
    letter = get_letter("Guess the letter: ")
    guessed_letters.add(letter)
    
    if letter not in random_word:
        try_count += 1
        print(f"Incorrect! You have {max_attempts - try_count} chances left")
    else:
        print("Correct!")
        if '_' not in guessed_word:
            print(f"Congratulations! You guessed the word '{random_word}'")
            break

if '_' in guessed_word:
    print(f"Out of chances! The word was '{random_word}'")

  
       

    
