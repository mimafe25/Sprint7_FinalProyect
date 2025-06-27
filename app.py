import pandas as pd
import plotly.express as px  # (¡ojo! era 'plotly_express' incorrecto)
import streamlit as st

# Título de la app
st.title("Histograma interactivo con Plotly")

# Cargar los datos desde el archivo CSV
@st.cache_data  # Esto acelera la carga y evita leer el CSV cada vez
def cargar_datos():
    return pd.read_csv('vehicles_us.csv')

df = cargar_datos()

# Mostrar encabezado
st.header('¿Qué autos son más populares?')

# Mostrar el DataFrame (opcional)
if st.checkbox("Mostrar datos"):
    st.write(df.head())

# Seleccionar columna numérica para el histograma
columnas_numericas = ['price', 'model_year', 'odometer', 'days_listed']
columna = st.selectbox("Selecciona una columna numérica para el histograma", columnas_numericas)

# Botón para generar el histograma
if st.button("Generar histograma"):
    # Crear histograma
    fig = px.histogram(df, x=columna, nbins=30, title=f"Histograma de {columna}")
    
    # Mostrar el gráfico
    st.plotly_chart(fig)
