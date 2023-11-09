# app.py

from flask import Flask, render_template
from streamlit import StreamlitCliRunner

app = Flask(__name__)

# Define the Streamlit app as a function
def run_streamlit():
    runner = StreamlitCliRunner()
    args = ["streamlit", "run", "app2.py"]
    runner.invoke(args)

# Define routes for different pages
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login")
def login():
    return render_template("login.html")

# Run the Streamlit app when the Flask app starts
if __name__ == "__main__":
    run_streamlit()

    # Run the Flask app
    app.run(debug=True)
