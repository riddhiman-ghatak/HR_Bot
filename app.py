from flask import Flask, render_template, request
from transformers import BertForQuestionAnswering
from transformers import AutoTokenizer
from transformers import pipeline

app = Flask(__name__)

# model loading and setup
model = BertForQuestionAnswering.from_pretrained('deepset/bert-base-cased-squad2')
tokenizer = AutoTokenizer.from_pretrained('deepset/bert-base-cased-squad2')
nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
valid_username = "user"
valid_password = "password"

# Dummy context for demonstration
file_path = "dataset.txt"
try:
    with open(file_path, "r") as file:
        text = file.read()
except FileNotFoundError:
    text = ""
except Exception as e:
    text = ""

context = text

# Define routes
# @app.route('/')
# def home():
#     return render_template('home.html', context=context)

# @app.route('/get_answer', methods=['POST'])
# def get_answer():
#     question = request.form['question']

#     if context and question:
#         # Get the answer using the question-answering model
#         answer = nlp({
#             'question': question,
#             'context': context
#         })
#         return render_template('home.html', answer=answer['answer'])
#     else:
#         return "Context or question is missing. Please provide both."

@app.route('/', methods=['GET', 'POST'])
def home():
    answer = None

    if request.method == 'POST':
        question = request.form['question']

        if context and question:
            # Get the answer using the question-answering model
            answer = nlp({
                'question': question,
                'context': context
            })

    return render_template('home.html', answer=answer)

@app.route('/faq')
def faq():
    # Add FAQ content here
    return render_template('faq.html')

@app.route('/about')
def about():
    # Add FAQ content here
    return render_template('about.html')

@app.route('/contact')
def contact():
    # Add contact information or a contact form here
    return render_template('contact.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == valid_username and password == valid_password:
            #return "Login Successful!"
            return render_template('home.html')
            # You can add code here to grant access to protected pages
        else:
            return "Login Failed. Please check your credentials."

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
