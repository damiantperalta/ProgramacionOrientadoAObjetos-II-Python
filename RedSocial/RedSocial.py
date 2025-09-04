#Damián Peralta, Luis Calegari, Lucas Morilla
#importaciones de bibliotecas internas                              1
import sys
import random
#importaciones de bibliotecas externas
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
import pygame

# Inicializar pygame y el mixer                           2
pygame.init()
pygame.mixer.init()

#-------------------------Grafo y diccionario-------------# 3

# Definir las relaciones y sus pesos. (Diccionario)
relaciones = {
    "amigo personal": 3,
    "conocido": 2,
    "compañero": 1
}

# Crear los grafos
G1 = nx.Graph()
G2 = nx.Graph()

#-----------------------Definición de sonidos--------------------------#         4

moneda = pygame.mixer.Sound('click.mp3')  # Cargar el archivo de sonido
moneda.set_volume(0.5)  # Ajustar el volumen del sonido

recarga = pygame.mixer.Sound('recargar.mp3')  
recarga.set_volume(0.8)  

apagar = pygame.mixer.Sound('apagar.mp3')  
apagar.set_volume(0.5)  

#-----------------------Funciones de utilidad--------------------------#         5

# Función para redimensionar imágenes manteniendo la proporción
def resize_image(imagen, base_width):
    porcentajew = (base_width / float(imagen.size[0]))
    hsize = int((float(imagen.size[1]) * float(porcentajew)))
    return imagen.resize((base_width, hsize), Image.LANCZOS)

# Función para reproducir el sonido
def sonido_moneda():
    moneda.play()  # Reproducir el sonido

def sonido_recarga():
    recarga.play()  

def sonido_apagar():
    apagar.play()  

def iniciar_cancion():
    pygame.mixer.music.load('fox.mp3')
    pygame.mixer.music.set_volume(0.5)  # Ajusta el volumen entre 0.0 y 1.0
    pygame.mixer.music.play(loops=0)  # Reproduce una vez (0 veces de repetición)
    
def parar_cancion(event=None):
    pygame.mixer.music.stop()  # Detener la música

    
#---------------------------Funciones de la interfaz gráfica---------------------------#       6

# Función para redimensionar la imagen de fondo
def resize_bg_image(event):
    global bg_image, bg_photo, bg_image_id
    new_width = event.width + 80
    new_height = event.height + 80
    resized_image = bg_image.resize((new_width, new_height), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(resized_image)
    canvas.itemconfig(bg_image_id, image=bg_photo)
    canvas.config(width=new_width, height=new_height)

def shake_background(canvas, bg_image_id, amplitude=30):
    # Generar desplazamientos aleatorios en X e Y
    dx = random.randint(-amplitude, amplitude)
    dy = random.randint(-amplitude, amplitude)

    # Mover la imagen de fondo en el canvas
    canvas.move(bg_image_id, dx, dy)

    # Programar el siguiente movimiento de temblor después de un intervalo corto
    canvas.after(1000, lambda: shake_background(canvas, bg_image_id, amplitude))

def entrar1(event):
    btn1.config(image=photo_hover1)
    sonido_recarga()

def salir1(event):
    btn1.config(image=photo_ingresar)
    
def entrar2(event):
    btn2.config(image=photo_hover2)
    sonido_recarga()

def salir2(event):
    btn2.config(image=photo_calcular)

def entrar3(event):
    btn3.config(image=photo_hover3)
    sonido_recarga()

def salir3(event):
    btn3.config(image=photo_mostrar)

def entrar4(event):
    btn4.config(image=photo_hover4)
    sonido_recarga()

def salir4(event):
    btn4.config(image=photo_salir)

#--------------------------Funciones del menú-------------------------#                 7
# Funciones para cada opción del menú
def seleccionar_grafo():
    seleccion = simpledialog.askstring("Seleccionar grafo", "Selecciona el grafo (1 o 2):", parent=root)
    if seleccion == '1':
        return G1
    elif seleccion == '2':
        return G2
    elif seleccion == '000':
        return None
    else:
        messagebox.showerror("Error", "Selección no válida. Por favor, selecciona 1 o 2.", parent=root)
        return None

def ingresar_relaciones():
    grafo = seleccionar_grafo()
    if grafo is None:
        return
    persona1 = simpledialog.askstring("Ingresar relaciones", "Nombre de la primera persona:", parent=root).upper()
    if persona1 == '000':
        return
    persona2 = simpledialog.askstring("Ingresar relaciones", "Nombre de la segunda persona:", parent=root).upper()
    if persona2 == '000':
        return

    if persona1 == persona2:
        messagebox.showerror("Error", "No puedes ingresar dos personas con el mismo nombre.", parent=root)
        return

    while True:
        tipo_relacion = simpledialog.askstring("Ingresar relaciones", "Tipo de relación (amigo personal, conocido, compañero):", parent=root).lower()
        if tipo_relacion in relaciones:
            grafo.add_edge(persona1, persona2, weight=relaciones[tipo_relacion])
            messagebox.showinfo("Información", f"Se agregó la relación {tipo_relacion} entre {persona1} y {persona2} en el grafo {1 if grafo == G1 else 2}.", parent=root)
            break
        elif tipo_relacion == '000':
            return
        else:
            messagebox.showerror("Error", "Tipo de relación no válido. Por favor, ingresa 'amigo personal', 'conocido' o 'compañero'.", parent=root)

def calcular_distancia():
    grafo = seleccionar_grafo()
    if grafo is None:
        return
    persona1 = simpledialog.askstring("Calcular distancia", "Nombre de la primera persona:", parent=root).upper()
    if persona1 == '000':
        return
    persona2 = simpledialog.askstring("Calcular distancia", "Nombre de la segunda persona:", parent=root).upper()
    if persona2 == '000':
        return

    if persona1 not in grafo or persona2 not in grafo:
        messagebox.showerror("Error", f"Una o ambas personas no existen en el grafo seleccionado.", parent=root)
        return

    try:
        distancia = nx.dijkstra_path_length(grafo, persona1, persona2, weight='weight')
        messagebox.showinfo("Resultado", f"La distancia de amistad entre {persona1} y {persona2} es {distancia}.", parent=root)
    except nx.NetworkXNoPath:
        messagebox.showerror("Error", "No existe un camino entre estas dos personas.", parent=root)

def mostrar_grafo():
    grafo = seleccionar_grafo()
    if grafo is None:
        return
    fig = plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(grafo)
    nx.draw(grafo, pos, with_labels=True, node_color='red', node_size=1500, font_size=12)
    labels = nx.get_edge_attributes(grafo, 'weight')
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)
    plt.title(f"Grafo {1 if grafo == G1 else 2}")
    
    # Mostrar la gráfica y asegurarse de que esté en primer plano
    plt.show(block=False)
    fig.canvas.manager.window.attributes('-topmost', 1)

def salir():
    pygame.mixer.music.stop()  # Detener la música
    sonido_apagar()  # Reproducir el sonido
    pygame.time.wait(3000)  # Esperar un segundo (1000 ms) para asegurar que se reproduzca el sonido

    root.destroy()  # Destruir la ventana principal
    pygame.quit()  # Cerrar pygame
    sys.exit()  # Salir del programa

#--------------------------------Configuración de la interfaz gráfica---------------------#        8

# Crear la ventana principal
root = tk.Tk()
root.title("Trabajo práctico 2: Interfaz gráfica")
root.geometry("+0+0")  # Ajusta la ventana coloca en la esquina superior izquierda

# Bind para detener la música con la tecla "F"
root.bind("<f>", parar_cancion)

# Obtener el tamaño de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Cargar la imagen de fondo
bg_image = Image.open("mapa.png")
bg_image = bg_image.resize((screen_width, screen_height), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Crear un canvas para colocar la imagen de fondo
canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg='#000000')
canvas.pack(fill="both", expand=True)
bg_image_id = canvas.create_image(0, 0, image=bg_photo, anchor="nw") 

# Manejar evento de redimensionamiento de la ventana
root.bind("<Configure>", resize_bg_image)

# Iniciar el efecto de temblor en el fondo
# Iniciar el efecto de temblor después de 1 segundo (1000 ms)
root.after(10000, lambda: shake_background(canvas, bg_image_id, amplitude=3))

#---------------------Creación de botones-------------------------#                9

# Base para las imagenes de los botones
base_width = 400  # Ajustar según el tamaño deseado de los botones

# Cargar las imágenes para el estado hover (al pasar el mouse)
hover_images = ["hover1.png", "hover2.png", "hover3.png", "hover4.png"]

# Crear una lista para las imágenes hover redimensionadas
photo_hover_images = []

for img in hover_images:
    hover_img = Image.open(img).convert("RGBA")
    # Redimensionar hover3 a 220 de ancho
    if img == "hover3.png":
        resized_hover_img = resize_image(hover_img, 220)
    elif img == "hover4.png":
        resized_hover_img = resize_image(hover_img, 150)
    else:
        resized_hover_img = resize_image(hover_img, base_width)

    photo_hover = ImageTk.PhotoImage(resized_hover_img)
    photo_hover_images.append(photo_hover)

# Desempaquetar las imágenes redimensionadas
photo_hover1, photo_hover2, photo_hover3, photo_hover4 = photo_hover_images

# Cargar las imágenes para el estado normal
normal_images = ["ingresar.png", "calcular.png", "mostrar.png", "salir.png"]

# Crear una lista para las imágenes redimensionadas
photo_images = []

for img in normal_images:
    normal_img = Image.open(img).convert("RGBA")
    if img == "mostrar.png":
        resized_normal_img = resize_image(normal_img, 220)
    elif img == "salir.png":
        resized_normal_img = resize_image(normal_img, 150)
    else:
        resized_normal_img = resize_image(normal_img, base_width)
    photo_normal = ImageTk.PhotoImage(resized_normal_img)
    photo_images.append(photo_normal)

# Desempaquetar las imágenes redimensionadas
photo_ingresar, photo_calcular, photo_mostrar, photo_salir = photo_images

# Crear un frame para centrar los botones
frame = tk.Frame(root, bg='#FFFFFF')
frame.pack(expand=True)

# Crear los botones sin fondo y sin borde
btn1 = tk.Button(root, image=photo_ingresar, command=lambda: [sonido_moneda(), ingresar_relaciones()], width=photo_ingresar.width(), height=photo_ingresar.height(), borderwidth=0, highlightthickness=0, bg='black', cursor="hand2")
btn1.image = photo_ingresar  # Mantener una referencia de la imagen
btn1_window = canvas.create_window(100, 100, window=btn1, anchor='nw')
btn1.bind("<Enter>", entrar1)
btn1.bind("<Leave>", salir1)

btn2 = tk.Button(root, image=photo_calcular, command=lambda: [sonido_moneda(), calcular_distancia()], width=photo_calcular.width(), height=photo_calcular.height(), borderwidth=0, highlightthickness=0, bg='black', cursor="hand2")
btn2.image = photo_calcular  # Mantener una referencia de la imagen
btn2_window = canvas.create_window(100, 360, window=btn2, anchor='nw')
btn2.bind("<Enter>", entrar2)
btn2.bind("<Leave>", salir2)

btn3 = tk.Button(root, image=photo_mostrar, command=lambda: [sonido_moneda(), mostrar_grafo()], width=photo_mostrar.width(), height=photo_mostrar.height(), borderwidth=0, highlightthickness=0, bg='black', cursor="hand2")
btn3.image = photo_mostrar  # Mantener una referencia de la imagen
btn3_window = canvas.create_window(950, 100, window=btn3, anchor='nw')
btn3.bind("<Enter>", entrar3)
btn3.bind("<Leave>", salir3)

btn4 = tk.Button(root, image=photo_salir, command=lambda: [sonido_apagar(), salir()], width=photo_salir.width(), height=photo_salir.height(), borderwidth=0, highlightthickness=0, bg='black', cursor="hand2")
btn4.image = photo_salir  # Mantener una referencia de la imagen
btn4_window = canvas.create_window(950, 360, window=btn4, anchor='nw')
btn4.bind("<Enter>", entrar4)
btn4.bind("<Leave>", salir4)

#-------------------------------------------Cargar el icono--------------#      10
# Cargar el icono
icono_path = "icono.png"
icon_png = Image.open(icono_path)

# Redimensionar el GIF
icon_png = icon_png.resize((32, 32), Image.LANCZOS)

# Crear un objeto PhotoImage para el Png
icon_photo = ImageTk.PhotoImage(icon_png)

# Establecer el Png como icono de la ventana
root.iconphoto(True, icon_photo)


# Ejecutar la aplicación            11
iniciar_cancion()
root.mainloop()
pygame.quit()