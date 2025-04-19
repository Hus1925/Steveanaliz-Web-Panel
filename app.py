
import streamlit as st
import pandas as pd

st.set_page_config(page_title="SteveAnaliz Panel", layout="centered")
st.title("🚀 SteveAnaliz – Test Paneli")

# Veriler
companies = [
    {"name": "TechNova", "score": 160, "sector": "Yapay Zeka"},
    {"name": "NextAI", "score": 142, "sector": "Yapay Zeka"},
    {"name": "BioFusion", "score": 124, "sector": "Biyoteknoloji"},
    {"name": "GreenCore", "score": 138, "sector": "Enerji"},
]

df = pd.DataFrame(companies)

# 1️⃣ Risk & Büyüme Analizi
st.subheader("🧬 Risk & Büyüme Analizi")
avg_score = df["score"].mean()
st.metric("Ortalama Skor", f"{avg_score:.2f}")

if avg_score > 150:
    yorum = "Yüksek büyüme potansiyeli, düşük risk"
elif avg_score > 130:
    yorum = "Orta risk, dikkatli izleme önerilir"
else:
    yorum = "Riskli bölge, detaylı analiz önerilir"

st.info(yorum)

# 2️⃣ AI Tahmin (Basit Simülasyon)
st.subheader("🤖 AI Fiyat Tahmini (±12%)")
df["tahmini_fiyat"] = df["score"] * 1.12
st.table(df[["name", "score", "tahmini_fiyat"]].rename(columns={
    "name": "Şirket",
    "score": "Skor",
    "tahmini_fiyat": "Tahmini Değer"
}))

# 3️⃣ Veri Politikası
st.subheader("📜 Veri İşleme Politikası")
st.markdown("""
SteveAnaliz, kullanıcı verilerini **GDPR** ve **CALOP** standartlarına uygun olarak işler.  
AI sistemleri önyargısız, etik ve şeffaf ilkelere göre yapılandırılmıştır.  
Herhangi bir veri, üçüncü kişilerle **paylaşılmaz**.  
Sistem üzerindeki tüm hareketler kayıt altına alınır ve analiz edilir.  
""")

st.markdown("➡️ Devam ederek [Kullanım Koşulları](#) ve [Veri Gizliliği Politikası](#)'nı kabul etmiş sayılırsınız.")
