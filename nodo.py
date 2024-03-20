## Definición del módulo Nodo
class nodo:
  """
  Definición del módulo Nodo.

  Esta clase crea el nodo que representa una hoja o rama del árbol.

  Atributos:
    nombre: El nombre del archivo usado para determinar si un archivo es mayor o menor.
    hash: El hash almacena el md5 del archivo.
    ruta: La ruta del archivo.
    altura: La altura del nodo en el arbol.
    izquierda: Referencia al hijo izquierdo del nodo.
    derecha: Referencia al hijo derecho del nodo.
  """
  def __init__(self, nombre, ruta, id_hash, size):
    """
    Parámetros:
      nombre: El nombre del archivo.
      ruta: La ruta del archivo en data.
      hash: El hash del archivo.
      """
    self.nombre = nombre
    self.ruta = ruta
    self.id_hash = id_hash
    self.size = size
    self.altura = 1
    self.izquierda = None
    self.derecha = None
