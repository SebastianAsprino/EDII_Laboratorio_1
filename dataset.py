"""Carga del dataset de imágenes (carpeta ``data``) en el árbol AVL."""

import os

from arbol import Arbol
from hash import generar_hash_archivo
from size import tamano_archivo

DIRECTORIO_DATOS = "data"
CATEGORIAS = ("bike", "cars", "cats", "dogs", "flowers", "horses", "human")


def ruta_categoria(categoria: str) -> str:
    """Retorna la ruta de la carpeta de una categoría del dataset."""
    return os.path.join(DIRECTORIO_DATOS, categoria)


def agregar_imagenes_al_arbol(arbol: Arbol, directorio: str) -> None:
    """
    Inserta en el árbol cada archivo de ``directorio``.

    Para cada archivo se guarda su nombre, ruta, hash MD5 y tamaño en bytes.

    Parámetros:
        arbol: Árbol AVL donde se insertan los archivos.
        directorio: Carpeta con las imágenes de una categoría.
    """
    print(f"Imágenes en {directorio} agregadas al arbol:")
    for nombre_archivo in os.listdir(directorio):
        ruta_archivo = os.path.join(directorio, nombre_archivo)
        if os.path.isfile(ruta_archivo):
            md5 = generar_hash_archivo(ruta_archivo)
            size = tamano_archivo(ruta_archivo)
            arbol.raiz = arbol.insertar(arbol.raiz, nombre_archivo, ruta_archivo, md5, size)


def cargar_categorias(arbol: Arbol, categorias=CATEGORIAS) -> None:
    """Inserta en el árbol todas las imágenes de las categorías indicadas."""
    for categoria in categorias:
        agregar_imagenes_al_arbol(arbol, ruta_categoria(categoria))
