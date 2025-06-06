import streamlit as st
import pandas as pd
import joblib

# Modeli yükle
model = joblib.load("emlak_deger_modeli.pkl")

st.title("🏡 Emlak Değer Tahmin Uygulaması")

# Kullanıcı girişleri
il = st.selectbox("İl", ["İstanbul", "Ankara", "İzmir"])
ilce = st.selectbox("İlçe", ["Kadıköy", "Çankaya", "Bornova", "Beşiktaş", "Keçiören"])
m2 = st.number_input("Metrekare (m²)", min_value=30, max_value=500, value=100)
oda_sayisi = st.selectbox("Oda Sayısı", [1, 2, 3, 4])
bina_yasi = st.slider("Bina Yaşı", 0, 50, 10)
kat_durumu = st.selectbox("Kat Durumu", ["Zemin", "Orta", "Üst"])
toplu_tasima = st.checkbox("Toplu Taşıma Yakınında mı?", value=True)
okul_yakinligi = st.checkbox("Yakında Okul Var mı?", value=True)
manzara = st.selectbox("Manzara Türü", ["şehir", "deniz", "yeşil"])

if st.button("Tahmini Fiyatı Hesapla"):
    # Kullanıcı verisini bir DataFrame'e çevir
    input_data = {
        'm2': [m2],
        'oda_sayisi': [oda_sayisi],
        'bina_yasi': [bina_yasi],
        'toplu_tasima': [int(toplu_tasima)],
        'okul_yakinligi': [int(okul_yakinligi)],
        'il_İstanbul': [1 if il == "İstanbul" else 0],
        'il_İzmir': [1 if il == "İzmir" else 0],
        'ilce_Beşiktaş': [1 if ilce == "Beşiktaş" else 0],
        'ilce_Bornova': [1 if ilce == "Bornova" else 0],
        'ilce_Çankaya': [1 if ilce == "Çankaya" else 0],
        'ilce_Keçiören': [1 if ilce == "Keçiören" else 0],
        'kat_durumu_Orta': [1 if kat_durumu == "Orta" else 0],
        'kat_durumu_Üst': [1 if kat_durumu == "Üst" else 0],
        'manzara_şehir': [1 if manzara == "şehir" else 0],
        'manzara_yeşil': [1 if manzara == "yeşil" else 0],
    }

    input_df = pd.DataFrame(input_data)

    # Tahmin yap
    prediction = model.predict(input_df)[0]
    formatted_price = f"{prediction:,.0f}".replace(",", ".") + " TL"

    st.success(f"Tahmini Piyasa Değeri: {formatted_price}")
