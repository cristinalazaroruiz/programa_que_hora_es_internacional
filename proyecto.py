from tkinter import *
from tkinter import filedialog as FileDialog 
from io import open 
ruta= "" #La utilizaremos para almacenar la ruta de un fichero. Si la ruta está vacía, el fichero es nuevo. 

#funciones que se ejecutarán en el programa (en el menú superior más bien)
def nuevo(): #para borrar el contenido del fichero 
    global ruta #esto indica que la variable "ruta" hace referencia a una variable que está más hacia fuera del código, y que es la que vamos a estar usando de manera global
    mensaje.set("Nuevo fichero")
    ruta = ""
    text.delete(1.0,END) #para borrar el texto, desde el primer carácter hasta el final, pero conservando el primer salto de línea
    root.title("Mi editor")

def abrir(): #buscar un directorio en una ventana emergente y selecccionar un fichero.txt, que se dee abrir en el programa
    global ruta 
    mensaje.set("Abrir fichero")
    ruta = FileDialog.askopenfilename(initialdir=".", filetypes=(("fichero de texto","*.txt"),),title="Arir un fichero de texto") #para que de primeras se abra el directorio actual, se pone un punto. 
    if ruta != "": #este if indica que ocurre cuando hemos elegido una ruta y un fichero que queremos abrir con el programa (solo ficheros de texto)
        fichero = open(ruta, "r")
        contenido = fichero.read() #guardamos en una variable el contenido del fichero
        text.delete(1.0,END) #nos aseguramos que esté vacío el cuadro de texto antes de cargar el contenido 
        text.insert("insert",contenido)
        fichero.close()
        root.title(ruta,"- Mi editor")
        
def guardar():
    #global ruta 
    mensaje.set("Guardar fichero")
    if ruta != "":
        contenido = text.get(1.0,"end-1c") #si la ruta está establecida, tenemos un contenido (de la función abrir) que podemos recuperar 
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("El fichero se ha guardado correctamente")

    else:
        guardar_como()

def guardar_como():
    global ruta 
    mensaje.set("Guardar fichero como")
    fichero = FileDialog.asksaveasfile(title="Guardar fichero", mode = "w", defaultextension=".txt")
    if fichero is not None:
        ruta = fichero.name #a ruta le damos la ruta de fichero 
        contenido = text.get(1.0,"end-1c") #si la ruta está establecida, tenemos un contenido (de la función abrir) que podemos recuperar 
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("El fichero se ha guardado correctamente")
    else: 
        mensaje.set("Guardado cancelado")
        ruta  = ""


root = Tk()
root.title("Editor de texto casero")

#Menú superior
menubar  = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir",command=abrir)
filemenu.add_command(label="Guardar",command=guardar)
filemenu.add_command(label="Guardar como",command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir",command=root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo")


#Caja de texto central 
text = Text(root)
text.pack(fill=BOTH, expand=1)
text.config(bd=0, padx=6, pady=4, font=("Consolas",12))

#Label para mostrar info en la parte inferior
mensaje = StringVar() #modo stringvar para ir modificando el contenido según la acción que se ejecute 
mensaje.set("Bienvenido a tu editor")
monitor = Label(root,textvar=mensaje, justify="left")
monitor.pack(side=LEFT)

#fin de la interfaz 
root.config(menu=menubar)
root.mainloop() 