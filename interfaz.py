"""
Interfaz gráfica (Tkinter) para operar el árbol AVL.

Permite cargar las imágenes del dataset, eliminar y buscar nodos por nombre.
Después de cada cambio el árbol se dibuja con Graphviz. Las opciones
"Buscar por criterios" y "Recorrido por niveles" todavía solo actualizan el
texto de la ventana.
"""

import tkinter as tk
from typing import Callable

from arbol import Arbol
from dataset import cargar_categorias
from visualizacion import renderizar_arbol

# Categorías que carga el botón "Insertar". Se limita a una para que el
# grafo generado sea legible; se pueden agregar más de dataset.CATEGORIAS.
CATEGORIAS_INTERFAZ = ("bike",)

COLOR_BARRA = "blue"
FUENTE = ("Arial", 14)
ANCHO_BOTON = 15


class FullScreenApp:
    """Ventana principal a pantalla completa con la barra de operaciones."""

    def __init__(self, master: tk.Tk, arbol: Arbol) -> None:
        """
        Construye la ventana.

        Parámetros:
            master: Ventana raíz de Tkinter.
            arbol: Árbol AVL sobre el que operan los botones.
        """
        self.master = master
        self.arbol = arbol
        master.geometry(f"{master.winfo_screenwidth()}x{master.winfo_screenheight()}+0+0")
        master.title("Full Screen App")

        self.frame = tk.Frame(master)
        self.frame.pack(expand=True, fill="both")

        self.create_navbar()
        self.create_input_frame()
        self.create_right_frame()

    # ------------------------------------------------------------------
    # Construcción de la ventana
    # ------------------------------------------------------------------

    def create_navbar(self) -> None:
        """Crea la barra superior con el título y los botones de operaciones."""
        self.navbar = tk.Frame(self.frame, bg=COLOR_BARRA)
        self.navbar.pack(side="top", fill="x")

        # Título en el extremo izquierdo
        title_label = tk.Label(self.navbar, text="Operaciones con árboles", bg=COLOR_BARRA, fg="white")
        title_label.pack(side="left", padx=5, pady=5)

        buttons = [
            ("Insertar", self.insert_node),
            ("Eliminar", self.delete_node),
            ("Buscar", self.search_node),
            ("Buscar por criterios", self.search_by_criteria),
            ("Recorrido por niveles", self.level_order_traversal),
        ]

        # Botones en el extremo derecho
        for text, command in buttons:
            button = tk.Button(self.navbar, text=text, command=command, width=ANCHO_BOTON)
            button.pack(side="right", padx=5, pady=5)

    def create_input_frame(self) -> None:
        """Crea el panel izquierdo con la etiqueta y el campo de entrada."""
        self.input_frame = tk.Frame(self.frame)
        self.input_frame.pack(fill="both", expand=True)

        # La parte izquierda es un poco más ancha que la mitad de la pantalla
        left_frame = tk.Frame(self.input_frame, width=self.master.winfo_screenwidth() // 2 + 25)
        left_frame.pack(side="left", fill="both", expand=True)

        input_panel = tk.Frame(left_frame, bg="gray")
        input_panel.place(relx=0.05, rely=0.5, anchor="w")

        self.label = tk.Label(input_panel, text="Ingrese la opción:", font=FUENTE)
        self.label.pack(pady=10, padx=10)

        self.entry = tk.Entry(input_panel, font=FUENTE)
        self.entry.pack(pady=10, padx=10)

    def create_right_frame(self) -> None:
        """Crea el panel derecho."""
        right_frame = tk.Frame(self.input_frame, bg="light gray")
        right_frame.pack(side="right", fill="both", expand=True, padx=(10, 50), pady=20)

        label_right = tk.Label(right_frame, text="Este es el frame derecho", font=FUENTE)
        label_right.pack(padx=10, pady=10)

    def _pedir_nombre(self, titulo: str, mensaje: str, accion: Callable[[str], None]) -> None:
        """
        Abre una ventana que pide el nombre de un nodo y ejecuta ``accion`` con él.

        Parámetros:
            titulo: Título de la ventana.
            mensaje: Texto que se muestra sobre el campo de entrada.
            accion: Función que recibe el nombre ingresado.
        """
        ventana = tk.Toplevel(self.master)
        ventana.title(titulo)

        tk.Label(ventana, text=mensaje).pack(pady=10)
        entrada = tk.Entry(ventana)
        entrada.pack(pady=5)

        def aceptar() -> None:
            nombre = entrada.get()
            ventana.destroy()
            accion(nombre)

        tk.Button(ventana, text="Aceptar", command=aceptar).pack(pady=10)

    # ------------------------------------------------------------------
    # Operaciones
    # ------------------------------------------------------------------

    def insert_node(self) -> None:
        """Carga las imágenes de ``CATEGORIAS_INTERFAZ`` en el árbol y lo dibuja."""
        self.label.config(text="Ingrese la opción:")
        self.entry.delete(0, tk.END)
        cargar_categorias(self.arbol, CATEGORIAS_INTERFAZ)
        renderizar_arbol(self.arbol)

    def delete_node(self) -> None:
        """Pide el nombre de un nodo y lo elimina del árbol."""
        self._pedir_nombre("Eliminar Nodo", "Ingrese el nombre del nodo a eliminar:", self.eliminar)

    def search_node(self) -> None:
        """Pide el nombre de un nodo y muestra si existe."""
        self._pedir_nombre("Buscar Nodo", "Ingrese el nombre del nodo a buscar:", self.buscar)

    def search_by_criteria(self) -> None:
        """Pendiente: por ahora solo actualiza el texto de la ventana."""
        self.label.config(text="Mostrar los nodos que cumplen con el criterio.")
        self.entry.delete(0, tk.END)

    def level_order_traversal(self) -> None:
        """Pendiente: por ahora solo actualiza el texto de la ventana."""
        self.label.config(text="Recorrido por nivel")
        self.entry.delete(0, tk.END)

    def eliminar(self, nombre_nodo: str) -> None:
        """Elimina el nodo del árbol y vuelve a dibujarlo."""
        self.arbol.raiz = self.arbol.eliminar(self.arbol.raiz, nombre_nodo)
        renderizar_arbol(self.arbol)

    def buscar(self, nombre_nodo: str) -> None:
        """Busca el nodo y muestra el resultado en una ventana."""
        resultado_busqueda = self.arbol.buscar_por_nombre(self.arbol.raiz, nombre_nodo)

        search_result_window = tk.Toplevel(self.master)
        search_result_window.title("Resultado de la búsqueda")
        tk.Label(search_result_window, text=resultado_busqueda).pack(padx=10, pady=10)


def main() -> None:
    """Inicia la interfaz gráfica."""
    root = tk.Tk()
    FullScreenApp(root, Arbol())
    root.mainloop()


if __name__ == "__main__":
    main()
