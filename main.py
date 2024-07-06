from random import randint
easy = 10
hard = 5
def check_ans(guess,ans,turns):
  if guess > ans:
    print("Too high")
    return turns - 1

  elif guess < ans:
    print("Too low")
    return turns - 1

  else:
    print(f"You got it! The answer was {ans}")

def dificulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return easy
  else:
    return hard

def game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}")
  turns = dificulty()
  guess = 0
  while guess!= answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turns = check_ans(guess, answer, turns)
    if turns == 0:
          print("You've run out of guesses, you lose.")
          return
    elif guess != answer:
      print("Guess again.")


game()



