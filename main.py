import random
# to create a function, do 
# def function():
# funcions can be nested

word_list = ["aardvark", "baboon", "camel"]

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