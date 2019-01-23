from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import getpass

pantalla = Tk()
#Interfaz gráfica para el usuario
pantalla.title("P R O Y E C T O:  M A R S")
pantalla.geometry("600x500")
titA = StringVar()
desA = StringVar()


#ETIQUETAS PARA LOS CUADROS DE TEXTOS
lbtitulo1 =      Label(pantalla, text="Usuario").place(x=5, y=20)
lbtitulo2 =      Label(pantalla, text="<<Nombre>>").place(x=50, y=20)

lbtitulo3 =      Label(pantalla, text="MÁQUINA ACTUAL: ").place(x=100, y=100)
lbtitulo4 =      Label(pantalla, text="<<# maquina>>").place(x=220, y=100)
lbtitulo3 =      Label(pantalla, text="MIS REPORTES: ").place(x=100, y=150)

#BOTÓN QUE LLAMARÁ A LA FUNCIÓN
btnguardar =    Button(pantalla, text="NUEVO REPORTE", bg="Blue",fg="White", width=20).place(x=100, y=400)
mainloop()
