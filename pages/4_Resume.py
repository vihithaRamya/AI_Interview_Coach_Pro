# pages/4_Resume.py


import streamlit as st
from pypdf import PdfReader


from backend.style_loader import load_css
from backend.question_generator import generate_questions
from backend.gemini_ai import improve_resume



# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)



# ==================================================
# LOAD CSS THEME
# ==================================================

load_css()



# ==================================================
# SESSION INITIALIZATION
# ==================================================

if "resume_review" not in st.session_state:

    st.session_state.resume_review = ""


if "generated" not in st.session_state:

    st.session_state.generated = False


if "questions" not in st.session_state:

    st.session_state.questions = []



# ==================================================
# HEADER
# ==================================================

st.markdown(
"""
<div class="hero">

<h1>📄 AI Resume Analyzer</h1>

<h3>Smart Resume Analysis using Artificial Intelligence</h3>

<p>
Upload your resume and AI will analyze skills,
ATS score and generate personalized interview questions.
</p>

</div>
""",
unsafe_allow_html=True
)



st.write("")



# ==================================================
# RESUME UPLOAD
# ==================================================

uploaded_file = st.file_uploader(
    "📂 Upload Resume PDF",
    type=["pdf"]
)



if uploaded_file:


    # ----------------------------------------------
    # Read PDF
    # ----------------------------------------------

    reader = PdfReader(
        uploaded_file
    )


    resume_text = ""


    for page in reader.pages:

        text = page.extract_text()

        if text:

            resume_text += text



    if resume_text.strip()=="":


        st.error(
            "Unable to extract text from this PDF."
        )

        st.stop()



    # Save resume

    st.session_state.resume_text = resume_text



    st.success(
        "Resume uploaded successfully ✅"
    )



    # ==================================================
    # EXTRACTED TEXT
    # ==================================================

    st.subheader(
        "📌 Extracted Resume Content"
    )


    st.text_area(
        "Resume Text",
        resume_text,
        height=250
    )



    # ==================================================
    # SKILL DETECTION
    # ==================================================

    skills_list = [

        "Python",
        "Java",
        "C",
        "C++",
        "SQL",
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Django",
        "Spring Boot",
        "Machine Learning",
        "Artificial Intelligence",
        "AI",
        "Data Science",
        "MongoDB",
        "MySQL",
        "Git",
        "GitHub",
        "REST API",
        "Streamlit",
        "AWS",
        "Docker"

    ]



    found_skills = []



    for skill in skills_list:


        if skill.lower() in resume_text.lower():

            found_skills.append(skill)



    st.session_state.skills = found_skills



    st.subheader(
        "🛠 Skills Detected"
    )



    if found_skills:


        cols = st.columns(3)


        for i,skill in enumerate(found_skills):


            cols[i % 3].success(
                f"✅ {skill}"
            )


    else:


        st.warning(
            "No technical skills detected."
        )



    # ==================================================
    # ATS SCORE
    # ==================================================

    st.divider()


    st.subheader(
        "📊 ATS Resume Score"
    )



    ats_score = min(
        40 + len(found_skills)*5,
        100
    )



    st.metric(
        "ATS Score",
        f"{ats_score}/100"
    )



    # ==================================================
    # AI RESUME REVIEW
    # ==================================================

    st.divider()


    st.subheader(
        "🤖 AI Resume Review"
    )



    if st.button(
        "🤖 Analyze Resume with AI"
    ):


        with st.spinner(
            "Gemini is analyzing resume..."
        ):


            st.session_state.resume_review = improve_resume(
                resume_text
            )



    if st.session_state.resume_review:


        st.success(
            "Resume Analysis Completed ✅"
        )


        st.markdown(
            st.session_state.resume_review
        )



    # ==================================================
    # MISSING SKILLS
    # ==================================================

    st.divider()


    st.subheader(
        "💡 Recommended Skills"
    )



    missing_skills = [

        skill

        for skill in skills_list

        if skill not in found_skills

    ]



    for skill in missing_skills[:5]:


        st.info(
            skill
        )



    # ==================================================
    # QUESTION GENERATION
    # ==================================================

    st.divider()


    if st.button(
        "🚀 Generate AI Interview Questions"
    ):


        with st.spinner(
            "Generating questions..."
        ):


            questions = generate_questions(
                found_skills
            )


            st.session_state.questions = questions


            st.session_state.generated = True



        st.success(
            "Interview questions generated 🎉"
        )



    # ==================================================
    # SHOW QUESTIONS
    # ==================================================

    if st.session_state.generated:


        st.subheader(
            "🤖 Generated Questions"
        )


        for i,q in enumerate(
            st.session_state.questions,
            1
        ):


            st.write(
                f"{i}. {q}"
            )



        st.divider()



        if st.button(
            "🎤 Start AI Interview"
        ):


            st.switch_page(
                "pages/5_Interview.py"
            )



else:


    st.info(
        "📄 Please upload your resume to continue."
    )