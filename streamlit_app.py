import streamlit as st

st.set_page_config(page_title="SteveAnaliz", page_icon="🚀")

st.title("🚀 SteveAnaliz – Yatırım Radar Paneli")

st.markdown("""
Bu, yapay zeka destekli yatırım analiz panelidir.
Gelişmiş algoritmalarla yüksek potansiyelli şirketleri tespit etmek için tasarlanmıştır.
""")

st.subheader("👥 Giriş / Kayıt Sistemi")
st.info("Bu alan simülasyon amaçlıdır. Giriş / Kayıt arayüzü gerçek zamanlı veriyle desteklenmedi.")

st.subheader("🌐 Dünya Piyasaları")
st.write({
    "S&P 500": 5123.45,
    "NASDAQ": 16234.12,
    "DAX": 18562.22,
    "Brent Petrol": 89.71,
    "Altın (USD/ons)": 2356.40
})

st.subheader("🧠 AI ile 10 Şirket Önerisi")
companies = ["NeuroNet", "GreenFusion", "DeepTrade AI", "SolarLink", "CloudSynapse",
             "AutoQuanta", "QuantumByte", "FinTechify", "NanoFuel Systems", "CyberCore Inc"]
st.write(companies)

st.subheader("📊 Veri Dışa Aktarımı")
with open("steveanaliz_export.csv", "w") as f:
    f.write("name,score\n")
    for c in companies:
        f.write(f"{c},100\n")
st.download_button("Veriyi İndir (.csv)", data=open("steveanaliz_export.csv").read(), file_name="steveanaliz_export.csv")
