# Project Title

**What Should I Watch Tonight?**

## Project Description
What Should I Watch Tonight? is a Flask-based film recommendation web application that helps users choose a movie through either a short interactive quiz or a random selector feature. The site combines Python back-end logic with HTML, CSS, and JavaScript front-end interactivity to create a themed recommendation experience inspired by the look and feel of a 1990s multipƒlex cinema. 

The project demonstrates core Flask concepts such as routing, template rendering, form handling, POST requests, and dynamic content generation alongside front-end techniques including multi-step form interaction, responsive layout, navigation toggling, and styled feedback messages. 

## Features

#### Feature 1 - Five question interactive film quiz
Users complete a short five-question quiz about their mood, prefered pace, level of focus, available runtime, and type of film pick they want. The quiz appears one question at a time, creating a guided step-by-step experience rather than presenting all questions at once. 

#### Feature 2 -Weighted recommendation system
Once the quiz is submitted, Python compares the user’s answers against a structured film library. Each film includes defined attributes such as mood, pace, focus, runtime, genre, year, description, and an accompanying poster image. The application then ranks the films according to a weighted scoring system and returns the strongest overall match, along with backup recommendations. 

#### Feature 3 - Random movie generator
Users who do not want to complete the quiz can instead use the **Take a Chance** feature. This selects a random film from the library and displays it as a one-click recommendation. This route uses Python’s random module to generate a different possible result from the existing dataset. 

#### Feature 4 - Suggest a movie form
The application includes a suggestion page where users can submit a film title, genre, and short reason for why the film should be included. This demonstrates Flask form handling, validation, POST request processing, flash messages, and rendering submitted suggestions back to the page. 


#### Feature 5 - Dynamic results and random recommendation pages
The application includes dedicated pages for both the quiz result and the random recommendation feature. These pages render film data dynamically from the Python film library, including title, genre, year, description, and poster image (to make the pages feel more visually striking and engaging). 

## Design choices

### Theme and visual style
The visual style was designed to evoke the atmosphere of a 1990s multiplex cinema. The aim was to create something more expressive than a standard minimal app by using bolder colours, striking headings, large buttons, poster imagery, and a lobby-style cinema background. 

### Colors
A cinema-inspired palette was used throughout the project. Reds, blues, gold tones, and light panel backgrounds were used to create contrast against the darker photographic background while still allowing the content to remain readable and accessibility friendly. 

### Fonts
Display fonts were used to create a bold, theatrical feel with supporting text using an easily readable sans-serif styling. The fonts used were chosen to balance strong visual identity with practical readability.

### Images/Graphics
Film posters are displayed on the recommendation and random movie pages to make the results feel more visually engaging. The poster images were stored locally in the static images folder and linked to each film entry in the Python film library structure. The background image was designed to reinforce the multiplex setting. 

## Development Process
###Project planning
The project did not begin as a full recommendation system. My original idea was to build a Flask site with a film theme and a couple of interactive elements, mainly a random film recommendation generator and a contact form. On starting the build, I realised the original contact-form idea could be better repurposed into a suggestion feature whereby users can input a film title, genre, and a reason for inclusion, and those submitted values could be processed in Flask and displayed back on the page. 

Because I was already building a film library as a structured Python data set, I saw that the same data could be better used for a recommendation system. That shifted the project from being mainly a themed multi-page site into a quiz-based recommender application. Drawing on some of the same ideas I had used in my early JavaScript quiz assignment, I planned a short sequence of questions to collect user preferences and compare them against the stored film attributes. 

From there, the planning focused on:
- building a film library with clearly defined attributes.
- designing a recommendation method that could compare user answers against the film library.
- keeping the random generator and suggestion form as additional features. 
 
The architecture for the site was then structured around several core routes: home, quiz, results, random recommendation, suggestions, and about. 


### Recommendation logic planning
The greatest amount of planning went into the app’s recommendation logic. I considered more advanced approaches such as a dot-product style model or vector-based comparison system, where both films, their attributes, and user preferences would be converted to numerical representations that are then compared for similarity. However, because the app uses a relatively small curated library rather than a large-scale dataset, a full vector-based implementation would have added significant complexity without meaningfully improving the final user experience.

Instead, I used a weighted scoring model. The user’s answer is compared directly with corresponding film attributes. Different question categories are given different weights depending on their importance. For example, mood is weighted on what kind of film the user is likely to want. This made the system easier to understand, easier for debugging, and more suitable for the project’s scale. 

### Building the film library
Each film was stored in Python as a structured dictionary containing:
-title
-genre
-mood
-pace
-focus
-runtime
-pick_type
-year
-description
-poster filename

I defined the parameter structure for the library and then used Claude AI to generate sample film entries that matched those parameters. 

### Front-end and template development
Jinja templates were used to render the different pages while keeping the structure modular. The quiz page uses a multi-step layout controlled by JavaScript. The results page dynamically displays the highest-scoring recommendation, supporting profile labels, backup recommendations, and poster images. The random page renders a randomly selected film using the same structured film data. 

### Interactivity
JavaScript is used for two main features:
- a hamburger menu toggle for navigation
- the multi-step quiz flow

The quiz uses DOM selection, event listeners, and step logic to show one question card at a time, move forward and back between cards, update the progress text, and animate the progress bar. It also prevents users from moving on or submitting if the current question has not been answered - showing a feedback message when validation fails. 


## Challenges Faced
###Connecting back-end logic to front-end templates
The biggest challenge was ensuring all parts of the Python script connected properly to the templates. Because the project depends on routes, template variables, structured dictionaries, form submission, and dynamic rendering, even small naming mismatches created app failure. 

###Layout testing in Flask
Unlike with a static front-end workflow with live preview, changes to the Flask app required rerunning or refreshing through the Python server. This made design iteration slower, especially when adjusting page layout, spacing, and route-linked content. 

## Resources Used
### Navigation menu
- [Easy hamburger menu with JS](https://dev.to/ljcdev/easy-hamburger-menu-with-js-2do0)
## JavaScript multi-step quiz form
-[CSS-Tricks - How to create multi-step forms with Javascript and CSS](https://css-tricks.com/how-to-create-multi-step-forms-with-vanilla-javascript-and-css)
- [W3Schools- How to: For with multiple steps](https://www.w3schools.com/howto/howto_js_form_steps.asp)
- [Tuts+ - How to build a multi-step form wizard with JavaScript](https://webdesign.tutsplus.com/how-to-build-a-multi-step-form-wizard-with-javascript--cms-93342t)

### Recommendation logic research
- [DataCamp - Beginner Tutorial: Recommender Systems in Python ](https://www.datacamp.com/tutorial/recommender-systems-python)
-[StrataScratch - Step-by-Step Guide to Building Content-Based Filtering](https://www.stratascratch.com/blog/step-by-step-guide-to-building-content-based-filtering)
-[Real Python - Build a Recommendation Engine With Collaborative Filtering	(https://realpython.com/build-recommendation-engine-collaborative-filtering/
)
- [Weighted Scoring System Repo](https://github.com/windowshopr/Weighted-Scoring-System-Repo/blob/main/main.py)

### Images and media
- Film poster images sourced from: [fanart.tv](https://fanart.tv/)
- Background image ‘Lobby_resized2.jpeg’ and ‘favicon.png’ generated in ChatGPT

## Development Notes
### Flask functionality used
The project makes use of: 
- Flask routes
- Jinja templating
- GET and POST request handling
- redirect and url_for
- flash messaging
- dynamic content rendering
- Python list/dictionary data structures

## Deployed site
This project is available at: 
[GitHub Repository](https://github.com/ScriptusDigital/Python_Assignment)

## Live deployment site
The application is available at: 
[Live App](https://python-assignment-bc40.onrender.com)







