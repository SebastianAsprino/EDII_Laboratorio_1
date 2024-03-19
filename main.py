import os
from arbol import arbol
from hash import generar_hash_archivo




if __name__ == "__main__":

  def agregar_imagenes_al_arbol(directorio):
    """

    """
    print(f"Imágenes en {directorio} agregadas al arbol:")
    for nombre_archivo in os.listdir(directorio):
        ruta_archivo = os.path.join(directorio, nombre_archivo)
        if os.path.isfile(ruta_archivo):
            md5 = generar_hash_archivo(ruta_archivo)
            mi_arbol.raiz = mi_arbol.insertar(mi_arbol.raiz, nombre_archivo, ruta_archivo, md5)




  mi_arbol = arbol()
  # mi_arbol.raiz = mi_arbol.insertar(mi_arbol.raiz, "archivo101.bpm", "/unaruta", 1)
  # mi_arbol.raiz = mi_arbol.insertar(mi_arbol.raiz, "archivo100.bpm", "/unaruta", 2)
  # mi_arbol.raiz = mi_arbol.insertar(mi_arbol.raiz, "archivo102.bpm", "/unaruta", 3)
  # mi_arbol.raiz = mi_arbol.eliminar(mi_arbol.raiz,"archivo101.bpm")
  
  ruta_bike = os.path.join("data", "bike")
  ruta_cars = os.path.join("data", "cars")
  ruta_cats = os.path.join("data", "cats")
  ruta_dogs = os.path.join("data", "dogs")
  ruta_flowers = os.path.join("data", "flowers")
  ruta_horses = os.path.join("data", "horses")
  ruta_human = os.path.join("data", "human")

  agregar_imagenes_al_arbol(ruta_bike)
  # agregar_imagenes_al_arbol(ruta_cars)
  # agregar_imagenes_al_arbol(ruta_cats)
  # agregar_imagenes_al_arbol(ruta_dogs)
  # agregar_imagenes_al_arbol(ruta_flowers)
  # agregar_imagenes_al_arbol(ruta_horses)
  # agregar_imagenes_al_arbol(ruta_human)



  print(mi_arbol.raiz)
  print(mi_arbol.raiz.nombre)
  print(mi_arbol.raiz.ruta)
  print(mi_arbol.raiz.id_hash)
  print(mi_arbol.raiz.altura)
  print(mi_arbol.raiz.izquierda)
  print(mi_arbol.raiz.derecha)
  mi_arbol.eliminar(mi_arbol.raiz,"bike_128.bmp")
  print(mi_arbol.raiz)
  print(mi_arbol.raiz.nombre)
  print(mi_arbol.raiz.ruta)
  print(mi_arbol.raiz.id_hash)
  print(mi_arbol.raiz.altura)
  print(mi_arbol.raiz.izquierda)
  print(mi_arbol.raiz.derecha)

