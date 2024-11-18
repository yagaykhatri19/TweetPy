# TweetPy - Tweet Classification Web App
Imagine having a tool that understands tweets at a deeper level, sorting them into specific categories like News, Events, Opinions, Deals, and Private Messages. TweetPy is precisely that tool—a smart text classifier that helps categorize tweets to quickly understand their main purpose.

This project is a tweet classification web application built using Flask, machine learning models, and natural language processing (NLP) techniques.

## Table of Contents
- [Installation Guide](#installation-guide)
- [Running the Project](#running-the-project)
  - [Option 1: Running from GitHub](#option-1-running-from-github)
  - [Option 2: Running from a ZIP file](#option-2-running-from-a-zip-file)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [License](#license)

## Installation Guide

### Prerequisites
Make sure you have the following installed on your machine:
- Python 3.x (Preferably Python 3.8 or later)
- Git (for cloning from GitHub, if using Option 1)

## Running the Project

### Option 1: Running from GitHub
1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yagaykhatri19/TweetPy.git
   cd TweetPy

2. Create and activate a virtual environment (recommended):
   ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On Mac/Linux
    source venv/bin/activate

3. Install the required dependencies using requirements.txt:

   ```bash
    pip install -r requirements.txt

4. Run the Flask application:

   ```bash
    python app.py

Open your browser and visit http://127.0.0.1:5000/ to see the web application in action.

### Option 2: Running from a ZIP file
1. Download and unzip the project files.

2. Navigate to the project folder and create a virtual environment:
   ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On Mac/Linux
    source venv/bin/activate

3. Install the required dependencies using requirements.txt:

   ```bash
    pip install -r requirements.txt

4. Run the Flask application:

   ```bash
    python app.py

Open your browser and visit http://127.0.0.1:5000/ to see the web application in action.

## Technologies Used
- Flask: A micro web framework for building the web app.
- Scikit-learn: For machine learning algorithms (Logistic Regression, Naive Bayes, Ensemble Models).
- NLTK: For natural language processing tasks like tokenization, stopword removal, and lemmatization.
- NumPy: For numerical operations.
- Pandas: For data manipulation and preprocessing.
- Joblib: For saving and loading machine learning models.


---

**Signed**,  
Yagay Khatri
