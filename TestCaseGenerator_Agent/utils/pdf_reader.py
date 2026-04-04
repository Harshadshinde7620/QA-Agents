import pdfplumber


def extract_text_from_pdf(file_path):
    try:
        text = ""

        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

        return text.strip()

    except Exception as e:
        return f"PDF Processing Error: {str(e)}"