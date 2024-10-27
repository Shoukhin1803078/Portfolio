


from flask import Flask, render_template
from flask import send_from_directory
import os 


app = Flask(__name__)






@app.route('/')
def home():
    # Your personal information
    personal_info = {
        'name': 'MD AL AMIN TOKDER',
        'title': 'Machine Learning Engineer',
        'email': 'alamintokdercse@gmail.com',
        'location': 'Dhaka, Bangladesh',
        'phone': '+8801750206042',
        'about': 'Hi this is Al Amin strongly passionate on Machine Learning technology specially in generative AI and LLMs.'
    }
    
    # Experience data
    experience = [
        {
            'title': 'Machine Learning Engineer',
            'company': 'JB Connect Ltd',
            'location': 'Dhaka, Bangladesh',
            'period': 'Jan 2024 - Present',
            'description': 'Build reallife application using AI, Generative AI model, Use GEMINI, OPEN AI API, open source model LAMA2,3 API in various business solution'
        },
        {
            'title': 'Machine Learning Engineer',
            'company': 'Devolved AI',
            'location': 'Bakersfield, CA, USA',
            'period': 'Sep 2022 - Nov 2023',
            'description': 'Building cutting edge LLMs for innovative solutions. Generative AI, LLMs, GPT, Decentralized AI'
        },
        {
            'title': 'Junior Software Engineer',
            'company': 'Code Studio Ltd',
            'location': 'Rajshahi , Bangladesh',
            'period': 'Jan 2022 - Nov 2022',
            'description': 'Develop Website with PHP ,MYSQL, HTML,CSS,JS'
        }

    ]
    
    # Education data
    education = {
        'degree': 'BSc in Computer Science and Engineering',
        'institution': 'Rajshahi University of Engineering and Technology (RUET)',
        'period': '2018 - 2023',
        'cgpa': '3.63'
    }
    
    # Projects data
    projects = [
        {
            'name': 'Luna',
            'skills': 'LLMs, Generative AI, GPT, Decentralized AI',
            'description': 'Advanced LLM-based project'
        },
        {
            'name': 'Prescription Handler',
            'skills': 'OCR, HTR, LLMs, Generative AI, GPT, Decentralized AI, Python',
            'description': 'AI Automated prescription handling system'
        }
    ]
    
    # Publications data
    publications = [
        {
            'title': 'Garbage Classification using a Transfer Learning with Parameter Tuning',
            'publisher': 'IEEE Xplore'
        },
        {
            'title': 'BloodStein Hyperspectral Image Classification Using 3D CNN',
            'publisher': 'ICEEICT, IEEE Xplore'
        }
    ]
    
    # Awards data
    awards = [
        'ICPC Preliminary Dhaka Site 2023 (522th out of 2600 teams)',
        'Innovative Idea and project Contest RUET 2023 (7th in Final round)',
        'North Bengal Startup Summit 2023 Startup Idea contest Finalist (4th)',
        'Project showcasing - RUET CSE FEST 2022 (14th position)'
    ]

    return render_template('index.html', 
                         personal_info=personal_info,
                         experience=experience,
                         education=education,
                         projects=projects,
                         publications=publications,
                         awards=awards)







@app.route('/resume')
def download_resume():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(
        os.path.join(current_dir, 'static', 'resume'),
        'CV.pdf',
        as_attachment=True
    )













if __name__ == '__main__':
    app.run(debug=True)