from art import logo
from replit import clear
import random
play = True
while play:
  target = random.randint(1,100)
  guess = 0
  clear()
  print(logo)
  print ("Welcome to the number guessing game,\ni'm thinking of a number between 1 and 100")
  attempts = 10 if input("Choose a level, type 'easy' or 'hard': ") == "easy" else 5
  while not target == guess and attempts:
    print(f"You have {attempts} remaining attempts to guess the number.")
    attempts -=1
    guess = int(input("Make a guess: "))
    if guess == target:
      print(f"Congratulation You did it, the number was {target}")
    elif guess > 100:
      print(f"You are out off range, the number is between 1 and 100, you chose {guess}")
    elif guess > target:
      print("too high.")
    elif guess < target:
      print("too low")
    if not target == guess and attempts == 0:
      print ("Sorry you loose\n")
  play = False if input("Do you want to play again? Yex/no") == "no" else True