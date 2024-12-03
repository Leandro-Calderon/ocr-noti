import pytesseract
from PIL import Image


def realizar_ocr(ruta_imagen):
    """Realiza OCR en la imagen especificada."""
    return pytesseract.image_to_string(Image.open(ruta_imagen))
