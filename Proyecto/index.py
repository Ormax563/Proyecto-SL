from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import getpass

pantalla = Tk()
#Interfaz gráfica para el usuario
pantalla.title("M.A.R.S Alpha 1.0")
pantalla.geometry("1025x545")
titA = StringVar()
desA = StringVar()

ColorFondo="#fff"
pantalla.configure(background = ColorFondo)

btnuno=Button(pantalla, text="Reportar problemas de software", bg="#d5d5d5",fg="#000", height=3,borderwidth= 0, width=35).place(x=50, y=100)
btndos=Button(pantalla, text="Reportar daños de software", bg="#d5d5d5",fg="#000", height=3, borderwidth=0, width=35).place(x=50, y=200)
btntre=Button(pantalla, text="Reportar daños de hardware", bg="#d5d5d5",fg="#000", height=3, borderwidth=0, width=35).place(x=50, y=300)

c= Canvas(pantalla,width=1025, height=545)
c.place(x=825,y=0)
c.configure(background="#36393f")

lbnombremars=Label(c, text=" M . A . R . S ", bg="#36393f" ,fg="#fff").place(x=65, y=50)

lbing=Label(c, text="Inicio de sesion", bg="#36393f" ,fg="#fff").place(x=20, y=130)
lbnom=Label(c, text="Usuario", bg="#36393f" ,fg="#fff").place(x=20, y=180)
tfnom=Entry(c, textvariable=titA, width=25).place(x=20, y=220)
lbcon=Label(c, text="Contraseña", bg="#36393f" ,fg="#fff").place(x=20, y=260)
tfcon=Entry(c, textvariable=titA, width=25).place(x=20, y=300)
btnini=Button(c, text="Iniciar Sesión", bg="#52565e",fg="White", width=21).place(x=20, y=350)
#BOTÓN QUE LLAMARÁ A LA FUNCIÓN

mainloop()

