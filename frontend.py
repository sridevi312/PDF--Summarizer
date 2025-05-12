import streamlit as st
from PDF_summariser_backend import *  # Assuming local version is used now

def main():
    # Page configuration
    st.set_page_config(page_title="Summarizer", layout="wide")

    # Page layout
    st.title("PDF SUMMARIZER")
    st.write("Summarize your Confidential PDFs in seconds")
    st.divider()

    # Custom CSS styles
    st.markdown("""
        <style>
            .st-emotion-cache-vk3wp9.eczjsme11 { background-color: #EAEAEA; color: #333333; }
            .st-emotion-cache-13ejsyy.ef3psqc12 { background-color: #008080; color: #EAEAEA; }
            .st-emotion-cache-taue2i.e1b2p2ww15 { background-color: #F5F5F5; border: 1px solid #008080; }
            .st-emotion-cache-10trblm.e1nzilvr1 { color: #008080; }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar UI
    with st.sidebar:
        st.subheader("Summarizer")
        st.sidebar.image("pdf.png", use_column_width=True)
        pdf = st.file_uploader('Upload your PDF Document', type='pdf', accept_multiple_files=True)
        submit = st.button("Upload")

    # Main execution
    if submit:
        st.subheader('Summary of the Files:')
        with st.spinner("Getting your PDF Summary Ready..."):
            process_pdf_text(pdf)

if __name__ == "__main__":
    main()
