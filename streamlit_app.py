import streamlit as st

st.title("Ardi Raya")
st.write(
"AKHIRNYA BISA JUGA"
)
st.image("Akhirnya.jpg", width=200)


st.title("Aplikasi Cihuy") 
st.header("Aplikasi Sulap") 
angka = st.number_input("tulis sebuah angka:", value=0, step=1) 

if (angka % 2) == 0:
  st.write(f"{angka} Tadaa Jadi bilangan Genap Eak") 
else:
  st.write(f"{angka} Tadaa Jadi Bilangan Ganjil Eak") 
st.image("a4fb4fb9-7d8d-483a-8c4f-a2c33a7cc1a7.jpeg", width=200) 

st.image("a4fb4fb9-7d8d-483a-8c4f-a2c33a7cc1a7.jpeg", width=200) 
