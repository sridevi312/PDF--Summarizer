# PDF--Summarizer
A full-stack web application that extracts text from PDF files and generates concise summaries using the  OpenAI GPT. Designed for students, researchers, and professionals who want quick insights from lengthy PDFs.

 Features
 
 Upload one or more PDF files for instant processing
 AI-powered summarization using OpenAI GPT
 Accurate text extraction using PyPDF2
 Semantic chunking + vector storage using LangChain + FAISS
 Instant result display via a Streamlit web interface
 Secure API key management using .env and constants.py
 Modular code structure with room for user auth, history tracking, and cloud deployment

 | Layer                | Technology Used              |
| -------------------- | ---------------------------- |
| Frontend             | Streamlit (with custom CSS)  |
| PDF Processing       | PyPDF2                       |
| AI Summarization     | OpenAI GPT (via LangChain)   |
| Chunking & Embedding | LangChain                    |
| Vector Search        | FAISS                        |
| API Key Handling     | python-dotenv + constants.py |

Architecture


 <img width="400" height="450" alt="image" src="https://github.com/user-attachments/assets/8d0466e8-58a2-4f16-a988-d7f65e18dc6b" />



