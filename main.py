import os
import graphviz
from arbol import arbol
from hash import generar_hash_archivo
from size import tamano_archivo


print("condicional que inicia la instancia arbol")
print("----------------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------")

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



  print("instancio el arbol: mi_arbol")
  mi_arbol = arbol()

  print("Crea las variables que guardan toda la info del dataset: ")
  ruta_bike = os.path.join("data", "bike")
  ruta_cars = os.path.join("data", "cars")
  ruta_cats = os.path.join("data", "cats")
  ruta_dogs = os.path.join("data", "dogs")
  ruta_flowers = os.path.join("data", "flowers")
  ruta_horses = os.path.join("data", "horses")
  ruta_human = os.path.join("data", "human")
  print("----------------------------------------------------------------------------------------------------------------")
  print("llama a la funcion .agregar_imagenes_al_arbol la cual es un metodo automatizado de agregar")
  print("todas las imagenes al arbol en el dataset.")

  agregar_imagenes_al_arbol(ruta_bike)
  agregar_imagenes_al_arbol(ruta_cars)
  agregar_imagenes_al_arbol(ruta_cats)
  agregar_imagenes_al_arbol(ruta_dogs)
  agregar_imagenes_al_arbol(ruta_flowers)
  agregar_imagenes_al_arbol(ruta_horses)
  agregar_imagenes_al_arbol(ruta_human)
  print("----------------------------------------------------------------------------------------------------------------")

  print("cada que se entra en la funcion se llama a mi_arbol.insertar(mi_arbol.raiz, nombre_archivo, ruta_archivo, md5, size)")
  print("los atributos a pasar en insertar son la raiz, el nombre del archivo, ruta de este en data, el hash y tamaño del archivo.")
  print("----------------------------------------------------------------------------------------------------------------")
  print("----------------------------------------------------------------------------------------------------------------")
  print("llamo al metodo .eliminar del arbol este recibe raiz y el nombre del nodo a eliminar.")

  print("en este caso elimino bike_128.bmp")

  mi_arbol.eliminar(mi_arbol.raiz,"bike_128.bmp")
  print("----------------------------------------------------------------------------------------------------------------")
  
  print("llamo al .metodo buscar_por_nombre, este recibe raiz y el nombre del nodo a eliminar.")
  print("busco bike_128.bmp:")
  mi_arbol.buscar_por_nombre(mi_arbol.raiz, "bike_128.bmp")
  print("busco bike_020.bmp:")
  mi_arbol.buscar_por_nombre(mi_arbol.raiz, "bike_020.bmp")
  print("----------------------------------------------------------------------------------------------------------------")
  print("----------------------------------------------------------------------------------------------------------------")
  print("----------------------------------------------------------------------------------------------------------------")
  
  print("creo una variable que tiene el nombre de los tipos que voy a buscaren este caso bike:")
  tipo_a_buscar = "bike"
  print("llamo al metodo .buscar_por_tipo que recibe raiz y la variable con el tipo a buscar.")
  nodos_encontrados = mi_arbol.buscar_por_tipo(mi_arbol.raiz, tipo_a_buscar)
  print("en el arreglo que cree con buscar lo leeo en un ciclo for para imprimirlos por pantalla.")
  if nodos_encontrados:
    print(f"Se encontraron nodos de tipo '{tipo_a_buscar}':")
    for nodo in nodos_encontrados:
        print(f"- Nombre: {nodo.nombre}, Ruta: {nodo.ruta}, Hash: {nodo.id_hash}, size: {nodo.size}")
  else:
    print(f"No se encontraron nodos de tipo '{tipo_a_buscar}'.")

  print("----------------------------------------------------------------------------------------------------------------")
  print("----------------------------------------------------------------------------------------------------------------")
  print("----------------------------------------------------------------------------------------------------------------")

  print("el metodo buscar, pero agregando el pesodel archivo en bytes.")
  nodos_encontrados = mi_arbol.buscar_por_tipo_y_peso(mi_arbol.raiz, tipo_a_buscar, 0, 90000)
  print("un ciclo igual al anterior.")
  if nodos_encontrados:
    print(f"Se encontraron nodos de tipo '{tipo_a_buscar}':")
    for nodo in nodos_encontrados:
        print(f"- Nombre: {nodo.nombre}, Ruta: {nodo.ruta}, Hash: {nodo.id_hash}, size: {nodo.size}")
  else:
    print(f"No se encontraron nodos de tipo '{tipo_a_buscar}' y de tamaño {nodo.size} Bytes.")


  print("----------------------------------------------------------------------------------------------------------------")
  print("----------------------------------------------------------------------------------------------------------------")
  print("----------------------------------------------------------------------------------------------------------------")



  print("llamo al metodo .recorrido_por_niveles el cual recibe raiz y retorna los nodos por nivel:")
  mi_arbol.recorrido_por_niveles(mi_arbol.raiz)

  print("----------------------------------------------------------------------------------------------------------------")
  print("----------------------------------------------------------------------------------------------------------------")
  print("----------------------------------------------------------------------------------------------------------------")

  print("llamo al metodo .encontrar_nivel_del_nodo el cual recibe raiz y el nombre del nodo a buscar y retorna en que nivel esta si no existe retorna None: ")
  print("busco el nodo bike_064.bmp")
  mi_arbol.encontrar_nivel_del_nodo(mi_arbol.raiz, "bike_064.bmp")

  print("busco el nodo bike_008.bmp")
  mi_arbol.encontrar_nivel_del_nodo(mi_arbol.raiz, "bike_008.bmp")

  print("busco el nodo bike_128.bmp")
  mi_arbol.encontrar_nivel_del_nodo(mi_arbol.raiz, "bike_128.bmp")

  print("----------------------------------------------------------------------------------------------------------------")
  print("----------------------------------------------------------------------------------------------------------------")
  print("----------------------------------------------------------------------------------------------------------------")

  print("llamo al metodo .obtener_factor_balanceo el cual recibe raiz y el nombre del nodo que se sabra su nivel de balance:")
  mi_arbol.obtener_factor_balanceo(mi_arbol.raiz, "bike_008.bmp" )

  print("----------------------------------------------------------------------------------------------------------------")
  print("----------------------------------------------------------------------------------------------------------------")
  print("----------------------------------------------------------------------------------------------------------------")

  print("llamo al metodo .encontrar_padre el cual recibe raiz y el nombre del nodo que se sabra cual es su padre:")
  mi_arbol.encontrar_padre(mi_arbol.raiz, "bike_064.bmp")

  print("----------------------------------------------------------------------------------------------------------------")
  print("----------------------------------------------------------------------------------------------------------------")
  print("----------------------------------------------------------------------------------------------------------------")

  print("llamo al metodo .encontrar_abuelo el cual recibe raiz y el nombre del nodo que se sabra cual es su abuelo:")
  mi_arbol.encontrar_abuelo(mi_arbol.raiz, "bike_064.bmp")

  print("----------------------------------------------------------------------------------------------------------------")
  print("----------------------------------------------------------------------------------------------------------------")
  print("----------------------------------------------------------------------------------------------------------------")

  print("llamo al metodo .encontrar_tio el cual recibe raiz y el nombre del nodo que se sabra cual es su tio:")
  mi_arbol.encontrar_tio(mi_arbol.raiz, "bike_032.bmp")



  dot = graphviz.Digraph()
  mi_arbol.print_avl_tree(mi_arbol.raiz, dot)
 
  
  dot.render('avl_tree', format='png', cleanup=True)
  dot.view()