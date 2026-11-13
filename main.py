"""
Demostración por consola de las operaciones del árbol AVL sobre el dataset.

Carga todas las imágenes de ``data/`` en el árbol y ejecuta, paso a paso,
cada una de las operaciones implementadas en ``arbol.py``. Al final dibuja el
árbol con Graphviz.
"""

from typing import List

from arbol import Arbol
from dataset import cargar_categorias
from nodo import Nodo
from visualizacion import renderizar_arbol

TIPO_A_BUSCAR = "bike"
PESO_MINIMO_BYTES = 0
PESO_MAXIMO_BYTES = 90000
ANCHO_SEPARADOR = 112


def separador(lineas: int = 1) -> None:
    """Imprime líneas separadoras entre secciones de la demostración."""
    for _ in range(lineas):
        print("-" * ANCHO_SEPARADOR)


def imprimir_nodos(nodos: List[Nodo], mensaje_vacio: str) -> None:
    """Imprime la información de cada nodo, o ``mensaje_vacio`` si la lista está vacía."""
    if not nodos:
        print(mensaje_vacio)
        return
    print(f"Se encontraron nodos de tipo '{TIPO_A_BUSCAR}':")
    for nodo in nodos:
        print(f"- Nombre: {nodo.nombre}, Ruta: {nodo.ruta}, Hash: {nodo.id_hash}, size: {nodo.size}")


def demo_carga(mi_arbol: Arbol) -> None:
    """Carga todo el dataset en el árbol."""
    print("llama a la funcion cargar_categorias, un metodo automatizado de agregar")
    print("todas las imagenes del dataset al arbol.")
    cargar_categorias(mi_arbol)
    separador()
    print("por cada archivo se llama a mi_arbol.insertar(mi_arbol.raiz, nombre_archivo, ruta_archivo, md5, size)")
    print("los atributos a pasar en insertar son la raiz, el nombre del archivo, ruta de este en data, el hash y tamaño del archivo.")
    separador(2)


def demo_eliminar_y_buscar(mi_arbol: Arbol) -> None:
    """Elimina un nodo y busca nodos por nombre."""
    print("llamo al metodo .eliminar del arbol este recibe raiz y el nombre del nodo a eliminar.")
    print("en este caso elimino bike_128.bmp")
    mi_arbol.raiz = mi_arbol.eliminar(mi_arbol.raiz, "bike_128.bmp")
    separador()

    print("llamo al metodo .buscar_por_nombre, este recibe raiz y el nombre del nodo a buscar.")
    for nombre in ("bike_128.bmp", "bike_020.bmp"):
        print(f"busco {nombre}:")
        print(mi_arbol.buscar_por_nombre(mi_arbol.raiz, nombre))
    separador(3)


def demo_busqueda_por_tipo(mi_arbol: Arbol) -> None:
    """Busca nodos por categoría y por categoría + rango de tamaño."""
    print(f"busco los nodos de tipo {TIPO_A_BUSCAR}:")
    print("llamo al metodo .buscar_por_tipo que recibe raiz y la variable con el tipo a buscar.")
    nodos_encontrados = mi_arbol.buscar_por_tipo(mi_arbol.raiz, TIPO_A_BUSCAR)
    imprimir_nodos(nodos_encontrados, f"No se encontraron nodos de tipo '{TIPO_A_BUSCAR}'.")
    separador(3)

    print("el metodo buscar, pero agregando el peso del archivo en bytes.")
    nodos_encontrados = mi_arbol.buscar_por_tipo_y_peso(
        mi_arbol.raiz, TIPO_A_BUSCAR, PESO_MINIMO_BYTES, PESO_MAXIMO_BYTES
    )
    imprimir_nodos(
        nodos_encontrados,
        f"No se encontraron nodos de tipo '{TIPO_A_BUSCAR}' con tamaño entre "
        f"{PESO_MINIMO_BYTES} y {PESO_MAXIMO_BYTES} Bytes.",
    )
    separador(3)


def demo_niveles_y_balance(mi_arbol: Arbol) -> None:
    """Muestra el recorrido por niveles, el nivel de algunos nodos y su factor de balanceo."""
    print("llamo al metodo .recorrido_por_niveles el cual recibe raiz e imprime los nodos por nivel:")
    mi_arbol.recorrido_por_niveles(mi_arbol.raiz)
    separador(3)

    print("llamo al metodo .encontrar_nivel_del_nodo el cual recibe raiz y el nombre del nodo a buscar y retorna en que nivel esta si no existe retorna None: ")
    for nombre in ("bike_064.bmp", "bike_008.bmp", "bike_128.bmp"):
        print(f"busco el nodo {nombre}")
        nivel = mi_arbol.encontrar_nivel_del_nodo(mi_arbol.raiz, nombre)
        print(f"el nivel es: {nivel}" if nivel is not None else "El nodo no existe")
    separador(3)

    print("llamo al metodo .obtener_factor_balanceo el cual recibe raiz y el nombre del nodo que se sabra su nivel de balance:")
    factor = mi_arbol.obtener_factor_balanceo(mi_arbol.raiz, "bike_008.bmp")
    print(f"el factor de equilibrio del nodo es: {factor}" if factor is not None else "El nodo no existe")
    separador(3)


def demo_parentesco(mi_arbol: Arbol) -> None:
    """Muestra el padre, el abuelo y el tío de algunos nodos."""
    print("llamo al metodo .encontrar_padre el cual recibe raiz y el nombre del nodo que se sabra cual es su padre:")
    mi_arbol.encontrar_padre(mi_arbol.raiz, "bike_064.bmp")
    separador(3)

    print("llamo al metodo .encontrar_abuelo el cual recibe raiz y el nombre del nodo que se sabra cual es su abuelo:")
    mi_arbol.encontrar_abuelo(mi_arbol.raiz, "bike_064.bmp")
    separador(3)

    print("llamo al metodo .encontrar_tio el cual recibe raiz y el nombre del nodo que se sabra cual es su tio:")
    mi_arbol.encontrar_tio(mi_arbol.raiz, "bike_032.bmp")


def main() -> None:
    """Ejecuta la demostración completa."""
    print("instancio el arbol: mi_arbol")
    mi_arbol = Arbol()
    separador()

    demo_carga(mi_arbol)
    demo_eliminar_y_buscar(mi_arbol)
    demo_busqueda_por_tipo(mi_arbol)
    demo_niveles_y_balance(mi_arbol)
    demo_parentesco(mi_arbol)

    renderizar_arbol(mi_arbol)


if __name__ == "__main__":
    main()
