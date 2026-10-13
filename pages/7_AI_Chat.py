import streamlit as st
from backend.gemini_ai import model

# Load CSS
with open("assets/style.css", "r", encoding="utf-8") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.set_page_config(
    page_title="AI Interview Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Interview Assistant")

st.write(
    "Ask anything about interviews, programming, HR questions, resume or career."
)

st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input(
    "Ask anything..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = model.generate_content(
                f"""
You are an expert AI Interview Coach.

Answer professionally and simply.

Question:
{prompt}
"""
            )

            answer = response.text

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )

st.divider()

col1,col2 = st.columns(2)

with col1:

    if st.button("📊 Dashboard"):
        st.switch_page("pages/3_Dashboard.py")

with col2:

    if st.button("🎤 Interview"):
        st.switch_page("pages/5_Interview.py")