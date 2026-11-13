"""Cálculo del hash MD5 de un archivo."""

import hashlib

TAMANO_BLOQUE = 65536


def generar_hash_archivo(ruta_archivo: str) -> str:
    """
    Genera el hash MD5 de un archivo.

    El MD5 se usa solo como huella para identificar archivos con el mismo
    contenido (no con fines de seguridad). El archivo se lee por bloques para no
    cargarlo completo en memoria.

    Parámetros:
        ruta_archivo: Ruta del archivo para el cual se calculará el hash.

    Retorna:
        El hash del archivo en hexadecimal.
    """
    hash_md5 = hashlib.md5(usedforsecurity=False)
    with open(ruta_archivo, "rb") as archivo:
        for bloque in iter(lambda: archivo.read(TAMANO_BLOQUE), b""):
            hash_md5.update(bloque)
    return hash_md5.hexdigest()
