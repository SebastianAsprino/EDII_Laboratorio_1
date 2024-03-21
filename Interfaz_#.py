import tkinter as tk

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

    def delete_node(self):
        self.label.config(text="Qué nodo quiere eliminar:")
        self.entry.delete(0, tk.END)

    def search_node(self):
        self.label.config(text="¿Que nodo quiere buscar?")
        self.entry.delete(0, tk.END)

    def search_by_criteria(self):
        self.label.config(text="Mostrar los nodos que cumplen con el criterio.")
        self.entry.delete(0, tk.END)

    def level_order_traversal(self):
        self.label.config(text="Recorrido por nivel")
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = FullScreenApp(root)
    root.mainloop()
