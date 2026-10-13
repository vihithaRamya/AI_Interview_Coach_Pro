import streamlit as st
from backend.style_loader import load_css

# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="AI Interview Coach Pro",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------
# Load CSS
# -----------------------------------

load_css()

# -----------------------------------
# Hero Section
# -----------------------------------

st.markdown(
"""
<div class="hero">

<h1>🤖 AI Interview Coach Pro</h1>

<h3>Master Every Interview with Artificial Intelligence</h3>

<p>
Prepare smarter with AI-powered Resume Analysis,
Mock Interviews, Voice Interview, Camera Monitoring,
ATS Score and Performance Reports.
</p>

</div>
""",
unsafe_allow_html=True
)

st.write("")

# -----------------------------------
# Feature Cards
# -----------------------------------

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
    """
    <div class="feature-box">

    <h3>📄 Resume Analysis</h3>

    ✔ ATS Resume Score<br>
    ✔ Skill Detection<br>
    ✔ Missing Skills<br>
    ✔ Resume Suggestions<br>
    ✔ AI Generated Questions

    </div>
    """,
    unsafe_allow_html=True
    )

with col2:

    st.markdown(
    """
    <div class="feature-box">

    <h3>🎤 AI Mock Interview</h3>

    ✔ HR Questions<br>
    ✔ Technical Questions<br>
    ✔ Voice Interview<br>
    ✔ Camera Monitoring<br>
    ✔ AI Evaluation

    </div>
    """,
    unsafe_allow_html=True
    )

with col3:

    st.markdown(
    """
    <div class="feature-box">

    <h3>📊 Performance Report</h3>

    ✔ Overall Score<br>
    ✔ Communication Score<br>
    ✔ Technical Score<br>
    ✔ Grammar Score<br>
    ✔ Hiring Prediction

    </div>
    """,
    unsafe_allow_html=True
    )

st.write("")
st.divider()

# -----------------------------------
# Workflow
# -----------------------------------

st.markdown("## 🚀 AI Interview Workflow")

workflow_col1, workflow_col2 = st.columns(2)

with workflow_col1:

    st.success("1️⃣ Register")
    st.success("2️⃣ Login")
    st.success("3️⃣ Dashboard")
    st.success("4️⃣ Upload Resume")

with workflow_col2:

    st.success("5️⃣ Resume Analysis")
    st.success("6️⃣ AI Interview")
    st.success("7️⃣ Performance Report")
    st.success("8️⃣ Thank You")

st.divider()

# -----------------------------------
# Why Choose
# -----------------------------------

st.markdown("## ⭐ Why Choose AI Interview Coach Pro?")

left, right = st.columns(2)

with left:

    st.info("✅ AI Powered Resume Analysis")
    st.info("✅ ATS Resume Score")
    st.info("✅ Resume Improvement Suggestions")
    st.info("✅ Personalized Questions")
    st.info("✅ Voice Enabled Interview")

with right:

    st.info("✅ Camera Monitoring")
    st.info("✅ AI Feedback")
    st.info("✅ Hiring Prediction")
    st.info("✅ Performance Dashboard")
    st.info("✅ Download Report")

st.divider()

# -----------------------------------
# Project Modules
# -----------------------------------

st.markdown("## 📚 Project Modules")

module1, module2 = st.columns(2)

with module1:

    st.markdown("""
- 🔐 Login
- 📝 Register
- 🏠 Dashboard
- 📄 Resume Analysis
""")

with module2:

    st.markdown("""
- 🎤 AI Interview
- 📊 Report
- 🤖 AI Chat
- ❤️ Thank You
""")

st.divider()

# -----------------------------------
# Navigation Buttons
# -----------------------------------

st.markdown("## 🚀 Get Started")

c1, c2 = st.columns(2)

with c1:

    if st.button("📝 Register"):

        st.switch_page("pages/2_Register.py")

with c2:

    if st.button("🔐 Login"):

        st.switch_page("pages/1_Login.py")

st.write("")
st.divider()

# -----------------------------------
# Footer
# -----------------------------------

st.markdown(
"""
<center>

### 🤖 AI Interview Coach Pro

AI Powered Resume Analysis • AI Interview • Voice Interview • Camera Monitoring • Reports

Made with ❤️ using Streamlit + Python + Gemini AI

© 2026 AI Interview Coach Pro

</center>
""",
unsafe_allow_html=True
)