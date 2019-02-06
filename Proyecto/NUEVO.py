from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sys
import os
import tkinter as tk
import pymysql

#--------------------BASE--------------------------
conn = pymysql.connect(host='localhost',user='root',password='',db='informacion')
a = conn.cursor()
sql = 'select * from registro'
a.execute(sql)
countrow = a.execute(sql)
data = a.fetchall()

#Consulta para cargar los géneros
dbc=("localhost","root","","informacion")
db=pymysql.connect(dbc[0], dbc[1],  dbc[2], dbc[3])
cursor=db.cursor()
sql="SELECT * FROM tipo"
try:
   cursor.execute(sql)
   results = cursor.fetchall()
   datos = []
   for row1 in results:
      titulogg = row1[1]
      datos.append(row1[1])
except:
   messagebox.showinfo("ERROR","No se ingresaron los datos...")
db.close()
#-------------------------------------------------
class Aplicacion:
    def IMPRIMIR(self):
       print(a)

    def terminar(self):
        sys.exit()
    def INSERTAR(self):
        dbc = ("localhost", "root", "", "informacion")
        db = pymysql.connect(dbc[0], dbc[1], dbc[2], dbc[3])
        cursor = db.cursor()
        GenSelec = self.tipo.get()
        cursor.execute("select id from registro LIMIT 1")
        results = cursor.fetchone()
        posicion = countrow+1

        l = int(self.lab.get())
        m = int(self.maq.get())
        fecha = self.fech.get()
        hor = self.hora.get()
        est = self.nom.get()
        mail = self.email.get()
        des = self.descrip.get()
        try:

            conA="INSERT INTO registro( id, lab, maq, fecha, hora, estudiante, email, descripcion, id_tipo) VALUES ( '%d', '%d', '%d','%s', '%s', '%s', '%s', '%s', '%d' )"
            if(GenSelec.__eq__("software")):
                g=int(1)
            else:
                g=int(2)
            conB= (posicion, l, m, fecha, hor, est, mail, des, g)

            cursor.execute( conA % conB)
            db.commit()
            messagebox.showinfo("Exito!","guardado exitosamente...")
            self.fech.set("")
            self.hora.set("")
            self.nom.set("")
            self.email.set("")
            self.descrip.set("")
            self.pantallaNuevo.withdraw()
            os.system("main.py 1")
        except:
            print("error ha ingresar los datos")

    def __init__(self):
     #---------------------------------------------------------
        self.pantallaNuevo = Tk()
        self.pantallaNuevo.config(bg="white")
        self.lab = StringVar()
        self.maq = StringVar()
        #Interfaz gráfica para el usuario
        self.pantallaNuevo.title("P R O Y E C T O:  M A R S")
        self.pantallaNuevo.geometry("400x600")
        #----------------------------------------------------------
        self.fech = StringVar()
        self.hora = StringVar()
        self.nom = StringVar()
        self.email = StringVar()
        self.tipo = StringVar()
        self.descrip = StringVar()
        #---------------------Cuadros de textos--------------------
        f = open("info.txt","r")
        d1 = f.readline()
        d2 = f.readline()
        f.close()
        self.lab.set(d1[4:])
        self.maq.set(d2[4:])
        tf1 = ttk.Entry(self.pantallaNuevo,state="readonly",textvariable=self.lab).place(x=200,y=50)
        tf2 = ttk.Entry(self.pantallaNuevo,state="readonly",textvariable=self.maq).place(x=200,y=100)
        tf3 = ttk.Entry(self.pantallaNuevo,textvariable=self.fech).place(x=200,y=150)
        tf4 = ttk.Entry(self.pantallaNuevo,textvariable=self.hora).place(x=200,y=200)
        tf5 = ttk.Entry(self.pantallaNuevo,textvariable=self.nom).place(x=200,y=250)
        tf6 = ttk.Entry(self.pantallaNuevo,textvariable=self.email).place(x=200,y=300)
        tf7 = ttk.Entry(self.pantallaNuevo,textvariable=self.descrip,  width=45).place(x=50,y=410)


        self.cmb = ttk.Combobox(self.pantallaNuevo,textvariable=self.tipo,  width=17)
        self.cmb.place(x=200,y=350)
        self.cmb['values'] = (datos)
        self.cmb.current(0)
        #---------------------Etiquetas-------------------
        img1=PhotoImage(file="mar.png")
        lbimg1=Label(self.pantallaNuevo, image=img1,borderwidth=0)
        lbimg1.place(x=50, y=460)
        fuent = "ALGERIAN  10"
        et1 = Label(self.pantallaNuevo, text= "LABORATORIO:",font=fuent,bg="white").place(x=50,y=50)
        et2 = Label(self.pantallaNuevo, text= "MÁQUINA: ",font=fuent,bg="white").place(x=50,y=100)
        et3 = Label(self.pantallaNuevo, text= "FECHA:",font=fuent,bg="white").place(x=50,y=150)
        et4 = Label(self.pantallaNuevo, text= "HORA:",font=fuent,bg="white").place(x=50,y=200)
        et5 = Label(self.pantallaNuevo, text= "NOBRE ESTUDIANTE:",font=fuent,bg="white").place(x=50,y=250)
        et6 = Label(self.pantallaNuevo, text= "CORREO ELECTRÓNICO:",font=fuent,bg="white").place(x=50,y=300)
        et7 = Label(self.pantallaNuevo, text= "Especifícanos el daño:",font=fuent,bg="white").place(x=50,y=380)
        et8 = Label(self.pantallaNuevo, text= "Tipo de daño:",font=fuent,bg="white").place(x=50,y=340)
        #--------------------BOTTONES------------------------
        btn1 = Button(self.pantallaNuevo,text="Guardar",command=self.INSERTAR,font="ALGERIAN 12",bg="blue",fg="white").place(x=150,y=450)

        mainloop()


aplicacion1=Aplicacion()



