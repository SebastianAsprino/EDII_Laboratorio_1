## Definición del módulo arbol
class arbol:
  """
  Definición del módulo arbol.

  Esta es la clase donde se construye el arbol AVL el cual
  sera usado para este laboratorio.

  Atributos:
  """
  
  def __init__(self):
    """
    Este metodo inicia el arbol AVL.
    Atributo:
      raiz: el nodo inicial del arbol es un objeto del tipo nodo.
    """
    self.raiz = None

  def altura(self, nodo):
    """
    Metodo el cual retorna 0 si estamos en una hoja, sino retorna la altura del nodo.
    """
    if nodo is None:
      return 0
    return nodo.altura
  
  def balance(self, nodo):
    """
    Metodo que revisa el balance del subarbol de cada nodo.
    """
    if nodo is None:
        return 0
    return self.altura(nodo.izquierda) - self.altura(nodo.derecha)
  

