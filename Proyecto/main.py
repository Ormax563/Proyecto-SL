from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import getpass


pantalla = Tk()
#Interfaz gráfica para el usuario
pantalla.title("P R O Y E C T O:  M A R S")
pantalla.geometry("600x500")
#-------------------Lista Desplegable-------------
a=1
i=[]
while(a<=21):
    aux = "Lab: "+str(a)
    i.append(aux)
    a=a+1
combo = ttk.Combobox(pantalla, value=i, state='readonly')
combo.place(x=200, y=50)
#------------------------------------------------
b=1
j=[]
while(b<=50):
    aux2 = "MAQ: "+str(b)
    j.append(aux2)
    b=b+1
combo = ttk.Combobox(pantalla, value=j, state='readonly')
combo.place(x=200, y=100)
#------------------------------------------------
text = Text(pantalla, height=15, width=60).place(x=50,y=175)
#---------------------Etiquetas-------------------
et1 = Label(pantalla, text= "Seleccione un laboratorio: ").place(x=50,y=50)
et2 = Label(pantalla, text= "Seleccione una máquina: ").place(x=50,y=100)
et3 = Label(pantalla, text= "REGISTROS:").place(x=50,y=150)
#--------------------BOTTONES------------------------
btn1 = Button(pantalla, text= "NUEVO").place(x=400,y=425)
btn2 = Button(pantalla, text= "CONSULTAR").place(x=460,y=425)
mainloop()

#-----------------Funciones-----------------------------



