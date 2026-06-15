import streamlit as st

from services.fraud_detector import FraudDetector

st.title("FraudGraph Brasil")

st.subheader(
    "Detecção Inteligente de Fraudes Digitais"
)

if st.button("Analisar Fraudes"):

    detector = FraudDetector()

    resultado = detector.detect_shared_devices()

    st.json(resultado)
