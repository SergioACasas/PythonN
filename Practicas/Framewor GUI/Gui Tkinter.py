import tkinter
ventana = tkinter.Tk()
ventana.geometry("400x300")
etiqueta= tkinter.Label(ventana, text="Hola mundo",bg="blue")
etiqueta.pack(fill=tkinter.X)
# etiqueta.pack(side=tkinter.BOTTOM)
ventana.mainloop()