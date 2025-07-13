
##REGISTRO DE GLUCOSA DE LOS PACIENTES

import streamlit as st
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions import connect_to_supabase, execute_query
st.set_page_config(
    page_title="Insulink | Registros",
    page_icon="📑",
    layout="centered" # "wide" or "centered"
)
# 

# Verificar si el paciente está logueado
if "login_id" not in st.session_state or st.session_state["login_id"] is None:
    st.error("Por favor, iniciá sesión primero en la página principal.")
    st.stop()

id_paciente = st.session_state["login_id"]

st.title("Registro de Glucosa")
st.subheader("Agregar nueva medición")
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
# Formulario para ingresar datos
with st.form("formulario_medicion"):
    comida = st.text_input("¿Qué comiste?")
    resultado_glucosa = st.number_input("Resultado de glucosa (mg/dL)", min_value=0)
    fecha = st.date_input("Fecha de la medición")
    hora= st.time_input("Hora de la medicion")
    submitted = st.form_submit_button("Guardar medición") 
# Insertar en la base de datos si se envió el formulario
if submitted:
    query = """
        INSERT INTO "Medicion de glucosa" (comida, resultado_glucosa, fecha, hora, id_paciente)
        VALUES (%s, %s, %s, %s, %s)
    """
    params = (comida, resultado_glucosa, fecha, hora, id_paciente)

    success = execute_query(query, params, is_select=False)
    if success:
        st.success("Medición guardada exitosamente.")
    else:
        st.error("Error al guardar la medición.")

# Mostrar las mediciones del paciente
st.subheader("Historial de mediciones")
query_select = """
    SELECT comida, resultado_glucosa, fecha, hora
    FROM "Medicion de glucosa"
    WHERE id_paciente = %s
    ORDER BY fecha DESC, hora DESC
"""
mediciones_df = execute_query(query_select, (id_paciente,))
 # Renombrar para visualización

if not mediciones_df.empty:

    mediciones_df.columns = ["comida", "resultado_glucosa", "fecha", "hora"]
    

    mediciones_df= mediciones_df.rename(columns={
        "comida":"Comida",
        "resultado_glucosa":"Resultado Glucosa",
        "fecha":"Fecha",
        "hora":"Hora"
    })
    st.dataframe(mediciones_df, hide_index=True)
else:
    st.info("Todavía no hay mediciones registradas.")

st.title("Registro de Insulina")
# ------------------- REGISTRO DE INSULINA -------------------

st.subheader("Registrá tu Aplicación de Insulina")

with st.form("formulario_insulina"):
    dosis_insulina = st.number_input("Dosis de insulina (unidades)", min_value=0.0, step=0.5)
    tipo_inyeccion = st.selectbox("Tipo de inyección", options=["Rápida", "Lenta", "Mixta", "Otra"])
    fecha = st.date_input("Fecha de la medición")
    hora= st.time_input("Hora de la medicion")
    
    
    submitted_insulina = st.form_submit_button("Registrar aplicación")

if submitted_insulina:
    # Combinar fecha y hora de aplicación como timestamp en formato string
    fecha_hora_aplicacion = f"{fecha} {hora}"

    # Buscar la última medición de glucosa previa a esa fecha y hora
    query_glucosa = """
        SELECT resultado_glucosa
        FROM "Medicion de glucosa"
        WHERE id_paciente = %s
          AND (fecha + hora) <= %s::timestamp
        ORDER BY fecha DESC, hora DESC
        LIMIT 1
    """
    params_glucosa = (id_paciente, fecha_hora_aplicacion)
    resultado = execute_query(query_glucosa, params_glucosa, is_select=True)

    if not resultado.empty:
        medicion_prev = int(resultado["resultado_glucosa"].iloc[0])  # <- conversión aquí
    else:
        medicion_prev = None
    # Insertar el registro de insulina
    query_insert_insulina = """
        INSERT INTO "Aplicacion insulina"
        (id_paciente, dosis_insulina, tipo_inyeccion, fecha, hora, medicion_prev_registrada)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    params_insert = (
        id_paciente,
        dosis_insulina,
        tipo_inyeccion,
        fecha,
        hora,
        medicion_prev
    )
    success_insulina = execute_query(query_insert_insulina, params_insert, is_select=False)

    if success_insulina:
        st.success("Aplicación de insulina registrada correctamente.")
    else:
        st.error("Error al registrar la aplicación.")

# ------------------- HISTORIAL DE INSULINA -------------------

st.subheader("Historial de Aplicaciones de Insulina")

query_insulina = """
    SELECT id_aplicacion, fecha, hora, dosis_insulina, medicion_prev_registrada
    FROM "Aplicacion insulina"
    WHERE id_paciente = %s
    ORDER BY fecha DESC, hora DESC
"""
insulina_df = execute_query(query_insulina, (id_paciente,), is_select=True)

if not insulina_df.empty:
    # Crear columna datetime
    insulina_df["fecha_hora"] = pd.to_datetime(insulina_df["fecha"].astype(str) + " " + insulina_df["hora"].astype(str))

    # Crear una nueva columna para la medición posterior
    glucosa_post_list = []

    for _, row in insulina_df.iterrows():
        fecha_hora = row["fecha_hora"]

        query_post = """
            SELECT resultado_glucosa
            FROM "Medicion de glucosa"
            WHERE id_paciente = %s AND (fecha + hora) > %s::timestamp
            ORDER BY fecha ASC, hora ASC
            LIMIT 1
        """
        result_post = execute_query(query_post, (id_paciente, fecha_hora.strftime("%Y-%m-%d %H:%M:%S")), is_select=True)

        if not result_post.empty:
            glucosa_post_list.append(int(result_post["resultado_glucosa"].iloc[0]))
        else:
            glucosa_post_list.append(None)

    insulina_df["medicion_post_registrada"] = glucosa_post_list

    # Reordenar columnas
    insulina_df = insulina_df[["fecha_hora", "dosis_insulina", "medicion_prev_registrada", "medicion_post_registrada"]]

    # Renombrar para visualización
    insulina_df = insulina_df.rename(columns={
        "fecha_hora": "Fecha y Hora",
        "dosis_insulina": "Dosis (U)",
        "medicion_prev_registrada": "Glucosa previa (mg/dL)",
        "medicion_post_registrada": "Glucosa posterior (mg/dL)"
    })

    st.dataframe(insulina_df, hide_index=True)

else:
    st.info("Aún no se han registrado aplicaciones de insulina.")

import plotly.graph_objects as go
from datetime import datetime, timedelta

# ------------------- GRÁFICO COMBINADO -------------------
st.title("¡Mira tus Registros!")
st.subheader("Evolución de Glucosa e Insulina (últimos 7 días)")

# Calcular la fecha límite (datetime)
fecha_limite = datetime.now() - timedelta(days=7)

# --- Obtener mediciones de glucosa ---
query_glucosa = """
    SELECT fecha, hora, resultado_glucosa
    FROM "Medicion de glucosa"
    WHERE id_paciente = %s
    ORDER BY fecha, hora
"""
glucosa_df = execute_query(query_glucosa, (id_paciente,), is_select=True)

# Combinar fecha y hora en datetime y filtrar por fecha_limite en Python
if not glucosa_df.empty:
    glucosa_df["fecha_hora"] = pd.to_datetime(glucosa_df["fecha"].astype(str) + " " + glucosa_df["hora"].astype(str))
    glucosa_df = glucosa_df[glucosa_df["fecha_hora"] >= fecha_limite]

# --- Obtener aplicaciones de insulina ---
query_insulina = """
    SELECT fecha, hora, dosis_insulina
    FROM "Aplicacion insulina"
    WHERE id_paciente = %s
    ORDER BY fecha, hora
"""
insulina_df = execute_query(query_insulina, (id_paciente,), is_select=True)

# Combinar fecha y hora en datetime y filtrar por fecha_limite en Python
if not insulina_df.empty:
    insulina_df["fecha_hora"] = pd.to_datetime(insulina_df["fecha"].astype(str) + " " + insulina_df["hora"].astype(str))
    insulina_df = insulina_df[insulina_df["fecha_hora"] >= fecha_limite]

# --- Verificar que haya datos para graficar ---
if (glucosa_df.empty) and (insulina_df.empty):
    st.info("No hay datos suficientes de los últimos 7 días para graficar.")
else:
    fig = go.Figure()

    # Línea de glucosa
    if not glucosa_df.empty:
        fig.add_trace(go.Scatter(
            x=glucosa_df["fecha_hora"],
            y=glucosa_df["resultado_glucosa"],
            mode='lines+markers',
            name='Glucosa (mg/dL)',
            line=dict(color='royalblue'),
            marker=dict(size=6)
        ))

    # Puntos de insulina
    if not insulina_df.empty:
        fig.add_trace(go.Scatter(
            x=insulina_df["fecha_hora"],
            y=insulina_df["dosis_insulina"],
            mode='markers',
            name='Insulina (U)',
            marker=dict(size=10, color='crimson', symbol='circle'),
            yaxis='y2'  # eje secundario para insulina
        ))

    # Configurar ejes y layout
    fig.update_layout(
        title="Glucosa e Insulina - Últimos 7 días",
        xaxis_title="Fecha y Hora",
        yaxis=dict(title="Glucosa (mg/dL)", side="left"),
        yaxis2=dict(title="Dosis de Insulina (U)", overlaying='y', side='right'),
        legend=dict(x=0, y=1.1, orientation="h"),
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

st.title("Mensajes de tu Médico")
st.subheader("Tu médico esta al tanto de tu evolución, está al tanto de vos.")
from functions import obtener_mensaje_paciente  # Asegurate de agregar esta función también

# Obtener mensaje del médico para este paciente
mensaje = obtener_mensaje_paciente(st.session_state["login_id"])

if mensaje:
    st.info(f"📩 **Mensaje del médico:** {mensaje}")
else:
    st.info("No hay mensajes nuevos del médico.")

