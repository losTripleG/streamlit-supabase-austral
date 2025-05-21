import streamlit as st

# Validamos que haya sesión iniciada
if not st.session_state.get("medico_logueado"):
    st.warning("Primero tenés que iniciar sesión como médico.")
    st.stop()

st.title("Registro de Pacientes")

st.write(f"Bienvenido/a, {st.session_state['nombre_medico']} 👨‍⚕️")

# ... acá ponés el formulario para registrar paciente ...

###################################################################
from functions import obtener_paciente_por_dni

# Mostrar sección de Registro de Pacientes
with st.expander("📋 Registro de Pacientes"):
    id_paciente = st.text_input("Ingresá el DNI del paciente (id_paciente)")
    
    if st.button("Buscar paciente"):
        datos_paciente = obtener_paciente_por_dni()
        
        if datos_paciente:
            st.subheader("✅ Datos del paciente:")
            st.write(f"Nombre y Apellido: {datos_paciente[1]}")
            st.write(f"Edad: {datos_paciente[2]}")
            st.write(f"Diagnóstico: {datos_paciente[3]}")
            # Agregá más campos según cómo esté tu tabla
        else:
            st.error("Paciente no encontrado. Verificá el DNI.")
