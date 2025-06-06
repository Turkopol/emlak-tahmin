import streamlit as st
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor

# Eğitim verisi (küçük bir örnek seti)
data = {
    'm2': [100, 120, 90, 110, 95],
    'oda_sayisi': [3, 2, 3, 4, 2],
    'bina_yasi': [10, 5, 15, 20, 7],
    'toplu_tasima': [1, 1, 0, 1, 0],
    'okul_yakinligi': [1, 0, 1, 1, 0],
    'il_İstanbul': [1, 0, 0, 1, 0],
    'il_İzmir': [0, 0, 1, 0, 0],
    'ilce_Beşiktaş': [0, 0, 0, 1, 0],
    'ilce_Bornova': [0, 0, 1, 0, 0],
    'ilce_Çankaya': [0, 1, 0, 0, 0],
    'ilce_Keçiören': [0, 0, 0, 0, 1],
    'kat_durumu_Orta': [1, 0, 0, 1, 0],
    'kat_durumu_Üst': [0, 0, 1, 0, 0],
    'manzara_şehir': [0, 1, 0, 0, 1],
    'manzara_yeşil': [0, 0, 1, 0, 0],
    'fiyat': [2000000, 1500000, 1300000, 2500000, 1400000]
}
df = pd.DataFrame(data)
X = df.drop('fiyat', axis=1)
y = df['fiyat']

model = RandomForestRegressor(n_estimators=100)
model.fit(X, y)

# Uygulama başlığı
st.title("\ud83c\udfe0 Emlak Değer Tahmini")

# Giriş alanları
m2 = st.number_input("Metrekare", 50, 500, 100)
oda = st.selectbox("Oda Sayısı", [1, 2, 3, 4])
yas = st.slider("Bina Yaşı", 0, 50, 10)
tasima = st.checkbox("Toplu Taşıma Yakın mı?", value=True)
okul = st.checkbox("Okula Yakın mı?", value=True)
il = st.selectbox("İl", ["İstanbul", "Ankara", "İzmir"])
ilce = st.selectbox("İlçe", ["Kadıköy", "Çankaya", "Bornova", "Beşiktaş", "Keçiören"])
kat = st.selectbox("Kat Durumu", ["Zemin", "Orta", "Üst"])
manzara = st.selectbox("Manzara", ["şehir", "deniz", "yeşil"])

# Özellik vektörünü oluştur
veri = {
    'm2': [m2],
    'oda_sayisi': [oda],
    'bina_yasi': [yas],
    'toplu_tasima': [int(tasima)],
    'okul_yakinligi': [int(okul)],
    'il_İstanbul': [1 if il == "İstanbul" else 0],
    'il_İzmir': [1 if il == "İzmir" else 0],
    'ilce_Beşiktaş': [1 if ilce == "Beşiktaş" else 0],
    'ilce_Bornova': [1 if ilce == "Bornova" else 0],
    'ilce_Çankaya': [1 if ilce == "Çankaya" else 0],
    'ilce_Keçiören': [1 if ilce == "Keçiören" else 0],
    'kat_durumu_Orta': [1 if kat == "Orta" else 0],
    'kat_durumu_Üst': [1 if kat == "Üst" else 0],
    'manzara_şehir': [1 if manzara == "şehir" else 0],
    'manzara_yeşil': [1 if manzara == "yeşil" else 0]
}
input_df = pd.DataFrame(veri)

if st.button("Tahmini Fiyatı Göster"):
    tahmin = model.predict(input_df)[0]
    st.success(f"Tahmini Değer: \u20ba{tahmin:,.0f}")
