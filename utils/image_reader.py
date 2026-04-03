import pytesseract
from PIL import Image


def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)

        text = pytesseract.image_to_string(img)

        return text.strip()

    except Exception as e:
        return f"Image Processing Error: {str(e)}"