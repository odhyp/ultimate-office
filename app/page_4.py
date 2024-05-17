import streamlit as st
import fitz  # PyMuPDF
import tempfile

# Streamlit UI for PDF compression
st.title("PDF Compressor with PyMuPDF")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Create a temporary directory to store the compressed PDF
    with tempfile.TemporaryDirectory() as tmpdirname:
        # Read the uploaded PDF file
        try:
            input_pdf_path = f"{tmpdirname}/input_file.pdf"
            output_pdf_path = f"{tmpdirname}/compressed_file.pdf"
            
            with open(input_pdf_path, 'wb') as f:
                f.write(uploaded_file.getbuffer())
            
            # Open the PDF with PyMuPDF
            pdf_document = fitz.open(input_pdf_path)

            # Compressing the PDF
            pdf_document.save(output_pdf_path, deflate=True)

            st.write("PDF compressed successfully!")

            # Provide a download link for the compressed PDF file
            with open(output_pdf_path, 'rb') as f:
                st.download_button(
                    label="Download compressed PDF file",
                    data=f,
                    file_name="compressed_file.pdf",
                    mime="application/pdf"
                )

        except Exception as e:
            st.error(f"An error occurred: {e}")

