import streamlit as st
import random

# Function to start or reset the game
def start_game():
    # Initialize session state variables if not already set
    if 'number_to_guess' not in st.session_state:
        st.session_state.number_to_guess = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.message = "Welcome to the Guessing Game! Guess a number between 1 and 100."
        st.session_state.game_over = False

# Function to handle the user's guess
def check_guess(guess):
    # Increase the number of attempts
    st.session_state.attempts += 1
    
    # Check if the guess is correct, too high, or too low
    if guess < st.session_state.number_to_guess:
        st.session_state.message = "Too low! Try again."
    elif guess > st.session_state.number_to_guess:
        st.session_state.message = "Too high! Try again."
    else:
        st.session_state.message = f"Congratulations! You guessed the correct number {st.session_state.number_to_guess} in {st.session_state.attempts} attempts."
        st.session_state.game_over = True

# Start the game when the script is run
start_game()

# Input box for the user's guess
if not st.session_state.game_over:
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
    
    # Button to submit the guess
    if st.button("Submit Guess"):
        if guess:
            check_guess(guess)

# Display the feedback message
st.write(st.session_state.message)

# Button to reset the game if the user guesses correctly or wants to try again
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.clear()  # Clear the session state to start a new game
        start_game()
        
