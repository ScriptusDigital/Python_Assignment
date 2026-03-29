import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, flash 
import random

app = Flask(__name__)


@app.route('/test_flash')
def test_flash():
    flash("This is a flash message!")
    return render_template('index.html', title="Home")

@app.route('/')
def home():
    return render_template('index.html', title="Home")


@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/random')
def random():
    return render_template('random.html', title="Random")

@app.route('/quiz')
def quiz():
    return render_template('quiz.html', title="Find a Film")

if __name__ == "__main__":
    debug_flag = str(os.environ.get("DEBUG", "False")).lower() in ("1", "true", "yes")
    app.run(debug=debug_flag)
    


