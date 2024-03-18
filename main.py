from arbol import arbol

if __name__ == "__main__":
    mi_arbol = arbol()
    mi_arbol.raiz = mi_arbol.insertar(mi_arbol.raiz, "archivo100", "/unaruta", 1)
    mi_arbol.raiz = mi_arbol.insertar(mi_arbol.raiz, "archivo101", "/unaruta", 2)
    mi_arbol.raiz = mi_arbol.insertar(mi_arbol.raiz, "archivo99", "/unaruta", 3)
    print(mi_arbol.raiz)
    print(mi_arbol.raiz.nombre)
    print(mi_arbol.raiz.ruta)
    print(mi_arbol.raiz.id_hash)
    print(mi_arbol.raiz.altura)
    print(mi_arbol.raiz.izquierda)
    print(mi_arbol.raiz.derecha)

# con 3 argumentos se rompe, al pasar 2 no, entonces pasar un objeto