import datetime
import pytz 
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from pytz import UnknownTimeZoneError
from io import open 

def zona_horaria():
    listbox.delete(0,END)
    for zona in pytz.all_timezones:
        listbox.insert(END,zona)    

#Criba zona horaria por país
def zona_horaria_pais():
    zona_pais = entry2.get()
    listbox2.delete(0,END)
    encontrada = False

    for zona in pytz.all_timezones:
        if  zona_pais in zona:
            listbox2.insert(END,zona)
            encontrada = True  
            
    if not encontrada:
            messagebox.showinfo("Atención","Ninguna coincidencia en la búsqueda")
            

def reloj ():
    dt =  datetime.datetime.now()
    dt_str = dt.strftime("%A %d %B %Y %H:%M") 
    label_01.config(text=dt_str)

def reloj_internacional():
    zona = entry.get()
    try:
        dt_zona_horaria = datetime.datetime.now(pytz.timezone(zona)) 
        dt_str = dt_zona_horaria.strftime("%A %d %B %Y %H:%M")
        label_3.config(text = dt_str)
    except: 
        messagebox.showerror("Error", "La zona horaria introducida no se reconoce")


def info():
    messagebox.showinfo("klk","Este programa te permitirá saber qué hora está viendo tu preciosa novia en cualquier parte del mundo")

def guardar_como():
    mensaje = text.get("1.0",END)
    fichero = filedialog.asksaveasfile(title="Guardar texto", mode="w",defaultextension=".txt")
    fichero.write(mensaje)
    fichero.close()

root = Tk() #inicio de la interfaz 
root.title("¿Qué horá será?")

#Menú interactivo 
menubar = Menu(root)
root.config(menu=menubar)

#Menú archivo
filemenu = Menu(menubar)
filemenu.add_command(label="Guardar texto como",command = guardar_como)
filemenu.add_command(label = "salir", command=root.quit)
menubar.add_cascade(label="Archivo",menu = filemenu)


#Menú ayuda
helpmenu =Menu(menubar)
helpmenu.add_command(label="acerca del programa", command = info)
menubar.add_cascade(label="Ayuda", menu = helpmenu) 


#paso 0, conocer tu hora actual
label_0 = Label(root,text="Consulta tu hora")
label_0.pack()
boton_conocer_tu_hora = Button(root, text="tu hora", command = reloj)
boton_conocer_tu_hora.pack()
label_01= Label(root,text="")
label_01.pack()



#Primer paso, conocer la zona horaria
label_1 = Label(root, text = "conocer zona horaria") 
label_1.pack()
boton_conocer_zona_horaria = Button(root,text = "zonas horarias", command= zona_horaria)
boton_conocer_zona_horaria.pack()

#prueba para cribar la zona horaria por país
label_criba = Label(root,text="Buscar solo zonas horarias de x país")
label_criba.pack()
entry2 = Entry(root)
entry2.pack()
boton_ciba_pais = Button(root, text="zonas x país",command=zona_horaria_pais)
boton_ciba_pais.pack()


#Listbox para mostrar las zonas horarias usando la clase Scrollbar
frame = Frame(root)
frame.pack()
scrollbar = Scrollbar(frame,orient=VERTICAL)
listbox = Listbox(frame, yscrollcommand=scrollbar.set, width=50,height=10)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=RIGHT,fill=Y)
listbox.pack(side=LEFT, fill=BOTH)
listbox.config(bg="lightblue")

#Para mostrar en el orden correcto las listas, ponemos el frame2 cribado por país debajo del frame donde se muestran todas las zonas horarias
frame2 = Frame(root)
frame2.pack()
scrollbar2 = Scrollbar(frame2, orient=VERTICAL)
listbox2 = Listbox(frame2, yscrollcommand=scrollbar2.set, width=50,height=10)
scrollbar2.config(command=listbox2.yview)
scrollbar2.pack(side=RIGHT,fill=Y)
listbox2.pack(side=LEFT, fill=BOTH)
listbox2.config(bg="pink")

#Segundo paso, conocer la hora en esa zona horaria 
label_2 = Label(root, text = "Introduce la zona horaria seleccionada") 
label_2.pack()
entry = Entry(root)
entry.pack()
boton_conocer_hora_internacional = Button(root, text= "conocer hora internacional", command = reloj_internacional)
boton_conocer_hora_internacional.pack()
label_3 = Label(root, text = "")
label_3.pack()

#cuadro de texto para poder escriir la hora o lo que quieras
label_fin = Label(root, text="\nEscribe lo que quieras, una carta de amor a tu novia por ejemplo\n")
label_fin.pack()
text = Text(root)
text.pack()
text.config(width=50, height=10, selectbackground="#FCFABF",bg="#EBD3ED")


root.mainloop() #fin de la interfaz 