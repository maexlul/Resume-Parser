Resume-Parser

A Streamlit application that automatically extracts structured candidate information from PDF or DOCX resumes (including scanned PDFs via OCR) and presents it in-browser with options to download JSON data or a formatted PDF summary.

resume-parser/
├── app.py             
├── file_handler.py    
├── ner_agent.py       
├── postprocess.py     
├── pdf_writer.py      
├── requirements.txt   
└── README.md

Features

- **Multi‐format support**: Ingest digital PDFs, scanned PDFs (via Tesseract OCR), and DOCX files  
- **Robust text extraction**:  
  - PyMuPDF for native PDF text  
  - Tesseract OCR fallback for image‐only pages  
  - python-docx for Word documents  
- **NLP‐powered parsing**:  
  - spaCy NER to identify names (PERSON) and locations (GPE)  
  - Regex patterns for email and phone number extraction  
  - Section‐based heuristics for Summary, Education, Work Experience, Skills, Certifications, and Extracurriculars  
- **Post‐processing**: Cleans whitespace, normalizes fields, removes duplicates  
- **Interactive UI**:  
  - Drag-and-drop or browse to upload one or multiple resumes  
  - On-screen tables for Profile, Education, Experience, Skills, etc.  


To Run: 
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py
