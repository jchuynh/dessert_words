##LAB 4.2: Dessert Words 

#discarded code
##comment

##using VS Code and Git bash terminal within program.'
##to run code ctrl+alt+n
##to stop code run ctrl+alt+mb
##to choose language to run ctrl+alt+j --> then select language



import random

dessert_words = ["pie", "pudding", "cake", "cookies", "doughnut", "baklava", "cheesecake", "sundae", "candy"]

secret_word = random.choice(dessert_words)
#secret_word = "pudding"
print(secret_word)
secret_word_length = len(secret_word)
print(secret_word_length)

print("Guess the dessert!")
user_guess = input("Guess a letter! > ")


def guess_word(word):
  #while True:
  for letter in secret_word:
    if user_guess == secret_word[letter]:
      print("That's correct!")
      print(secret_word[letter])
    else:
      print("Try again")
  #elif user_guess = secret

guess_word(secret_word)

#testing testing
  