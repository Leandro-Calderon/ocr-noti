import re


def extraer_palabras(texto):
    """Extrae todas las palabras del texto."""
    return re.findall(r"\b\w+\b", texto)


def extraer_numeros(texto):
    """Extrae todos los números del texto."""
    return re.findall(r"\b\d+\b", texto)
