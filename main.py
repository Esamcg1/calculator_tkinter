import tkinter as tk
from logic import Interfaz, Calculadora


#Instanciar clase Calculadora y metodos para crear la interfaz
root = tk.Tk()
interfaz = Interfaz(root)
interfaz.create_widgets()
interfaz.create_buttons()
root.mainloop()