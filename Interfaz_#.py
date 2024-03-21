import tkinter as tk
import os
import graphviz
from arbol import arbol
from hash import generar_hash_archivo
from size import tamano_archivo



class FullScreenApp:
  def __init__(self, master, **kwargs):
    self.master = master
    master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
    master.title("Full Screen App")
        
    self.frame = tk.Frame(master)
    self.frame.pack(expand=True, fill='both')
        
    self.create_navbar()
    self.create_input_frame()
    self.create_right_frame()

  def create_navbar(self):
      self.navbar = tk.Frame(self.frame, bg='blue')
      self.navbar.pack(side='top', fill='x')
      
      # Título en el extremo izquierdo
      title_label = tk.Label(self.navbar, text="Operaciones con árboles", bg='blue', fg='white')
      title_label.pack(side='left', padx=5, pady=5)
      
      buttons = [
          ("Insertar", self.insert_node),
          ("Eliminar", self.delete_node),
          ("Buscar", self.search_node),
          ("Buscar por criterios", self.search_by_criteria),
          ("Recorrido por niveles", self.level_order_traversal)
      ]
      
      self.button_eliminar = tk.Button(self.navbar, text="Eliminar", command=self.delete_node, width=15)
      self.button_eliminar.pack(side='right', padx=5, pady=5)
      
      # Botones en el extremo derecho
      for text, command in buttons:
          button = tk.Button(self.navbar, text=text, command=command, width=15)
          button.pack(side='right', padx=5, pady=5)

  def create_input_frame(self):
      self.input_frame = tk.Frame(self.frame)
      self.input_frame.pack(fill='both', expand=True)
      
      left_frame = tk.Frame(self.input_frame, width=self.master.winfo_screenwidth() // 2 + 25)  # La parte izquierda es 50px más grande
      left_frame.pack(side='left', fill='both', expand=True)
      
      input_panel = tk.Frame(left_frame, bg='gray')
      input_panel.place(relx=0.05, rely=0.5, anchor='w')  # Cambiado a relx=0.05 para mover hacia el lado izquierdo
      
      self.label = tk.Label(input_panel, text="Ingrese la opción:", font=('Arial', 14))
      self.label.pack(pady=10, padx=10)
      
      self.entry = tk.Entry(input_panel, font=('Arial', 14))
      self.entry.pack(pady=10, padx=10)

  def create_right_frame(self):
      right_frame = tk.Frame(self.input_frame, bg='light gray')
      right_frame.pack(side='right', fill='both', expand=True, padx=(10, 50), pady=20)  # Aumentando el padding
      
      label_right = tk.Label(right_frame, text="Este es el frame derecho", font=('Arial', 14))
      label_right.pack(padx=10, pady=10)
  
  def insert_node(self):
      self.label.config(text="Ingrese la opción:")
      self.entry.delete(0, tk.END)
      agregado_en_bloque()

  def delete_node(self):
    # Crear una nueva ventana Tkinter para solicitar el string
    self.delete_window = tk.Toplevel(self.master)
    self.delete_window.title("Eliminar Nodo")
    
    # Etiqueta y campo de entrada para que el usuario ingrese el string
    label = tk.Label(self.delete_window, text="Ingrese el nombre del nodo a eliminar:")
    label.pack(pady=10)
    self.delete_entry = tk.Entry(self.delete_window)
    self.delete_entry.pack(pady=5)
    
    # Botón "Aceptar" para confirmar la entrada y llamar a la función eliminar
    accept_button = tk.Button(self.delete_window, text="Aceptar", command=self.accept_deletion)
    accept_button.pack(pady=10)

  def accept_deletion(self):
    # Obtener el string ingresado por el usuario
    string_ingresado = self.delete_entry.get()
    
    # Llamar a la función eliminar con el string como argumento
    eliminar(string_ingresado)
    
    # Cerrar la ventana de entrada
    self.delete_window.destroy()


  def search_node(self):
    # Crear una nueva ventana Tkinter para solicitar el nombre del nodo
    self.search_window = tk.Toplevel(self.master)
    self.search_window.title("Buscar Nodo")
    
    # Etiqueta y campo de entrada para que el usuario ingrese el nombre del nodo
    label = tk.Label(self.search_window, text="Ingrese el nombre del nodo a buscar:")
    label.pack(pady=10)
    self.search_entry = tk.Entry(self.search_window)
    self.search_entry.pack(pady=5)
    
    # Botón "Aceptar" para confirmar la entrada y llamar a la función buscar
    accept_button = tk.Button(self.search_window, text="Aceptar", command=self.accept_search)
    accept_button.pack(pady=10)

  def accept_search(self):
    # Obtener el nombre del nodo ingresado por el usuario
    nombre_nodo = self.search_entry.get()
    
    # Llamar a la función buscar con el nombre del nodo como argumento
    buscar(nombre_nodo)
    
    # Cerrar la ventana de entrada
    self.search_window.destroy()

  def search_by_criteria(self):
      self.label.config(text="Mostrar los nodos que cumplen con el criterio.")
      self.entry.delete(0, tk.END)

  def level_order_traversal(self):
      self.label.config(text="Recorrido por nivel")
      self.entry.delete(0, tk.END)

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

  def agregado_en_bloque():
    agregar_imagenes_al_arbol(ruta_bike)
    # agregar_imagenes_al_arbol(ruta_cars)
    # agregar_imagenes_al_arbol(ruta_cats)
    # agregar_imagenes_al_arbol(ruta_dogs)
    # agregar_imagenes_al_arbol(ruta_flowers)
    # agregar_imagenes_al_arbol(ruta_horses)
    # agregar_imagenes_al_arbol(ruta_human)
    dot = graphviz.Digraph()
    mi_arbol.print_avl_tree(mi_arbol.raiz, dot)
    dot.render('avl_tree', format='png',  directory='/data/arbol/')
    dot.view()

  def eliminar(nombre_nodo):
    mi_arbol.eliminar(mi_arbol.raiz,nombre_nodo)
    dot = graphviz.Digraph()
    mi_arbol.print_avl_tree(mi_arbol.raiz, dot)
    dot.render('avl_tree', format='png',  directory='/data/arbol/')
    dot.view()
  
  def buscar(nombre_nodo):
    # Realizar la búsqueda y obtener el resultado como un string
    resultado_busqueda = mi_arbol.buscar_por_nombre(mi_arbol.raiz, nombre_nodo)
    
    # Crear una nueva ventana Tkinter para mostrar el resultado de la búsqueda
    search_result_window = tk.Toplevel()
    search_result_window.title("Resultado de la búsqueda")
    
    # Crear una etiqueta para mostrar el resultado
    result_label = tk.Label(search_result_window, text=resultado_busqueda)
    result_label.pack(padx=10, pady=10)

  




  root = tk.Tk()
  app = FullScreenApp(root)
  root.mainloop()
