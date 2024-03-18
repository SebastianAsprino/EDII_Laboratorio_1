from nodo import nodo

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




  def rotacion_derecha(self, z):
    y = z.izquierda
    x = y.derecha

    y.derecha = z
    z.izquierda = x

    z.altura = 1 + max(self.altura(z.izquierda), self.altura(z.derecha))
    y.altura = 1 + max(self.altura(y.izquierda), self.altura(y.derecha))

    return y




  def rotacion_izquierda(self, z):
    y = z.derecha
    x = y.izquierda

    y.izquierda = z
    z.derecha = x

    z.altura = 1 + max(self.altura(z.izquierda), self.altura(z.derecha))
    y.altura = 1 + max(self.altura(y.izquierda), self.altura(y.derecha))

    return y
  



  def insertar(self, raiz, nombre, ruta, hash_id):
    """

    """
    if raiz is None:
      # ruta = "test"
      return nodo( nombre, ruta, hash_id)
    elif nombre < raiz.nombre:
      raiz.izquierda = self.insertar(raiz.izquierda, nombre, ruta, hash_id)
    elif nombre > raiz.nombre:
      raiz.derecha = self.insertar(raiz.derecha, nombre, ruta, hash_id)
    else:
      return raiz

    raiz.altura = 1 + max(self.altura(raiz.izquierda), self.altura(raiz.derecha))

    balance = self.balance(raiz)

    if balance > 1 and nombre < raiz.izquierda.nombre:
      return self.rotacion_derecha(raiz)
    
    if balance < -1 and nombre > raiz.derecha.nombre:
      return self.rotacion_izquierda(raiz)
    
    if balance > 1 and nombre > raiz.izquierda.nombre:
      raiz.izquierda = self.rotacion_izquierda(raiz.izquierda)
      return self.rotacion_derecha(raiz)
    
    if balance < -1 and nombre < raiz.derecha.nombre:
      raiz.derecha = self.rotacion_derecha(raiz.derecha)
      return self.rotacion_izquierda(raiz)

    return raiz