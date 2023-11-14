import streamlit as st
import os

st.set_page_config(page_title="Calculadora", page_icon="📝", layout="wide")

#Hacer codigo que si existen los dos csv los elimine
diretorio_atual = os.getcwd()
print("O diretório atual é:", diretorio_atual)
if os.path.exists("expenses.csv"):
    os.remove("expenses.csv")

if os.path.exists("income.csv"):
    os.remove("income.csv")


with st.container():
    st.subheader("Hola, mi nombre es Camilo :wave:")
    st.title("Soy estudiante de la Universidad Nacional :smile:")
    st.write("Esta app fue creada para tomar control de tu gastos personales.")
    st.write("Para saber más del código de esta app dirigete al repositorio del proyecto [aquí>](https://github.com/ChewCEC/ppi_personal_app).")

# Explicación de la app 
# Se separa en un nuevo container
with st.container():
    st.subheader("¿Cómo funciona la app?")
    st.write(
        """
        1. Ve a la página Calculara
        2. 
        """
    )

