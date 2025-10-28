import streamlit as st 
import pandas as pd
import plotly.express as px

vehicles_df = pd.read_csv('vehicles_us.csv')

st.header('Vehicles for sale')
hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
         # escribir un mensaje
         st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
         fig = px.histogram(vehicles_df, x="model_year")
     
         # mostrar un gráfico Plotly interactivo
         st.plotly_chart(fig, use_container_width=True)

build_disp = st.checkbox('Construir una gráfica de dispersión') # crear una casilla de verificación

if build_disp: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
        
    fig = px.scatter(vehicles_df, x="model_year", y="price") # crear un gráfico de dispersión
        
    fig.show() 
        