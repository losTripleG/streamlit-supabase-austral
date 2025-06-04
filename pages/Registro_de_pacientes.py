import streamlit as st
import pandas as pd
import sys
import os
import datetime # ¡Asegúrate de importar datetime!

# Asegúrate de que el directorio padre esté en el PYTHONPATH para importar 'functions'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa las funciones necesarias de tu archivo 'functions.py'
# Solo necesitamos 'get_glucose_measurements' para esta funcionalidad específica
from functions import get_glucose_measurements

# --- Verificación de sesión activa del médico ---
# Esta página solo debe ser accesible si un médico ha iniciado sesión
if "medico_id" not in st.session_state or st.session_state["medico_id"] is None:
    st.error("Por favor, inicia sesión como médico en la página principal para acceder a esta sección.")
    st.stop() # Detiene la ejecución del script si el médico no está logueado

# --- Título de la página para médicos ---
st.title("👨🏻‍⚕️ Visualizar Mediciones de Glucosa de Pacientes")
st.write(f"Bienvenido/a, Dr/a. {st.session_state.get('medico_nombre', 'Médico')}. Aquí puedes buscar las mediciones de glucosa de tus pacientes.")


# --- Sección para que el médico ingrese el ID del paciente ---
st.subheader("Buscar Mediciones por ID de Paciente")

with st.form("buscar_paciente_mediciones"):
    # Campo para que el médico ingrese el ID del paciente
    patient_id_to_search = st.text_input("Ingrese el ID del paciente", help="Este es el DNI o ID único del paciente.")
    
    submitted_search = st.form_submit_button("Buscar Mediciones")

# --- Lógica para mostrar las mediciones y el gráfico una vez que el médico ingresa un ID ---
if submitted_search:
    if patient_id_to_search:
        st.info(f"Buscando mediciones para el paciente con ID: **{patient_id_to_search}**...")
        
        # Llama a la función para obtener todas las mediciones de glucosa para la tabla completa
        # Asegúrate de que get_glucose_measurements en functions.py retorne las columnas 'fecha' y 'resultado_glucosa'
        glucose_data_all = get_glucose_measurements(patient_id_to_search.strip())
        
        if not glucose_data_all.empty:
            st.subheader(f"Historial Completo de Mediciones para Paciente ID: {patient_id_to_search}")
            st.dataframe(glucose_data_all)

            # --- Preparar datos para el gráfico del último mes ---
            # Asegurarse de que la columna 'fecha' sea tipo datetime para poder filtrar y graficar correctamente
            # Esto es crucial para que los filtros de fecha y el gráfico funcionen
            glucose_data_all['fecha'] = pd.to_datetime(glucose_data_all['fecha'])
            
            # Calcular la fecha de hace 30 días para definir el rango del "último mes"
            fecha_hace_30_dias = datetime.date.today() - datetime.timedelta(days=30)
            
            # Convertir a datetime.Timestamp para que la comparación con la columna 'fecha' del DataFrame sea correcta
            fecha_hace_30_dias_dt = pd.to_datetime(fecha_hace_30_dias)

            # Filtrar mediciones de los últimos 30 días
            glucose_data_last_month = glucose_data_all[glucose_data_all['fecha'] >= fecha_hace_30_dias_dt]

            # Verificar si hay datos suficientes para el gráfico después de filtrar
            if not glucose_data_last_month.empty:
                st.subheader("Gráfico de Glucosa - Último Mes")
                # Usa st.line_chart para generar un gráfico de línea simple
                st.line_chart(glucose_data_last_month, x='fecha', y='resultado_glucosa')
                st.caption(f"Mostrando mediciones desde el {fecha_hace_30_dias.strftime('%d-%m-%Y')} hasta hoy.")
            else:
                # Mensaje si no hay suficientes datos para el gráfico
                st.info(f"No hay suficientes mediciones de glucosa registradas en el último mes para el paciente con ID: **{patient_id_to_search}** para mostrar el gráfico.")

        else:
            # Mensaje si no se encuentran mediciones para el ID del paciente en absoluto
            st.warning(f"No se encontraron mediciones de glucosa para el paciente con ID: **{patient_id_to_search}**. Por favor, verifique el ID.")
    else:
        # Mensaje si el campo de ID del paciente está vacío
        st.error("Por favor, ingrese un ID de paciente para buscar.")