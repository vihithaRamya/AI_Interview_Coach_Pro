import streamlit as st
import sounddevice as sd
import scipy.io.wavfile as wav
import speech_recognition as sr
import pyttsx3
import os
import time


# ==========================================
# TEXT TO SPEECH
# ==========================================

def speak_text(text):

    try:

        engine = pyttsx3.init()


        # Voice speed
        engine.setProperty(
            "rate",
            150
        )


        # Volume
        engine.setProperty(
            "volume",
            1.0
        )


        engine.say(
            text
        )


        engine.runAndWait()



    except Exception as e:

        st.error(
            f"Text to Speech Error: {e}"
        )




# ==========================================
# INTERVIEW PAGE VOICE FUNCTION
# ==========================================

def speak(text):

    """
    Used to speak AI interview questions
    """

    speak_text(text)




# ==========================================
# RECORD USER ANSWER
# ==========================================

def record_voice(duration=10):

    try:


        st.info(
            "🎤 Recording started... Speak now"
        )


        sample_rate = 44100



        # Create recordings folder

        os.makedirs(
            "recordings",
            exist_ok=True
        )



        file_path = os.path.join(
            "recordings",
            f"answer_{int(time.time())}.wav"
        )



        recording = sd.rec(

            int(duration * sample_rate),

            samplerate=sample_rate,

            channels=1

        )



        sd.wait()



        wav.write(

            file_path,

            sample_rate,

            recording

        )



        st.success(
            "✅ Recording completed"
        )



        return file_path



    except Exception as e:


        st.error(
            f"Recording Error: {e}"
        )


        return None




# ==========================================
# SPEECH TO TEXT
# ==========================================

def speech_to_text(audio_file):

    try:


        recognizer = sr.Recognizer()



        # Better Indian English recognition

        recognizer.energy_threshold = 300

        recognizer.pause_threshold = 1



        with sr.AudioFile(audio_file) as source:


            audio = recognizer.record(
                source
            )



        text = recognizer.recognize_google(

            audio,

            language="en-IN"

        )



        return text




    except sr.UnknownValueError:


        return "Could not understand voice"



    except sr.RequestError:


        return "Speech recognition service unavailable"



    except Exception as e:


        return f"Voice conversion error: {e}"





# ==========================================
# VOICE TEST
# ==========================================

def test_voice():

    speak_text(
        "Hello Vihitha. AI Interview Coach voice testing is successful."
    )



# ==========================================
# RUN DIRECTLY FOR TESTING
# ==========================================

if __name__ == "__main__":


    test_voice()