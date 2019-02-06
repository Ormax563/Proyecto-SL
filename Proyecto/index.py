from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import getpass
import os

def ingresar():
    if tfnom.get()!="":
        btnini.config(state=DISABLED, text="Correo Ingresado")
        tfnom.config(state=DISABLED)
        lbinf.config(text="Status: Correo electrónico ingresado", fg="#000")


def cmuno():
    if btnini["state"] == "disabled":
        pantalla.withdraw()
        os.system("main.py 1")
    else:
        lbinf.config(fg="#FF0000")

def cmdos():
    if btnini["state"] == "disabled":
        print("aqui va el codigo para ir ala siguiente ventana DOS")
    else:
        lbinf.config(fg="#FF0000")

def labell():
    print("Desarrollado por xCrack Studios")

pantalla = Tk()
pantalla.title("M.A.R.S Alpha 1.0")
pantalla.geometry("1025x545")
titA = StringVar()
desA = StringVar()
titB = StringVar()

img1=PhotoImage(file="central.png")
img2=PhotoImage(file="inferior.png")


ColorFondo="#fff"
pantalla.configure(background = ColorFondo)


btnuno=Button(pantalla, text="Reportar problemas de software", bg="#d5d5d5",fg="#000", height=3,borderwidth= 0, width=35,cursor="hand2", command=cmuno)
btnuno.place(x=50, y=200)
lbinf=Label(pantalla, text="Status: Debe ingresar un correo electrónico para enviar reportes", bg="#fff")
lbinf.place(x=50, y=500)
lbimg1=Label(pantalla, image=img1,borderwidth=0)
lbimg1.place(x=305, y=60)


c= Canvas(pantalla,width=1080, height=1920)
c.place(x=825,y=0)
c.configure(background="#36393f")


lbnombremars=Label(c, text=" M . A . R . S ", bg="#36393f" ,fg="#fff")
lbnombremars.place(x=65, y=50)
lbing=Label(c, text="Autenticación", bg="#36393f" ,fg="#fff")
lbing.place(x=20, y=130)
lbnom=Label(c, text="Correo electrónico", bg="#36393f" ,fg="#fff")
lbnom.place(x=20, y=180)
tfnom=Entry(c, textvariable=titA, width=25)
tfnom.place(x=20, y=220)
btnini=Button(c, text="Ingresar", bg="#52565e",fg="White", width=21, cursor="hand2", command=ingresar)
btnini.place(x=20, y=260)           #llamar inmediatamente a su ubicacion imposiblita la devolucion de su estado
lbimg2=Button(c, image=img2,borderwidth=0, bg="#36393f",relief="flat",fg="#36393f", cursor="hand2", command=labell)
lbimg2.place(x=6, y=455)

mainloop()

