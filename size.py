import os

def tamano_archivo(ruta_archivo):
  """
  Retorna el tañamo de un archivo.

  Parámetros:
    ruta_archivo: La ruta del archivo para el cual se sabra su tamaño.
  """  
  tamano_bytes = os.path.getsize(ruta_archivo)
  return tamano_bytes

