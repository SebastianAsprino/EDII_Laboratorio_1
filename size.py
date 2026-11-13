"""Tamaño de un archivo en disco."""

import os


def tamano_archivo(ruta_archivo: str) -> int:
    """
    Retorna el tamaño de un archivo en bytes.

    Parámetros:
        ruta_archivo: Ruta del archivo cuyo tamaño se quiere conocer.
    """
    return os.path.getsize(ruta_archivo)
