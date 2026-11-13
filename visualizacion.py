"""Renderizado del árbol AVL como imagen con Graphviz."""

import graphviz

from arbol import Arbol

DIRECTORIO_SALIDA = "salida"
NOMBRE_GRAFO = "avl_tree"


def renderizar_arbol(arbol: Arbol, directorio: str = DIRECTORIO_SALIDA, abrir: bool = True) -> str:
    """
    Dibuja el árbol en un PNG y opcionalmente lo abre con el visor del sistema.

    Parámetros:
        arbol: Árbol AVL a dibujar.
        directorio: Carpeta donde se guarda la imagen.
        abrir: Si es ``True``, abre la imagen generada.

    Retorna:
        La ruta del PNG generado.
    """
    dot = graphviz.Digraph()
    arbol.print_avl_tree(arbol.raiz, dot)
    return dot.render(NOMBRE_GRAFO, format="png", directory=directorio, cleanup=True, view=abrir)
