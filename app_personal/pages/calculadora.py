import streamlit as st
import numpy as np
import pandas as pd  # Importa la biblioteca de pandas
import matplotlib.pyplot as plt
from datetime import datetime
import calendar
import warnings

warnings.filterwarnings("ignore")

st.title("Bienvenido a Calculadora")

# ---- opciones de de income y outcome de la calculadora ----
incomes = ["Salario", "Mesa de dinero", "Inversiones", "Otros ingresos"]
expenses = ["Alimentación", "Transporte", "Entretenimiento", "Ahorros", "Otros gastos"]

page_title = "Calculadora de gastos personales"
page_icon = "📝"
layout = "centered"


# ---- funciones de calculadora ----

# Definimos la lista de años, meses y días
years = [datetime.now().year + i for i in range(0, 5)]
months = list(calendar.month_name[1:])

# Definimos la función para calcular el total de ingresos
def sumar_datos(data):
    return data.sum(axis=1).sum()

# Definimos la función para calcular la media de ingresos con Numpy
def calcular_media(data):
    return np.mean(data.sum(axis=1))


# -----------  Calculadora de gastos personales -----------
# Definimos la función para calcular el total de ingresos
st.subheader("Ingrese sus ingresos")

# Crear formulario con Streamlit
with st.form("entry_form", clear_on_submit=True):
    # Crear dos columnas para seleccionar mes y año
    col1, col2 = st.columns(2)
    col1.selectbox("Elija el mes", months, key="month")
    col2.selectbox("Elija el año", years, key="year")

    # Expander para ingresos
    with st.expander("Ingresos"):
        for income in incomes:
            st.number_input(f"{income}", min_value=0, format="%i", value=0, step=1000, key=income)
# Expander para gastos por categoría
    with st.expander("Gastos por categoría"):
        for expense in expenses:
            st.number_input(f"{expense}", min_value=0, format="%i", value=0, step=1000, key=expense)
    # Expander para comentarios
    with st.expander("Comentarios:"):
        comment = st.text_area("", max_chars=200, placeholder="Escriba sus comentarios aquí...", key="comment")

    submit_button = st.form_submit_button(label="Guardar información")


    # Procesar el formulario cuando se envía
    if submit_button:
        st.write("Calculando...")

        # Crear una cadena que representa el período (año-mes)
        period = str(st.session_state["year"]) + "-" + str(st.session_state["month"])

        # Obtener los ingresos y gastos de la sesión
        incomes = {income: st.session_state[income] for income in incomes}
        expenses = {expense: st.session_state[expense] for expense in expenses}

        # TODO - Guardar la información en la base de datos

        # Mensaje de éxito
        st.success("Información guardada con éxito")
        st.write(f"period: {period}")
        st.write(f"incomes: {incomes}")
        st.write(f"expenses: {expenses}")

        # Crear DataFrames con los ingresos y gastos
        df_incomes = pd.DataFrame([incomes], index=[period])
        df_expenses = pd.DataFrame([expenses], index=[period])

        # Crear Series con los ingresos y gastos
        result_income = pd.Series(data=incomes, name=period)
        result_expense = pd.Series(data=expenses, name=period)

        # Leer o crear DataFrames maestros
        try:
            DF_MASTER_EXPENSES = pd.read_csv("expenses.csv", index_col=[0])
            DF_MASTER_INCOME = pd.read_csv("income.csv", index_col=[0])
        except:
            DF_MASTER_EXPENSES = pd.DataFrame()
            DF_MASTER_INCOME = pd.DataFrame()

        # Agregar las nuevas filas a los DataFrames maestros
        DF_MASTER_EXPENSES = DF_MASTER_EXPENSES.append(result_expense, ignore_index=False)
        DF_MASTER_INCOME = DF_MASTER_INCOME.append(result_income, ignore_index=False)

        # Guardar los DataFrames maestros en archivos CSV
        DF_MASTER_EXPENSES.to_csv("expenses.csv", index=True)
        DF_MASTER_INCOME.to_csv("income.csv", index=True)

        # Mensaje de éxito y mostrar los DataFrames maestros
        st.success("Información guardada con éxito")
        st.write("Dataframe:")
        # st.write(DF_MASTER_INCOME)
        # st.write(DF_MASTER_EXPENSES)
 
# Verificar si se ha hecho clic en el botón "Describir datos" en la interfaz de Streamlit
if st.button("Describir datos"):
    # Mostrar subencabezado y mensaje mientras se calcula el balance
    st.subheader("Balance de ingresos y gastos")
    st.write("Calculando balance...")

    # Intentar cargar los DataFrames maestros de ingresos y gastos desde archivos CSV
    try:
        DF_MASTER_EXPENSES = pd.read_csv("expenses.csv", index_col=[0])
        DF_MASTER_INCOME = pd.read_csv("income.csv", index_col=[0])
    except:
        # Manejar la excepción si no se pueden cargar los datos
        st.write("No hay datos para calcular el balance")

    # Calcular el total de ingresos y gastos
    total_ingresos = sumar_datos(DF_MASTER_INCOME)
    total_gastos = sumar_datos(DF_MASTER_EXPENSES)

    # Calcular el balance (ingresos - gastos)
    balance = total_ingresos - total_gastos

    # Mostrar los resultados
    st.write(f"Total de ingresos: {total_ingresos}")
    st.write(f"Total de gastos: {total_gastos}")

    # Determinar si el balance es positivo o negativo y mostrar el subencabezado correspondiente
    if balance > 0:
        st.subheader(f"Balance positivo: {balance}")
    else:
        st.subheader("Tienes un balance negativo, debes revisar tus gastos")
        st.write(f"Balance negativo: {balance}")

    # Mostrar subencabezado para la media de ingresos y gastos
    st.subheader("Media de ingresos y gastos")

    # Calcular la media de ingresos y gastos utilizando funciones externas (sumar_datos y calcular_media)
    media_ingresos = calcular_media(DF_MASTER_INCOME)
    media_gastos = calcular_media(DF_MASTER_EXPENSES)

    # Mostrar los resultados de la media
    st.write(f"Media de ingresos: {media_ingresos}")
    st.write(f"Media de gastos: {media_gastos}")


# Verificar si se ha hecho clic en el botón "Graficar mis gastos e ingresos" en la interfaz de Streamlit
if st.button("Graficar mis gastos e ingresos"): 
    # Intentar cargar los DataFrames maestros de ingresos y gastos desde archivos CSV
    try:
        DF_MASTER_EXPENSES = pd.read_csv("expenses.csv", index_col=[0])
        DF_MASTER_INCOME = pd.read_csv("income.csv", index_col=[0])
    except:
        # Manejar la excepción si no se pueden cargar los datos
        st.write("No hay datos para graficar el balance")
        
    # Sumar los valores de ingresos y gastos y convertirlos a listas
    income_values = DF_MASTER_INCOME.sum().tolist()
    expense_values = DF_MASTER_EXPENSES.sum().tolist()

    # Obtener las etiquetas (nombres de las categorías) de ingresos y gastos
    income_labels = list(DF_MASTER_INCOME.columns)
    expenses_labels = list(DF_MASTER_EXPENSES.columns)

    # Crear gráfico de barras para ingresos
    fig_gastos, ax = plt.subplots()
    ax.bar(income_labels, income_values, label="Ingresos")

    # Crear gráfico de barras para gastos
    fig_ingresos, ax2 = plt.subplots()
    ax2.bar(expenses_labels, expense_values, label="Gastos")

    # Mostrar la gráfica de gastos en la interfaz de Streamlit
    st.subheader("Gráfica de gastos")
    st.pyplot(fig_gastos)

    # Mostrar la gráfica de ingresos en la interfaz de Streamlit
    st.subheader("Gráfica de ingresos")
    st.pyplot(fig_ingresos)



