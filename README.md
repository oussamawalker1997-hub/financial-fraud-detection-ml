# 🛡️ Système de Détection de Fraude Financière

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-green)

## 📌 Business Context
Financial fraud costs billions every year. This project is an interactive microservice that detects in real time whether a transaction is legitimate or fraudulent.

## 🧠 Technical Architecture
*   **Model:** Decision tree algorithm (Random Forest).
*   **Data Handling:** Uses SMOTE to address the massive imbalance between normal and fraudulent transactions.
*   **Interface:** Deployed via Streamlit to make the machine learning model accessible to business teams.

## 🚀 Local Launch
1. Install dependencies: `pip install -r requirements.txt`
2. Run the application: `streamlit run app.py`

## 🤝 Credits
The modeling architecture and data analysis are inspired by the open-source work of [nageshsinghc4](https://github.com/nageshsinghc4/Fraud-Detection). The code has been adapted and integrated to simulate a production deployment via Streamlit.
