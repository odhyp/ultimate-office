import streamlit as st
import pandas as pd
import tempfile

# Streamlit UI to upload .xls file
st.title("XLS to XLSX Converter")

uploaded_file = st.file_uploader("Upload an .xls file", type="xls")

if uploaded_file is not None:
    # Create a temporary directory to store the .xlsx file
    with tempfile.TemporaryDirectory() as tmpdirname:
        # Read the uploaded .xls file
        try:
            df = pd.read_excel(uploaded_file, engine='xlrd')
            st.write("File read successfully!")
            
            # Create a path for the temporary .xlsx file
            xlsx_path = f"{tmpdirname}/converted_file.xlsx"
            
            # Save the dataframe to a new .xlsx file
            df.to_excel(xlsx_path, index=False, engine='openpyxl')
            st.write("File converted to .xlsx successfully!")
            
            # Provide a download link for the .xlsx file
            with open(xlsx_path, 'rb') as f:
                st.download_button(
                    label="Download converted .xlsx file",
                    data=f,
                    file_name="converted_file.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
        
        except Exception as e:
            st.error(f"An error occurred: {e}")

