import streamlit as st
import time


from backend.voice import (
    speak,
    record_voice,
    speech_to_text
)

from backend.gemini_ai import (
    evaluate_with_gemini,
    generate_ideal_answer
)

from backend.camera import (
    start_camera,
    stop_camera,
    get_camera_status
)


# ==============================
# PAGE CONFIG
# ==============================

st.set_page_config(
    page_title="AI Mock Interview",
    page_icon="🎤",
    layout="wide"
)


# ==============================
# SESSION INITIALIZATION
# ==============================

defaults = {

    "questions": [],

    "current_question": 0,

    "answers": [],

    "evaluations": [],

    "camera_started": False,

    "interview_started": False,

    "question_spoken": False,

    "voice_text": ""

}


for key,value in defaults.items():

    if key not in st.session_state:
        st.session_state[key] = value



# ==============================
# QUESTIONS CHECK
# ==============================

questions = st.session_state.questions


if not questions:

    st.warning("No questions available")

    st.info(
        "Please upload resume and generate questions first."
    )

    st.stop()



# ==============================
# START INTERVIEW
# ==============================

if not st.session_state.interview_started:


    st.title("🎤 AI Mock Interview")


    st.info(
        "Camera monitoring will start before interview."
    )


    if st.button("🚀 Start Interview"):


        start_camera()

        st.session_state.camera_started = True

        st.session_state.interview_started = True

        st.rerun()


    st.stop()



# ==============================
# COMPLETED
# ==============================

index = st.session_state.current_question


if index >= len(questions):


    stop_camera()


    st.success(
        "🎉 Interview Completed"
    )


    if st.button("📊 View Report"):

        st.switch_page(
            "pages/6_Report.py"
        )


    st.stop()



# ==============================
# CURRENT QUESTION
# ==============================

question = questions[index]


st.title(
    "🎤 AI Mock Interview"
)


st.write(
    f"Question {index+1}/{len(questions)}"
)



# ==============================
# CAMERA
# ==============================

st.subheader(
    "📷 Camera Monitoring"
)


if st.session_state.camera_started:


    status = get_camera_status()


    if not status.get("camera_open",False):

        st.error(
            "❌ Camera not opened"
        )


    elif status.get("multiple_faces",False):

        st.warning(
            "⚠️ Multiple faces detected"
        )


    elif status.get("face",False):

        st.success(
            "🙂 Face detected"
        )


    else:

        st.warning(
            "⚠️ Face not detected"
        )


    st.caption(
        f"Frames monitored: {status.get('frames',0)}"
    )





# ==============================
# QUESTION
# ==============================

st.subheader(
    "🤖 Interview Question"
)


st.info(question)



# ==============================
# QUESTION VOICE
# ==============================

if not st.session_state.question_spoken:

    speak(question)

    st.session_state.question_spoken = True



if st.button("🔊 Listen Again"):

    speak(question)




# ==============================
# ANSWER
# ==============================

st.subheader(
    "✍️ Your Answer"
)


answer_key = f"answer_{index}"


if answer_key not in st.session_state:

    st.session_state[answer_key] = ""



answer = st.text_area(

    "Type your answer",

    height=180,

    key=answer_key

)





# ==============================
# VOICE ANSWER
# ==============================

if st.button(
    "🎤 Answer Using Voice"
):


    audio_file = record_voice(
        duration=10
    )


    if audio_file:


        text = speech_to_text(
            audio_file
        )


        st.session_state[answer_key] = text


        st.rerun()





# ==============================
# SUBMIT
# ==============================

if st.button(
    "✅ Submit Answer"
):


    final_answer = st.session_state[answer_key].strip()


    if final_answer == "":


        st.error(
            "Please enter answer"
        )


    else:


        with st.spinner(
            "🤖 AI analysing answer..."
        ):


            result = evaluate_with_gemini(

                question,

                final_answer

            )


        st.session_state.answers.append(
            final_answer
        )


        st.session_state.evaluations.append(
            result
        )


        st.success(
            "Evaluation completed"
        )


        st.markdown(result)





# ==============================
# IDEAL ANSWER
# ==============================

with st.expander(
    "💡 View Ideal Answer"
):

    st.write(
        generate_ideal_answer(question)
    )





# ==============================
# NEXT QUESTION
# ==============================

st.divider()


col1,col2 = st.columns(2)



with col1:


    if st.button(
        "➡️ Next Question"
    ):


        # remove current answer

        del st.session_state[answer_key]


        st.session_state.current_question += 1


        st.session_state.question_spoken = False


        st.rerun()



# ==============================
# QUIT
# ==============================

with col2:


    if st.button(
        "🛑 Quit Interview"
    ):


        stop_camera()


        st.success(
            "Interview stopped"
        )


        time.sleep(1)


        st.switch_page(
            "pages/6_Report.py"
        )