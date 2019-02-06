
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sys
import tkinter as tk
import time
import getpass
import os
import pymysql

#-----------------Funciones-----------------------------
def select():
    combomaq['state'] = 'readonly'
    if(combolab.get() == "Lab: 1"):
       lim = 30
    if(combolab.get() == "Lab: 2"):
       lim = 20
    if(combolab.get() == "Lab: 3"):
       lim = 30
    if(combolab.get() == "Lab: 4"):
       lim = 30
    if(combolab.get() == "Lab: 5"):
       lim = 50
    if(combolab.get() == "Lab: 6"):
       lim = 50
    if(combolab.get() == "Lab: 7"):
       lim = 35
    if(combolab.get() == "Lab: 8"):
       lim = 35
    if(combolab.get() == "Lab: 9"):
       lim = 35
    if(combolab.get() == "Lab: 10"):
       lim = 23
    if(combolab.get() == "Lab: 11"):
       lim = 34
    if(combolab.get() == "Lab: 12"):
       lim = 54
    if(combolab.get() == "Lab: 13"):
       lim = 12
    if(combolab.get() == "Lab: 14"):
       lim = 34
    if(combolab.get() == "Lab: 15"):
       lim = 23
    if(combolab.get() == "Lab: 16"):
       lim = 35
    if(combolab.get() == "Lab: 17"):
       lim = 21
    if(combolab.get() == "Lab: 18"):
       lim = 26
    if(combolab.get() == "Lab: 19"):
       lim = 20
    if(combolab.get() == "Lab: 20"):
       lim = 20
    if(combolab.get() == "Lab: 21"):
       lim = 30
    b=1
    j=[]
    while(b<=lim):
        aux2 = "MAQ: "+str(b)
        j.append(aux2)
        b=b+1
    combomaq['value'] = j
    combomaq.current(0)
#--------------------BASE--------------------------
conn = pymysql.connect(host='localhost',user='root',password='',db='informacion')

#------------------------------------------------
def mostrar():
    f = open("info.txt","w")
    f.write(lb.get()+"\n"+mq.get())
    f.close()
    pantalla.withdraw()
    os.system("NUEVO.py 1")
def prueba():
    a = conn.cursor()
    sql = "select * from registro"
    a.execute(sql)
    f = StringVar()
    f=""
    for row in a:
        l = "Lab: %s"%row[1]
        m = "MAQ: %s"%row[2]
        if(lb.get().__eq__(l)):
            if(mq.get().__eq__(m)):
                f = f+"reporte #%s Laboratorio: %s Máquina: %s  Fecha: %s Hora: %s Descripción: %s \n" % (row[0],row[1],row[2],row[3],row[4],row[7])
    if(f.__eq__("")):
        f = "Esta máquina se ecuentra sin reportes"
    dat.set(f)



def Salir():
    sys.exit()
#---------------------------------------------------------
pantalla = Tk()

img1=PhotoImage(file="leon.png")
lbimg1=Label(pantalla, image=img1,borderwidth=0)
lbimg1.place(x=600, y=30)

img2=PhotoImage(file="gn.png")
lbimg2=Label(pantalla, image=img2,borderwidth=0)
lbimg2.place(x=28, y=400)

pantalla.config(background="white")
#Interfaz gráfica para el usuario
pantalla.title("P R O Y E C T O:  M A R S")
pantalla.geometry("800x500")
#-------------------Lista Desplegable-------------
a=1
i=[]
while(a<=21):
    aux = "Lab: "+str(a)
    i.append(aux)
    a=a+1

lb=StringVar()
mq=StringVar()
pnt=StringVar()

combolab = ttk.Combobox(pantalla, value=i,textvariable=lb)
combolab.place(x=300, y=50)
combolab.current(0)

combomaq = ttk.Combobox(pantalla, state='disable',textvariable=mq)
combomaq.place(x=300, y=100)
#------------------------------------------------
dat = StringVar()
dat.set("---------------------------------------------------Bienvenidos------------------------------------------------------" )
lbpanta = Label(pantalla,textvariable=dat,bd=1,relief="solid",font="Times 12",width=78,height=12,anchor=NW,bg="lightgray").place(x=50,y=175)

#---------------------Etiquetas-------------------

et1 = Label(pantalla, text= "Seleccione un laboratorio: ",bg="white",font="ALGERIAN 12").place(x=50,y=50)
et2 = Label(pantalla, text= "Seleccione una máquina: ",bg="white",font="ALGERIAN 12").place(x=50,y=100)
et3 = Label(pantalla, text= "REGISTROS:",bg="white",font="ALGERIAN 12").place(x=50,y=150)

#--------------------BOTTONES------------------------
btn1 = Button(pantalla,text= "NUEVO", command=mostrar,bg="blue",fg="white",font="ALGERIAN 12").place(x=550,y=425)
btn2 = Button(pantalla, text= "CONSULTAR",command=prueba,bg="blue",fg="white",font="ALGERIAN 12").place(x=650,y=425)
btn3 = Button(pantalla, text= "SELECCNIONAR",command=select,bg="blue",fg="white",font="ALGERIAN 12").place(x=450,y=45)
btn4 = Button(pantalla, text= "SALIR",command=Salir,bg="red",fg="white",font="ALGERIAN 12").place(x=50,y=425)
mainloop()

