import streamlit as st
import matplotlib.pyplot as plt

# Load CSS
with open("assets/style.css", "r", encoding="utf-8") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.set_page_config(
    page_title="Interview Report",
    page_icon="📑",
    layout="wide"
)

st.title("📑 AI Interview Report")

st.write("---")

user = st.session_state.get(
    "user",
    {"name":"Candidate"}
)

st.subheader(f"👤 Candidate : {user['name']}")

communication = st.session_state.get("communication",78)
technical = st.session_state.get("technical",82)
grammar = st.session_state.get("grammar",80)
confidence = st.session_state.get("confidence",84)

overall = int(
    (
        communication+
        technical+
        grammar+
        confidence
    )/4
)

if overall>=85:
    status="Highly Recommended ✅"
elif overall>=70:
    status="Recommended 👍"
else:
    status="Needs Improvement ⚠"

col1,col2=st.columns(2)

with col1:

    st.metric(
        "Overall Score",
        f"{overall}/100"
    )

with col2:

    st.metric(
        "Hiring Prediction",
        status
    )

st.write("---")

labels=[
    "Communication",
    "Technical",
    "Grammar",
    "Confidence"
]

scores=[
    communication,
    technical,
    grammar,
    confidence
]

fig=plt.figure(figsize=(7,4))

plt.bar(
    labels,
    scores
)

plt.ylim(0,100)

plt.ylabel("Score")

plt.title("Interview Performance")

st.pyplot(fig)

st.write("---")

fig2=plt.figure(figsize=(5,5))

plt.pie(
    scores,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Skill Distribution")

st.pyplot(fig2)

st.write("---")

st.subheader("⭐ Strengths")

st.success("""
✔ Good communication

✔ Positive attitude

✔ Strong technical fundamentals

✔ Confident during interview
""")

st.subheader("⚠ Areas to Improve")

st.warning("""
• Improve technical depth

• Practice HR questions

• Give shorter and clearer answers

• Add more real-world project examples
""")

st.subheader("🎯 Final Recommendation")

if overall>=85:

    st.success("""
Excellent performance.

You are ready for most fresher interviews.
""")

elif overall>=70:

    st.info("""
Good performance.

Practice a little more and you'll perform even better.
""")

else:

    st.error("""
You need more interview practice.

Work on communication and technical concepts.
""")

st.write("---")

if st.button("🏠 Back to Dashboard"):

    st.switch_page(
        "pages/3_Dashboard.py"
    )