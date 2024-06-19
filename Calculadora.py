import tkinter as tk

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        # Estilo de fuente para los botones y pantalla
        font = ("Arial", 20)

        # Crea la pantalla de visualización
        self.pantalla = tk.Entry(master, width=20, borderwidth=0, font=font, justify="right", relief="flat")
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        # Crea los botones con un estilo más limpio
        botones = [
            "AC", "+/-", "%", "÷",
            "7", "8", "9", "×",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "0", ".", "=",
        ]

        fila = 1
        columna = 0
        for boton in botones:
            comando = lambda x=boton: self.click(x)
            boton_widget = tk.Button(master, text=boton, width=5, height=2, font=font, relief="flat", command=comando)
            boton_widget.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")

            columna += 1
            if columna > 3:
                columna = 0
                fila += 1

        # Configura el comportamiento de redimensionamiento dinámico
        master.columnconfigure((0, 1, 2, 3), weight=1)  # Columnas 0 a 3 expandibles
        master.rowconfigure((1, 2, 3, 4, 5), weight=1)  # Filas 1 a 5 expandibles

    def click(self, texto):
        if texto == "=":
            expresion = self.pantalla.get()
            try:
                resultado = str(eval(expresion))
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(0, resultado)
            except ZeroDivisionError:
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(0, "Error: División por cero")
            except (SyntaxError, NameError, TypeError):
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(0, "Error: Expresión inválida")
        elif texto == "AC":
            self.pantalla.delete(0, tk.END)
        elif texto == "+/-":
            contenido = self.pantalla.get()
            if contenido and contenido[0] == "-":
                self.pantalla.delete(0)
            else:
                self.pantalla.insert(0, "-")
        else:
            self.pantalla.insert(tk.END, texto)

# Configura la ventana principal
root = tk.Tk()
root.title("Calculadora")

# Crea una instancia de la calculadora
calculadora = Calculadora(root)

# Hacer la ventana redimensionable
root.resizable(False, False)  # Desactivar redimensionamiento

# Inicia el bucle principal de la aplicación
root.mainloop()
