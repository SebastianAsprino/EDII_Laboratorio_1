import os
from arbol import arbol
from hash import generar_hash_archivo
from size import tamano_archivo




if __name__ == "__main__":

  def agregar_imagenes_al_arbol(directorio):
    """

    """
    print(f"Imágenes en {directorio} agregadas al arbol:")
    for nombre_archivo in os.listdir(directorio):
        ruta_archivo = os.path.join(directorio, nombre_archivo)
        if os.path.isfile(ruta_archivo):
            md5 = generar_hash_archivo(ruta_archivo)
            size = tamano_archivo(ruta_archivo)
            mi_arbol.raiz = mi_arbol.insertar(mi_arbol.raiz, nombre_archivo, ruta_archivo, md5, size)




  mi_arbol = arbol()

  
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



  # print(mi_arbol.raiz)
  # print(mi_arbol.raiz.nombre)
  # print(mi_arbol.raiz.ruta)
  # print(mi_arbol.raiz.id_hash)
  # print(mi_arbol.raiz.altura)
  # print(mi_arbol.raiz.size)
  # print(mi_arbol.raiz.izquierda)
  # print(mi_arbol.raiz.derecha)
  # mi_arbol.eliminar(mi_arbol.raiz,"bike_128.bmp")
  # print(mi_arbol.raiz)
  # print(mi_arbol.raiz.nombre)
  # print(mi_arbol.raiz.ruta)
  # print(mi_arbol.raiz.id_hash)
  # print(mi_arbol.raiz.altura)
  # print(mi_arbol.raiz.izquierda)
  # print(mi_arbol.raiz.derecha)
  # mi_arbol.buscar_por_nombre(mi_arbol.raiz, "bike_128.bmp") #recordar que lo acabo de eliminar.
  # mi_arbol.buscar_por_nombre(mi_arbol.raiz, "bike_020.bmp")


  # tipo_a_buscar = "bike"
  # nodos_encontrados = mi_arbol.buscar_por_tipo(mi_arbol.raiz, tipo_a_buscar)

  # if nodos_encontrados:
  #   print(f"Se encontraron nodos de tipo '{tipo_a_buscar}':")
  #   for nodo in nodos_encontrados:
  #       print(f"- Nombre: {nodo.nombre}, Ruta: {nodo.ruta}, Hash: {nodo.id_hash}, size: {nodo.size}")
  # else:
  #   print(f"No se encontraron nodos de tipo '{tipo_a_buscar}'.")


  # nodos_encontrados = mi_arbol.buscar_por_tipo_y_peso(mi_arbol.raiz, tipo_a_buscar, 0, 90000)

  # if nodos_encontrados:
  #   print(f"Se encontraron nodos de tipo '{tipo_a_buscar}':")
  #   for nodo in nodos_encontrados:
  #       print(f"- Nombre: {nodo.nombre}, Ruta: {nodo.ruta}, Hash: {nodo.id_hash}, size: {nodo.size}")
  # else:
  #   print(f"No se encontraron nodos de tipo '{tipo_a_buscar}' y de tamaño {nodo.size} Bytes.")







  # mi_arbol.recorrido_por_niveles(mi_arbol.raiz)




  # mi_arbol.encontrar_nivel_del_nodo(mi_arbol.raiz, "bike_064.bmp")
  # mi_arbol.encontrar_nivel_del_nodo(mi_arbol.raiz, "bike_008.bmp")



  mi_arbol.obtener_factor_balanceo(mi_arbol.raiz, "bike_128.bmp" )