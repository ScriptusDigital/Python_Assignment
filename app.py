import os
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, flash, url_for 
import random

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "default_secret_key")

suggested_movies = []


#----------------------
#FILM LIBRARY BUILD 
#----------------------

FILMS = [
    {
        "title": "Sample",
        "genre": "Comedy",
        "mood": "laugh",
        "pace": "fast",
        "focus": "light",
        "runtime": "medium",
        "pick_type": "crowd",
        "year": "2007",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in volu."
    }
]



#----------------------
# QUIZ LABELS
#----------------------
PROFILE_LABELS = {
    "mood" : {
        "laugh":"Looking for humour",
        "excited": "Looking for excitement",
        "emotional": "Open to emotional impact",
        "thoughtful": "In the mood for something thoughtful"
    },
    "pace" : {
        "slow":"Prefers a calm pace",
        "balanced": "Wants a balanced pace",
        "fast": "Wants something fast-moving",
        "intense": "Wants something intense"
    },
    "focus" : {
        "light":"Low-effort viewing",
        "medium": "Fairly light viewing",
        "focused": "Happy to concentrate",
        "layered": "Open to something layered"
    },
    "runtime" : {
        "short":"Shorter runtime preferred",
        "medium": "Standard runtime preferred",
        "long": "Longer runtime preferred",
        "any": "Runtime is not a big deal"
    },
    "pick_type" : {
        "crowd":"Leaning toward a crowd plased",
        "critics": "Leaning toward a critic's choice",
        "hidden": "Interested in a hidden gem",
        "surprise": "Open to anything "
    },

}

#----------------------
# Defining Scoring weights
#----------------------
WEIGHTS = {
    "mood": 3,
    "pace": 2,
    "focus": 2,
    "runtime": 2,
    "pick_type": 1
}

MAX_SCORE = sum(WEIGHTS.values())


#----------------------
# Python Logic funtions
#----------------------

# Fetch answers from form 
def get_answers_from_form(form):
    return{
        "mood": form.get("mood", "").strip(),
        "pace": form.get("pace", "").strip(),
        "focus": form.get("focus", "").strip(),
        "runtime": form.get("runtime", "").strip(),
        "pick_type": form.get("pick_type", "").strip(),
    }
# Confirm answers 
def answers_are_complete(answers):
    return all(value for value in answers.values())

# creating profile from answers 
def build_user_profile(answers):
    profile = []

    for key, value in answers.items():
        label = PROFILE_LABELS.get(key, {}).get(value)
        if label:
            profile.append(label)

    return profile

# Answer score system build
def score_standard_match(film, answers):
    score = 0
    reasons = []

    if film["mood"] == answers["mood"]:
        score += WEIGHTS["mood"] 
        reasons.append("matched your mood")

    if film["pace"] == answers["pace"]:
        score += WEIGHTS["pace"] 
        reasons.append("fit your preferred pace")
    
    if film["focus"] == answers["focus"]:
        score += WEIGHTS["focus"] 
        reasons.append("matched your level of attention tonight")

    if answers["runtime"] == "any":
        score += 1
        reasons.append("worked for a flexible runtime")
    elif film["runtime"] == answers["runtime"]:
        score += WEIGHTS["runtime"] 
        reasons.append("suited your available time")

    if answers["pick_type"] == "surprise":
        score += 1
        reasons.append("staued open to a wildcard pick")
    elif film["pick_type"] == answers["pick_type"]:
        score += WEIGHTS["pick_type"] 
        reasons.append("fit the kind of pick you wanted")

    return score, reasons

# Surprise me button config
def add_surprise_bonus(film_copy, answers):
    if answers["pick_type"] != "surprise":
        return
    

# Build for copy on results panels routing
def score_film(film, answers):
    score, reasons = score_standard_match(film, answers)

    film_copy = film.copy()
    film_copy["score"] = score
    film_copy["reasons"] = reasons

    add_surprise_bonus(film_copy, answers)

    film_copy["match_percent"] = round((film_copy["score"] / MAX_SCORE * 100))

    return film_copy

# Back up recommendations ranking build

def get_ranked_recommenations(answers, limit=3):
    scored_films = [score_film(film, answers) for film in FILMS]

    scored_films.sort(
        key=lambda item: (item["score"], item["year"]),
        reverse=True
    )

    return scored_films[:limit]

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


@app.route('/results', methods=["POST"])
def results():
    answers = get_answers_from_form(request.form)

    if not answers_are_complete(answers):
        flash("Please answer all five questions before continuing.")
        return render_template("quiz.html", title="Find a Film")
    
    recommendations = get_ranked_recommenations(answers, limit=3)
    top_pick = recommendations[0]
    backup_picks = recommendations[1:]
    user_profile = build_user_profile(answers)

    return render_template(
        'results.html', 
        title="Your Result",
        top_pick=top_pick,
        backup_picks=backup_picks,
        user_profile=user_profile,
        answers=answers
    )
   


if __name__ == "__main__":
    debug_flag = str(os.environ.get("DEBUG", "False")).lower() in ("1", "true", "yes")
    app.run(debug=debug_flag)
    


