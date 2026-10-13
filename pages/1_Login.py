import streamlit as st

from backend.style_loader import load_css
from backend.auth import login_user


# ---------------------------------
# Page Configuration (FIRST)
# ---------------------------------

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="centered"
)


# ---------------------------------
# Load Theme
# ---------------------------------

load_css()



# ---------------------------------
# Session
# ---------------------------------

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False



# ---------------------------------
# Login UI
# ---------------------------------

st.markdown(
"""
<div class="hero">

<h1>🔐 Login</h1>

<h3>Welcome Back!</h3>

<p>
Login to continue your AI Interview Journey
</p>

</div>
""",
unsafe_allow_html=True
)


st.write("")


# ---------------------------------
# Input Fields
# ---------------------------------

email = st.text_input(
    "📧 Email"
)


password = st.text_input(
    "🔒 Password",
    type="password"
)



st.write("")


# ---------------------------------
# Login Button
# ---------------------------------

if st.button("🚀 Login"):


    if email == "" or password == "":

        st.warning(
            "Please enter email and password"
        )


    else:


        user = login_user(
            email,
            password
        )


        if user:


            st.session_state.logged_in = True

            st.session_state.user = user


            st.success(
                f"Welcome {user['name']} 🎉"
            )


            st.balloons()


            st.switch_page(
                "pages/3_Dashboard.py"
            )


        else:


            st.error(
                "Invalid Email or Password"
            )



# ---------------------------------
# Navigation Buttons
# ---------------------------------

st.divider()


col1,col2 = st.columns(2)



with col1:


    if st.button("🏠 Home"):

        st.switch_page(
            "app.py"
        )



with col2:


    if st.button("📝 Register"):

        st.switch_page(
            "pages/2_Register.py"
        )