import streamlit as st
import random


def main():
    st.set_page_config(page_title="Hangman Game", page_icon="😵")
    st.title("😵 Hangman Game")

    words = ['python', 'streamlit', 'hangman', 'developer', 'banana', 'education']

    if 'word' not in st.session_state:
        st.session_state.word = random.choice(words)
        st.session_state.guesses = []
        st.session_state.attempts = 6

    word_display = ' '.join([letter if letter in st.session_state.guesses else '_' for letter in st.session_state.word])
    st.write(f"Word: {word_display}")
    st.write(f"Attempts remaining: {st.session_state.attempts}")

    guess = st.text_input("Enter a letter:", max_chars=1).lower()

    if st.button("Guess") and guess.isalpha() and len(guess) == 1:
        if guess in st.session_state.guesses:
            st.warning("You already guessed that letter!")
        elif guess in st.session_state.word:
            st.session_state.guesses.append(guess)
            st.success(f"Good guess! '{guess}' is in the word.")
        else:
            st.session_state.guesses.append(guess)
            st.session_state.attempts -= 1
            st.error(f"Wrong guess! '{guess}' is not in the word.")

    if '_' not in word_display:
        st.success(f"🎉 You won! The word was '{st.session_state.word}'.")
        st.session_state.word = random.choice(words)
        st.session_state.guesses = []
        st.session_state.attempts = 6

    if st.session_state.attempts <= 0:
        st.error(f"😵 You lost! The word was '{st.session_state.word}'.")
        st.session_state.word = random.choice(words)
        st.session_state.guesses = []
        st.session_state.attempts = 6


if __name__ == "__main__":
    main()
