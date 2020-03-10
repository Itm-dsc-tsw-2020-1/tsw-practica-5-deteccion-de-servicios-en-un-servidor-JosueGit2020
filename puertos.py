
import os
import tkinter as tk
import mysql.connector as mysql
import re
from tkinter import ttk


def BLista(patron, texto):
    li = re.findall(patron, texto)
    return li


#Conección de BD
conexion = mysql.connect(host='localhost', user='root', passwd='', db='puertitos')
operacion = conexion.cursor()

red = "200.33.171.13"
resultado = os.popen("nmap -sT "+red).read()

#Patrones para extraer cadenas
pat = '([0-9]+/tcp|[0-9]+/udp)'
li_port = BLista(pat, resultado)
pat = '(open|closed)'
li_state = BLista(pat, resultado)
pat = '(open.+[a-z0-9]+|closed.+[a-z0-9]+)'
li_service = BLista(pat, resultado)

#servicio de li_service
i = 0
while i < len(li_service):
    llave = li_service[i].find("open")
    if llave == 0:
        li_service[i] = li_service[i][6:]
    llave = li_service[i].find("open")
    if llave == 0:
        li_service[i] = li_service[i][8:]
    i = i + 1



i = 0
while i < len(li_service):
    operacion.execute("INSERT INTO bitacora (ip, puertos, estado, servicio) VALUES (%s, %s, %s, %s)", (red, li_port[i], li_state[i], li_service[i]))
    conexion.commit()
    i = i + 1

operacion.execute( "SELECT * FROM bitacora" )
for ip, puertos, estado, servicio in operacion.fetchall() :
    print (ip, puertos, estado, servicio)
conexion.close()

#------------Generacion de graficos ----------------

#obj ventana
ventana = tk.Tk()

#Se crean 4 grupos para listas, cada grupo corresponde a un campo: IP, Ports, States, Services
fila1 = tk.Listbox(ventana)
fila1.grid(column=0, row=0)
fila2 = tk.Listbox(ventana)
fila2.grid(column=1, row=0)
fila3 = tk.Listbox(ventana)
fila3.grid(column=2, row=0)
fila4 = tk.Listbox(ventana)
fila4.grid(column=3, row=0)

#Título de la ventana
ventana.title("Mis puertos")

#Se escriben estáticamente los campos de la ventana
fila1.insert(0, "IP")
fila2.insert(0, "Puertos")
fila3.insert(0, "Estado")
fila4.insert(0, "Servicio")

#Ciclo para añadir los datos a los grupos de listas creados anteriormente
i = 0
while i < len(li_service):
    fila1.insert(i+1, red)
    fila2.insert(i+1, li_port[i])
    fila3.insert(i+1, li_state[i])
    fila4.insert(i+1, li_service[i])
    i = i + 1

#Indicamos la redimensión y corremos el loop para que se muestre la ventana
ventana.resizable(0,0)
ventana.mainloop()

