import streamlit as st
from transformers import BertForQuestionAnswering
from transformers import AutoTokenizer
from transformers import pipeline

# Load the pre-trained BERT model for question-answering
model = BertForQuestionAnswering.from_pretrained('deepset/bert-base-cased-squad2')
tokenizer = AutoTokenizer.from_pretrained('deepset/bert-base-cased-squad2')
nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)


# Streamlit web app
st.title("HR Hive bot")

# Input field for the context
context = st.text_area("Enter the context:", "An internship is...")

# Input field for the question
question = st.text_input("Ask a question:", "What is an internship?")

# Answer button
if st.button("Get Answer"):
    if context and question:
        # Get the answer using the question-answering model
        answer = nlp({
            'question': question,
            'context': context
        })

        # Display the answer
        st.write("Answer:", answer['answer'])

# Optionally, you can add more Streamlit elements, customize the layout, and enhance the user interface as needed.


