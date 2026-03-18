import streamlit as st
import os
from openai import OpenAI

# Initialize OpenAI client (API key will be set in Streamlit Secrets)
client = OpenAI()

def generate_study_materials(text):
    # Generate Summary
    summary_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes text for students."},
            {"role": "user", "content": f"Summarize the following text concisely, highlighting key concepts:\n\n{text}"}
        ]
    )
    summary = summary_response.choices[0].message.content

    # Generate Flashcards
    flashcards_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that creates flashcards from text."},
            {"role": "user", "content": f"Create 5 flashcards (Question: Answer) from the following text. Format each flashcard on a new line.\n\n{text}"}
        ]
    )
    flashcards = flashcards_response.choices[0].message.content

    # Generate Quiz
    quiz_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that creates multiple-choice quizzes from text."},
            {"role": "user", "content": f"Create a 5-question multiple-choice quiz from the following text. For each question, provide 4 options (A, B, C, D) and indicate the correct answer. Format each question and its options on new lines, followed by 'Correct Answer: [Letter]'.\n\n{text}"}
        ]
    )
    quiz = quiz_response.choices[0].message.content

    return summary, flashcards, quiz

# Streamlit UI
st.set_page_config(page_title="SBA Digital: AI Study Guide Generator", layout="wide")
st.title("🧠 SBA Digital: AI Study Guide Generator")
st.markdown("--- ")

st.write("**Turn your notes into summaries, flashcards, and quizzes in seconds!**")

user_input = st.text_area("Paste your notes or text here:", height=300)

if st.button("Generate Study Materials"):
    if user_input:
        with st.spinner("Generating your study materials with AI..."):
            try:
                summary, flashcards, quiz = generate_study_materials(user_input)

                st.subheader("📝 Summary")
                st.write(summary)

                st.subheader("🧠 Flashcards")
                st.write(flashcards)

                st.subheader("❓ Quiz")
                st.write(quiz)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text to generate study materials.")

st.markdown("--- ")
st.markdown("Built by SBA Digital for smarter studying.")
