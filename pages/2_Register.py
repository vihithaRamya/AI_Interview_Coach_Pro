import streamlit as st
from backend.auth import register_user

# Load CSS
with open("assets/style.css", "r", encoding="utf-8") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.set_page_config(
    page_title="Register",
    page_icon="📝",
    layout="centered"
)

st.markdown("""
<div class="hero">
<h1>📝 Create Account</h1>
<h3>Start Your AI Interview Journey</h3>
</div>
""", unsafe_allow_html=True)

name = st.text_input("👤 Full Name")

email = st.text_input("📧 Email")

password = st.text_input(
    "🔒 Password",
    type="password"
)

confirm = st.text_input(
    "🔒 Confirm Password",
    type="password"
)

if st.button("🚀 Register"):

    if password != confirm:
        st.error("Passwords do not match!")

    elif name == "" or email == "" or password == "":
        st.warning("Please fill all fields.")

    else:

        success = register_user(
            name,
            email,
            password
        )

        if success:

            st.success(
                "Registration Successful 🎉"
            )

            st.balloons()

            st.info(
                "Please login to continue."
            )

            if st.button("➡️ Go to Login"):
                st.switch_page("pages/1_Login.py")

        else:

            st.error(
                "Email already exists."
            )

st.divider()

col1, col2 = st.columns(2)

with col1:

    if st.button("🏠 Home"):
        st.switch_page("app.py")

with col2:

    if st.button("🔐 Login"):
        st.switch_page("pages/1_Login.py")