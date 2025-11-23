import streamlit as st
import pandas as pd
import time
import random

st.set_page_config(layout="wide")

# ---------------- CSS Dark UI + Animation ----------------
st.markdown("""
<style>

.stApp {
    background: #0d1117;
    color: white;
}

/* card container */
.metric-card {
    background: #161b22;
    padding: 22px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0px 0px 12px rgba(0,0,0,0.45);
    transition: 0.3s;
}

.metric-card:hover {
    transform: translateY(-6px);
    box-shadow: 0px 0px 18px rgba(0,0,0,0.7);
}

/* pulse animation */
.pulse {
    animation: pulseAnim 1.8s infinite;
}

@keyframes pulseAnim {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

</style>
""", unsafe_allow_html=True)

# ---------------- Title ----------------
st.markdown("<h1 style='color:#58a6ff'>📊 Spam Classification Dashboard</h1>", unsafe_allow_html=True)

# ---------------- Top Cards ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='metric-card pulse'> <h3>Total Classified</h3><h2>3,482</h2></div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='metric-card pulse'> <h3>Total Spam</h3><h2>2,739</h2></div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='metric-card pulse'> <h3>Total Not Spam</h3><h2>743</h2></div>", unsafe_allow_html=True)


# ---------------- Activity Simulation ----------------
st.subheader("📈 Live Classification Activity")

placeholder = st.empty()

activity_data = []
labels = ["spam", "not spam"]

for _ in range(20):
    new_value = random.randint(5, 25)
    activity_data.append(new_value)

    placeholder.line_chart(activity_data)
    time.sleep(0.1)


# ---------------- Extra Stats ----------------
with st.expander("📌 Model Performance Summary"):
    st.write("""
    **Model** : MultinomailNB 
    **Training samples**: 50,000  
    **Vectorizer**: TF-IDF  
    ---
    - Accuracy: **97%**
    - Precision: **96%**
    
    """)




