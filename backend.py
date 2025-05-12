from transformers import pipeline
from PyPDF2 import PdfReader
import streamlit as st

# Load summarization pipeline using a local HuggingFace model
summarizer = pipeline("summarization", model="t5-small")

# Function to summarize the extracted text
def summarize_text(text, file_name):
    if len(text) > 1000:
        text = text[:1000]  # Limit to avoid model max input size

    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    result = f"### Summary of {file_name}:\n{summary[0]['summary_text']}"
    return result

# Main function to process the uploaded PDFs
def process_pdf_text(pdf_files):
    if pdf_files:
        for file in pdf_files:
            file_name = file.name
            pdf_reader = PdfReader(file)
            raw_text = ""

            for page in pdf_reader.pages:
                text = page.extract_text()
                if text:
                    raw_text += text

            if raw_text.strip() == "":
                st.warning(f"No readable text found in: {file_name}")
                continue

            summary = summarize_text(raw_text, file_name)
            st.markdown(summary)
