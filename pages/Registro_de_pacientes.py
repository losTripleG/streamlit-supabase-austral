import streamlit as st


# Verificación de sesión activa

# Contenido disponible solo para médicos logueados
st.title("Registro de pacientes 📝")
st.write(f"Bienvenido/a, Dr/a. {st.session_state.get('username', '')}")

# Aquí va la lógica de visualización y edición de registros de pacientes
st.info("Aquí se mostrarán los registros de los pacientes.")

# ... acá ponés el formulario para registrar paciente ...

###################################################################
import streamlit as st
import pandas as pd
import sys
import os

# Asegúrate de que el directorio padre esté en el PYTHONPATH para importar 'functions'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa las funciones necesarias de tu archivo 'functions.py'
# Asegúrate de que 'get_glucose_measurements' esté disponible en 'functions.py'
from functions import connect_to_supabase, execute_query, get_glucose_measurements


# Verificar si el médico está logueado
# Esta página solo debe ser accesible si un médico ha iniciado sesión
if "medico_id" not in st.session_state or st.session_state["medico_id"] is None:
    st.error("Por favor, inicia sesión como médico en la página principal para acceder a esta sección.")
    st.stop() # Detiene la ejecución del script si el médico no está logueado

# Título de la página para médicos
st.title("👨🏻‍⚕️ Visualizar Mediciones de Glucosa de Pacientes")
st.write(f"Bienvenido/a, Dr/a. {st.session_state.get('medico_nombre', 'Médico')}. Aquí puedes buscar las mediciones de glucosa de tus pacientes.")


# Sección para que el médico ingrese el ID del paciente
st.subheader("Buscar Mediciones por ID de Paciente")

with st.form("buscar_paciente_mediciones"):
    # Campo para que el médico ingrese el ID del paciente
    patient_id_to_search = st.text_input("Ingrese el ID del paciente", help="Este es el DNI o ID único del paciente.")
    
    submitted_search = st.form_submit_button("Buscar Mediciones")

# Lógica para mostrar las mediciones una vez que el médico ingresa un ID
if submitted_search:
    if patient_id_to_search:
        st.info(f"Buscando mediciones para el paciente con ID: **{patient_id_to_search}**...")
        
        # Llama a la función para obtener las mediciones de glucosa
        # Esta función debe estar definida en tu archivo 'functions.py'
        glucose_data_df = get_glucose_measurements(patient_id_to_search.strip())
        
        if not glucose_data_df.empty:
            st.subheader(f"Historial de Mediciones de Glucosa para Paciente ID: {patient_id_to_search}")
            st.dataframe(glucose_data_df)
        else:
            st.warning(f"No se encontraron mediciones de glucosa para el paciente con ID: **{patient_id_to_search}**. Por favor, verifique el ID.")
    else:
        st.error("Por favor, ingrese un ID de paciente para buscar.")

# Opcional: Si quieres mantener alguna otra funcionalidad para el médico en esta página, puedes añadirla aquí.
# Por ejemplo, un botón para volver a la página principal o para registrar nuevos pacientes (si esa es otra funcionalidad).

