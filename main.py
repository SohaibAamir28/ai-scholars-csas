import streamlit as st
import openai

# Replace YOUR_API_KEY with your actual OpenAI API key
openai.api_key = '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'

def ask_gpt_4(question, model="text-davinci-003", temperature=0.5):
    """Function to query OpenAI's GPT-4 API with a question."""
    response = openai.Completion.create(
        engine=model,
        prompt=question,
        temperature=temperature,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].text.strip()

# Streamlit app UI setup
st.title('AI Campus Companion')
st.write('Ask any question about the university and get instant answers.')

# User input
user_question = st.text_input('Enter your question:', '')

# Button to get the answer
if st.button('Ask'):
    if user_question:
        with st.spinner('Fetching your answer...'):
            # Fetch the answer from GPT-4
            answer = ask_gpt_4(user_question)
            st.write(answer)
    else:
        st.write('Please enter a question to get an answer.')

