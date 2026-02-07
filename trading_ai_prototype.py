# trading_ai_prototype.py

import streamlit as st
from PIL import Image
import random

st.set_page_config(page_title="Trading KI Analyse", layout="wide")

st.title("📈 Trading-KI Analyse Prototyp")
st.markdown(
    "Lade ein Chart-Bild hoch oder gib ein Symbol ein, "
    "und die KI simuliert eine Analyse inklusive Trend, Einstieg, SL & TP."
)

# Upload oder Symbol eingeben
uploaded_file = st.file_uploader("📤 Chart-Bild hochladen", type=["png", "jpg", "jpeg"])
symbol_input = st.text_input("oder Symbol eingeben (z.B. BTC/USD)")

# Funktion zur simulierten Analyse
def analyze_chart(image=None, symbol=None):
    trends = ["Aufwärts", "Abwärts", "Seitwärts"]
    trend = random.choice(trends)
    
    # Simulierter Einstieg, SL & TP
    base_price = random.randint(50, 500)  # zufälliger Basispreis
    if trend == "Aufwärts":
        entry = base_price
        sl = base_price - random.randint(5, 20)
        tp = base_price + random.randint(10, 50)
    elif trend == "Abwärts":
        entry = base_price
        sl = base_price + random.randint(5, 20)
        tp = base_price - random.randint(10, 50)
    else:  # Seitwärts
        entry = base_price
        sl = base_price - random.randint(5, 10)
        tp = base_price + random.randint(5, 10)
    
    return {
        "Trend": trend,
        "Einstieg": entry,
        "SL": sl,
        "TP": tp
    }

# Analyse ausführen
if uploaded_file or symbol_input:
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Hochgeladenes Chart", use_column_width=True)
        result = analyze_chart(image=image)
    else:
        st.write(f"Analyse für Symbol: **{symbol_input}**")
        result = analyze_chart(symbol=symbol_input)
    
    st.subheader("🔍 Analyse Ergebnis")
    st.metric("Trend", result["Trend"])
    st.metric("Einstiegspunkt", result["Einstieg"])
    st.metric("Stop-Loss (SL)", result["SL"])
    st.metric("Take-Profit (TP)", result["TP"])
    
    st.info("⚠️ Hinweis: Diese Analyse ist **simuliert** und dient nur als Prototyp. Keine echte Handelsempfehlung!")

else:
    st.write("🔹 Bitte lade ein Chart-Bild hoch oder gib ein Symbol ein, um die Analyse zu starten.")
