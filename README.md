# EDII — Laboratorio 1: Árbol AVL sobre un dataset de imágenes

Laboratorio del curso **Estructuras de Datos II**. Se implementa desde cero un **árbol AVL**
(árbol binario de búsqueda autobalanceado) en Python y se usa para indexar un dataset de
~1800 imágenes. Cada archivo se guarda como un nodo con su nombre, ruta, **hash MD5** y tamaño
en bytes; el árbol se ordena por el nombre del archivo y se puede dibujar con **Graphviz**.

## Funcionalidades

Operaciones del árbol (`arbol.py`):

- **Inserción** con rebalanceo (rotaciones simples y dobles: LL, RR, LR, RL).
- **Eliminación** con rebalanceo; si el nodo tiene dos hijos se reemplaza por su sucesor
  inmediato.
- **Búsqueda por nombre** (`buscar_por_nombre`, `buscar_nodo`).
- **Búsqueda por categoría** (`buscar_por_tipo`): nodos cuya imagen está en `data/<tipo>/`.
- **Búsqueda por categoría y tamaño** (`buscar_por_tipo_y_peso`): además filtra por un rango
  de bytes `[min, max)`.
- **Recorrido por niveles** (`recorrido_por_niveles`).
- **Nivel de un nodo** (`encontrar_nivel_del_nodo`, la raíz es el nivel 0).
- **Factor de balanceo** de un nodo (`obtener_factor_balanceo`).
- **Parentesco**: padre, abuelo y tío de un nodo (`padre`, `abuelo`, `encontrar_tio`, …).
- **Visualización**: genera un PNG del árbol con Graphviz (`print_avl_tree` +
  `visualizacion.renderizar_arbol`).

Además hay dos formas de usarlo:

- `main.py`: demostración por consola que carga todo el dataset y ejecuta cada operación
  explicando lo que hace.
- `interfaz.py`: interfaz gráfica en Tkinter (en desarrollo) para cargar imágenes, eliminar y
  buscar nodos; después de cada cambio dibuja el árbol.

## Estructura del proyecto

```
EDII_Laboratorio_1/
├── nodo.py           # Clase Nodo: nombre, ruta, hash MD5, tamaño, altura e hijos
├── arbol.py          # Clase Arbol: árbol AVL y todas sus operaciones
├── hash.py           # generar_hash_archivo(): MD5 del contenido de un archivo
├── size.py           # tamano_archivo(): tamaño del archivo en bytes
├── dataset.py        # Carga de las imágenes de data/ en el árbol
├── visualizacion.py  # Dibuja el árbol en salida/avl_tree.png con Graphviz
├── main.py           # Demostración por consola
├── interfaz.py       # Interfaz gráfica (Tkinter)
├── requirements.txt
└── data/             # Dataset: bike, cars, cats, dogs, flowers, horses, human
```

`arbol.py` no depende de Graphviz ni de Tkinter: la estructura de datos está separada de la
carga del dataset (`dataset.py`) y de la presentación (`visualizacion.py`, `main.py`,
`interfaz.py`).

### Uso del árbol desde código

Los métodos reciben la raíz del (sub)árbol y los que modifican el árbol retornan la nueva raíz,
que hay que reasignar:

```python
from arbol import Arbol

arbol = Arbol()
arbol.raiz = arbol.insertar(arbol.raiz, "bike_001.bmp", "data/bike/bike_001.bmp", "<md5>", 921654)
arbol.raiz = arbol.eliminar(arbol.raiz, "bike_001.bmp")
print(arbol.buscar_por_nombre(arbol.raiz, "bike_001.bmp"))
```

## Requisitos

- Python 3.9 o superior (con Tkinter para la interfaz gráfica).
- [Graphviz](https://graphviz.org/download/) instalado en el sistema (el ejecutable `dot` debe
  estar en el `PATH`).
- Paquete de Python `graphviz` (ver `requirements.txt`).

## Cómo ejecutar

Desde la raíz del repositorio (las rutas del dataset son relativas a `data/`):

```bash
python -m venv .venv
source .venv/bin/activate          # En Windows: .venv\Scripts\activate
pip install -r requirements.txt

python main.py       # demostración por consola
python interfaz.py   # interfaz gráfica
```

La imagen del árbol se guarda en `salida/avl_tree.png` y se abre con el visor del sistema.

## Colaboradores

Proyecto en equipo del curso Estructuras de Datos II (usuarios de GitHub): SebastianAsprino,
AndresMonserrat y Alinsonp.
