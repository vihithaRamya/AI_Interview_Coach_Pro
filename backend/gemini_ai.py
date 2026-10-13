# backend/gemini_ai.py


import os
from dotenv import load_dotenv

import google.generativeai as genai



# ==================================================
# GEMINI CONFIGURATION
# ==================================================

load_dotenv()


API_KEY = os.getenv("GEMINI_API_KEY")


if API_KEY:

    genai.configure(
        api_key=API_KEY
    )


# Fast Gemini Model

model = genai.GenerativeModel(
    "gemini-2.0-flash"
)



# ==================================================
# RESUME ANALYSIS
# ==================================================

def improve_resume(resume_text):

    try:


        # Limit input size
        resume_text = resume_text[:5000]


        prompt = f"""

You are an expert ATS resume reviewer.

Analyze this fresher resume.


Resume:

{resume_text}


Provide:

1. Resume Strengths

2. Missing Skills

3. ATS Improvement Tips

4. Technical Improvements

5. Formatting Suggestions

6. Interview Preparation Tips


Give only clear bullet points.
Keep answer under 500 words.

"""


        response = model.generate_content(

            prompt,

            generation_config={

                "temperature":0.2,

                "max_output_tokens":500

            }

        )


        if response.text:

            return response.text


        else:

            return local_resume_analysis(
                resume_text
            )


    except Exception as e:


        return f"""

# 📄 Resume Review


Gemini analysis unavailable.


## Local AI Analysis


{local_resume_analysis(resume_text)}



Error:

{e}

"""





# ==================================================
# LOCAL RESUME ANALYSIS FALLBACK
# ==================================================

def local_resume_analysis(resume_text):


    text = resume_text.lower()


    strengths=[]

    improvements=[]


    skills=[

        "python",

        "java",

        "sql",

        "react",

        "spring boot",

        "machine learning",

        "aws",

        "django",

        "streamlit"

    ]


    found=[]


    for skill in skills:


        if skill in text:

            found.append(skill)



    if found:


        strengths.append(

            "Technical skills detected: "

            + ", ".join(found)

        )



    if "project" in text:


        strengths.append(

            "Projects are included in resume"

        )

    else:


        improvements.append(

            "Add more project details"

        )



    if "certification" in text:


        strengths.append(

            "Certifications are mentioned"

        )



    else:


        improvements.append(

            "Add relevant certifications"

        )



    if "github" not in text:


        improvements.append(

            "Add GitHub links for projects"

        )



    improvements.append(

        "Add measurable achievements"

    )




    return f"""

# 📄 Resume Review



## ✅ Strengths


{chr(10).join("• "+x for x in strengths)}



## 🔧 Improvements


{chr(10).join("• "+x for x in improvements)}



## 🎯 ATS Suggestions


• Add job related keywords

• Keep resume format simple

• Highlight technical skills

• Add project achievements

"""





# ==================================================
# INTERVIEW ANSWER EVALUATION
# ==================================================

def evaluate_with_gemini(question, answer):


    try:


        prompt=f"""

You are a strict technical interviewer.


Question:

{question}


Candidate Answer:

{answer}


Evaluate ONLY this answer.


Give:

Overall Score /100

Communication Score /100

Technical Knowledge Score /100

Confidence Score /100

Grammar Score /100


Strengths

Areas To Improve

Suggestions


Do not give fixed scores.
Score based on answer quality.

"""


        response=model.generate_content(

            prompt,

            generation_config={

                "temperature":0.1,

                "max_output_tokens":600

            }

        )


        return response.text



    except Exception:


        return smart_evaluation(

            question,

            answer

        )





# ==================================================
# SMART LOCAL EVALUATION
# ==================================================

def smart_evaluation(question, answer):


    q = question.lower()

    a = answer.lower()



    if len(a.strip()) < 5:


        return create_zero_score(

            "No proper answer provided"

        )



    wrong=[

        "i don't know",

        "dont know",

        "no idea",

        "nothing",

        "not sure"

    ]



    for w in wrong:


        if w in a:


            return create_zero_score(

                "Answer is not relevant"

            )



    score=0



    keywords=[]



    if "yourself" in q:


        keywords=[

            "education",

            "skills",

            "project",

            "technology"

        ]



    elif "project" in q:


        keywords=[

            "project",

            "technology",

            "developed"

        ]



    elif "hire" in q:


        keywords=[

            "skills",

            "learn",

            "contribute"

        ]



    else:


        keywords=q.split()



    matched=0


    for k in keywords:


        if k in a:

            matched+=1



    if matched:

        score += int(

            (matched/len(keywords))*70

        )



    if len(answer.split())>50:


        score+=20



    if "example" in a:


        score+=10



    score=min(score,100)




    strengths=[]

    improvements=[]



    if score>=70:


        strengths.append(

            "Answer is relevant"

        )


    if score>=80:


        strengths.append(

            "Good explanation provided"

        )



    if score<50:


        improvements.append(

            "Provide more technical details"

        )



    improvements.append(

        "Include practical examples"

    )




    return f"""

# 📊 AI Evaluation


## Overall Score: {score}/100


## Communication Score: {score}/100


## Technical Knowledge Score: {score}/100


## Confidence Score: {score}/100


## Grammar Score: {score}/100



## ✅ Strengths


{chr(10).join("• "+x for x in strengths) if strengths else "No strengths found."}



## 🔧 Areas To Improve


{chr(10).join("• "+x for x in improvements)}





## 💡 Suggestions


• Use STAR method

• Explain your role clearly

• Add examples

"""





# ==================================================
# ZERO SCORE
# ==================================================

def create_zero_score(reason):


    return f"""

# 📊 AI Evaluation


## Overall Score: 0/100


## Communication Score: 0/100


## Technical Knowledge Score: 0/100


## Confidence Score: 0/100


## Grammar Score: 0/100



## ❌ Strengths

No strengths found.



## 🔧 Areas To Improve

• Understand the question

• Provide relevant answer



## 💡 Suggestions

• Practice interview questions

• Give structured answers



Reason:

{reason}

"""





# ==================================================
# IDEAL ANSWER
# ==================================================

def generate_ideal_answer(question):


    q=question.lower()



    if "yourself" in q:


        return """

I am a Computer Science student.

I have knowledge in programming,
databases and AI technologies.

I have completed projects where I applied my technical skills.

I am a quick learner and interested in contributing to your organization.

"""



    elif "project" in q:


        return """

My project is AI Interview Coach.

It helps candidates prepare for interviews by analyzing resumes,
generating questions and evaluating answers using AI.

The project uses Python, Streamlit and Gemini AI.

"""



    elif "hire" in q:


        return """

You should hire me because I have strong technical fundamentals,
learning ability and problem-solving skills.

I am ready to learn new technologies and contribute to the company.

"""



    else:


        return """

A good answer should include:

• Introduction

• Explanation

• Example

• Conclusion

"""