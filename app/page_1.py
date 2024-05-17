import streamlit as st

from src.xls_to_xlsx import convert_xls_to_xlsx

st.set_page_config(
    page_title="File Converter - Ultimate Office",
    page_icon=":briefcase:",
    layout="wide"
)


def convert_xls():
    pass
    # st.title("XLS to XLSX")
    # st.text("Convert .xls file to .xslx file")

    # input_file = st.file_uploader(
    #     "Upload your '.xls' file:", type=["xls"])

    # if input_file is not None:
    #     output_file = convert_xls_to_xlsx(input_file)

    #     st.download_button("Download XLSX", output_file)



# define three tabs
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

# tab 1
with tab1:
    convert_xls()

# tab 2
with tab2:
    st.title("Tab 2")
    st.text("This is the content of Tab 2.")

# tab 3
with tab3:
    st.title("Tab 3")
    st.text("This is the content of Tab 3.")
