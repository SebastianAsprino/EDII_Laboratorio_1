## Definición del módulo Nodo
class Nodo:
    """Esta clase crea el nodo el cual es una hoja o rama
        del arbol.
    """
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


