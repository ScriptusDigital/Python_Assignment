import os
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, flash, url_for 
import random

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "default_secret_key")

suggested_movies = []

@app.route('/')
def home():
    return render_template('index.html', title="Home")


@app.route('/suggestions', methods=['GET', 'POST'])
def suggestions():
    if request.method == 'POST':
        title = request.form.get('title')
        genre = request.form.get('genre')
        reason = request.form.get('reason')

        if not title or not genre or not reason:
            flash("Please fill in all fields.")
            return redirect(url_for('suggestions'))
        
        suggested_movies.append({
            'title': title,
            'genre': genre,
            'reason': reason
        })

        flash("Thank you for your suggestion!")
        return redirect(url_for('suggestions'))
    return render_template('suggestions.html', title="Suggest a Movie", suggested_movies=suggested_movies)  
    
@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/random')
def random():
    return render_template('random.html', title="Random")

@app.route('/quiz')
def quiz():
    return render_template('quiz.html', title="Find a Film")


@app.route('/results')
def results():
    return render_template('results.html', title="Results")


if __name__ == "__main__":
    debug_flag = str(os.environ.get("DEBUG", "False")).lower() in ("1", "true", "yes")
    app.run(debug=debug_flag)
    


