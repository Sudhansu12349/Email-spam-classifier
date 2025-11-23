import streamlit as st
import numpy as np
import pandas as pd
import time
import altair as alt
import pickle
import datetime

# ---------------------------
# Load artifacts
# ---------------------------
with open("spam_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("spam_model.pkl", "rb") as f:
    model = pickle.load(f)


# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Email/sms Spam Classifier",
    layout="wide"
)


# ---------------------------
# Animated Background
# ---------------------------
st.markdown("""
<style>
body {
  background: linear-gradient(120deg,#e9f4ff,#f5faff,#e9f4ff);
  background-size: 300% 300%;
  animation: wave 14s ease infinite;
}
@keyframes wave {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
</style>
""", unsafe_allow_html=True)


# ---------------------------
# Detect suspicious words
# ---------------------------
SUSPICIOUS = ["free", "win", "click", "money", "offer", "urgent", "lucky", "prize", "credit", "loan"]


def highlight_suspicious_words(text):
    for word in SUSPICIOUS:
        text = text.replace(word, f"<b><span style='color:red'>{word}</span></b>")
        text = text.replace(word.upper(), f"<b><span style='color:red'>{word.upper()}</span></b>")
    return text


# ---------------------------
# Predict Email
# ---------------------------
def predict_email(text):
    X = vectorizer.transform([text])
    probs = model.predict_proba(X)[0]
    classes = list(model.classes_)

    # normalize class labels to lowercase string
    normalized = [str(c).lower().strip() for c in classes]

    # find spam index
    if "spam" in normalized:
        spam_idx = normalized.index("spam")
    elif "1" in normalized:
        spam_idx = normalized.index("1")
    elif "yes" in normalized:
        spam_idx = normalized.index("yes")
    else:
        # assume highest probability is spam
        spam_idx = int(np.argmax(probs))

    ham_idx = 1 - spam_idx

    spam_prob = float(probs[spam_idx])
    ham_prob = float(probs[ham_idx])

    if spam_prob >= 0.40:
            result = "🚨 SPAM"
    elif spam_prob >= 0.25:
            result = "⚠️ Suspicious Email"
    else:
        result = "✅ NOT SPAM"

    #label = "Spam" if spam_prob >= ham_prob else "Not Spam"

    return result, spam_prob, ham_prob



# ---------------------------
# Session state (history)
# ---------------------------
if "history" not in st.session_state:
    st.session_state.history = []


# ---------------------------
# UI
# ---------------------------
st.title("📧 Email Spam Classifier")

examples = {
    "Advertisement": "WIN FREE MONEY NOW!",
    "Job Offer": "We want to hire you. Apply today!",
    "Normal Conversation": "Let's meet tomorrow at the office."
}

st.markdown("#### Select Example Mail")
opt = st.selectbox("Choose:", ["None"] + list(examples.keys()))
default_text = examples[opt] if opt != "None" else ""

email = st.text_area("Paste email text:", default_text, height=220)


if st.button("Analyze Email", use_container_width=True):

    with st.spinner("Analyzing..."):
        time.sleep(1)
        label, spam_prob, ham_prob = predict_email(email)

    st.markdown("---")

    # update history
    st.session_state.history.append({
        "Email": email[:45]+"...",
        "Label": label,
        "Spam%": round(spam_prob*100,2),
        "Time": datetime.datetime.now().strftime("%H:%M:%S")
    })

    # result visual
    if label == "Spam":
        st.error(f"🚨 Prediction: **{label}**")
    else:
        st.success(f"✅ Prediction: **{label}**")


    # Threat level
    st.subheader("⚠ Threat Level")

    if spam_prob < 0.40:
        st.info("🟢 Low")
    elif spam_prob < 0.70:
        st.warning("🟡 Medium")
    else:
        st.error("🔴 HIGH")


    # Confidence
    st.subheader("🔥 Confidence Score")

    col1, col2 = st.columns(2)
    col1.metric("Spam Probability", f"{spam_prob*100:.2f}%")
    col2.metric("Not Spam Probability", f"{ham_prob*100:.2f}%")

    st.progress(int(spam_prob*100))


   

    chart_df = pd.DataFrame([
    {"Category":"Spam", "Score":spam_prob},
    {"Category":"Not Spam", "Score":ham_prob}
    ])

    chart = (
    alt.Chart(chart_df)
    .mark_arc(innerRadius=70)
    .encode(
        theta=alt.Theta("Score:Q"),
        color=alt.Color("Category:N"),
        tooltip=["Category","Score"]
    )
    )

    st.altair_chart(chart, use_container_width=True)



    # Explanation Panel
    st.subheader("🧾 Why this result?")
    st.write("""
    - Keyword similarity with spam emails  
    - Message formatting patterns  
    - Linguistic fraud indicators  
    - Frequency of promotional phrases  
    """)

    st.subheader("🔍 Suspicious Word Highlights")
    st.markdown(highlight_suspicious_words(email), unsafe_allow_html=True)



# HISTORY
st.markdown("---")
st.subheader("📜 Recent Activity")
st.table(st.session_state.history)


