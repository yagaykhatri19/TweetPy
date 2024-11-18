from flask import Flask, render_template, redirect, request
import joblib
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
import numpy as np

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

app = Flask(__name__)

ml_model = joblib.load('ensemble_model.pkl')
tfidf_vectorizer = joblib.load('tweet_tfidf_vectorizer.pkl')

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)
    text = re.sub(r"[^a-z0-9\s]", "", text)
    words = nltk.word_tokenize(text)
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return " ".join(words)

def get_top_categories(model, vectorizer, input_text, top_n=5):
    input_tfidf = vectorizer.transform([input_text]) 
    probabilities = model.predict_proba(input_tfidf)[0]  
    top_indices = np.argsort(probabilities)[-top_n:][::-1]  
    top_categories = [(model.classes_[i], probabilities[i]) for i in top_indices]  
    return top_categories

# ENDPOINTS
@app.route('/')
def main():
    return render_template('dashboard.html')

@app.route('/info')
def information():
    return render_template('information.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/classify', methods=['GET', 'POST'])
def classify():
    if request.method == 'POST':
        text = request.form.get('text', '')
        if not text:
            return render_template('dashboard.html', error='Enter text.')

        processed_text = preprocess_text(text)

        top_categories = get_top_categories(ml_model, tfidf_vectorizer, processed_text, top_n=3)
             
        return render_template(
            'classify.html',
            text=text,
            top_categories=top_categories
        )
    return render_template('classify.html')

if __name__ == '__main__':
    app.run(debug=True)
