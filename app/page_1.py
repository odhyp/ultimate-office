import streamlit as st

st.set_page_config(
    page_title="File Converter - Ultimate Office",
    page_icon=":briefcase:",
    layout="wide"
)

# define three tabs
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

# tab 1
with tab1:
    st.title("Tab 1")
    st.write("This is the content of Tab 1.")

# tab 2
with tab2:
    st.title("Tab 2")
    st.text("This is the content of Tab 2.")

# tab 3
with tab3:
    st.title("Tab 3")
    st.text("This is the content of Tab 3.")
