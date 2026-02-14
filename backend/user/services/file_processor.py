import os


def detect_file_type(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return "pdf"
    elif ext in [".mp3", ".wav", ".m4a"]:
        return "audio"
    elif ext in [".mp4", ".mov", ".mkv"]:
        return "video"
    else:
        return "unknown"


from pypdf import PdfReader


def extract_pdf_text(file_path):
    reader = PdfReader(file_path)

    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text
