import streamlit as st

st.set_page_config(
    page_title="Email Spam Classifier",
    layout="wide",
)

# --------------------------------
# CSS HERO ANIMATION
# --------------------------------
st.markdown("""
<style>

.stApp {
    background-color: #0d1117;
    color: #fff;
}

.hero-box {
    width: 100%;
    padding: 60px;
    border-radius: 18px;
    background: linear-gradient(135deg, #1f2937, #111827);
    animation: glow 4s infinite alternate;
    text-align: center;
    margin-top: 40px;
    box-shadow: 0 0 24px rgba(0,0,0,0.6);
}

@keyframes glow {
    from { box-shadow: 0 0 15px rgba(0,180,255,0.35); }
    to { box-shadow: 0 0 35px rgba(0,180,255,0.85); }
}

.tagline {
    font-size: 22px;
    margin-top: -12px;
    opacity: 0.78;
}

.feature-box {
    background: rgba(255,255,255,0.05);
    padding: 14px;
    border-radius: 12px;
    text-align: center;
    transition: 0.3s;
}

.feature-box:hover {
    transform: translateY(-6px);
    background: rgba(255,255,255,0.12);
}

</style>
""", unsafe_allow_html=True)

# --------------------------------
# HERO SECTION
# --------------------------------

st.markdown(f"""
    <div class="hero-box">
        <h1>📧 AI Email Spam Classifier</h1>
        <p class="tagline">Machine Learning powered Spam Detection with 97% accuracy</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("")

# --------------------------------
# FEATURES GRID
# --------------------------------

st.markdown("## 🚀 Key Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""<div class='feature-box'>🔍 Real-time Prediction</div>""", unsafe_allow_html=True)

with col2:
    st.markdown("""<div class='feature-box'>📈 Confidence Scoring</div>""", unsafe_allow_html=True)

with col3:
    st.markdown("""<div class='feature-box'>🧠 Machine Learning Model</div>""", unsafe_allow_html=True)

colA, colB, colC = st.columns(3)

with colA:
    st.markdown("""<div class='feature-box'>✉ Dataset Trained</div>""", unsafe_allow_html=True)

with colB:
    st.markdown("""<div class='feature-box'>🌐 Streamlit UI</div>""", unsafe_allow_html=True)

with colC:
    st.markdown("""<div class='feature-box'>📊 Analytics Dashboard</div>""", unsafe_allow_html=True)



st.markdown("---")

st.caption("Minor Project | Department of Computer Science")
