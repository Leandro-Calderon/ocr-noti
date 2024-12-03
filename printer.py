import os


def imprimir_documento(ruta_documento):
    """Envía el documento a imprimir."""
    os.startfile(ruta_documento, "print")  # Solo para Windows
