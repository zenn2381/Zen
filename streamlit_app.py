import streamlit as st

st.title("Ardi Raya")
st.write(
"AKHIRNYA BISA JUGA"
)
st.image("Akhirnya.jpg", width=200)

st.image("4bb1aa37-1444-425a-8338-4055e50ea3fa.jpeg", width=200)

st.title("Aplikasi Cihuy") 
st.header("Aplikasi Sulap") 
angka = st.number_input("tulis sebuah angka:", value=0, step=1) 

if (angka % 2) == 0:
  st.write(f"{angka} Tadaa Jadi bilangan Genap Eak") 
else:
  st.write(f"{angka} Tadaa Jadi Bilangan Ganjil Eak") 
st.image("a4fb4fb9-7d8d-483a-8c4f-a2c33a7cc1a7.jpeg", width=200) 

st.image("6401f256-4753-4ffb-8b7a-d6275746b630.jpeg", width=200) 
