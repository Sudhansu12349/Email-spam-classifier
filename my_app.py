import streamlit as st
import joblib
import re
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

stop_words = {
    'a','an','the','and','or','is','am','are','was','were','be','been','to','for','in','on','at',
    'this','that','of','with','from','as','by','it','you','we','they','he','she','but','if','not'
}

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    tokens = text.split()
    tokens = [ps.stem(w) for w in tokens if w not in stop_words]
    return " ".join(tokens)

# Load model
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("spam_vectorizer.pkl")

# ---- Page Config ----
st.set_page_config(
    page_title="Email Spam Classifier",
    page_icon="📧",
    layout="centered",
)

# ---- Pure White Background CSS ----
st.markdown("""
    <style>
    /* Main page background */
    .stApp {
        background-color: white !important;
    }

    /* Remove grey from blocks/containers */
    .stMarkdown, .stTextArea, .stButton, .stAlert {
        background-color: white !important;
    }

    /* Center heading */
    .main-title {
        font-size: 40px;
        text-align: center;
        color: #222;
        font-weight: 700;
        margin-bottom: 0.5em;
    }
    .sub-title {
        font-size: 18px;
        text-align: center;
        color: #555;
        margin-bottom: 1.5em;
    }

    .result-box {
        padding: 20px;
        border-radius: 12px;
        margin-top: 20px;
        font-size: 20px;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# ---- UI ----
st.markdown("<div class='main-title'>📧 Email Spam Classifier</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Detect whether an email is Spam or Not Spam using Machine Learning</div>", unsafe_allow_html=True)

email_text = st.text_area("Enter Email Content:", height=200)

if st.button("Classify Email", use_container_width=True):
    if email_text.strip() == "":
        st.warning("Please enter some email text.")
    else:
        cleaned_text = clean_text(email_text)     # must exist here
        transformed = vectorizer.transform([cleaned_text])
        prediction = model.predict(transformed)[0]

        if prediction == 1:
            st.error("🚨 Spam Email Detected")
        else:
            st.success("✅ Not Spam")


        if prediction == 1:
            st.markdown(
                "<div class='result-box' style='background-color:#ffe1e1; color:#b30000;'>🚨 Spam Email Detected</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                "<div class='result-box' style='background-color:#e1ffe4; color:#0f730c;'>✅ Not Spam</div>",
                unsafe_allow_html=True
            )

st.markdown("<br><center style='color:#777;'>Minor Project • Machine Learning • 2025</center>", unsafe_allow_html=True)


