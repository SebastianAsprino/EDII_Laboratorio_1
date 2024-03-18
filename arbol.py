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
    if nodo is None:
      return 0
    return nodo.altura