import pytesseract
from PIL import Image
from icecream import ic


# Extraer texto desde una imagen PNG
image = Image.open("/home/lean/Downloads/Documento escaneado-1.jpg")
texto = pytesseract.image_to_string(image, lang="spa")
ic(texto)
