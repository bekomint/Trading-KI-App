# trading_ai_app.py

import streamlit as st
from PIL import Image
import random

# --- Seite konfigurieren ---
st.set_page_config(
    page_title="Trading-KI Analyse",
    layout="wide",
    page_icon="📈"
)

# --- Farben und Styles ---
TREND_COLORS = {
    "Aufwärts": "green",
    "Abwärts": "red",
    "Seitwärts": "orange"
}

st.markdown("""
<style>
body {
    background-color: #1E1E2F;
    color: #FFFFFF;
}
.stButton>button {
    background-color: #4B6EF6;
    color: white;
    font-weight: bold;
    border-radius: 8px;
    padding: 8px 16px;
}
.stButton>button:hover {
    background-color: #3A5EE0;
}
.stFileUploader>div {
    background-color: #2C2C3C;
    border-radius: 8px;
    padding: 8px;
}
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.title("📈 Trading-KI Analyse")
st.markdown("Lade ein Chart hoch oder gib ein Symbol ein, und die KI analysiert den Trend, Einstieg, SL & TP.")

# --- Upload oder Symbol ---
col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("📤 Chart-Bild hochladen", type=["png", "jpg", "jpeg"])

with col2:
    symbol_input = st.text_input("oder Symbol eingeben (z.B. BTC/USD)")

# --- Simulierte Analyse ---
def analyze_chart(image=None, symbol=None):
    trends = ["Aufwärts", "Abwärts", "Seitwärts"]
    trend = random.choice(trends)
    
    base_price = random.randint(50, 500)
    if trend == "Aufwärts":
        entry = base_price
        sl = base_price - random.randint(5, 20)
        tp = base_price + random.randint(10, 50)
    elif trend == "Abwärts":
        entry = base_price
        sl = base_price + random.randint(5, 20)
        tp = base_price - random.randint(10, 50)
    else:
        entry = base_price
        sl = base_price - random.randint(5, 10)
        tp = base_price + random.randint(5, 10)
    
    return {
        "Trend": trend,
        "Einstieg": entry,
        "SL": sl,
        "TP": tp
    }

# --- Analyse ausführen ---
if uploaded_file or symbol_input:
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Hochgeladenes Chart", use_column_width=True)
        result = analyze_chart(image=image)
    else:
        st.write(f"Analyse für Symbol: **{symbol_input}**")
        result = analyze_chart(symbol=symbol_input)
    
    st.subheader("🔍 Analyse Ergebnis")
    
    trend_color = TREND_COLORS.get(result["Trend"], "white")
    st.markdown(f"**Trend:** <span style='color:{trend_color};font-weight:bold'>{result['Trend']}</span>", unsafe_allow_html=True)
    st.markdown(f"**Einstiegspunkt:** {result['Einstieg']}")
    st.markdown(f"**Stop-Loss (SL):** {result['SL']}")
    st.markdown(f"**Take-Profit (TP):** {result['TP']}")
    
    st.info("⚠️ Hinweis: Diese Analyse ist **simuliert** und dient nur als Prototyp. Keine echte Handelsempfehlung!")

else:
    st.write("🔹 Bitte lade ein Chart hoch oder gib ein Symbol ein, um die Analyse zu starten.")
