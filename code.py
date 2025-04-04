import random

# Initialize scores
compScore = 0
userScore = 0

print("Welcome to Rock, Paper, Scissors")

while True:
    move = input("What is your move? (r,p or s)")
    print("You picked", move)
    
    # Computer makes a move
    allMoves = ["r", "p", "s"]
    compMove = random.choice(allMoves)
    print("The computer picked", compMove)
    
    # Check for tie
    if compMove == move.lower():
        print("Great minds think alike!🧠🎩")
    # Rock scenarios
    elif move.lower() == 'r':
        if compMove == 's':
            print("You've unleashed the crushing power of rock! You win! 🥳")
            userScore += 1
        elif compMove == 'p':
            print("Your rock has been elegantly covered by the paper. Computer wins! ✂️🏆")
            compScore += 1
    # Paper scenarios
    elif move.lower() == 'p':
        if compMove == 'r':
            print("Your paper has elegantly covered the rock! You win! 🎉")
            userScore += 1
        elif compMove == 's':
            print("Snip-snap! The scissors has cut through your paper! Computer wins! ✂️🏆")
            compScore += 1
    # Scissors scenarios
    elif move.lower() == 's':
        if compMove == 'p':
            print("Snip-snap! Your scissors cut through paper! You win! ✂️🏆")
            userScore += 1
        elif compMove == 'r':
            print("Your scissors has been crushed by the power of rock! Computer wins! 🥳")
            compScore += 1
    
    # Display scores
    print("Scores")
    print(f"😀{userScore}")
    print(f"🤖{compScore}")
    
    # Ask to continue
    continue2 = input("Ready for another adventure? 🚀")
    if continue2.lower() == "no":
        break

# Display final message
print("\nThanks for playing!")
print(f"Final Scores: You: {userScore} | Computer: {compScore}")

if userScore > compScore:
    print("Congratulations! You are the champion! 🏆")
elif compScore > userScore:
    print("Better luck next time! The computer is the champion! 🤖")
else:
    print("It's a tie game! 🤝")
