#En este ejercicio tenéis que crear una lista de RadioButton
#que muestre la opción que se ha seleccionado y que contenga
#un botón de reinicio para que deje todo como al principio.
#Al principio no tiene que haber una opción seleccionada.

import tkinter as tk    

ventana = tk.Tk()
ventana.title("Mi aplicacion")
ventana.geometry("800x600")

etiqueta = tk.Label(ventana,
                    text="Envio de datos",
                    font=("bold"),
                    background="red",
                    foreground="green",
                    relief=tk.GROOVE,
                    border=30
                    )               
etiqueta.pack()

numero= tk.Label(ventana,
                text=0,
                background="yellow",
                foreground="green",
                border=30)
numero.pack()

boton = tk.Button(ventana,
                   text="CONTAR",
                   bg="lightblue",
                   fg="red",
                   padx=20,pady=30,
                   )
boton.pack()

ventana.mainloop()
