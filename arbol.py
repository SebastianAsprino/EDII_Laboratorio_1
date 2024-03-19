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
    """
    Metodo que hace la rotaciona a la derecha.
    """
    y = z.izquierda
    x = y.derecha

    y.derecha = z
    z.izquierda = x

    z.altura = 1 + max(self.altura(z.izquierda), self.altura(z.derecha))
    y.altura = 1 + max(self.altura(y.izquierda), self.altura(y.derecha))

    return y




  def rotacion_izquierda(self, z):
    """
    Metodo que hace la rotaciona a la izquierda.
    """
    y = z.derecha
    x = y.izquierda

    y.izquierda = z
    z.derecha = x

    z.altura = 1 + max(self.altura(z.izquierda), self.altura(z.derecha))
    y.altura = 1 + max(self.altura(y.izquierda), self.altura(y.derecha))

    return y




  def insertar(self, raiz, nombre, ruta, hash_id):
    """
    Metodo que permite ingresar un nodo al arbol y valancearlo.

    Atributos:
      raiz: El objeto nodo (o hoja del arbol).
      nombre: El atributo que seusa para balancear el arbol.
      ruta: la ubicacion del archivo en la carpeta data.
      hash_id: el hash MD5 de cada archivo (pensaba usarlo
              para eliminar las imagenes que se repiten con
              nombre de archivo diferente, pero me dio flojera).
    """
    if raiz is None:
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




  def eliminar(self, raiz, nombre):

    if raiz is None:
      return raiz

    if nombre < raiz.nombre:
      raiz.izquierda = self.eliminar(raiz.izquierda, nombre)

    elif nombre > raiz.nombre:
      raiz.derecha = self.eliminar(raiz.derecha, nombre)

    else:
      if raiz.izquierda is None:
        temp = raiz.derecha
        raiz = None
        return temp
      
      elif raiz.derecha is None:
        temp = raiz.izquierda
        raiz = None
        return temp

      temp = self.min_valor_nodo(raiz.derecha)
      raiz.nombre = temp.nombre
      raiz.derecha = self.eliminar(raiz.derecha, temp.nombre)

    if raiz is None:
      return raiz

    raiz.altura = 1 + max(self.altura(raiz.izquierda), self.altura(raiz.derecha))
    balance = self.balance(raiz)

    if balance > 1 and self.balance(raiz.izquierda) >= 0:
      return self.rotacion_derecha(raiz)

    if balance < -1 and self.balance(raiz.derecha) <= 0:
      return self.rotacion_izquierda(raiz)

    if balance > 1 and self.balance(raiz.izquierda) < 0:
      raiz.izquierda = self.rotacion_izquierda(raiz.izquierda)
      return self.rotacion_derecha(raiz)

    if balance < -1 and self.balance(raiz.derecha) > 0:
      raiz.derecha = self.rotacion_derecha(raiz.derecha)
      return self.rotacion_izquierda(raiz)

    return raiz




  def min_valor_nodo(self, nodo):
        """
        Metodo que busca el nodo minimo para el
        proceso de eliminacion.
        """
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual