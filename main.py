#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

##################################################

#TODO:
#1: Logo
from art import logo
print(logo)

#2: Welcome the player and ask for input for easy/hard
print("Greetings player, welcome to Number Nuance! Think you have the smarts to accurately guess the correct number?")
print("The number is a random value between 1 - 100.")
print("Would you like to play on easy mode (10 guesses), or hard mode (5 guesses)?")
DIFFICULTY = input("Type 'easy' or 'hard' to begin: ")
DIFFICULTY = DIFFICULTY.lower()
 
#3: Create a random number generator
import random
CORRECT_NUMBER = random.randint(1,100)
#Hint: Un-hash if troubleshooting: print(f"Psst, the correct number is {CORRECT_NUMBER}")

#4: Difficulty guesses
if DIFFICULTY == "easy":
  PLAYER_LIVES = 10
elif DIFFICULTY == "hard":
  PLAYER_LIVES = 5

#4.5 Define the "too high/low" statement
def too_high_low(value):
  return value - 1
 
#5: Define a function to run the game
def NEW_GAME():
  attempts = PLAYER_LIVES
  while attempts != 0: 
    print("")
    print(f"You have {attempts} of your attempts remaining to guess the correct number.")
    player_guess = int(input("Guess the correct number: "))
    if player_guess == CORRECT_NUMBER:
      print(f"We have a winner! It was indeed {CORRECT_NUMBER}. Congrats friend :)")
      break  
    else:
      if player_guess > CORRECT_NUMBER:
        print("Your guess is too high.")
        attempts = too_high_low(attempts)
      elif player_guess < CORRECT_NUMBER:
        print("Your guess is too low.")
        attempts = too_high_low(attempts)
  if attempts == 0:
    print(f"Game Over. The correct number was {CORRECT_NUMBER}.")

#6: Game Starts
GAME_RUNNING = True
while GAME_RUNNING:
  NEW_GAME()
  GAME_RUNNING = False

