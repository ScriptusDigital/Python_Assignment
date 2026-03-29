import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, flash 
import random

app = Flask(__name__)




@app.route('/')
def home():
    return render_template('index.html', title="Home")

if __name__ == "__main__":
    debug_flag = str(os.environ.get("DEBUG", "False")).lower() in ("1", "true", "yes")
    app.run(debug=debug_flag)
    


