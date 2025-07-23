# 💳 AI FraudShield

![Flask](https://img.shields.io/badge/Flask-2.3+-blue?logo=flask)
![Python](https://img.shields.io/badge/Made%20with-Python%203.x-yellow?logo=python)
![Scikit-learn](https://img.shields.io/badge/ML-Scikit--learn-orange?logo=scikit-learn)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

**AI FraudShield** is a Flask-based web application that detects fraudulent credit card transactions using a trained machine learning model. The app allows users to input key features extracted from transaction data and receive an instant prediction.

<br>

## 🚀 Features

- ⚠️ Predicts whether a transaction is **fraudulent** or **legitimate**
- 🧠 ML-powered classification using Scikit-learn
- 📊 Based on real-world anonymized credit card transaction data
- 🌐 Simple and responsive frontend with HTML/CSS
- 💡 Educational explanation of how the system works

<br>

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python, Flask
- **ML**: Scikit-learn, Pandas, NumPy
- **Deployment**: Flask built-in server (or deploy on Render, Heroku, etc.)

<br>

## 🧪 Model Training Overview
**Dataset:** Kaggle Credit Card Fraud Dataset (credit_data.csv)

**Preprocessing:**

- Removed duplicates

- Used only relevant features (V1–V28, Amount, Time)

- Balanced using stratified sampling

**Model:**

- Trained a Random Forest Classifier

-Achieved high precision and recall

**Exported Model:**

- Saved as fraud_model.pkl

**Training script:** train_model.py

<br>

## 🖥️ Preview 

![Legit Example](static/assets/preview1.png)
<br>
![Fraud Example](static/assets/preview2.png)

<br>

## 📂 Project Structure

credit-fraud-api/  
├── static/ 
|   ├── index.html 
|   ├── script.js  
│   └── assets/  
│       ├── fraud.png  
│       └── legit.png  
├── fraud_model.pkl  
├── train_model.py
├── main.py  
├── requirements.txt
├── LICENSE
└── README.md

<br>

## 🧪 Run Locally

1. **Clone the repo**
   
   git clone https://github.com/mahnoorimran563/ai-fraudshield.git
   cd ai-fraudshield
   
2. **Create virtual environment (optional but recommended)**

  python -m venv venv
  venv\Scripts\activate   # On Windows
  
3. **Install dependencies**

  pip install -r requirements.txt
  
4. **Run the Flask app**
   
  python app.py
  
5. **Open in browser**
   
  http://localhost:5000
  
<br>

🔒 License
This project is licensed under the MIT License.

<br>
🙋‍♀️ Author
Mahnoor Imran
💼 LinkedIn
📧 mahnoorimran563@gmail.com

Made with 💻 and ☕ by Mahnoor
