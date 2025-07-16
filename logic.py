import tkinter as tk
import constantes as const

class Calculadora:

    def __init__(self, master):
        #Interfaz
        self.master = master
        self.master.title("Calculadora")
        self.master.geometry("295x400")
        self.master.configure(bg="lightblue")
        
    def create_widgets(self):
        self.display = tk.Entry(self.master, width=16, font=('Arial', 24), borderwidth=2, relief="solid", bg="seashell")
        self.display.grid(row=0, column=0, columnspan=4, pady=10, sticky="ew")
        self.display2 = tk.Entry(self.master, width=16, font=('Arial', 24), borderwidth=2, relief="solid", bg="seashell")
        self.display2.grid(row=2, column=0, columnspan=4, pady=10, sticky="ew" )

    def create_buttons(self):
        #Botones
        
        #Boton de la suma
        self.button_sum = tk.Button(self.master, text="+", bg=const.COLOR_BOTON, width=const.ANCHO, height=const.ALTO)
        self.button_sum.grid(row=10, column=0, padx=5, pady=5)
        
        #Boton de la resta
        self.button_res = tk.Button(self.master, text="-", bg=const.COLOR_BOTON, width=const.ANCHO, height=const.ALTO)
        self.button_res.grid(row=11, column=0, padx=5, pady=5)
        
        #Boton de la multiplicacion
        self.button_mult = tk.Button(self.master, text="*", bg=const.COLOR_BOTON, width=const.ANCHO, height=const.ALTO)
        self.button_mult.grid(row=10, column=1, padx=0, pady=0)
        # #Boton de la division
        self.button_div = tk.Button(self.master, text="/", bg=const.COLOR_BOTON, width=const.ANCHO, height=const.ALTO)
        self.button_div.grid(row=11, column=1, padx=0, pady=0)
