import streamlit as st

# Load CSS
with open("assets/style.css", "r", encoding="utf-8") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# Check Login
if "logged_in" not in st.session_state:

    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.warning("Please login first.")

    if st.button("🔐 Go to Login"):

        st.switch_page("pages/1_Login.py")

    st.stop()


user = st.session_state.get(
    "user",
    {
        "name":"User"
    }
)

st.markdown(f"""
<div class="hero">

<h1>👋 Welcome {user['name']}</h1>

<h3>Your Personal AI Interview Dashboard</h3>

</div>
""",
unsafe_allow_html=True)

st.write("")

# --------------------------

col1,col2,col3,col4 = st.columns(4)

with col1:

    st.markdown("""

<div class="feature-box">

<h3>📄 Resume</h3>

Upload Resume

ATS Analysis

</div>

""",unsafe_allow_html=True)

with col2:

    st.markdown("""

<div class="feature-box">

<h3>🎤 Interview</h3>

Practice Interview

</div>

""",unsafe_allow_html=True)

with col3:

    st.markdown("""

<div class="feature-box">

<h3>📊 Progress</h3>

Track Performance

</div>

""",unsafe_allow_html=True)

with col4:

    st.markdown("""

<div class="feature-box">

<h3>📑 Reports</h3>

Download Report

</div>

""",unsafe_allow_html=True)

st.divider()

st.subheader("🚀 Quick Actions")

col1,col2=st.columns(2)

with col1:

    if st.button("📄 Resume Analyzer"):

        st.switch_page("pages/4_Resume.py")

with col2:

    if st.button("🎤 Start Interview"):

        st.switch_page("pages/5_Interview.py")

st.divider()

st.subheader("📈 Interview Progress")

questions = st.session_state.get(
    "question_no",
    0
)

total = len(
    st.session_state.get(
        "questions",
        [
            1,2,3,4,5,6,7
        ]
    )
)

score = 0

if "scores" in st.session_state:

    if len(st.session_state.scores)>0:

        score = sum(
            st.session_state.scores
        )/len(
            st.session_state.scores
        )

st.progress(
    questions/total
)

c1,c2=st.columns(2)

with c1:

    st.metric(
        "Questions Completed",
        f"{questions}/{total}"
    )

with c2:

    st.metric(
        "Average Score",
        f"{score:.0f}/100"
    )

st.divider()

col1,col2=st.columns(2)

with col1:

    if st.button("🏠 Home"):

        st.switch_page("app.py")

with col2:

    if st.button("🚪 Logout"):

        st.session_state.logged_in=False

        st.switch_page("pages/1_Login.py")
with col3:

    if st.button("🤖 AI Chat Assistant"):

        st.switch_page(
            "pages/7_AI_Chat.py"
        )