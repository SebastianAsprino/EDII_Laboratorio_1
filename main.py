from arbol import arbol

if __name__ == "__main__":
    mi_arbol = arbol()
    mi_arbol.raiz = mi_arbol.insertar(mi_arbol.raiz, "soy una ruta", 100)
    mi_arbol.raiz = mi_arbol.insertar(mi_arbol.raiz, "soy una ruta1", 101)
    mi_arbol.raiz = mi_arbol.insertar(mi_arbol.raiz, "soy una ruta2", 99)
    print(mi_arbol.raiz)
    print(mi_arbol.raiz.ruta)
    print(mi_arbol.raiz.id_hash)
    print(mi_arbol.raiz.altura)
    print(mi_arbol.raiz.izquierda)
    print(mi_arbol.raiz.derecha)

