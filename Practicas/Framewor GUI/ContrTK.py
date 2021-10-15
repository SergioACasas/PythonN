import string
from tkinter import *
import secrets

def borrar(evento):
    intext.delete(0,END)
def newpass (num):
    psw = ""
    for i in range(num):
        psw = psw + secrets.choice(string.ascii_letters+string.digits)
    return psw
def isunum(input):
    if input.isdigit() or input == "":
        return True
    else:
        return False
def toclipboard():
    a = outext.get()
    root.clipboard_clear()
    root.clipboard_append(str(a))
    root.update()
def on_button():
    outext.config(state=NORMAL)
    outext.delete(0,END)
    num = intext.get()
    num = int(num)
    psw = newpass(num)
    outext.insert(0,psw)#Esto va antes de .grid !!!!
    outext.config(state=DISABLED)

    return 
#Comienza la ventana---------------------------------------------
root = Tk()
#root.config(width=300,height=200)
#texto enbebido--------------------------------------------------
space0 = Label(root,text="                           ").grid(row=0)
text1 = Label(root,text="       Introduce la cantidad de caracteres :       ").grid(row=1)
#----------------------------------------------------------------
intext = Entry(root,justify="center",fg="red")
intext.insert(0,"N°")
#validacion solo para ingresar numeros
validation = root.register(isunum)
intext.config(validate="key",validatecommand=(validation,'%P'))
intext.grid(row=2)
#----------------------------------------------------------------
text2 = Label(root,text= "Codigo generado :",).grid(row=4)
#----------------------------------------------------------------
outext = Entry(root,justify="center",fg="blue",state=DISABLED)
boton1 = Button(root,text="Crear",command=on_button).grid(row=3)
outext.grid(row=5)
intext.bind('<Button-1>',borrar)
#----------------------------------------------------------------
boton2 = Button(root,text="Copiar",command=toclipboard).grid(row=6)
#----------------------------------------------------------------
space = Label(root,text="                ").grid(row=7)
#----------------------------------------------------------------
root.mainloop()
