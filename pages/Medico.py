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
st.title("Médico")

##############################################################

##############################################################

st.markdown("""
    <h3 style='text-align: wide; font-size: 24px;'>¿Deseas registrarte?</h3>
""", unsafe_allow_html=True)


# Check if the user is already signed in (using session state)
if not st.session_state.get("signed_in", False):
    # If not signed in, show the sign in form
    with st.form("signin_form"):
        username = st.text_input("Nombre de usuario")
        password = st.text_input("Contraseña", type="password")
        submitted = st.form_submit_button("Registrarse")

        if submitted:
            # For this demo, any username/password is accepted
            if username and password:
                st.session_state["signed_in"] = True
                st.session_state["username"] = username # Optional: store username
                st.success("Usuario registrado correctamente! 😃")
            else:
                st.error("Por favor, ingrese nombre de usuario y contraseña. 😠")
else:
    # If signed in, show a welcome message
    st.success(f"Welcome, {st.session_state.get('username', 'User')}!")
    st.info("Navigate using the sidebar on the left to manage different sections.")
    #st.balloons() # Fun little animation

    # Optional: Add a logout button
    if st.button("Logout"):
        del st.session_state["logged_in"]
        if "username" in st.session_state:
            del st.session_state["username"]

##################################################################

st.markdown("""
    <h3 style='text-align: wide; font-size: 24px;'>¿Deseas iniciar sesión?</h3>
""", unsafe_allow_html=True)
# Check if the user is already logged in (using session state)
if not st.session_state.get("logged_in", False):
    # If not logged in, show the login form
    with st.form("login_form"):
        username = st.text_input("Nombre de usuario")
        password = st.text_input("Contraseña", type="password")
        submitted = st.form_submit_button("Iniciar sesión")

        if submitted:
            # For this demo, any username/password is accepted
            if username and password:
                st.session_state["logged_in"] = True
                st.session_state["username"] = username # Optional: store username
                st.success("Inicio exitoso! 👍")
            else:
                st.error("Por favor, ingrese nombre de usuario y contraseña. 😠")
else:
    # If logged in, show a welcome message
    st.success(f"Welcome back, {st.session_state.get('username', 'User')}!")
    st.info("Navigate using the sidebar on the left to manage different sections.")
    #st.balloons() # Fun little animation

    # Optional: Add a logout button
    if st.button("Logout"):
        del st.session_state["logged_in"]
        if "username" in st.session_state:
            del st.session_state["username"]