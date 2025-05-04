
import streamlit as st

def apply_theme():
    theme = st.session_state.get("theme", "Light Mode")  # Default if not set

    light_mode_css = """
    <style>
    header[data-testid="stHeader"] {
        background-color: #66bb6a;
    }
    [data-testid="stAppViewContainer"] {
        background-color: #e8ebe0;
        color: #000000;
    }
    [data-testid="stSidebar"] {
        background-color: #a5d6a7;
    }
    h1, h2, h3, h4, h5, h6, p, li, span, div {
        color: #5D5D5D !important;
    }
    [data-testid="stExpander"] {
        background-color: #e0f2f1;
        border: 1px solid #66bb6a;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #e0f2f1;
        color: white;
        border: 1px solid #66bb6a;
        border-radius: 10px;
    }
    .stButton>button:hover {
        background-color: #66bb6a;
        color: black;
    }
    </style>
    """

    dark_mode_css = """
    <style>
    header[data-testid="stHeader"] {
        background-color: #333;
    }
    [data-testid="stAppViewContainer"] {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    [data-testid="stSidebar"] {
        background-color: #2e2e2e;
    }
    h1, h2, h3, h4, h5, h6, p, li, span, div {
        color: #BDD9F2 !important;
    }
    [data-testid="stExpander"] {
        background-color: #333;
        border: 1px solid #66bb6a;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #333;
        color: white;
        border: 1px solid #66bb6a;
        border-radius: 10px;
    }
    .stButton>button:hover {
        background-color: #66bb6a;
        color: black;
    }
    </style>
    """

    css = light_mode_css if theme == "Light Mode" else dark_mode_css
    st.markdown(css, unsafe_allow_html=True)
