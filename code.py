import streamlit as st
import random

# Set page title and configure layout
st.set_page_config(page_title="Rock Paper Scissors Game", layout="centered")

# Add a title and description
st.title("🎮 Rock, Paper, Scissors")
st.markdown("Play the classic game against the computer!")

# Initialize session state to store game data
if 'user_score' not in st.session_state:
    st.session_state.user_score = 0

if 'comp_score' not in st.session_state:
    st.session_state.comp_score = 0

if 'game_history' not in st.session_state:
    st.session_state.game_history = []

# Function to determine the winner
def determine_winner(user_move, comp_move):
    # Check for tie
    if user_move == comp_move:
        return "tie", "Great minds think alike!🧠🎩"
    
    # Rock scenarios
    elif user_move == 'r':
        if comp_move == 's':
            return "user", "You've unleashed the crushing power of rock! You win! 🥳"
        else:  # comp_move == 'p'
            return "comp", "Your rock has been elegantly covered by the paper. Computer wins! ✂️🏆"
    
    # Paper scenarios
    elif user_move == 'p':
        if comp_move == 'r':
            return "user", "Your paper has elegantly covered the rock! You win! 🎉"
        else:  # comp_move == 's'
            return "comp", "Snip-snap! The scissors has cut through your paper! Computer wins! ✂️🏆"
    
    # Scissors scenarios
    elif user_move == 's':
        if comp_move == 'p':
            return "user", "Snip-snap! Your scissors cut through paper! You win! ✂️🏆"
        else:  # comp_move == 'r'
            return "comp", "Your scissors has been crushed by the power of rock! Computer wins! 🥳"

# Function to play a round
def play_round(user_choice):
    # Map full names to single letter codes
    move_map = {
        "Rock": "r",
        "Paper": "p",
        "Scissors": "s"
    }
    
    user_move = move_map[user_choice]
    
    # Computer makes a move
    all_moves = ["r", "p", "s"]
    comp_move = random.choice(all_moves)
    
    # Determine winner
    winner, message = determine_winner(user_move, comp_move)
    
    # Update scores
    if winner == "user":
        st.session_state.user_score += 1
    elif winner == "comp":
        st.session_state.comp_score += 1
    
    # Map single letter codes to full names for display
    move_display = {
        "r": "Rock 🪨",
        "p": "Paper 📄",
        "s": "Scissors ✂️"
    }
    
    # Add to game history
    st.session_state.game_history.append({
        "user_move": move_display[user_move],
        "comp_move": move_display[comp_move],
        "message": message
    })

# Create a sidebar with game information
with st.sidebar:
    st.header("Game Info")
    st.markdown("**How to play:**")
    st.markdown("1. Click on Rock, Paper, or Scissors button")
    st.markdown("2. The computer will make its choice")
    st.markdown("3. See who wins the round!")
    
    st.markdown("---")
    st.markdown("**Game Rules:**")
    st.markdown("- Rock crushes Scissors")
    st.markdown("- Scissors cuts Paper")
    st.markdown("- Paper covers Rock")
    
    # Reset button
    if st.button("Reset Game"):
        st.session_state.user_score = 0
        st.session_state.comp_score = 0
        st.session_state.game_history = []
        st.rerun()

# Display current scores
st.header("Scores")
col1, col2 = st.columns(2)
with col1:
    st.metric("You 😀", st.session_state.user_score)
with col2:
    st.metric("Computer 🤖", st.session_state.comp_score)

# Game controls
st.header("Make Your Move!")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Rock 🪨", use_container_width=True):
        play_round("Rock")
        st.rerun()

with col2:
    if st.button("Paper 📄", use_container_width=True):
        play_round("Paper")
        st.rerun()

with col3:
    if st.button("Scissors ✂️", use_container_width=True):
        play_round("Scissors")
        st.rerun()

# Display game history
if st.session_state.game_history:
    st.header("Game History")
    for i, round_data in enumerate(reversed(st.session_state.game_history)):
        with st.container(border=True):
            st.markdown(f"**Round {len(st.session_state.game_history) - i}**")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"You: {round_data['user_move']}")
            with col2:
                st.markdown(f"Computer: {round_data['comp_move']}")
            st.markdown(round_data['message'])

# Display champion when either player reaches 5 points
if st.session_state.user_score >= 5 or st.session_state.comp_score >= 5:
    st.header("🏆 Championship Results 🏆")
    if st.session_state.user_score > st.session_state.comp_score:
        st.success("Congratulations! You are the champion! 🏆")
    elif st.session_state.comp_score > st.session_state.user_score:
        st.error("Better luck next time! The computer is the champion! 🤖")
    else:
        st.info("It's a tie game! 🤝")
