import random
# to create a function, do 
# def function():
# funcions can be nested

#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

chosen_word = random.choice(word_list)
letters_list = []
for spot in range(len(chosen_word)):
  letters_list.append('_')

print(chosen_word)
print(letters_list)
print(chosen_word)
guess = input("Guess a letter ").lower()
# if chosen_word.count(guess) > 0:
#   print("correct")
# else:
#   print("incorrect")
for position in range(len(chosen_word)):
  letter = chosen_word[position]
  
  if letter == guess:
    letters_list[position] = letter
    print("right")
  else:
    print ("wrong")
print(letters_list)
# over = False
# wrong_count = 0

# while over == False:
#   guess = input("Guess a letter ").lower()
#   for letter in chosen_word:
#     if letter == guess:
#       print("letter")

#     else:
#       print("_")
#       wrong_count += 1
#       if wrong_count > 5:
#         over = True