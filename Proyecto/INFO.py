from tkinter import *
from tkinter import messagebox
from tkinter import ttk

pantalla = Tk()
#Interfaz gráfica para el usuario
pantalla.title("P R O Y E C T O:  M A R S")
pantalla.geometry("400x300")
titA = StringVar()
desA = StringVar()


#ETIQUETAS PARA LOS CUADROS DE TEXTOS
lbtitulo =      Label(pantalla, text="USUARIO:").place(x=25, y=80)
lbdescripcion = Label(pantalla, text="CONTRASEÑA:").place(x=25, y=110)
#CUADROS DE TEXTOS PARA INGRESAR LOS DATOS
tftitulo =      Entry(pantalla, textvariable=titA, width=30).place(x=170, y=80)
tfdescripcion = Entry(pantalla, textvariable=desA, width=30).place(x=170, y=110)
#BOTÓN QUE LLAMARÁ A LA FUNCIÓN
btnguardar =    Button(pantalla, text="GUARDAR", bg="Blue",fg="White", width=30).place(x=75, y=220)
mainloop()

