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
    page_title="Insulink | Médico",
    page_icon="🩺",
    layout="centered" # "wide" or "centered"
)

# --- Main Application ---
st.title("Médico")

# --- INICIO DEL CÓDIGO CSS PERSONALIZADO ---
# Este bloque aplica estilos CSS a toda la aplicación Streamlit.
st.markdown("""
<style>
    /* Importar fuente de Google Fonts (ej. Montserrat) */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

    /* Asegura que el color de texto del cuerpo sea oscuro por defecto */
    body {
        color: #3C5A8A; /* Gris oscuro para el texto por defecto de toda la página */
    }

    /* Estilo para el fondo completo de la aplicación */
    .stApp {
        background-color: #dbe4f3; /* Usamos un gris muy claro para el fondo */
        color: #254679; /* Color de texto general para la aplicación */
    }

    /* Estilo para los títulos principales (H1) */
    h1 {
        color: #254679; /* Un azul vibrante */
        font-family: 'Montserrat', sans-serif;
        text-align: center; /* Centrar el título */
        margin-bottom: 30px;
    }

    /* Estilos para subtítulos (H2, H3) */
    h2 {
        color: #254679; /* Color para los subtítulos */
        font-family: 'Montserrat', sans-serif;
    }
    h3 {
        color: #254679; /* Color para otros subtítulos */
        font-family: 'Montserrat', sans-serif;
    }

    /* Estilo para el texto normal generado por st.write o st.markdown (sin etiquetas HTML específicas) */
    p {
        color: #2A4068; /* Texto general oscuro */
        font-size: 16px;
        line-height: 1.6; /* Mejora la legibilidad */
    }
    .stMarkdown {
        color: #2A4068; /* Para asegurar el color de texto en todos los st.markdown */
    }
    
    /* Estilo para los botones generales */
    /* Utilizamos selectores más específicos con `!important` para asegurar la aplicación de los estilos */
    .stButton>button,
    [data-testid="stButton"] > button,
    [data-testid="stFormSubmitButton"] > button
    {
        background-color: #8b9fbf !important; /* Color de fondo del botón en estado normal (azul grisáceo) */
        color: white !important; /* Texto blanco en estado normal */
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        font-size: 18px;
        font-weight: bold;
        transition: all 0.3s ease-in-out; /* Transición suave para efectos hover */
        box-shadow: 2px 2px 5px rgba(0, 0, 128, 0.4); /* Sombra en estado normal */
    }

    /* Estilo para cuando pasas el mouse por encima del botón (botones generales) */
    .stButton>button:hover,
    [data-testid="stButton"] > button:hover,
    [data-testid="stFormSubmitButton"] > button:hover
    {
        background-color: #FFFFFF !important; /* Fondo blanco al pasar el mouse */
        color: #007bff !important; /* Texto azul al pasar el mouse */
        box-shadow: 3px 3px 8px rgba(0, 0, 128, 0.9); /* Sombra al pasar el mouse */
        border: 1px solid #007bff; /* Borde azul para mejor contraste al pasar el mouse */
    }

    /* Estilos para los formularios (inputs de texto, números, selectbox, date input, etc.) */
    /* Cuadro de texto debe ser blanco y el borde azul */
    .stTextInput>div>div>input,
    .stNumberInput>div>div>input,
    .stDateInput>div>div>input,
    .stTimeInput>div>div>input,
    .stSelectbox>div>div>div.st-cs, /* Selector específico para el cuadro del selectbox */
    .stSelectbox>div>div>div.st-cr { /* Otro selector para el cuadro del selectbox */
        border-radius: 8px;
        border: 1px solid #254679 !important; /* Borde azul para todos los inputs */
        padding: 8px 12px;
        background-color: #FFFFFF !important; /* Fondo blanco para los inputs */
        box-shadow: inset 1px 1px 3px rgba(0,0,0,0.1);
        color: #254679; /* Asegura que el texto dentro de los inputs sea oscuro */
        outline: none !important; /* Elimina el contorno predeterminado en estado normal */
    }

    /* Estilo para el borde de los inputs cuando están enfocados (seleccionados) */
    .stTextInput>div>div>input:focus,
    .stNumberInput>div>div>input:focus,
    .stDateInput>div>div>input:focus,
    .stTimeInput>div>div>input:focus,
    .stSelectbox>div>div>div.st-cs:focus,
    .stSelectbox>div>div>div.st-cr:focus {
        border-color: #254679 !important; /* El mismo azul que el borde normal */
        box-shadow: 0 0 0 0.2rem rgba(37, 70, 121, 0.4) !important; /* Sombra más visible en tu color azul */
        outline: none !important; /* Elimina el contorno predeterminado en foco */
    }

    /* Estilos para los botones de incremento/decremento en st.number_input */
    /* Botones en estado normal */
    [data-testid="stNumberInputButtons"] button {
        background-color: #3C5A8A !important; /* Color de tu sidebar/header */
        color: white !important;
        border: none !important; /* Asegurar que no tenga borde */
    }

    /* Botones al pasar el mouse (hover) */
    [data-testid="stNumberInputButtons"] button:hover {
        background-color: #2A4068 !important; /* Azul más oscuro para el hover */
        color: white !important;
    }

    /* Ajuste de border-radius para los botones del number_input (opcional, para visualización) */
    /* Puedes ajustar estos valores si no se ven bien las esquinas */
    [data-testid="stNumberInputButtons"] button:first-of-type { /* Botón de decremento (-) */
        border-top-left-radius: 0 !important;
        border-bottom-left-radius: 0 !important;
        border-top-right-radius: 0 !important;
        border-bottom-right-radius: 0 !important;
    }
    [data-testid="stNumberInputButtons"] button:last-of-type { /* Botón de incremento (+) */
        border-top-left-radius: 0 !important;
        border-bottom-left-radius: 0 !important;
        border-top-right-radius: 8px !important; /* Redondea la esquina superior derecha */
        border-bottom-right-radius: 8px !important; /* Redondea la esquina inferior derecha */
    }


    /* Estilo para el fondo de las listas desplegables (selectbox, calendario) */
    /* Los selectores son para los contenedores que Streamlit usa para los dropdowns */
    div[data-testid="stVirtualDropdown"], /* Contenedor principal de la lista desplegable */
    .st-bu, /* Clase para el fondo de la lista en algunos casos */
    .st-bv { /* Otra clase para el fondo de la lista */
        background-color: #3C5A8A !important; /* El celeste oscuro para el fondo de la lista */
    }
    
    /* Estilo para los ítems individuales del selectbox en el dropdown y del calendario */
    div[data-testid="stVirtualDropdown"] .st-bh, /* Clase común para ítems de lista */
    div[data-testid="stVirtualDropdown"] .st-ch, /* Otra clase común para ítems de lista */
    .st-bd, /* Clase para los días del calendario */
    .st-be { /* Otra clase para los días del calendario */
        background-color: #3C5A8A !important; /* Fondo de las opciones en la lista y días del calendario */
        color: white !important; /* Texto blanco en las opciones y días */
    }

    /* Estilo para los ítems al pasar el mouse o seleccionados en el dropdown y calendario */
    div[data-testid="stVirtualDropdown"] .st-bh:hover,
    div[data-testid="stVirtualDropdown"] .st-ch:hover,
    div[data-testid="stVirtualDropdown"] .st-bh.selected,
    div[data-testid="stVirtualDropdown"] .st-ch.selected,
    .st-bd:hover, .st-be:hover, /* Días del calendario al pasar el mouse */
    .st-bd.selected, .st-be.selected
     {
        background-color: #2A4068 !important; /* Azul más oscuro para hover/seleccionado */
        color: white !important;
    }

    /* Estilo para la flecha de los selectbox y date inputs */
    .stSelectbox [data-testid="stExpanderChevron"] svg path,
    .stDateInput [data-testid="stExpanderChevron"] svg path {
        stroke: #254679 !important; /* Color azul vibrante para la flecha */
        fill: #254679 !important; /* Color azul vibrante para la flecha */
    }

    /* Estilo para los DataFrames (tablas) */
    .stDataFrame {
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        overflow: hidden;
    }
    /* Asegura que el texto dentro de la tabla sea oscuro */
    .stDataFrame table {
        color: #2A4068; /* Texto oscuro para la tabla */
    }
    .stDataFrame th {
        color: #254679; /* Color para los encabezados de tabla */
        background-color: #e0eaf7; /* Fondo ligeramente diferente para los encabezados */
    }

    /* Estilo para los cuadros de información (info, warning, success, error) */
    .stAlert {
        border-radius: 10px;
        padding: 15px;
        margin-top: 15px;
        margin-bottom: 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .stAlert.info { background-color: #e0f7fa; color: #007bff; border-left: 5px solid #007bff; }
    .stAlert.warning { background-color: #fff3e0; color: #ff9800; border-left: 5px solid #ff9800; }
    .stAlert.success { background-color: #e8f5e9; color: #254679; border-left: 5px solid #254679; }
    .stAlert.error { background-color: #ffebee; color: #dc3545; border-left: 5px solid #dc3545; }

    /* Estilos para el Sidebar y la Barra Superior */
    /* Estilo para la BARRA GRIS DE LA IZQUIERDA (Sidebar) */
    div[data-testid="stSidebarContent"] {
        background-color: #3C5A8A; /* Azul oscuro/marino para el sidebar */
        color: white; /* Asegura que el texto del sidebar sea blanco */
        border-right: 1px solid #3C5A8A; /* Línea sutil en el borde derecho */
    }

    /* Estilo para la BARRA NEGRA DE ARRIBA (Header) */
    div[data-testid="stHeader"] {
        color: white;
        background-color: #3C5A8A; /* Color de fondo para el header */
    }

    /* Selector más específico para el fondo del header (puede variar en diferentes versiones de Streamlit) */
    .st-emotion-cache-1ihwvbb {
        background-color: #3C5A8A !important;
    }

    /* Opcional: Estilo para los elementos de navegación en el sidebar */
    .st-emotion-cache-1ihwvbb {
        color: #FFFFFF; /* Gris claro para el texto de los enlaces en el sidebar */
    }
    .st-emotion-cache-1ihwvbb:hover {
        background-color: #2A4068; /* Azul más claro al pasar el ratón */
        color: white;
    }
    .st-emotion-cache-1ihwvbb.active { /* Para la página activa en el sidebar */
        background-color: #2A4068; /* Color principal para la página activa */
        color: white;
        font-weight: bold;
    }


</style>
""", unsafe_allow_html=True)
# --- FIN DEL CÓDIGO CSS PERSONALIZADO ---
import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions import add_medico, verify_medico  # asegúrate que estén bien definidos

st.title("Registro de Médico 👨🏻‍⚕")

# ---- REGISTRO DE MÉDICO ----
with st.form("registro_medico"):
    nombre_apellido = st.text_input("Nombre y Apellido")
    id_medico = st.text_input("DNI del Médico")
    hospital = st.text_input("Hospital")
    
    submitted = st.form_submit_button("Registrar")

if submitted:
    try:
        success = add_medico(
            nombre_apellido=nombre_apellido.strip().lower(),
            id_medico=id_medico,
            hospital=hospital
        )
        if success:
            st.success("Médico registrado exitosamente.")
        else:
            st.error("Error al registrar al médico. ¿Ya estás registrado?")
    except Exception as e:
        st.error(f"Ocurrió un error al registrar al médico: {e}")

# ---- LOGIN DEL MÉDICO ----
st.title("¿Ya estás registrado? Inicia sesión aquí:")

if not st.session_state.get("medico_logged_in", False):
    with st.form("login_medico"):
        login_nombre = st.text_input("Nombre y Apellido (Login)")
        login_id = st.text_input("DNI del Médico (Login)")
        submitted_login = st.form_submit_button("Iniciar Sesión")

        if submitted_login:
            if verify_medico(login_nombre.strip().lower(), login_id.strip()):
                st.session_state["medico_logged_in"] = True
                st.session_state["medico_id"] = login_id.strip() #guardo login id, lo usamos en registros de pacientes
                st.session_state["medico_nombre"] = login_nombre.strip().title()
                st.success(f"Bienvenido/a Dr/a. {st.session_state['medico_nombre']}!")
            else:
                st.error("Nombre o DNI incorrectos, o no estás registrado.")
else:
    username = st.session_state.get("medico_nombre", "Médico")
    st.success(f"Bienvenido/a de nuevo, Dr/a. {username}!")

    if st.button("Cerrar sesión"):
        st.session_state.clear()

# ---- ENLACE A PÁGINA EXCLUSIVA ----
if st.session_state.get("medico_logged_in", False):
    st.switch_page("pages/Registro_de_pacientes.py")
