import streamlit as st
from pypdf import PdfReader
import subprocess

st.title("AI Research Copilot")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)

    text = ""
    for page in reader.pages:
        text += page.extract_text()

    st.success("PDF loaded successfully!")

    question = st.text_input("Ask a question about the paper")

    if question:
        prompt = f"""
Use the following document to answer the question.

Document:
{text}

Question:
{question}
"""

        result = subprocess.run(
            [r"C:\Users\himan\AppData\Local\Programs\Ollama\ollama.exe", "run", "tinyllama"],
            input=prompt,
            text=True,
            capture_output=True
        )

        st.write("AI Answer:")
        st.write(result.stdout)