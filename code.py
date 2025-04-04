#Start code here
import random
print("Welcome to Rock, Paper, Scissors")
compScore = 0
userScore = 0
while True:
  move = input("What is your move? (r,p or s)")
  print("You picked", move)
  allMoves = ["r", "p", "s"]
  compMove = random.choice(allMoves)
  print("The computer picked", compMove)
  if compMove == move.lower():
    print("Great minds think alike!🧠🎩")
  elif move.lower() == 'r':
    if compMove == 's':
      print("You've unleashed the crushing power of rock! You win! 🥳")
      userScore += 1
    elif compMove == 'p':
      print("Your rock has been elegantly covered by the paper. Computer wins! ✂️🏆")
      compScore += 1
  elif move.lower() == 'p':
    if compMove == 'r':
      print("Your paper has elegantly covered the rock! You win! 🎉")
      userScore += 1
    elif compMove == 's':
      print("Snip-snap! The scissors has cut through your paper! Computer wins! ✂️🏆")
      compScore += 1
  elif move.lower() == 's':
    if compMove == 'p':
      print("Snip-snap! Your scissors cut through paper! You win! ✂️🏆")
      userScore += 1
    elif compMove == 'r':
      print("Your scissors has been crushed by the power of rock! Computer wins! 🥳")
      compScore += 1
  print("Scores")
  print(f"😀{userScore}")
  print(f"🤖{compScore}")
  continue2 = input("Ready for another adventure?” 🚀")
  if continue2.lower() == "no":
    break
