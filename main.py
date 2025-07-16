import tkinter as tk
from logic import Calculadora


#Instanciar clase Calculadora y metodos para crear la interfaz
root = tk.Tk()
interfaz = Calculadora(root)
interfaz.create_widgets()
interfaz.create_buttons()
root.mainloop()