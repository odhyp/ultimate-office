import streamlit as st
import PyPDF2
import tempfile
from PyPDF2 import PdfReader, PdfWriter

# Streamlit UI for PDF compression
st.title("PDF Compressor")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Create a temporary directory to store the compressed PDF
    with tempfile.TemporaryDirectory() as tmpdirname:
        # Read the uploaded PDF file
        try:
            reader = PdfReader(uploaded_file)
            writer = PdfWriter()

            # Compress the PDF
            for page in reader.pages:
                page.compress_content_streams()
                writer.add_page(page)

            # Create a path for the temporary compressed PDF file
            compressed_pdf_path = f"{tmpdirname}/compressed_file.pdf"
            
            # Write the compressed PDF to the file
            with open(compressed_pdf_path, 'wb') as f:
                writer.write(f)
            
            st.write("PDF compressed successfully!")
            
            # Provide a download link for the compressed PDF file
            with open(compressed_pdf_path, 'rb') as f:
                st.download_button(
                    label="Download compressed PDF file",
                    data=f,
                    file_name="compressed_file.pdf",
                    mime="application/pdf"
                )

        except Exception as e:
            st.error(f"An error occurred: {e}")

