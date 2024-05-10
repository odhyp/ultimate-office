import streamlit as st
from st_pages import show_pages_from_config

st.set_page_config(
    page_title="Welcome - Ultimate Office",
    page_icon=":briefcase:",
    layout="centered"
)

st.title("Welcome to Ultimate Office! :wave::nerd_face:")
st.write("This is the home page!")

show_pages_from_config()
