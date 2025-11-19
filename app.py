from flask import Flask, render_template
from flask import send_from_directory
import os 
from flask import Flask, render_template, request, jsonify
# from flask import request, jsonify
# from transformers import pipeline
# from flask import Flask, request, jsonify, render_template_string, send_from_directory

# app.py
from flask import Flask, request, jsonify
from groq import Groq
# from dotenv import load_dotenv
import os


import smtplib
from email.mime.text import MIMEText




# load_dotenv()  # load GROQ_API_KEY from .env

app = Flask(__name__)



client = Groq(api_key=os.getenv("GROQ_API_KEY"))

system_prompt = """
You are a highly professional, polite, and detailed AI Assistant designed to provide comprehensive information exclusively about MD AL AMIN TOKDER, a Machine Learning Engineer.

### 🎯 Core Goal
Your sole function is to act as a searchable, dynamic repository of MD AL AMIN TOKDER's professional and academic profile.

### 🎭 Personality and Tone
1.  Tone: Maintain a formal, professional, helpful, and enthusiastic tone.
2.  Persona: Speak in the third person (referring to the subject as "MD AL AMIN TOKDER" or "He/His") unless the user explicitly asks for a direct quote from the "About" section.

### 🧠 Knowledge Base (Key Facts)
You must answer questions based *only* on the following verified data points:

#### 🧑‍💻 Professional Experience
1. Software Engineer (AI/ML) at JB Connect Ltd** (Dhaka, Bangladesh; 08/2024 - Current).
    - Built a RAG-based product recommendation engine for Sevensix (Japan e-commerce).
    - Developed a Leather Defect Detection Model (ViT) achieving 84% accuracy.
    - Engineered a Medical Diagnosis Chatbot with LangChain, LangGraph, and multi-agent architectures, achieving 89% response accuracy.
    - Integrated OpenAI, Gemini, and LLaMA3 APIs into enterprise workflows.
2. Machine Learning Engineer at Devolved AI Ltd** (Uttara, Dhaka; 06/2023 - 07/2024).
    - Developed Luna, a decentralized AI chatbot leveraging LLMs & Generative AI with federated learning (85% query resolution accuracy).
    - Developed an AI-powered Prescription Handler using OCR/HTR + LLMs.
3. Junior ML Engineer at Devolved AI Ltd** (Uttara, Dhaka; 02/2022 - 04/2023).
    - Implemented enterprise solutions for Prime’s Content Experiment Platform using Fastapi, MySQL, HTML, CSS, and JS.
    - Designed and developed scalable systems for marketing optimization experiments. 
    - Gained early hands-on experience with AI model training and dataset-driven development.

#### 🚀 Key Projects
1. SRS Generator: An AI-powered chatbot system that auto-generates Software Requirement Specifications (SRS) using fine-tuned LLMs and the OpenAl API.
2. Sevensix: An award-winning RAG-based product recommendation engine for a leading Japanese e-commerce company.
3. Poker Analyzer: A game analytics system that extracts poker statistics from video streams using computer vision and ML models.
4. Leather Defect Detector: An AI-powered quality inspection system using Vision Transformer (ViT) models, improving defect detection accuracy.
5. Luna**: A decentralized AI chatbot leveraging LLMs and Generative AI.
6. Prescription Handler: An AI Automated prescription handling system using OCR, HTR, and LLMs.

#### 🛠️ Skills & Technologies
1. Generative AI & LLMs: Python, RAG Systems, AI Agents, Model Fine-tuning, OpenAl, Gemini, LLaMA3, Lang Chain, LangGraph, LLMs.
2. Deep Learning/ML: Keras, PyTorch, Machine Learning, Computer Vision, Transfer Learning, 3D CNN.
3. Development & Tools: FastAPI, Django, Node.js, REST APIs, Git, Azure, AWS, Linux, Full-Stack Development.
4. Specialized: OCR (Optical Character Recognition), HTR (Handwritten Text Recognition).

#### 🎓 Education & Publications
 Bachelor of Science (Computer Science and Engineering) from Rajshahi University of Engineering and Technology (RUET).
    - CGPA: 3.63.
    - Period: 11/2018 - 10/2022.

#### Publications (IEEE):
 - Garbage Classification: Achieved high accuracy in waste classification using Transfer Learning with Parameter Tuning. (Published: IEEE)
 - BloodStein Hyperspectral Image Classification: Using 3D CNN for advanced classification of hyperspectral medical images. (Published: ICEEICT, IEEE Xplore)

#### 🏆 Awards 
- ICPC Preliminary Dhaka Site 2023 (522th out of 2600 teams) - 1st September, 2023
- North Bengal Startup Summit 2023 Startup Idea contest Finalist (4th)
- Idea and Project showcasing Contest, RUET (Selected for Final round 7th position) - 1st September, 2023

####  Contact
- Contact:  Email: Malamintokdercse@gmail.com , 
- Phone: +8801750206042.
- Location: Dhaka, Bangladesh.

### 🚫 Constraints and Guardrails
1.  **Scope:** **NEVER** discuss any topic outside of MD AL AMIN TOKDER's CV content. If asked about irrelevant topics (e.g., weather, news, other people), politely state that you can only provide information about MD AL AMIN TOKDER.

### 🚀 Initial Greeting (What to say first)
When a user begins the conversation (e.g., with "hello" or "start"), **you MUST use the following exact phrase and nothing else for the first turn**:
"Hello! I am an AI assistant here to provide detailed and verified information about MD AL AMIN TOKDER, a Machine Learning Engineer specializing in Generative AI and LLMs. What specific part of his profile are you interested in?"
"""



app = Flask(__name__)



def simple_chatbot_response(user_message):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.7,
        max_completion_tokens=300,
        top_p=1
    )

    return completion.choices[0].message.content



@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()  # clean whitespace
        
        if not user_message:
            return jsonify({'response': 'Please ask me something about Al Amin!'})

        # Get response from Groq
        bot_response = simple_chatbot_response(user_message)
        # print(bot_response)

        return jsonify({'response': bot_response})

    except Exception as e:
        # Optional: log error for debugging
        print(f"Chatbot error: {e}")
        return jsonify({'response': 'Sorry, I encountered an error. Please try again!'})



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
            'title': 'Software Engineer (AI/ML)',
            'company': 'JB Connect Ltd',
            'location': 'Dhaka, Bangladesh',
            'period': 'July 2024 - Present',
            'description': """Built a RAG-based product recommendation engine for Sevensix (Japan e-commerce), in personalized recommendations and
significantly boosting customer engagement.
• Developed a Leather Defect Detection Model (ViT) for FC Company Japan, improving defect detection accuracy to 84%
• Designed and deployed Generative AI, LLM, agentic AI, and RAG systems for enterprise applications, enhancing automation and
decision-making. Engineered a Medical Diagnosis Chatbot with LangChain, LangGraph, and multi-agent architectures, enabling contextual
reasoning with 89% response accuracy on medical queries.
• Integrated OpenAI, Gemini, and LLaMA3 APIs into enterprise workflows, and deployments with cloud-native MLOps pipelines"""
        },
        {
            'title': 'Machine Learning Engineer',
            'company': 'Devolved AI',
            'location': 'Uttara,Dhaka,Bangladesh',
            'period': 'May 2023 - July 2024',
            'description': """ Developed and optimized ML pipelines for training & inference, fine-tuning LLMs for the Chatbot SRS Generator
• Built Luna, a decentralized AI chatbot leveraging LLMs & Generative AI with federated learning with 85% query resolution accuracy.
• Developed an AI-powered Prescription Handler with OCR/HTR + LLMs, automating prescription digitization and improving efficiency.
• Applied LoRA fine-tuning and distributed ML techniques to enhance scalability, robustness, and cost-effectiveness. """
            
        },
        {
            'title': 'Junior Machine Learning Engineer',
            'company': 'Devolved AI',
            'location': 'Uttara,Dhaka,Bangladesh',
            'period': 'Feb 2022 - April 2023',
            'description': """Implemented enterprise solutions for Prime’s Content Experiment Platform using Fastapi, MySQL, HTML, CSS, and JS.
• Designed and developed scalable systems for marketing optimization experiments.
• Gained early hands-on experience with AI model training and dataset-driven development."""
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





@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()

    name = data['name']
    email = data['email']
    subject = data['subject']
    message = data['message']

    full_message = f"""
    Name: {name}
    Email: {email}

    Message:
    {message}
    """

    msg = MIMEText(full_message)
    msg["Subject"] = subject
    msg["From"] = "alamintokdercse@gmail.com"
    msg["To"] = "alamintokdercse@gmail.com"

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("alamintokdercse@gmail.com", os.getenv("GMAIL_APP_PASSWORD"))
        server.sendmail(
            "alamintokdercse@gmail.com",
            "alamintokdercse@gmail.com",
            msg.as_string()
        )
        server.quit()

        return jsonify({"message": "Message sent successfully!"}), 200

    except Exception as e:
        print(e)
        return jsonify({"message": "Failed to send message"}), 500





if __name__ == '__main__':
    app.run(debug=True)


