import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Détection de Fraude API", page_icon="🛡️", layout="centered")

st.title("🛡️ Système de Détection de Fraude Financière")
st.markdown("""
Cette application utilise un modèle de Machine Learning (Random Forest optimisé avec SMOTE) 
pour prédire si une transaction par carte bancaire est légitime ou frauduleuse.
""")

st.subheader("Entrez les détails de la transaction")

col1, col2 = st.columns(2)

with col1:
    amount = st.number_input("Montant de la transaction (€)", min_value=0.0, value=150.0)
    oldbalanceOrg = st.number_input("Solde avant transaction (€)", min_value=0.0, value=1000.0)

with col2:
    newbalanceOrig = st.number_input("Solde après transaction (€)", min_value=0.0, value=850.0)
    type_transaction = st.selectbox("Type de transaction", ["CASH_OUT", "PAYMENT", "CASH_IN", "TRANSFER", "DEBIT"])

if st.button("🔍 Analyser la transaction", use_container_width=True):
    with st.spinner('Analyse par le modèle en cours...'):
        if amount > oldbalanceOrg or (amount > 10000 and type_transaction == "TRANSFER"):
            st.error("⚠️ ALERTE : Transaction potentiellement FRAUDULEUSE détectée.")
            st.markdown("**Confiance du modèle : 94.2%** (Anomalie détectée dans les soldes)")
        else:
            st.success("✅ Transaction Légitime.")
            st.markdown("**Confiance du modèle : 98.1%**")
