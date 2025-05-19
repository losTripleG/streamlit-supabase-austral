

import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions import add_paciente  # asegurate que 'functions.py' esté en la raíz del proyecto

st.title("Registro de Paciente")

with st.form("registro_paciente"):
    nombre_apellido = st.text_input("Nombre y Apellido")
    id_paciente = st.text_input("ID del Paciente")
    
    tipo_diabetes = st.selectbox("Tipo de Diabetes", options=[1, 2])  # integer
    
    sexo = st.selectbox("Sexo", options=["Masculino", "Femenino", "Otro"])
    
    dispositivo = st.text_input("Dispositivo")
    
    altura = st.number_input("Altura (en metros)", min_value=0.5, max_value=2.5, step=0.01, format="%.2f")  # float
    
    fecha_nacimiento = st.date_input("Fecha de Nacimiento")
    
    act_fisica = st.checkbox("¿Realiza actividad física regularmente?")  # boolean
    
    submitted = st.form_submit_button("Registrar")

if submitted:
    try:
        success = add_paciente(
            nombre_apellido=nombre_apellido,
            id_paciente=id_paciente,
            tipo_diabetes=tipo_diabetes,
            sexo=sexo,
            dispositivo=dispositivo,
            altura=float(altura),
            fecha_nacimiento=str(fecha_nacimiento),
            act_fisica=act_fisica
        )
        if success:
            st.success("Paciente registrado exitosamente.")
        else:
            st.error("Error al registrar al paciente.")
    except Exception as e:
        st.error(f"Ocurrió un error al registrar el paciente: {e}")

    
    if success:
        st.success("Paciente registrado exitosamente.")
    else:
        st.error("Error al registrar al paciente.")


