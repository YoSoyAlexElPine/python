import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz de ejemplo")
ventana.geometry("800x800")

# Crear una etiqueta y agregarla a la ventana
etiqueta = tk.Label(text="Bienvenido a la interfaz gráfica de usuario")
etiqueta.pack()

# Ejecutar la ventana
ventana.mainloop()