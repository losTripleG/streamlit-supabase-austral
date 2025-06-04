# En Inicio.py (o donde pegaste tu CSS personalizado)
import streamlit as st
# ... tus otras importaciones ...

# Configuración de la página (esto ya lo tienes)
st.set_page_config(
    page_title="Mi App Insulink",
    page_icon="💉", # Un emoji que te guste
    layout="centered"
    # Asegúrate de NO tener 'theme="dark"' aquí, a menos que quieras forzar el tema oscuro.
    # Si lo tienes y quieres un fondo claro con letras oscuras, bórralo o coméntalo.
)

# --- INICIO DEL CÓDIGO CSS PERSONALIZADO (CORREGIDO) ---
st.markdown("""
<style>
    /* Importar fuente de Google Fonts (ej. Montserrat) */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

    /* ESTO ES LO CLAVE: Asegurarse de que el color de texto del cuerpo sea oscuro */
    body {
        color: #3C5A8A; /* Gris oscuro para el texto por defecto de toda la página */
    }

    /* Estilo para el fondo completo */
    .stApp {
        background-color: #dbe4f3; /* Usamos un gris muy claro para el fondo */
        /* Opcional: puedes añadir una imagen de fondo o una textura */
        /* background-image: url("https://www.transparenttextures.com/patterns/clean-textile.png"); */
        /* background-size: cover; */
        color: #254679; /* También podemos poner el color del texto aquí para mayor seguridad */
    }

    /* Cambiar el color y la fuente de los títulos principales (H1) */
    h1 {
        color: #254679; /* Un azul vibrante */
        font-family: 'Montserrat', sans-serif;
        text-align: center; /* Centrar el título */
        margin-bottom: 30px;
    }

    /* Estilos para subtítulos (H2, H3) */
    h2 {
        color: #254679; /* Verde para los subtítulos */
        font-family: 'Montserrat', sans-serif;
    }
    h3 {
        color: #254679; /* Azul claro para otros subtítulos */
        font-family: 'Montserrat', sans-serif;
    }

    /* Estilo para el texto normal generado por st.write o st.markdown (sin etiquetas HTML específicas) */
    p {
        color: #2A4068; /* ¡CORREGIDO AQUÍ! Ahora el texto general será oscuro */
        font-size: 16px;
        line-height: 1.6; /* Mejora la legibilidad */
    }
    .stMarkdown {
        color: #2A4068; /* Para asegurar el color de texto en todos los st.markdown */
    }


    
    /* Estilo para los botones */
    .stButton>button {
        background-color: #8b9fbf; /* El color de fondo del botón en estado normal */
        color: white !important; /* ¡CORREGIDO AQUÍ! Fuerza las letras blancas en estado normal */
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        font-size: 18px;
        font-weight: bold;
        transition: all 0.3s ease-in-out; /* Para una transición suave */
        box-shadow: 2px 2px 5px rgba(0, 0, 128, 0.4); /* Sombra en estado normal */
    }

    /* ESTILO PARA CUANDO PASAS EL MOUSE POR ENCIMA DEL BOTÓN */
    .stButton>button:hover {
        background-color: #FFFFFF; /* Color de fondo del botón al pasar el mouse (blanco, como quieres) */
        color: #007bff !important; /* ¡CORREGIDO AQUÍ! Fuerza las letras azules al pasar el mouse */
        box-shadow: 3px 3px 8px rgba(0, 0, 128, 0.9); /* Sombra al pasar el mouse */
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
        background-color: #2A4068;
        box-shadow: inset 1px 1px 3px rgba(0,0,0,0.1);
        color: #254679; /* Asegura que el texto dentro de los inputs también sea oscuro */
    }

    /* Estilo para los DataFrames (tablas) */
    .stDataFrame {
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        overflow: hidden;
    }
    /* Asegura que el texto dentro de la tabla sea oscuro */
    .stDataFrame table {
        color: #6bb349;
    }
    .stDataFrame th {
        color: #6bb349; /* Color para los encabezados de tabla */
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


    /* ----- NUEVOS ESTILOS PARA EL SIDEBAR Y LA BARRA SUPERIOR ----- */

    /* Estilo para la BARRA GRIS DE LA IZQUIERDA (Sidebar) */
    div[data-testid="stSidebarContent"] {
        background-color: #3C5A8A; /* Un azul oscuro/marino para el sidebar */
        color: white; /* Asegura que el texto del sidebar sea blanco */
        border-right: 1px solid #2A4068; /* Una línea sutil en el borde derecho del sidebar */
    }

    /* Estilo para la BARRA NEGRA DE ARRIBA (Header) */
    div[data-testid="stHeader"] {
        background-color: #2A4068; /* Un azul muy oscuro para la barra superior */
        color: white; /* Asegura que el contenido (como el botón de Deploy) sea visible */
    }

    /* Opcional: Si quieres cambiar el color de los elementos de navegación en el sidebar */
    .st-emotion-cache-nahz7x { /* Este selector puede variar, pero apunta a los enlaces de página */
        color: #2A4068; /* Un gris claro para el texto de los enlaces en el sidebar */
    }
    .st-emotion-cache-nahz7x:hover {
        background-color: #2A4068; /* Azul más claro al pasar el ratón */
        color: white;
    }
    .st-emotion-cache-nahz7x.active { /* Para la página activa en el sidebar */
        background-color: #2A4068; /* Tu color principal para la página activa */
        color: white;
        font-weight: bold;
    }

</style>
""", unsafe_allow_html=True)
# --- FIN DEL CÓDIGO CSS PERSONALIZADO ---

# ... el resto de tu código de la página ...
st.title("Insulink")

col_vacia_izq_img, col_central_img, col_vacia_der_img = st.columns([1.5, 2, 1])
with col_central_img:
    st.image(
        "https://drive.google.com/file/d/1Z4Zel77PUJjn6q_PpG9DEFKANKtyiZd6/view?usp=drive_link", # Reemplaza esta URL con la URL de tu imagen
        caption="Con vos, siempre", # Texto opcional que aparece debajo de la imagen
        width=200, # Ancho de la imagen en píxeles. Ajusta este valor si es muy grande o pequeño.
                   # Si quieres que la imagen ocupe todo el ancho de esta columna central,
                   # puedes quitar 'width=200' y usar 'use_column_width=True' en su lugar.
        # use_column_width=True # Opción alternativa para que la imagen se ajuste al ancho de la columna central
        
    )
    st.subheader("Parra entretainments")
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