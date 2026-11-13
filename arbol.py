"""Árbol AVL de archivos ordenado por nombre."""

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Callable, List, Optional

from nodo import Nodo

if TYPE_CHECKING:
    import graphviz


class Arbol:
    """
    Árbol AVL (árbol binario de búsqueda autobalanceado) usado en el laboratorio.

    Cada nodo representa un archivo del dataset y se ordena por su nombre. Los
    métodos reciben explícitamente la raíz del (sub)árbol sobre el que operan,
    por lo que las operaciones que modifican el árbol devuelven la nueva raíz:

        arbol.raiz = arbol.insertar(arbol.raiz, ...)
        arbol.raiz = arbol.eliminar(arbol.raiz, nombre)

    Atributos:
        raiz: Nodo raíz del árbol, o ``None`` si está vacío.
    """

    def __init__(self) -> None:
        """Inicia un árbol AVL vacío."""
        self.raiz: Optional[Nodo] = None

    # ------------------------------------------------------------------
    # Altura, balance y rotaciones
    # ------------------------------------------------------------------

    def altura(self, nodo: Optional[Nodo]) -> int:
        """Retorna la altura del nodo, o 0 si el nodo no existe."""
        if nodo is None:
            return 0
        return nodo.altura

    def balance(self, nodo: Optional[Nodo]) -> int:
        """Retorna el factor de balance (altura izquierda - altura derecha) del nodo."""
        if nodo is None:
            return 0
        return self.altura(nodo.izquierda) - self.altura(nodo.derecha)

    def _actualizar_altura(self, nodo: Nodo) -> None:
        """Recalcula la altura del nodo a partir de la de sus hijos."""
        nodo.altura = 1 + max(self.altura(nodo.izquierda), self.altura(nodo.derecha))

    def rotacion_derecha(self, z: Nodo) -> Nodo:
        """Rota el subárbol con raíz ``z`` a la derecha y retorna la nueva raíz."""
        y = z.izquierda
        x = y.derecha

        y.derecha = z
        z.izquierda = x

        self._actualizar_altura(z)
        self._actualizar_altura(y)
        return y

    def rotacion_izquierda(self, z: Nodo) -> Nodo:
        """Rota el subárbol con raíz ``z`` a la izquierda y retorna la nueva raíz."""
        y = z.derecha
        x = y.izquierda

        y.izquierda = z
        z.derecha = x

        self._actualizar_altura(z)
        self._actualizar_altura(y)
        return y

    # ------------------------------------------------------------------
    # Inserción y eliminación
    # ------------------------------------------------------------------

    def insertar(
        self, raiz: Optional[Nodo], nombre: str, ruta: str, hash_id: str, size: int
    ) -> Nodo:
        """
        Inserta un archivo en el árbol y lo rebalancea.

        Si ya existe un nodo con el mismo nombre, el árbol no cambia.

        Parámetros:
            raiz: Raíz del (sub)árbol donde se inserta.
            nombre: Nombre del archivo; es la clave que ordena el árbol.
            ruta: Ubicación del archivo en la carpeta ``data``.
            hash_id: Hash MD5 del archivo.
            size: Tamaño del archivo en bytes.

        Retorna:
            La nueva raíz del (sub)árbol.
        """
        if raiz is None:
            return Nodo(nombre, ruta, hash_id, size)
        if nombre < raiz.nombre:
            raiz.izquierda = self.insertar(raiz.izquierda, nombre, ruta, hash_id, size)
        elif nombre > raiz.nombre:
            raiz.derecha = self.insertar(raiz.derecha, nombre, ruta, hash_id, size)
        else:
            return raiz

        self._actualizar_altura(raiz)
        balance = self.balance(raiz)

        # Caso izquierda-izquierda
        if balance > 1 and nombre < raiz.izquierda.nombre:
            return self.rotacion_derecha(raiz)
        # Caso derecha-derecha
        if balance < -1 and nombre > raiz.derecha.nombre:
            return self.rotacion_izquierda(raiz)
        # Caso izquierda-derecha
        if balance > 1 and nombre > raiz.izquierda.nombre:
            raiz.izquierda = self.rotacion_izquierda(raiz.izquierda)
            return self.rotacion_derecha(raiz)
        # Caso derecha-izquierda
        if balance < -1 and nombre < raiz.derecha.nombre:
            raiz.derecha = self.rotacion_derecha(raiz.derecha)
            return self.rotacion_izquierda(raiz)

        return raiz

    def eliminar(self, raiz: Optional[Nodo], nombre: str) -> Optional[Nodo]:
        """
        Elimina el nodo con el nombre dado y rebalancea el árbol.

        Si el nodo tiene dos hijos se reemplaza por su sucesor inmediato (el
        menor del subárbol derecho).

        Parámetros:
            raiz: Raíz del (sub)árbol.
            nombre: Nombre del nodo a eliminar.

        Retorna:
            La nueva raíz del (sub)árbol (``None`` si quedó vacío).
        """
        if raiz is None:
            return None

        if nombre < raiz.nombre:
            raiz.izquierda = self.eliminar(raiz.izquierda, nombre)
        elif nombre > raiz.nombre:
            raiz.derecha = self.eliminar(raiz.derecha, nombre)
        else:
            if raiz.izquierda is None:
                return raiz.derecha
            if raiz.derecha is None:
                return raiz.izquierda

            sucesor = self.min_valor_nodo(raiz.derecha)
            raiz.nombre = sucesor.nombre
            raiz.ruta = sucesor.ruta
            raiz.id_hash = sucesor.id_hash
            raiz.size = sucesor.size
            raiz.derecha = self.eliminar(raiz.derecha, sucesor.nombre)

        self._actualizar_altura(raiz)
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

    def min_valor_nodo(self, nodo: Nodo) -> Nodo:
        """Retorna el nodo de menor nombre del subárbol (usado al eliminar)."""
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    # ------------------------------------------------------------------
    # Búsquedas
    # ------------------------------------------------------------------

    def buscar_nodo(self, raiz: Optional[Nodo], nombre: str) -> Optional[Nodo]:
        """Retorna el nodo con el nombre dado, o ``None`` si no existe."""
        actual = raiz
        while actual is not None and actual.nombre != nombre:
            actual = actual.izquierda if nombre < actual.nombre else actual.derecha
        return actual

    def buscar_por_nombre(self, raiz: Optional[Nodo], nombre: str) -> str:
        """
        Busca un nodo por su nombre y retorna un mensaje con el resultado.

        Parámetros:
            raiz: Raíz del árbol.
            nombre: Nombre del nodo a buscar.
        """
        nodo = self.buscar_nodo(raiz, nombre)
        if nodo is None:
            return "El nodo no existe"
        return f"El nodo {nombre} con ruta en data: {nodo.ruta} y hash {nodo.id_hash} existe."

    def _filtrar(self, raiz: Optional[Nodo], condicion: Callable[[Nodo], bool]) -> List[Nodo]:
        """Retorna, en preorden, los nodos del árbol que cumplen ``condicion``."""
        encontrados: List[Nodo] = []
        if raiz is not None:
            if condicion(raiz):
                encontrados.append(raiz)
            encontrados.extend(self._filtrar(raiz.izquierda, condicion))
            encontrados.extend(self._filtrar(raiz.derecha, condicion))
        return encontrados

    @staticmethod
    def _es_de_tipo(nodo: Nodo, tipo: str) -> bool:
        """Indica si el archivo del nodo está en la carpeta de la categoría ``tipo``."""
        return os.path.basename(os.path.dirname(nodo.ruta)) == tipo

    def buscar_por_tipo(self, raiz: Optional[Nodo], tipo: str) -> List[Nodo]:
        """
        Retorna todos los nodos de una categoría (subcarpeta de ``data``).

        Parámetros:
            raiz: Raíz del árbol.
            tipo: Categoría a buscar, por ejemplo ``"bike"``.
        """
        return self._filtrar(raiz, lambda nodo: self._es_de_tipo(nodo, tipo))

    def buscar_por_tipo_y_peso(
        self, raiz: Optional[Nodo], tipo: str, min_size: int, max_size: int
    ) -> List[Nodo]:
        """
        Retorna los nodos de una categoría cuyo tamaño está en ``[min_size, max_size)`` bytes.

        Parámetros:
            raiz: Raíz del árbol.
            tipo: Categoría a buscar.
            min_size: Tamaño mínimo en bytes (incluido).
            max_size: Tamaño máximo en bytes (excluido).
        """
        return self._filtrar(
            raiz,
            lambda nodo: self._es_de_tipo(nodo, tipo) and min_size <= nodo.size < max_size,
        )

    # ------------------------------------------------------------------
    # Recorridos y niveles
    # ------------------------------------------------------------------

    def recorrido_por_niveles(self, raiz: Optional[Nodo]) -> None:
        """Imprime el árbol nivel por nivel (el nivel 0 es la raíz)."""
        for nivel in range(1, self.altura(raiz) + 1):
            print(f"nivel: {nivel - 1}")
            self.imprimir_nivel(raiz, nivel)

    def imprimir_nivel(self, raiz: Optional[Nodo], nivel: int) -> None:
        """
        Imprime los nodos de un nivel del árbol (``nivel`` empieza en 1 para la raíz).

        Parámetros:
            raiz: Raíz del árbol.
            nivel: Nivel que se quiere imprimir.
        """
        if raiz is None:
            return
        if nivel == 1:
            print(raiz.nombre)
        elif nivel > 1:
            self.imprimir_nivel(raiz.izquierda, nivel - 1)
            self.imprimir_nivel(raiz.derecha, nivel - 1)

    def encontrar_nivel_del_nodo(
        self, raiz: Optional[Nodo], nombre: str, nivel_actual: int = 0
    ) -> Optional[int]:
        """Retorna el nivel del nodo con el nombre dado (raíz = 0), o ``None`` si no existe."""
        actual = raiz
        nivel = nivel_actual
        while actual is not None:
            if actual.nombre == nombre:
                return nivel
            actual = actual.izquierda if nombre < actual.nombre else actual.derecha
            nivel += 1
        return None

    def factor_balanceo(self, nodo: Optional[Nodo]) -> int:
        """Retorna el factor de balanceo del nodo (altura izquierda - altura derecha)."""
        return self.balance(nodo)

    def obtener_factor_balanceo(self, raiz: Optional[Nodo], nombre: str) -> Optional[int]:
        """Retorna el factor de balanceo del nodo con el nombre dado, o ``None`` si no existe."""
        nodo = self.buscar_nodo(raiz, nombre)
        if nodo is None:
            return None
        return self.factor_balanceo(nodo)

    # ------------------------------------------------------------------
    # Parentesco
    # ------------------------------------------------------------------

    def padre(
        self, raiz: Optional[Nodo], nombre: str, padre: Optional[Nodo] = None
    ) -> Optional[Nodo]:
        """Retorna el padre del nodo con el nombre dado (``None`` si es la raíz o no existe)."""
        actual = raiz
        anterior = padre
        while actual is not None and actual.nombre != nombre:
            anterior = actual
            actual = actual.izquierda if nombre < actual.nombre else actual.derecha
        return anterior if actual is not None else None

    def encontrar_padre(self, raiz: Optional[Nodo], nombre: str) -> None:
        """Imprime el padre del nodo con el nombre dado."""
        if self.buscar_nodo(raiz, nombre) is None:
            print(f"El nodo {nombre} no existe.")
            return
        padre = self.padre(raiz, nombre)
        if padre is None:
            print(f"{nombre} es la raíz del árbol.")
        else:
            print(f"El nodo padre de {nombre} es: {padre.nombre}")

    def abuelo(self, raiz: Optional[Nodo], nombre: str) -> Optional[Nodo]:
        """Retorna el abuelo del nodo con el nombre dado, o ``None`` si no tiene."""
        padre = self.padre(raiz, nombre)
        if padre is None or padre is raiz:
            return None
        return self.padre(raiz, padre.nombre)

    def encontrar_abuelo(self, raiz: Optional[Nodo], nombre: str) -> None:
        """Imprime el abuelo del nodo con el nombre dado."""
        abuelo = self.abuelo(raiz, nombre)
        if abuelo is None:
            print(f"{nombre} es la raíz del árbol o su padre no tiene padre.")
        else:
            print(f"El nodo abuelo de {nombre} es: {abuelo.nombre}")

    def encontrar_tio(self, raiz: Optional[Nodo], nombre: str) -> Optional[Nodo]:
        """
        Imprime y retorna el tío del nodo con el nombre dado.

        El tío es el hermano del padre: si el padre es el hijo izquierdo del
        abuelo, el tío es el hijo derecho, y viceversa.
        """
        abuelo = self.abuelo(raiz, nombre)
        if abuelo is None:
            print(f"{nombre} es la raíz del árbol o su padre no tiene padre.")
            return None

        padre = self.padre(raiz, nombre)
        tio = abuelo.derecha if padre is abuelo.izquierda else abuelo.izquierda

        if tio is None:
            print(f"{nombre} no tiene tío.")
        else:
            print(f"El nodo tío de {nombre} es: {tio.nombre}")
        return tio

    # ------------------------------------------------------------------
    # Visualización
    # ------------------------------------------------------------------

    def print_avl_tree(
        self,
        raiz: Optional[Nodo],
        dot: "graphviz.Digraph",
        parent_label: Optional[str] = None,
        direction: Optional[str] = None,
    ) -> None:
        """
        Agrega los nodos y aristas del árbol a un grafo de Graphviz.

        Parámetros:
            raiz: Raíz del (sub)árbol a dibujar.
            dot: Grafo ``graphviz.Digraph`` donde se dibuja.
            parent_label: Nombre del nodo padre (uso interno de la recursión).
            direction: ``'left'`` o ``'right'`` según el lado del padre (uso interno).
        """
        if raiz is None:
            return
        etiqueta = str(raiz.nombre)
        dot.node(etiqueta, etiqueta)
        if parent_label is not None:
            dot.edge(parent_label, etiqueta, label="L" if direction == "left" else "R")
        self.print_avl_tree(raiz.izquierda, dot, etiqueta, "left")
        self.print_avl_tree(raiz.derecha, dot, etiqueta, "right")
