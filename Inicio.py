# En Inicio.py (o donde pegaste tu CSS personalizado)
import streamlit as st
# ... tus otras importaciones ...

# Configuración de la página (esto ya lo tienes)
st.set_page_config(
    page_title="Insulink | Menu",
    page_icon="💉", # Un emoji que te guste
    layout="centered"
    # Asegúrate de NO tener 'theme="dark"' aquí, a menos que quieras forzar el tema oscuro.
    # Si lo tienes y quieres un fondo claro con letras oscuras, bórralo o coméntalo.
)

##############################################################

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
    
    /* Estilo para los botones */
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

    /* Estilo para cuando pasas el mouse por encima del botón */
    .stButton>button:hover,
    [data-testid="stButton"] > button:hover,
    [data-testid="stFormSubmitButton"] > button:hover
    {
        background-color: #FFFFFF !important; /* Fondo blanco al pasar el mouse */
        color: #007bff !important; /* Texto azul al pasar el mouse */
        box-shadow: 3px 3px 8px rgba(0, 0, 128, 0.9); /* Sombra al pasar el mouse */
        border: 1px solid #007bff; /* Borde azul para mejor contraste al pasar el mouse */
    }

    /* Estilos para los formularios (inputs de texto, números, etc.) */
    .stTextInput>div>div>input,
    .stNumberInput>div>div>input,
    .stDateInput>div>div>input,
    .stTimeInput>div>div>input,
    .stSelectbox>div>div>div {
        border-radius: 8px;
        border: 1px solid #ced4da;
        padding: 8px 12px;
        background-color: #f8f9fa; /* Fondo claro para los inputs */
        box-shadow: inset 1px 1px 3px rgba(0,0,0,0.1);
        color: #254679; /* Asegura que el texto dentro de los inputs sea oscuro */
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

# ... el resto de tu código de la página ...
st.title("Insulink")

col_vacia_izq_img, col_central_img, col_vacia_der_img = st.columns([0.7, 2, 1])
with col_central_img:
    st.image(
        "ChatGPT Image 7 jun 2025, 03_16_56 p.m..png", # Reemplaza esta URL con la URL de tu imagen
        caption="Con vos, siempre", # Texto opcional que aparece debajo de la imagen
        width=400, # Ancho de la imagen en píxeles. Ajusta este valor si es muy grande o pequeño.
                   # Si quieres que la imagen ocupe todo el ancho de esta columna central,
                   # puedes quitar 'width=200' y usar 'use_column_width=True' en su lugar.
        # use_column_width=True # Opción alternativa para que la imagen se ajuste al ancho de la columna central
        
    )
    
##############################################################

# En Inicio.py (o donde tengas estas líneas)

# Reemplaza st.subheader("Bienvenido a la app de control de glucosa") con:
st.markdown("<h2 style='text-align: center; color: #3C5A8A;'>Bienvenido a la app de control de glucosa</h2>", unsafe_allow_html=True)

# Reemplaza st.write("Por favor, selecciona tu perfil para iniciar sesión:") con:
st.markdown("<p style='text-align: center; font-size: 1.1em; color: #3C5A8A;'>Por favor, selecciona tu perfil para iniciar sesión:</p>", unsafe_allow_html=True)

# --- Inicio del fragmento para botones centrados ---

# Creamos tres columnas para centrar el grupo de botones.
# Las proporciones [1, 2, 1] hacen que la columna central sea el doble de ancha
# que las laterales, ayudando a centrar visualmente el contenido.
# Puedes ajustar estos números si necesitas más o menos espacio a los lados.
col_espacio_izquierdo, col_para_botones, col_espacio_derecho = st.columns([1, 2, 1])

with col_para_botones:
    # Dentro de la columna central (col_para_botones), creamos otras dos columnas
    # Esto permite que los botones "Soy Paciente" y "Soy Médico" sigan apareciendo
    # uno al lado del otro, pero ahora todo el par de botones está centrado en la página.
    btn_paciente_col, btn_medico_col = st.columns(2)

    with btn_paciente_col:
        # Botón "Soy Paciente"
        # use_container_width=True hace que el botón ocupe todo el ancho de su columna
        if st.button("👤 Soy Paciente", use_container_width=True):
            # Asegúrate que este path coincida con la ubicación real de tu archivo Paciente.py
            st.switch_page("pages/Paciente.py")

    with btn_medico_col:
        # Botón "Soy Médico"
        # use_container_width=True hace que el botón ocupe todo el ancho de su columna
        if st.button("🩺 Soy Médico", use_container_width=True):
            # Asegúrate que este path coincida con la ubicación real de tu archivo Medico.py
            st.switch_page("pages/Medico.py")

# --- Fin del fragmento para botones centrados ---