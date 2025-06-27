import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la app
st.title("Análisis Interactivo de Autos Usados")

# Cargar los datos desde el archivo CSV
@st.cache_data
def cargar_datos():
    return pd.read_csv('vehicles_us.csv')

df = cargar_datos()

# Mostrar encabezado
st.header('¿Qué autos son más populares?')

# Mostrar el DataFrame (opcional)
if st.checkbox("Mostrar datos"):
    st.write(df.head())

# Lista de columnas numéricas para los gráficos
columnas_numericas = ['price', 'model_year', 'odometer', 'days_listed']

# =====================
# Histograma interactivo
# =====================
st.subheader("Histograma interactivo")
columna_hist = st.selectbox("Selecciona una columna para el histograma", columnas_numericas)

if st.button("Generar histograma", key="btn_histograma"):
    fig_hist = px.histogram(df, x=columna_hist, nbins=30, title=f"Histograma de {columna_hist}")
    st.plotly_chart(fig_hist)

# ===========================
# Gráfico de dispersión (scatter)
# ===========================
st.subheader("Gráfico de dispersión interactivo")

x_axis = st.selectbox("Eje X", columnas_numericas, key="x_axis")
y_axis = st.selectbox("Eje Y", columnas_numericas, key="y_axis")

if st.button("Generar gráfico de dispersión", key="btn_dispersion"):
    fig_scatter = px.scatter(df, x=x_axis, y=y_axis, title=f"Dispersión: {x_axis} vs {y_axis}")
    st.plotly_chart(fig_scatter)
    st.write(f"Gráfico de dispersión entre **{x_axis}** y **{y_axis}**.")
