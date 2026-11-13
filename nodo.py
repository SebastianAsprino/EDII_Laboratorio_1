"""Definición del nodo del árbol AVL."""

from __future__ import annotations

from typing import Optional


class Nodo:
    """
    Nodo que representa una hoja o rama del árbol AVL.

    Atributos:
        nombre: Nombre del archivo; es la clave que ordena el árbol.
        ruta: Ruta del archivo dentro de la carpeta ``data``.
        id_hash: Hash MD5 del contenido del archivo.
        size: Tamaño del archivo en bytes.
        altura: Altura del nodo en el árbol (una hoja tiene altura 1).
        izquierda: Hijo izquierdo (nombres menores).
        derecha: Hijo derecho (nombres mayores).
    """

    def __init__(self, nombre: str, ruta: str, id_hash: str, size: int) -> None:
        """
        Crea un nodo hoja.

        Parámetros:
            nombre: Nombre del archivo.
            ruta: Ruta del archivo en ``data``.
            id_hash: Hash MD5 del archivo.
            size: Tamaño del archivo en bytes.
        """
        self.nombre = nombre
        self.ruta = ruta
        self.id_hash = id_hash
        self.size = size
        self.altura = 1
        self.izquierda: Optional[Nodo] = None
        self.derecha: Optional[Nodo] = None
