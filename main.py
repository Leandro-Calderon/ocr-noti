from document_generator import generar_documento
from extractor import extraer_numeros, extraer_palabras
from ocr import realizar_ocr
from printer import imprimir_documento


def main():
    # 1. Realizar OCR
    ruta_imagen = "/home/lean/Downloads/Documento escaneado.jpg"
    texto = realizar_ocr(ruta_imagen)

    # 2. Extraer datos clave
    palabras = extraer_palabras(texto)
    numeros = extraer_numeros(texto)

    # 3. Generar documento
    ruta_documento = generar_documento(palabras, numeros)

    # 4. Imprimir documento
    imprimir_documento(ruta_documento)


if __name__ == "__main__":
    main()
