from collections import deque
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




  def insertar(self, raiz, nombre, ruta, hash_id, size):
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
      return nodo( nombre, ruta, hash_id, size)
    elif nombre < raiz.nombre:
      raiz.izquierda = self.insertar(raiz.izquierda, nombre, ruta, hash_id, size)
    elif nombre > raiz.nombre:
      raiz.derecha = self.insertar(raiz.derecha, nombre, ruta, hash_id, size)
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
      raiz.ruta = temp.ruta
      raiz.id_hash = temp.id_hash
      raiz.size = temp.size
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




  def buscar_por_nombre(self, raiz, nombre):
    """
    Método que busca un nodo por su nombre en el árbol AVL.

    Args:
    - raiz: Nodo raíz del arbol actual.
    - nombre: Nombre del nodo a buscar.
    """
    if raiz is None:
        print("El nodo no existe")
        return None
    elif nombre == raiz.nombre:
        print(f"El nodo {nombre} con ruta en data: {raiz.ruta} y hash {raiz.id_hash} existe.")
        return raiz
    elif nombre < raiz.nombre:
        return self.buscar_por_nombre(raiz.izquierda, nombre)
    else:
        return self.buscar_por_nombre(raiz.derecha, nombre)




  def buscar_por_tipo(self, raiz, tipo):
    """
    Método que busca todos los nodos que pertenecen a una categoría (type) específica en el árbol AVL.

    Args:
    - raiz: Nodo raíz del arbol.
    - tipo: Categoría específica que se desea buscar.
    """
    nodos_encontrados = []
    if raiz is not None:
        if raiz.ruta.startswith("data\\" + tipo + "\\"):
            nodos_encontrados.append(raiz)
        nodos_encontrados.extend(self.buscar_por_tipo(raiz.izquierda, tipo))
        nodos_encontrados.extend(self.buscar_por_tipo(raiz.derecha, tipo))
    return nodos_encontrados




  def buscar_por_tipo_y_peso(self, raiz, tipo, min_size, max_size):
    """
    """
  
    nodos_encontrados = []
    if raiz is not None:
        if raiz.ruta.startswith("data\\" + tipo + "\\") and min_size <= raiz.size < max_size:
            nodos_encontrados.append(raiz)
        nodos_encontrados.extend(self.buscar_por_tipo_y_peso(raiz.izquierda, tipo, min_size, max_size))
        nodos_encontrados.extend(self.buscar_por_tipo_y_peso(raiz.derecha, tipo, min_size, max_size))
    return nodos_encontrados




  def recorrido_por_niveles(self, raiz):
    """
    Muestra el recorrido por niveles del árbol de la unica forma que lo se hacer osea recursivo.

    Args:
      - raiz: Nodo raíz del árbol.
    """
    altura = self.altura(raiz)
    for nivel in range(1, altura + 1):
      print(f"nivel: {nivel-1}")
      self.imprimir_nivel(raiz, nivel)

  def imprimir_nivel(self, raiz, nivel):
    """
    Imprime los nodos de un nivel específico del árbol.

    Args:
      - raiz: Nodo raíz del árbol.
      - nivel: Nivel del árbol que se quiere imprimir.
    """
    if raiz is None:
      return
    if nivel == 1:
      print(raiz.nombre)
    elif nivel > 1:
      self.imprimir_nivel(raiz.izquierda, nivel - 1)
      self.imprimir_nivel(raiz.derecha, nivel - 1)





  def encontrar_nivel_del_nodo(self, raiz, nombre, nivel_actual=0):
    """
    Encuentra el nivel de un nodo dado su nombre en el arbol.
    """
    if raiz is None:
      return None
        
    if raiz.nombre == nombre:
      return print(f"el nivel es: {nivel_actual}")
        
    nivel_izquierda = self.encontrar_nivel_del_nodo(raiz.izquierda, nombre, nivel_actual + 1)
    if nivel_izquierda is not None:
      return nivel_izquierda
        
    nivel_derecha = self.encontrar_nivel_del_nodo(raiz.derecha, nombre, nivel_actual + 1)
    return nivel_derecha




  def buscar_nodo(self, raiz, nombre):

    if raiz is None:
        print("El nodo no existe")
        return None
    elif nombre == raiz.nombre:
        return raiz
    elif nombre < raiz.nombre:
        return self.buscar_nodo(raiz.izquierda, nombre)
    else:
        return self.buscar_nodo(raiz.derecha, nombre)




  def factor_balanceo(self, nodo):

    if nodo is None:
      return 0
    altura_izquierda = self.altura(nodo.izquierda)
    altura_derecha = self.altura(nodo.derecha)
    return print(f"el factor de equilobrio del nodo es: {altura_izquierda - altura_derecha}")
    
    
    
    
  def obtener_factor_balanceo(self, raiz, nombre):
    nodo = self.buscar_nodo(raiz, nombre)
    if nodo is not None:
      return self.factor_balanceo(nodo)
    else:
        return None




  def encontrar_padre(self, raiz, nombre, padre=None):

    if raiz is None:
      return None
        
    if raiz.nombre == nombre:
      if padre is not None:
        print(f"El nodo padre de {nombre} es: {padre.nombre}")
      else:
        print(f"{nombre} es la raíz del árbol.")
      return
        
    self.encontrar_padre(raiz.izquierda, nombre, raiz)
        
    self.encontrar_padre(raiz.derecha, nombre, raiz)




  def padre(self, raiz, nombre, padre=None):

    if raiz is None:
      return None
        
    if raiz.nombre == nombre:
      return padre
        
    nodo_padre_izquierda = self.padre(raiz.izquierda, nombre, raiz)
    if nodo_padre_izquierda is not None:
      return nodo_padre_izquierda
        
    nodo_padre_derecha = self.padre(raiz.derecha, nombre, raiz)
    return nodo_padre_derecha



  
  def encontrar_abuelo(self, raiz, nombre):
        
    if raiz is None:
      return
        
        # Buscar el padre del nodo dado su nombre
    padre = self.padre(raiz, nombre)
    if padre is None or padre == raiz:
      print(f"{nombre} es la raíz del árbol o su padre no tiene padre.")
      return
        
        # Encontrar el abuelo del nodo
    abuelo = self.padre(raiz, padre.nombre)
    if abuelo is not None:
      print(f"El nodo abuelo de {nombre} es: {abuelo.nombre}")
    else:
      print(f"{nombre} es la raíz del árbol o su padre no tiene padre.")
