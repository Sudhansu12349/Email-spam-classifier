Email Spam Classifier —
This project is a machine learning-based Email Spam Classifier that predicts whether an email is Spam or Not Spam based on the text entered by the user.
The project uses Natural Language Processing (NLP) techniques and a Multinomial Naive Bayes model.

Project Overview
The goal of this project is to classify email text into two categories:
   Spam (1)
   Not Spam (0)

   It does this by analyzing the content of the email, not the sender address.

Technologies Used

Python
Pandas, NumPy
NLTK (for stopwords + stemming)
Scikit-Learn (for TF-IDF + Naive Bayes)
Joblib (to save model)
Streamlit (for UI / Deployment)

 Workflow

1. Data Preprocessing
   Convert text to lowercase
   Remove special characters
   Remove stopwords
   Apply stemming
   Create a cleaned version of each email

2. Feature Extraction

Using TF-IDF Vectorizer with max_features = 3000.

3. Model Training
   Algorithm: Multinomial Naive Bayes
   Train-test split: 80% training, 20% testing
   Achieved accuracy: 95–97%

4. Saving the Model

   Model and vectorizer saved using joblib:
   spam_model.pkl
   spam_vectorizer.pkl

6. Streamlit Application

A simple UI to test the classifier:
Paste an email
Click “Classify Email”
See result: Spam or Not Spam


How to Run Locally

Install requirements:
pip install -r requirements.txt

Run Streamlit:
streamlit run app.py
Paste email text and test.


Deployment (Streamlit Cloud)

Push project to GitHub

Go to https://share.streamlit.io

Select your repo and app.py

Deploy instantly

 Example Inputs

Spam example:

Congratulations! You have won $5000 gift voucher. Click here to claim.


Not spam example:

Please find the meeting agenda attached for tomorrow's session.

 
Project Files

app.py — Streamlit UI
train_model.py — Training script
spam_model.pkl — Trained model
spam_vectorizer.pkl — Saved vectorizer
requirements.txt — Dependencies

README.md — Project documentation

 Conclusion

This project successfully demonstrates:

Text preprocessing
NLP feature extraction
ML classification
Deploying a real ML app
