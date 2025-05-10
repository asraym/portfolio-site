import os
from flask import Flask, render_template

# Create the Flask application
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET")

# Data for the portfolio
portfolio_data = {
    "name": "Ashish Raymajhi",
    "title": "Computer Science Student",
    "bio": "A passionate learner specializing in AI for IoT with a strong foundation in programming and machine learning.",
    "education": [
        {
            "degree": "Bachelors of Technology in Computer Science",
            "specialization": "AI for IoT",
            "institution": "Sharda University",
            "period": "2023-2027 (ongoing)",
            "description": "Currently pursuing a B.Tech degree with a focus on Artificial Intelligence for Internet of Things."
        }
    ],
    "skills": [
        {"name": "Data Structures & Algorithms", "level": 85},
        {"name": "Python", "level": 90},
        {"name": "C", "level": 80},
        {"name": "Machine Learning", "level": 75},
        {"name": "OCR (Optical Character Recognition)", "level": 70},
        {"name": "Full-stack Web Development", "level": 80}
    ],
    "projects": [
        {
            "name": "LitPals",
            "description": "A platform connecting book enthusiasts to discuss and share literary works.",
            "technologies": ["Python", "Flask", "HTML/CSS", "JavaScript", "SQL"]
        },
        {
            "name": "Text Recognition and Translation",
            "description": "An application that recognizes text from images and translates it to different languages.",
            "technologies": ["Python", "OCR", "Machine Learning", "Translation APIs"]
        },
        {
            "name": "Sentiment Analysis",
            "description": "A tool that analyzes text to determine the emotional tone behind it.",
            "technologies": ["Python", "Natural Language Processing", "Machine Learning"]
        }
    ],
    "certifications": [
        {
            "name": "Machine Learning and Deep Learning using Python",
            "issuer": "UI EduCon",
            "date": "2023"
        }
    ],
    "languages": [
        {"name": "Hindi", "level": "Native"},
        {"name": "English", "level": "Fluent"},
        {"name": "Chinese", "level": "HSK 2 level (Elementary)"}
    ],
    "contact": {
        "email": "raymajhiashish@gmail.com",
        "github": "https://github.com/asraym",
        "linkedin": "https://www.linkedin.com/in/ashish-raymajhi-32xa"
    }
}

@app.route('/')
def index():
    return render_template('index.html', data=portfolio_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
