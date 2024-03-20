import hashlib

def generar_hash_archivo(ruta_archivo):
    """
    Genera el hash MD5 de un archivo pasado por parametro.

    Parámetros:
        ruta_archivo: La ruta del archivo para el cual se calculará el hash.

    Retorna:
        hash_md5: El hash del archivo en formato string.
    """
    with open(ruta_archivo, "rb") as archivo:
        contenido = archivo.read()
    
    hash_md5 = hashlib.md5(contenido)

    return hash_md5.hexdigest()