
import datetime
import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions import add_paciente, check_paciente_login  # asegurate que functions.py esté en la raíz

st.title("Registro de Paciente")

with st.form("registro_paciente"):
    nombre_apellido = st.text_input("Nombre y Apellido")
    id_paciente = st.text_input("DNI del Paciente")
    
    tipo_diabetes = st.selectbox("Tipo de Diabetes", options=[1, 2])
    sexo = st.selectbox("Sexo", options=["Masculino", "Femenino", "Otro"])
    dispositivo = st.text_input("Dispositivo")
    altura = st.number_input("Altura (en metros)", min_value=0.5, max_value=2.5, step=0.01, format="%.2f")
    
    fecha_nacimiento = st.date_input("Fecha de Nacimiento", min_value=datetime.date(1900, 1, 1))

    act_fisica = st.checkbox("¿Realiza actividad física regularmente?")
    
    submitted = st.form_submit_button("Registrar")

if submitted:
    try:
        success = add_paciente(
            nombre_apellido=nombre_apellido.strip().lower(),
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

# ---- LOGIN ----

st.title("¿Ya tienes una cuenta? Inicia sesión:")

if not st.session_state.get("logged_in", False):
    with st.form("login_form"):
        login_id = st.text_input("ID del Paciente (DNI)")
        login_nombre = st.text_input("Nombre y Apellido")
        submitted_login = st.form_submit_button("Iniciar Sesión")

        if submitted_login:
            if check_paciente_login(login_id.strip(), login_nombre.strip()):
                st.session_state["logged_in"] = True
                st.session_state["login_id"] = login_id.strip()  # ⭐ GUARDAR login_id para usarlo en Registros.py
                st.session_state["username"] = login_nombre.strip().title()
                st.success(f"Bienvenido/a, {st.session_state['username']}!")
            else:
                st.error("Me parece que no estás registrado, o hay un error en los datos.")
else:
    username = st.session_state.get("username", "Usuario")
    st.success(f"Bienvenido/a de nuevo, {username}!")

    if st.button("Cerrar sesión"):
        st.session_state.clear()

# ---- ENLACE A REGISTROS ----

if st.session_state.get("logged_in", False):
    st.sidebar.page_link("pages/Registros.py", label="Registros de Glucosa")

