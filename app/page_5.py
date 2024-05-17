import streamlit as st
import tempfile
import subprocess
import os

# Full path to pdfsizeopt executable
PDFSIZEOPT_PATH = "C:/path/to/pdfsizeopt"

# Streamlit UI for PDF compression using pdfsizeopt
st.title("PDF Compressor with pdfsizeopt")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Create a temporary directory to store the compressed PDF
    with tempfile.TemporaryDirectory() as tmpdirname:
        # Save the uploaded PDF file to a temporary location
        uploaded_pdf_path = os.path.join(tmpdirname, uploaded_file.name)
        with open(uploaded_pdf_path, 'wb') as f:
            f.write(uploaded_file.read())
        
        # Create a path for the compressed PDF file
        compressed_pdf_path = os.path.join(tmpdirname, "compressed_file.pdf")
        
        try:
            # Execute pdfsizeopt to compress the PDF
            subprocess.run([PDFSIZEOPT_PATH, uploaded_pdf_path, compressed_pdf_path])
            st.write("PDF compressed successfully!")
            
            # Provide a download link for the compressed PDF file
            with open(compressed_pdf_path, 'rb') as f:
                st.download_button(
                    label="Download compressed PDF file",
                    data=f,
                    file_name="compressed_file.pdf",
                    mime="application/pdf"
                )
        
        except subprocess.CalledProcessError as e:
            st.error(f"Compression failed. Error: {e}")
