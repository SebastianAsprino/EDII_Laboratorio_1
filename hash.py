import hashlib

def generar_hash_archivo(ruta_archivo):

    with open(ruta_archivo, "rb") as archivo:
        print(ruta_archivo)
        contenido = archivo.read()
    
    hash_md5 = hashlib.md5(contenido)
    print(hash_md5)
    return hash_md5.hexdigest()