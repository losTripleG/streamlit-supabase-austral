
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

##############################################################33

st.markdown("""
    <h3 style='text-align: wide; font-size: 24px;'>¿Deseas registrarte?</h3>
""", unsafe_allow_html=True)


# Check if the user is already signed in (using session state)
if not st.session_state.get("signed_in", False):
    # If not signed in, show the sign in form
    with st.form("signin_form"):
        username = st.text_input("Username (any value)")
        password = st.text_input("Password (any value)", type="password")
        submitted = st.form_submit_button("Sign in")

        if submitted:
            # For this demo, any username/password is accepted
            if username and password:
                st.session_state["signed_in"] = True
                st.session_state["username"] = username # Optional: store username
                st.success("Sign in successful!")
            else:
                st.error("Please enter both username and password.")
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
        username = st.text_input("Username (any value)")
        password = st.text_input("Password (any value)", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            # For this demo, any username/password is accepted
            if username and password:
                st.session_state["logged_in"] = True
                st.session_state["username"] = username # Optional: store username
                st.success("Login successful!")
            else:
                st.error("Please enter both username and password.")
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

