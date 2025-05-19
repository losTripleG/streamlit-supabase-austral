
import streamlit as st

# --- Page Configuration (Optional but Recommended) ---
st.set_page_config(
    page_title="Insulink",
    page_icon="💉",
    layout="centered" # "wide" or "centered"
)

# --- Main Application ---
st.title("Parra entretainments")
st.title("Insulink")

##############################################################

st.subheader("Bienvenido a la app de control de glucosa")

st.write("Por favor, selecciona tu perfil para iniciar sesión:")

col1, col2 = st.columns(2)

with col1:
    if st.button("👤 Soy Paciente"):
        st.switch_page("pages/Paciente.py")  # Asegúrate que este path coincide con tu archivo

with col2:
    if st.button("🩺 Soy Médico"):
        st.switch_page("pages/Medico.py")  # Asegúrate que este path coincide con tu archivo

