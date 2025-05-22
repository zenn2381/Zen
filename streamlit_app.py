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
  st.write(f"{angka} adalah bilangan genap") 
else:
  st.write(f"{angka} adalah Bilangan Ganjil") 
