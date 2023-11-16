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
    st.title("Hola, mi nombre es Camilo :wave:")
    st.subheader("Soy estudiante de la Universidad Nacional :smile:")
    st.write("Esta app fue creada para tomar control de tu gastos personales.")
    st.write("Para saber más del código de esta app dirigete al repositorio del proyecto [aquí>](https://github.com/ChewCEC/ppi_personal_app).")

# Explicación de la app 
# Se separa en un nuevo container
with st.container():
    st.subheader("¿Cómo funciona la app?")
    st.write(
        """
        ¡Bienvenido a nuestra Aplicación de Seguimiento Financiero!\nEste manual proporciona instrucciones paso a paso sobre cómo utilizar la 
        aplicación para registrar, visualizar y analizar tus ingresos y gastos. Sigue estos pasos para aprovechar al máximo la herramienta:
        """
    )

    st.subheader("1. Inicio de la Aplicación:")
    st.write(
        """
        Abre la aplicación en tu navegador web.
        """
    )
    st.write("Selecciona el mes y el año para los cuales deseas realizar el seguimiento financiero.") 
    st.subheader("2. Registro de Ingresos y Gastos:")
    
    st.markdown("Completa la información sobre tus ingresos y gastos utilizando los selectores y campos de entrada proporcionados.")
    st.write ('Utiliza la sección "Comentarios" para agregar cualquier nota relevante')
    

    st.subheader("3. Guardar la Información:")
    st.markdown(
        """Haz clic en el botón "Guardar información" al final del formulario para almacenar tus datos."""
    )
    

    st.subheader("4. Descripción y Análisis de Datos:")
    st.write("""Haz clic en el botón "Describir datos" para ver un resumen detallado de tus ingresos y gastos.""")
    st.write("Obtendrás información sobre el total de ingresos, total de gastos, balance, medias de ingresos y gastos.")    

    st.subheader("5. Visualización de Datos:")
    st.write(
        """
        Haz clic en "Graficar mis gastos e ingresos" para ver gráficos de barras separados para ingresos y gastos.
        """
    )
    st.write("Analiza visualmente cómo tus ingresos y gastos varían a lo largo del tiempo.")

    st.subheader("6. Persistencia de Datos:")
    st.write(
        """
        La información se guarda automáticamente en archivos CSV ("expenses.csv" e "income.csv") para que puedas retomar tu seguimiento en futuras sesiones.
        ¡Listo! Con estos pasos, podrás utilizar nuestra Aplicación de Seguimiento Financiero de manera efectiva.
        """
    )