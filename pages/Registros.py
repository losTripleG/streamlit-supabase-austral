
##REGISTRO DE GLUCOSA DE LOS PACIENTES

import streamlit as st
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions import connect_to_supabase, execute_query


# 

# Verificar si el paciente está logueado
if "login_id" not in st.session_state or st.session_state["login_id"] is None:
    st.error("Por favor, iniciá sesión primero en la página principal.")
    st.stop()

id_paciente = st.session_state["login_id"]

st.title("Registro de Glucosa")
st.subheader("Agregar nueva medición")

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
    ORDER BY fecha DESC
"""
mediciones_df = execute_query(query_select, (id_paciente,))
if not mediciones_df.empty:
    st.dataframe(mediciones_df)
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

    st.dataframe(insulina_df)

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
