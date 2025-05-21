
##REGISTRO DE GLUCOSA DE LOS PACIENTES

import streamlit as st
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions import connect_to_supabase, execute_query


# 

# Verificar si el paciente está logueado
if "login_id" not in st.session_state or st.session_state["login_id"] is None:
    st.error("Por favor, iniciá sesión primero en la página principal.")
    st.stop()

id_paciente = st.session_state["login_id"]

st.title("Registro de Glucosa")
st.subheader("Agregar nueva medición")

# Formulario para ingresar datos
with st.form("formulario_medicion"):
    comida = st.text_input("¿Qué comiste?")
    resultado_glucosa = st.number_input("Resultado de glucosa (mg/dL)", min_value=0)
    fecha = st.date_input("Fecha de la medición")
    hora= st.time_input("Hora de la medicion")
    submitted = st.form_submit_button("Guardar medición") 
# Insertar en la base de datos si se envió el formulario
if submitted:
    query = """
        INSERT INTO "Medicion de glucosa" (comida, resultado_glucosa, fecha, hora, id_paciente)
        VALUES (%s, %s, %s, %s, %s)
    """
    params = (comida, resultado_glucosa, fecha, hora, id_paciente)

    success = execute_query(query, params, is_select=False)
    if success:
        st.success("Medición guardada exitosamente.")
    else:
        st.error("Error al guardar la medición.")

# Mostrar las mediciones del paciente
st.subheader("Historial de mediciones")
query_select = """
    SELECT comida, resultado_glucosa, fecha, hora
    FROM "Medicion de glucosa"
    WHERE id_paciente = %s
    ORDER BY fecha DESC
"""
mediciones_df = execute_query(query_select, (id_paciente,))
if not mediciones_df.empty:
    st.dataframe(mediciones_df)
else:
    st.info("Todavía no hay mediciones registradas.")
