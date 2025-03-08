import streamlit as st
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="Streamlit App",  layout="centered")

# Initialize session state variables
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 10)
if 'lives' not in st.session_state:
    st.session_state.lives = 3
if 'next_try' not in st.session_state:
    st.session_state.next_try = None

st.title("Number Guessing Game")



if st.session_state.next_try and datetime.now() < st.session_state.next_try:
    st.write("Opps :sob: You have run out of lives. Please come back later.")
else:
    st.write("I have a number between 1 and 10 in mind. Can you guess it?")
    st.write(f"Lives : {st.session_state.lives}")
    guess = st.text_input("Enter your guess:")

    if guess:
        guess = int(guess)
        if guess == st.session_state.number:
            st.write("Congratulations! You guessed it right.🤗")
            st.session_state.number = random.randint(1, 10)
            st.session_state.lives = 3
        else:
            st.session_state.lives -= 1
            if st.session_state.lives > 1:
                if guess < st.session_state.number:
                    st.write("Too low. Try again.")
                else:
                    st.write("Too high. Try again.")
            else:
                st.session_state.next_try = datetime.now() + timedelta(days=1)

st.write("Made with :heart: by [Habiba Madni]")