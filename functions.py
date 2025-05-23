import psycopg2
import os
from dotenv import load_dotenv
import pandas as pd
import sqlite3


# Load environment variables from .env file
load_dotenv()

def connect_to_supabase():
    """
    Connects to the Supabase PostgreSQL database using transaction pooler details
    and credentials stored in environment variables.
    """
    try:
        # Retrieve connection details from environment variables
        host = os.getenv("SUPABASE_DB_HOST")
        port = os.getenv("SUPABASE_DB_PORT")
        dbname = os.getenv("SUPABASE_DB_NAME")
        user = os.getenv("SUPABASE_DB_USER")
        password = os.getenv("SUPABASE_DB_PASSWORD")

        # Check if all required environment variables are set
        if not all([host, port, dbname, user, password]):
            print("Error: One or more Supabase environment variables are not set.")
            print("Please set SUPABASE_DB_HOST, SUPABASE_DB_PORT, SUPABASE_DB_NAME, SUPABASE_DB_USER, and SUPABASE_DB_PASSWORD.")
            return None

        # Establish the connection
        conn = psycopg2.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password,
        )
        print("Successfully connected to Supabase database.")
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to Supabase database: {e}")
        return None


def execute_query(query, params=None, conn=None, is_select=True):
    """
    Executes a SQL query with optional parameters. Returns a pandas DataFrame for SELECT queries,
    or executes DML operations (INSERT, UPDATE, DELETE) and returns success status.

    Args:
        query (str): The SQL query to execute
        params (tuple or list, optional): Parameters to pass to the query safely
        conn (psycopg2.extensions.connection, optional): Database connection object.
            If None, a new connection will be established.
        is_select (bool, optional): Whether the query is a SELECT query (True) or 
            a DML operation like INSERT/UPDATE/DELETE (False). Default is True.

    Returns:
        pandas.DataFrame or bool: A DataFrame containing the query results for SELECT queries,
            or True for successful DML operations, False otherwise.
    """
    try:
        # Create a new connection if one wasn't provided
        close_conn = False
        if conn is None:
            conn = connect_to_supabase()
            close_conn = True

        # Create cursor and execute query
        cursor = conn.cursor()

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        if is_select:
            # Fetch all results for SELECT queries
            results = cursor.fetchall()

            # Get column names from cursor description
            colnames = [desc[0] for desc in cursor.description]

            # Create DataFrame
            result = pd.DataFrame(results, columns=colnames)
        else:
            # For DML operations, commit changes and return success
            conn.commit()
            result = True

        # Close cursor and connection if we created it
        cursor.close()
        if close_conn:
            conn.close()

        return result

    except Exception as e:
        print(f"Error executing query: {e}")
        # Rollback any changes if an error occurred during DML operation
        if conn and not is_select:
            conn.rollback()
        return pd.DataFrame() if is_select else False


def add_paciente(nombre_apellido, id_paciente, tipo_diabetes, sexo, dispositivo, altura, fecha_nacimiento, act_fisica):
    # Normalización de entradas
    nombre_apellido = nombre_apellido.strip().title()  # Capitaliza nombre
    id_paciente = id_paciente.strip()  # Elimina espacios accidentales

    query = """
        INSERT INTO paciente (
            nombre_apellido,
            id_paciente,
            tipo_diabetes,
            sexo,
            dispositivo,
            altura,
            fecha_nacimiento,
            act_fisica
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    params = (
        nombre_apellido,
        id_paciente,
        int(tipo_diabetes),
        sexo,
        dispositivo,
        float(altura),
        fecha_nacimiento,
        bool(act_fisica)
    )
    try:
        execute_query(query, params=params, is_select=False)
        return True
    except Exception as e:
        print(f"Error en add_paciente: {e}")
        return False

def add_medico(id_medico, nombre_apellido, hospital):
    """
    Adds a new employee to the Empleado table.
    """
    # Normalización de entradas
    nombre_apellido = nombre_apellido.strip().title()  # Capitaliza nombre
    id_medico = id_medico.strip()  # Elimina espacios accidentales

    query = """INSERT INTO "Médico" (id_medico, nombre_apellido, hospital) VALUES (%s, %s, %s)"""
    params = (id_medico, nombre_apellido, hospital)
    
    try:
        execute_query(query, params=params, is_select=False)
        return True
    except Exception as e:
        print(f"Error en add_medico: {e}")
        return False

import psycopg2

def verify_medico(nombre_apellido, id_medico):
    try:
        # Conexión a Supabase PostgreSQL
        conn = psycopg2.connect(
            host="aws-0-us-east-1.pooler.supabase.com",
            port=5432,
            database="postgres",
            user="postgres.nuauokteicgejvyestli",
            password="Kr7SGT_er?WQHkf"
        )
        cursor = conn.cursor()

        # Consulta SQL con comillas por el nombre de tabla con tilde y mayúscula
        cursor.execute("""
            SELECT * FROM "Médico" 
            WHERE nombre_apellido = %s AND id_medico = %s
        """, (nombre_apellido, id_medico))

        resultado = cursor.fetchone()
        cursor.close()
        conn.close()

        return resultado is not None

    except Exception as e:
        print(f"Ocurrió un error al verificar el médico: {e}")
        return False



print(os.getenv("SUPABASE_DB_HOST"))
print(os.getenv("SUPABASE_DB_PORT"))
print(os.getenv("SUPABASE_DB_NAME"))
print(os.getenv("SUPABASE_DB_USER"))
print(os.getenv("SUPABASE_DB_PASSWORD"))



def check_paciente_login(id_paciente, nombre_apellido):
    query = """
        SELECT * FROM "Pacientes"
        WHERE id_paciente = %s AND LOWER(TRIM(nombre_apellido)) = %s
    """
    params = (id_paciente.strip(), nombre_apellido.strip().lower())
    result = execute_query(query, params=params, is_select=True)
    return not result.empty
# En tu archivo functions.py, al final o donde desees añadir nuevas funciones



###################################################################################

def get_paciente_info(id_paciente):
    """
    Busca la información de un paciente por su DNI (id_paciente) en la tabla "Pacientes" de Supabase.

    Args:
        id_paciente (str): El DNI del paciente a buscar.

    Returns:
        dict or None: Un diccionario con la información del paciente si se encuentra.
                      Las claves del diccionario serán los nombres de las columnas.
                      Retorna None si el paciente no existe o si ocurre un error.
    """
    # Consulta SQL para seleccionar todas las columnas del paciente por su DNI
    # ¡Importante! Asegúrate de que "paciente" es el nombre exacto de tu tabla en Supabase.
    # Y que las columnas que se seleccionan ('nombre_apellido', 'id_paciente', etc.)
    # coincidan con los nombres reales de tus columnas en la tabla 'paciente'.
    query = """
        SELECT nombre_apellido, id_paciente, tipo_diabetes, sexo, dispositivo, altura, fecha_nacimiento, act_fisica
        FROM "Pacientes"
        WHERE id_paciente = %s
    """
    params = (id_paciente,)
    
    # Ejecuta la consulta usando tu función existente execute_query
    # is_select=True es el valor por defecto, pero lo dejamos explícito por claridad.
    result_df = execute_query(query, params=params, is_select=True)
    
    if not result_df.empty:
        # Si se encontró al menos una fila, toma la primera y conviértela a un diccionario.
        return result_df.iloc[0].to_dict()
    else:
        # Si el DataFrame está vacío, significa que el paciente no fue encontrado.
        return None
    
################################################################################

def obtener_paciente_por_dni(id_paciente):
    try:
        conn = psycopg2.connect(
            host="aws-0-us-east-1.pooler.supabase.com",
            port=5432,
            database="postgres",
            user="postgres.nuauokteicgejvyestli",
            password="Kr7SGT_er?WQHkf"
        )
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT * FROM "Pacientes"
            WHERE id_paciente = %s
        """, (id_paciente,))
        
        paciente = cursor.fetchone()

        cursor.close()
        conn.close()

        return paciente

    except Exception as e:
        print(f"Error al buscar paciente: {e}")
        return None
