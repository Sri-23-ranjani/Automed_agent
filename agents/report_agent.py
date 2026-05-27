from pypdf import PdfReader
import docx

def extract_report_text(file_path):
    if file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    if file_path.endswith(".docx"):
        document = docx.Document(file_path)
        return "\n".join([para.text for para in document.paragraphs])

    if file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    return "Unsupported file format."

def summarize_report_agent(report_text):
    if not report_text.strip():
        return "No readable text found in the uploaded report."

    return f"""
Medical Report Upload Agent:

Report content extracted successfully.

Key report text preview:
{report_text[:1500]}

Note:
This report summary is for informational purposes only. Please consult a qualified doctor for interpretation.
"""