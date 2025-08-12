


from flask import Flask, render_template
from flask import send_from_directory
import os 
from flask import Flask, render_template, request, jsonify
# from flask import request, jsonify
# from transformers import pipeline
# from flask import Flask, request, jsonify, render_template_string, send_from_directory



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




#-------------------------------------Chatbot building----------------------------------------

# Add this chatbot function and endpoint to your main.py

def simple_chatbot_response(question):
    question_lower = question.lower()
    
    if any(word in question_lower for word in ['hello', 'hi', 'hey', 'greetings']):
        return "Hello! I'm here to help you learn about MD AL AMIN TOKDER. What would you like to know?"
    elif any(word in question_lower for word in ['contact', 'email', 'phone', 'reach']):
        return "📧 Email: alamintokdercse@gmail.com\n📞 Phone: +8801750206042\n📍 Location: Dhaka, Bangladesh"
    elif any(word in question_lower for word in ['experience', 'work', 'job', 'career']):
        return "🔹 Current: ML Engineer at JB Connect Ltd, Dhaka (Jan 2024 - Present)\n🔹 Previous: ML Engineer at Devolved AI, USA (Sep 2022 - Nov 2023)\n🔹 Earlier: Junior Software Engineer at Code Studio Ltd (Jan 2022 - Nov 2022)"
    elif any(word in question_lower for word in ['education', 'study', 'university', 'degree']):
        return "🎓 BSc in Computer Science and Engineering\n🏫 Rajshahi University of Engineering and Technology (RUET)\n📅 2018 - 2023 | CGPA: 3.63"
    elif any(word in question_lower for word in ['project', 'luna', 'prescription']):
        return "🚀 **Luna**: Advanced LLM project using Generative AI, GPT, Decentralized AI\n🏥 **Prescription Handler**: AI-powered OCR system with HTR, LLMs, Python"
    elif any(word in question_lower for word in ['skill', 'technology', 'expertise', 'ai', 'ml']):
        return "💻 Skills: Generative AI, LLMs, GPT models, Decentralized AI, OCR, HTR, Python, Web Development (PHP, MySQL, HTML, CSS, JS)"
    elif any(word in question_lower for word in ['award', 'achievement', 'contest']):
        return "🏆 Awards:\n• ICPC Preliminary Dhaka Site 2023 (522th/2600 teams)\n• RUET Contest 2023 (7th Final)\n• North Bengal Startup Summit 2023 (4th)"
    else:
        return "I can help with info about:\n• Work experience & career\n• Education background\n• Projects & research\n• Skills & expertise\n• Contact details\n• Awards & achievements\n\nWhat interests you?"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message.strip():
            return jsonify({'response': 'Please ask me something about Al Amin!'})
        
        bot_response = simple_chatbot_response(user_message)
        return jsonify({'response': bot_response})
    
    except Exception as e:
        return jsonify({'response': 'Sorry, I encountered an error. Please try again!'})

#-----------------------------------------------------------------------------





if __name__ == '__main__':
    app.run(debug=True)
























