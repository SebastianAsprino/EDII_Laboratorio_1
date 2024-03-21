*********Documentacion Arbol.py********

Definición del módulo arbol.
class arbol:
construccion arbol avl

Este metodo inicia el arbol AVL.
def __init__(self):

metodo: hoja return 0, sino altura.
def altura(self, nodo):
     retorna 0 si estamos en una hoja, sino retorna la altura del nodo.
   
metodo de balanceo por nodo
def balance(self, nodo):
si nodo es none,return 0
        
metodo rotacion a la derecha y a la izquierda:
  def rotacion_derecha(self, z):
    y = z.izquierda
    x = y.derecha

    y.derecha = z
    z.izquierda = x

  def rotacion_izquierda(self, z):
    y = z.derecha
    x = y.izquierda

    y.izquierda = z
    z.derecha = x

metodo de incertacion por nodo y Balanceo:
  def insertar(self, raiz, nombre, ruta, hash_id, size):

    Atributos:
      raiz: El objeto nodo (o hoja del arbol).
      nombre: El atributo que se usa para balancear el arbol.
      ruta: la ubicacion del archivo en la carpeta data.
      hash_id: el hash MD5 de cada archivo ( eliminar las imagenes que se repiten con
              nombre de archivo diferente).
   
      
    condicionales para:
    return nodo( nombre, ruta, hash_id, size)
    Se inserta un nuevo nodo en el árbol AVL.
      Se actualiza la altura del nodo actual.
      Se calcula el factor de equilibrio (balance) del nodo actual.
      Se realizan rotaciones simples o dobles según sea necesario para mantener el árbol balanceado.
      Finalmente, se devuelve el nodo actual.
      return raiz


    def eliminar(self, raiz, nombre):
     raiz: El nodo raíz del árbol binario de búsqueda.
     nombre: El nombre del nodo que se desea eliminar.
     Funcionamiento:
       Se comprueba si la raíz es nula. Si es así, se retorna None.
       Se realiza una búsqueda recursiva para encontrar el nodo con el nombre especificado.
    Si el nodo es encontrado:
      Si el nodo no tiene hijo izquierdo, se reemplaza el nodo por su hijo derecho.
      Si el nodo no tiene hijo derecho, se reemplaza el nodo por su hijo izquierdo.
      Si el nodo tiene ambos hijos, se encuentra el sucesor inmediato (el nodo más pequeño en el subárbol derecho) y se reemplaza el nodo a eliminar con este sucesor. Luego, se elimina el sucesor del subárbol derecho.
    Se actualiza la altura de la raíz y se verifica el balance del árbol.
    Se realizan rotaciones simples o dobles según sea necesario para mantener el balance del árbol.
    Se retorna la raíz actualizada del árbol.

  
Metodo que busca el nodo minimo para elproceso de eliminacion.
  def min_valor_nodo(self, nodo):
        return actual



Método que busca un nodo por su nombre en el árbol AVL.
  def buscar_por_nombre(self, raiz, nombre):   
    Args:
    - raiz: Nodo raíz del arbol actual.
    - nombre: Nombre del nodo a buscar.

Método que busca todos los nodos que pertenecen a una categoría (type) específica en el árbol AVL.
  def buscar_por_tipo(self, raiz, tipo):
    Args:
    - raiz: Nodo raíz del arbol.
    - tipo: Categoría específica que se desea buscar.
    return nodos_encontrados

muestra el recorrido por niveles, recursivamente
  def recorrido_por_niveles(self, raiz):
    Args:
      - raiz: Nodo raíz del árbol.

Imprime los nodos de un nivel específico del árbol.
  def imprimir_nivel(self, raiz, nivel):
    Args:
      - raiz: Nodo raíz del árbol.
      - nivel: Nivel del árbol que se quiere imprimir.
    
Encuentra el nivel de un nodo dado su nombre en el arbol.
  def encontrar_nivel_del_nodo(self, raiz, nombre, nivel_actual=0):
    retorna 0 si es 0
    retorna "el nivel es: {nivel_actual}"
   
encontrar_nivel_del_nodo
 Esta función encuentra el nivel de un nodo en el árbol dado su nombre.
   Parámetros:
    raiz: El nodo raíz del árbol.
    nombre: El nombre del nodo cuyo nivel se desea encontrar.
    nivel_actual: El nivel actual del nodo en el árbol (por defecto, 0).
    Funcionamiento:
Retorna el nivel del nodo cuando lo encuentra.

buscar_nodo
  Esta función busca un nodo en el árbol dado su nombre.
    raiz: El nodo raíz del árbol.
    nombre: El nombre del nodo que se desea buscar.
    Funcionamiento:
Retorna el nodo si es encontrado, o imprime un mensaje de error si el nodo no existe.

factor_balanceo
    Esta función calcula el factor de balanceo de un nodo dado.
    nodo: El nodo para el cual se desea calcular el factor de balanceo.
    Calcula la altura del subárbol izquierdo y derecho del nodo.
Retorna el factor de balanceo, que es la diferencia entre las alturas de los subárboles.

obtener_factor_balanceo
    Esta función obtiene el factor de balanceo de un nodo dado su nombre.
    raiz: El nodo raíz del árbol.
    nombre: El nombre del nodo para el cual se desea obtener el factor de balanceo.
Si el nodo es encontrado, llama a la función factor_balanceo para calcular y retornar su factor de balanceo.

encontrar_padre
    Esta función encuentra el padre de un nodo en el árbol dado su nombre.
    raiz: El nodo raíz del árbol.
    nombre: El nombre del nodo cuyo padre se desea encontrar.
    padre: El nodo padre actual durante la recursión.
Imprime el nombre del padre del nodo cuando es encontrado.

padre
    Esta función encuentra el padre de un nodo en el árbol dado su nombre.
    raiz: El nodo raíz del árbol.
    nombre: El nombre del nodo cuyo padre se desea encontrar.
    padre: El nodo padre actual durante la recursión.
    Realiza una búsqueda recursiva para encontrar el nodo con el nombre especificado.
Retorna el nodo padre cuando es encontrado.


encontrar_abuelo
Esta función encuentra el abuelo de un nodo en el árbol dado su nombre.
    raiz: El nodo raíz del árbol.
    nombre: El nombre del nodo cuyo abuelo se desea encontrar.
    Busca el padre del nodo dado su nombre.
    Si el nodo es la raíz o su padre no tiene padre, imprime un mensaje correspondiente.
    Si el nodo tiene un padre y este tiene un padre, encuentra al abuelo del nodo.
Imprime el nombre del abuelo del nodo si es encontrado.

abuelo
    Esta función encuentra el abuelo de un nodo en el árbol dado su nombre.
    raiz: El nodo raíz del árbol.
    nombre: El nombre del nodo cuyo abuelo se desea encontrar.
    Busca el padre del nodo dado su nombre.
    Si el nodo es la raíz o su padre no tiene padre, retorna None.
Retorna el abuelo del nodo si es encontrado.

encontrar_tio
    Esta función encuentra el tío de un nodo en el árbol dado su nombre.
    raiz: El nodo raíz del árbol.
    nombre: El nombre del nodo cuyo tío se desea encontrar.
    Si el nodo es la raíz o su padre no tiene padre, imprime un mensaje correspondiente.
    Busca al padre del nodo dado su nombre.
    Si no se encuentra el padre del nodo, imprime un mensaje correspondiente.
    Si el padre del nodo es el hijo izquierdo del abuelo, el tío es el hijo derecho del abuelo, y viceversa.
Imprime el nombre del tío del nodo si es encontrado.


**********Documentacion avl.py**********

Clase NodoAVL
__init__(self, valor)
Descripción:
Constructor de la clase NodoAVL. Inicializa un nodo AVL con un valor dado.

Parámetros:

valor: El valor que se almacenará en el nodo.
Atributos:

valor: El valor almacenado en el nodo.
altura: La altura del nodo en el árbol (inicializada en 1).
izquierda: Referencia al hijo izquierdo del nodo (inicializada en None).
derecha: Referencia al hijo derecho del nodo (inicializada en None).
Clase AVL
__init__(self)
Descripción:
Constructor de la clase AVL. Inicializa un árbol AVL con la raíz como None.

Atributos:

raiz: La raíz del árbol AVL (inicializada en None).
altura(self, nodo)
Descripción:
Calcula la altura de un nodo en el árbol AVL.

Parámetros:

nodo: El nodo del cual se desea conocer la altura.
Retorno:

La altura del nodo especificado.
balance(self, nodo)
Descripción:
Calcula el factor de balance de un nodo en el árbol AVL.

Parámetros:

nodo: El nodo del cual se desea calcular el factor de balance.
Retorno:

El factor de balance del nodo especificado.
insertar(self, raiz, valor)
Descripción:
Inserta un nuevo nodo con el valor dado en el árbol AVL.

Parámetros:

raiz: El nodo raíz del árbol o un subárbol.
valor: El valor que se desea insertar en el árbol.
Retorno:

La raíz del árbol AVL después de la inserción.
rotacion_izquierda(self, z)
Descripción:
Realiza una rotación a la izquierda en el nodo dado.

Parámetros:

z: El nodo alrededor del cual se realizará la rotación.
Retorno:

El nuevo nodo que se convierte en la raíz del subárbol después de la rotación.
rotacion_derecha(self, z)
Descripción:
Realiza una rotación a la derecha en el nodo dado.

Parámetros:

z: El nodo alrededor del cual se realizará la rotación.
Retorno:

El nuevo nodo que se convierte en la raíz del subárbol después de la rotación.
eliminar(self, raiz, valor)
Descripción:
Elimina un nodo con el valor dado del árbol AVL.

Parámetros:

raiz: El nodo raíz del árbol o un subárbol.
valor: El valor del nodo que se desea eliminar del árbol.
Retorno:

La raíz del árbol AVL después de la eliminación.
min_valor_nodo(self, nodo)
Descripción:
Encuentra el nodo con el valor mínimo en el subárbol dado.

Parámetros:

nodo: El nodo raíz del subárbol en el que se desea encontrar el valor mínimo.
Retorno:

El nodo con el valor mínimo en el subárbol especificado.




