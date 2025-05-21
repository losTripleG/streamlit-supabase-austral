# le cambiamos el nombre a la pagina, hay q ir al github a ver si registro el cambio, y borrar el nombre anterior

#importamos streamlit as st
#from functions import execute_query
# paraponerle un titulo vamos a streamlit y buscamos st.title
#st.title("titulo")
#streamlit dataframe documentation buscamos en streamlit para mostrar una tabla:
        #query= SELECT .... la tabla que queremos
        #df= execute_query  // df ahora es la variable que vamos a usar para trabajar con los datos de la tabla
        #st.dataframe(df, funciones de estetica)
    #funcion estetica: hide_index=TRUE es una funcion para eliminar los index de la tabla que mostramos
#todo lo que este con st. es lo que a´parece en la app
#st.text("")


import streamlit as st

# --- Page Configuration (Optional but Recommended) ---
st.set_page_config(
    page_title="Médico - Insulink",
    page_icon="🩺",
    layout="centered" # "wide" or "centered"
)

# --- Main Application ---
st.title("Insulink")

##############################################################

##############################################################

# st.markdown("""
#     <h3 style='text-align: wide; font-size: 24px;'>¿Deseas iniciar sesión?</h3>
# """, unsafe_allow_html=True)
# # Check if the user is already logged in (using session state)
# if not st.session_state.get("logged_in", False):
#     # If not logged in, show the login form
#     with st.form("login_form"):
#         username = st.text_input("Nombre de usuario")
#         password = st.text_input("Contraseña", type="password")
#         submitted = st.form_submit_button("Iniciar sesión")

#         if submitted:
#             # For this demo, any username/password is accepted
#             if username and password:
#                 st.session_state["logged_in"] = True
#                 st.session_state["username"] = username # Optional: store username
#                 st.success("Inicio exitoso! 👍")
#             else:
#                 st.error("Por favor, ingrese nombre de usuario y contraseña. 😠")
# else:
#     # If logged in, show a welcome message
#     st.success(f"Welcome back, {st.session_state.get('username', 'User')}!")
#     st.info("Navigate using the sidebar on the left to manage different sections.")
#     #st.balloons() # Fun little animation

#     # Optional: Add a logout button
#     if st.button("Logout"):
#         del st.session_state["logged_in"]
#         if "username" in st.session_state:
#             del st.session_state["username"]

import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions import add_medico  # asegurate que 'functions.py' esté en la raíz del proyecto

st.title("Registro de médico 👨🏻‍⚕")

with st.form("registro_medico"):
    nombre_apellido = st.text_input("Nombre y Apellido")

    id_medico = st.text_input("DNI del médico")
    
    hospital = st.text_input("Hospital")
    
    submitted = st.form_submit_button("Registrar")

if submitted:
    try:
        success = add_medico(
            nombre_apellido=nombre_apellido,
            id_medico =id_medico,
            hospital = hospital,
        )
        if success:
            st.success("Médico registrado exitosamente.")
        else:
            st.error("Error al registrar al médico.")
    except Exception as e:
        st.error(f"Ocurrió un error al registrar el médico: {e}")

    
    if success:
        st.success("Médico registrado exitosamente.")
    else:
        st.error("Error al registrar al médico.")


import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions import verify_medico  # Asegúrate de que 'functions.py' esté en la raíz del proyecto y contenga la función verify_medico

st.title("¿Ya tienes una cuenta? Inicia sesión aquí 👇")

with st.form("inicio_sesion_medico"):
    nombre_apellido = st.text_input("Nombre y Apellido")
    id_medico = st.text_input("DNI del médico")
    
    submitted = st.form_submit_button("Iniciar Sesión")

if submitted:
    try:
        # Aquí llamamos a una función que verifica las credenciales en la base de datos
        # Esta función (verify_medico) debería estar en 'functions.py'
        # y devolver True si las credenciales coinciden, False en caso contrario.
        success = verify_medico(
            nombre_apellido=nombre_apellido,
            id_medico=id_medico,
        )
        
        if success:
            st.success("¡Inicio de sesión exitoso! Bienvenido/a.")
            # Aquí podrías redirigir al médico a otra página o mostrar contenido específico
        else:
            st.error("Error de inicio de sesión: Nombre y/o DNI incorrectos.")
    except Exception as e:
        st.error(f"Ocurrió un error al intentar iniciar sesión: {e}")