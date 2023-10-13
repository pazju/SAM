import pygame
from moviepy.editor import*

pygame.init() 
pygame.mixer.init() 

#Ajuste de la pantalla
info = pygame.display.Info()
screen_width, screenheight = info.current_w, info.current_h
print(screen_width, screenheight)
screen = pygame.display.set_mode((screen_width, screenheight))
screen = pygame.display.set_mode((screen_width, screenheight))
pygame.display.set_caption('Juego Memoria')

# Colores
# https://htmlcolorcodes.com/es/tabla-de-colores/
color_red = (255,0,0)
color_white = (255,255,255)
color_black = (0,0,0)
color_fondo = (52, 78, 91)
color_menta = (72, 201, 176)

# Fuentes y Tamaños
font = pygame.font.SysFont("arialblack", 40)
#print(pygame.font.get_fonts()) # Comando para ver las fuentes disponibles

# Textos
intro_text = font.render("¡PONGAMOS A PRUEBA TU MEMORIA!" , True, color_white) #Aún no lo he utilizado
intro_text = font.render("¡PONGAMOS A PRUEBA TU MEMORIA!" , True, color_white)
game_name1_text = font.render("SONRISAS LLENAS DE SALUD" , True, color_white)
game_name2_text = font.render("Una rutina para recordar" , True, color_white)
instruc_text = font.render("Instrucciones del Juego" , True, color_black)
first_level_text = font.render("Primer Nivel" , True, color_black)
second_level_text = font.render("Segundo Nivel" , True, color_black)
third_level_text = font.render("Tercer Nivel" , True, color_black)
fourth_level_text = font.render("Cuarto Nivel" , True, color_black)

# Variables de Juego / Estados
open_game = True # Variable de Inicio
paused_game = False
game_state = 'intro'
state_before_pause = 0
isGame = False
next_window = False
back_window = False
level_check = False
cont_game = False
ret_intro = False

# ERRORES DE CONTEO

error = 0


#"IMÁGENES/bg-water.jpg"


# IMAGENES
fondo = pygame.image.load("FONDOS/inicio.png").convert_alpha() 
fondo_instruc = pygame.image.load("FONDOS/instruc.png").convert_alpha() 
fondo_pausa = pygame.image.load("FONDOS/pausa.png").convert_alpha() 

#VIDEOS
clip = VideoFileClip('VIDEOS/animacion_prueba.mp4').resize((screen_width, screenheight))

# Texto en pantalla
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
    
# TEXTO EN PANTALLA CENTRADO (FUNCIÓN PROPIA)
def center_text(text,Y): # Ingresa el texto de la sección TEXTOS y la posición en Y
    RECT = text.get_rect(center=(screen.get_width()/2,Y)) # El valor de 960 cambia según la pantalla
    screen.blit(text, RECT)

# CONFIGURACIÓN/CONEXIÓN CONTROL
def CONTROL(x):
    pass


# SONIDOS

success_sound_1 = pygame.mixer.Sound("AUDIOS/ganador_1.wav")
wrong_sound_1 = pygame.mixer.Sound("AUDIOS/equivocado_1.wav")


# FUNCIONES JUEGO / PANTALLAS / MENÚS

    #  PANTALLA DE CARGA 
def load_state():
    screen.fill(color_black) 
    pygame.display.update() # Actualiza Display

#   Introducción memoria
def intro():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window

    pygame.display.set_caption('Introducción Memoria') # Caption - Nombre de la ventana
    screen.blit(fondo, (0,0)) # Función que dibuja el fondo
    paused_game = False
    if next_window == True: # Tecla n oprimida
        print('instruc')
        game_state = 'instruc'
        next_window = False

    if back_window == True: # Tecla b oprimida
        print('Salir')
        open_game = False    
        back_window = False
    
    isGame = False # False porque no se encuentra dentro de un juego

    return game_state, paused_game, isGame, open_game, next_window, back_window

def instruc():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window

    pygame.display.set_caption('Instrucciones Memoria') # Caption - Nombre de la ventana
    screen.blit(fondo_instruc, (0,0)) # Función que dibuja el fondo
    paused_game = False
    if next_window == True: # Tecla n oprimida
        print('f_step')
        game_state = 'f_step'
        next_window = False

    if back_window == True: # Tecla b oprimida
        print('intro')
        game_state = 'intro'  
        back_window = False  
    
    isGame = False # False porque no se encuentra dentro de un juego    

    return game_state, paused_game, isGame, open_game, next_window, back_window

def f_step():
    global game_state
    pygame.display.set_caption('Primer Paso') # Caption - Nombre de la ventana
    ipython_display(clip, maxduration=1000000)
    clip.preview()
    game_state = 'first_level'
    return game_state

def first_level():  # Primer nivel
    global isGame
    global game_state
    global paused_game
    global level_check
    
    pygame.display.set_caption('first_level') # Caption - Nombre de la ventana
    screen.fill(color_white) 
    center_text(first_level_text,100) # Texto 
    isGame = True # Bandera que indica estado de juego activo, lo que implica que se puede pausar

    if paused_game == True: # and juegos == True: # PANTALLA DE PAUSA
        game_state = 'Pausado'

    # level_check = True / Indica que se ha superado la actividad dentro del juego
    #level_check = True    
    if level_check == True:
        game_state = 'second_level'
    return isGame, paused_game, game_state, next_window, back_window

def PAUSA(state_before_pause):
    global paused_game
    global game_state
    global cont_game
    global ret_intro
    
   
    pygame.display.set_caption('Pausa') # Caption - Nombre de la ventana
    screen.blit(fondo_pausa, (0,0)) # Función que dibuja el fondo
    if cont_game == True: #continuar juego
        paused_game = False
        cont_game = False
        if state_before_pause == 1:
            game_state = 'first_level'
    if ret_intro == True: #volver a intro memoria
        paused_game = False 
        ret_intro = False
        game_state = 'intro'
    
    return paused_game, game_state, ret_intro, cont_game


while open_game:

    #screen.blit(fondo, (0,0)) # Función que dibuja el fondo
    
    if game_state == 'intro':
        intro()

    if game_state == 'instruc':
        instruc()
    
    if game_state == 'f_step':
        f_step()

    if game_state == 'first_level':
        first_level()
        state_before_pause = 1

    if game_state == 'Pausado': # PANTALLA DE PAUSA
        PAUSA(state_before_pause)
        
    # Event Handler
    for event in pygame.event.get(): # Evento de pygame
        if event.type == pygame.KEYDOWN: # Evento: Tecla presionada
            if event.key == pygame.K_e: # Tecla e para pausar
                paused_game = True
            if event.key == pygame.K_s: # Tecla s para continuar
                next_window = True
            if event.key == pygame.K_a: # Tecla a para atrás
                back_window = True
            if event.key == pygame.K_o: # Tecla o para volver a la intro de memoria
                ret_intro = True
            if event.key == pygame.K_p: # Tecla  para continuar con el juego
                cont_game = True

        # Quit Game
        if event.type == pygame.QUIT: # Si el evento es .QUIT (Darle click en la X de la ventana generada) se deja de ejecutar el while
            open_game = False

    pygame.display.update() # Actualiza Display

pygame.quit() # Se cierra pygame
quit() # Cierra Aplicación


#######################################################################
import pygame
import sys  
import math # Redondear
import time # Permite generar un loop durante un timpo establecido (Para que las tarjetas se volteen solas de nuevo si están mal)
import random # Permite que las tarjetas salgan siempre en forma aleatoria
from moviepy.editor import*

pygame.init() 
pygame.font.init() # Inicializar fuentes a utilizar
pygame.mixer.init() 

#Ajuste de la pantalla
info = pygame.display.Info()
screen_width, screenheight = info.current_w, info.current_h
print(screen_width, screenheight)
screen = pygame.display.set_mode((screen_width, screenheight))
screen = pygame.display.set_mode((screen_width, screenheight))
pygame.display.set_caption('Juego Memoria')

# Colores
# https://htmlcolorcodes.com/es/tabla-de-colores/
color_red = (255,0,0)
color_white = (255,255,255)
color_black = (0,0,0)
color_fondo = (52, 78, 91)
color_menta = (72, 201, 176)

# Fuentes y Tamaños
font = pygame.font.SysFont("arialblack", 40)
#print(pygame.font.get_fonts()) # Comando para ver las fuentes disponibles

# Textos
intro_text = font.render("¡PONGAMOS A PRUEBA TU MEMORIA!" , True, color_white) #Aún no lo he utilizado
intro_text = font.render("¡PONGAMOS A PRUEBA TU MEMORIA!" , True, color_white)
game_name1_text = font.render("SONRISAS LLENAS DE SALUD" , True, color_white)
game_name2_text = font.render("Una rutina para recordar" , True, color_white)
instruc_text = font.render("Instrucciones del Juego" , True, color_black)
first_level_text = font.render("Primer Nivel" , True, color_black)
Fst_level_text = font.render("Segundo Nivel" , True, color_black)
third_level_text = font.render("Tercer Nivel" , True, color_black)
fourth_level_text = font.render("Cuarto Nivel" , True, color_black)

# Variables de Juego / Estados
open_game = True # Variable de Inicio
paused_game = False
game_state = 'intro'
state_before_pause = 0
isGame = False
next_window = False
back_window = False
level_check = False
cont_game = False
ret_intro = False

# ERRORES 
error_1 = 0

#ACIERTOS 
acierto_1 = 0

# CRONOMETROS

# Cronometro  primer nivel
timer_font = pygame.font.SysFont("adobedevanagaribold", 30)
level_time = 20 # 20s
timer_text = timer_font.render(str(level_time), True, color_black)
timer_event = pygame.USEREVENT+1 # Evento de Usuario + 1 (USEREVENT 25 - ID) 
timer_active = False # Variable para controlar si el temporizador está o no activo





# Movimiento del cursor
velocidad = 1 # pixeles que se moveran en cada dirección
movimiento_x = 0 
movimiento_y = 0

# Primer nivel
medida_cuadro_h = screen_width/5  # Medida de la imagen en pixeles
medida_cuadro_v = screenheight/2  # Medida de la imagen en pixeles

ganar1 = False

# Imagen cuando la figura está oculta
tarjeta_oculta = "F_LEVEL/oculta.png"
imagen_oculta = pygame.image.load(tarjeta_oculta)
segundos_mostrar_pieza = 2  # Segundos para ocultar la pieza si no es la correcta
# Esta clase representa el cuadro de la tarjeta
class Cuadro:
    def __init__(self, fuente_imagen):
        self.mostrar = False
        self.descubierto = False
        """
        Una cosa es la fuente de la imagen (es decir, el nombre del archivo) y otra
        la imagen lista para ser pintada por PyGame
        La fuente la necesitamos para más tarde, comparar las tarjetas
        """
        self.fuente_imagen = fuente_imagen # Fuente: nombre de la img. para hacer la comparación
        self.imagen_real = pygame.image.load(fuente_imagen) # imagen 
cuadros = [
    [Cuadro("F_LEVEL/crema.png"), Cuadro("F_LEVEL/agua.png"), Cuadro("F_LEVEL/crema.png"), Cuadro("F_LEVEL/enjuague.png"),Cuadro("F_LEVEL/cepillo.png")],
    [Cuadro("F_LEVEL/hilo.png"), Cuadro("F_LEVEL/agua.png"), Cuadro("F_LEVEL/hilo.png"), Cuadro("F_LEVEL/cepillo.png"),Cuadro("F_LEVEL/enjuague.png")],  
]



# Los sonidos a utilizar
sonido_fondo = pygame.mixer.Sound("F_LEVEL/fondo.wav")
sonido_clic = pygame.mixer.Sound("F_LEVEL/clic.mp3")
sonido_exito = pygame.mixer.Sound("F_LEVEL/ganador.mp3")
sonido_fracaso = pygame.mixer.Sound("F_LEVEL/equivocado.mp3")
sonido_voltear = pygame.mixer.Sound("F_LEVEL/voltear.mp3")

# Banderas
# Bandera para saber si se debe ocultar la tarjeta dentro de N segundos
ultimos_segundos = None
puede_jugar = True  # Bandera para saber si reaccionar a los eventos del usuario
# Saber si el juego está iniciado; así sabemos si ocultar o mostrar piezas, además del botón
juego_iniciado = False
# Banderas de las tarjetas cuando se busca una pareja. Las necesitamos como índices para el arreglo de cuadros
# Se conoce si es la primera vez que se voltea una tarjeta o si es la segunda
# x1 con y1 sirven para la primer tarjeta
x1 = None
y1 = None
# Y las siguientes para la segunda tarjeta
x2 = None
y2 = None
# Ocultar todos los cuadros
# Recorre las filas y colmunas de los cuadros
def ocultar_todos_los_cuadros():
    for fila in cuadros:
        for cuadro in fila:
            cuadro.mostrar = False
            cuadro.descubierto = False


# Calcula la cantidad de filas y cantidad de columnas y elige aleatoriamente una imagen
def aleatorizar_cuadros():
    # Elegir X e Y aleatorios, intercambiar
    cantidad_filas = len(cuadros)
    cantidad_columnas = len(cuadros[0])
    for y in range(cantidad_filas):
        for x in range(cantidad_columnas):
            x_aleatorio = random.randint(0, cantidad_columnas - 1)
            y_aleatorio = random.randint(0, cantidad_filas - 1)
            cuadro_temporal = cuadros[y][x]
            cuadros[y][x] = cuadros[y_aleatorio][x_aleatorio]
            cuadros[y_aleatorio][x_aleatorio] = cuadro_temporal

# Determina si se gana, reinicia el juego y suena la pista correspondiente
def comprobar_si_gana():
    global acierto_1
    global game_state
    global ganar1
    if gana():
        pygame.mixer.Sound.play(sonido_exito)
        print("Aciertos:", acierto_1)
        print("Errores:", error_1)
        ganar1 = True
    return acierto_1, game_state, ganar1
        
        


# Regresa False si al menos un cuadro NO está descubierto. True en caso de que absolutamente todos estén descubiertos
# Recorre todas las filas de la matriz y en caso de que alguno no esté descubierto retorna a falso, de lo contrario pasa a true
def gana():
    for fila in cuadros:
        for cuadro in fila:
            if not cuadro.descubierto:
                return False
    return True

    

# si es falso, se reinicia el juego donde se modifica una variable global con falso
def reiniciar_juego():
    global juego_iniciado
    juego_iniciado = False

# Reproduce el sonido de click para que empiece, modifica el juego iniciado y lo aleatoriza 3 veces (primero mezcla los cuadros y luego los oculta)
def iniciar_juego():
    global juego_iniciado
    global automatico
    pygame.mixer.Sound.play(sonido_clic)
    automatico = pygame.MOUSEBUTTONDOWN
    
    # Aleatorizar 3 veces
    """for i in range(3):
        aleatorizar_cuadros()"""
    ocultar_todos_los_cuadros()
    juego_iniciado = True



# IMAGENES
fondo = pygame.image.load("FONDOS/inicio.png").convert_alpha() 
fondo_instruc = pygame.image.load("FONDOS/instruc.png").convert_alpha() 
fondo_pausa = pygame.image.load("FONDOS/pausa.png").convert_alpha() 
fondo_ganador1 = pygame.image.load("FONDOS/ganador1.png").convert_alpha() 
agua = pygame.image.load("F_LEVEL/agua.png").convert_alpha() 
cepillo = pygame.image.load("F_LEVEL/cepillo.png").convert_alpha() 
crema = pygame.image.load("F_LEVEL/crema.png").convert_alpha() 
hilo = pygame.image.load("F_LEVEL/hilo.png").convert_alpha()
enjuague = pygame.image.load("F_LEVEL/enjuague.png").convert_alpha()  

#IMAGENES CURSOR
#cursor_original = pygame.image.load("F_LEVEL/cursor.png").convert_alpha() 
cursor_original = pygame.image.load("F_LEVEL/cursor_clic.png").convert_alpha() 



#VIDEOS
clip = VideoFileClip('VIDEOS/animacion_prueba.mp4').resize((screen_width, screenheight))

# Texto en pantalla
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
    
# TEXTO EN PANTALLA CENTRADO (FUNCIÓN PROPIA)
def center_text(text,Y): # Ingresa el texto de la sección TEXTOS y la posición en Y
    RECT = text.get_rect(center=(screen.get_width()/2,Y)) # El valor de 960 cambia según la pantalla
    screen.blit(text, RECT)

# CONFIGURACIÓN/CONEXIÓN CONTROL
def CONTROL(x):
    pass


# SONIDOS

success_sound_1 = pygame.mixer.Sound("AUDIOS/ganador_1.wav")
wrong_sound_1 = pygame.mixer.Sound("AUDIOS/equivocado_1.wav")


# FUNCIONES JUEGO / PANTALLAS / MENÚS

    #  PANTALLA DE CARGA 
def load_state():
    screen.fill(color_black) 
    pygame.display.update() # Actualiza Display

#   Introducción memoria
def intro():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window

    pygame.display.set_caption('Introducción Memoria') # Caption - Nombre de la ventana
    screen.blit(fondo, (0,0)) # Función que dibuja el fondo
    paused_game = False

    pygame.mouse.set_visible(False)#Ocultar el cursor 

    if next_window == True: # Tecla n oprimida
        print('instruc')
        game_state = 'instruc'
        next_window = False

    if back_window == True: # Tecla b oprimida
        print('Salir')
        open_game = False
        back_window = False
    
    isGame = False # False porque no se encuentra dentro de un juego

    return game_state, paused_game, isGame, open_game, next_window, back_window

def instruc():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window

    pygame.display.set_caption('Instrucciones Memoria') # Caption - Nombre de la ventana
    screen.blit(fondo_instruc, (0,0)) # Función que dibuja el fondo
    paused_game = False
    if next_window == True: # Tecla n oprimida
        game_state = 'first_level'
        next_window = False

    if back_window == True: # Tecla b oprimida
        print('intro')
        game_state = 'intro'  
        back_window = False  
    
    isGame = False # False porque no se encuentra dentro de un juego    

    return game_state, paused_game, isGame, open_game, next_window, back_window

def f_step():
    global game_state
    global isGame
    isGame = False
    pygame.display.set_caption('Primer Paso') # Caption - Nombre de la ventana
    ipython_display(clip, maxduration=1000000)
    clip.preview()
    game_state = 'first_level'
    return game_state

def first_level():  # Primer nivel
    global isGame
    global game_state
    global paused_game
    global agua
    global crema
    global enjuague
    global cepillo
    global hilo
    global screen_width
    global screenheight
    global timer_text, level_time, timer_active
    
    pygame.display.set_caption('first_level') # Caption - Nombre de la ventana
    screen.fill(color_white) 
    isGame = False # Bandera que indica estado de juego activo, lo que implica que se puede pausar
    image_matrix = [ [crema, agua, crema, enjuague, cepillo],  [hilo, agua, hilo, cepillo, enjuague]]

    rows = len(image_matrix)
    cols = len(image_matrix[0])
    image_width = image_matrix[0][0].get_width()
    image_height = image_matrix[0][0].get_height()
    padding_x = (screen_width - (cols * image_width)) // (cols + 1)
    padding_y = (screenheight - (rows * image_height)) // (rows + 1)
    timer_rect = timer_text.get_rect(center = (90,90)) # Centro de la pantalla: center = screen.get_rect().center
    

    for i in range(rows):
        for j in range(cols):
            x = padding_x + j * (image_width + padding_x)
            y = padding_y + i * (image_height + padding_y)
            screen.blit(image_matrix[i][j], (x, y))
            #center_text(first_level_text,100) # Texto
            screen.blit(timer_text, timer_rect) 
        
    if not timer_active and game_state == 'first_level':
        level_time = 20
        pygame.time.set_timer(timer_event, 1000) # set_timer crea una acción cada 1s
        timer_active = True

    if paused_game == True: # and juegos == True: # PANTALLA DE PAUSA
        game_state = 'Pausado'

    return isGame, paused_game, game_state, next_window, back_window, timer_text, level_time, timer_active


def Fst_level():
    global isGame
    global game_state
    global paused_game
    global segundos_mostrar_pieza
    global cuadros
    global imagen_oculta
    global medida_cuadro_h
    global medida_cuadro_v
    global puede_jugar
    global ultimos_segundos
    global x1, y1, x2, y2

    #pygame.mouse.set_visible(True)# Hacer visible el cursor   

    pygame.display.set_caption('Fst_level') # Caption - Nombre de la ventana
    screen.fill(color_white) 
    isGame = True # Bandera que indica estado de juego activo, lo que implica que se puede pausar
    center_text(Fst_level_text,100) # Texto

    ahora = int(time.time())
    # Y aquí usamos la bandera del tiempo, de nuevo. Si los segundos actuales menos los segundos
    # en los que se empezó el ocultamiento son mayores a los segundos en los que se muestra la pieza, entonces
    # se ocultan las dos tarjetas y se reinician las banderas
    if ultimos_segundos is not None and ahora - ultimos_segundos >= segundos_mostrar_pieza:
        cuadros[y1][x1].mostrar = False
        cuadros[y2][x2].mostrar = False
        x1 = None
        y1 = None
        x2 = None
        y2 = None
        ultimos_segundos = None
        # En este momento el usuario ya puede hacer clic de nuevo pues las imágenes ya estarán ocultas
        puede_jugar = True

    # Hacer toda la pantalla blanca
    screen.fill(color_white)
    # Banderas para saber en dónde dibujar las imágenes, pues al final
    # la pantalla de PyGame son solo un montón de pixeles
    x = 0
    y = 0
    # Recorrer los cuadros
    for fila in cuadros:
        x = 0
        for cuadro in fila:
            """
            Si está descubierto o se debe mostrar, dibujamos la imagen real. Si no,
            dibujamos la imagen oculta
            """
            if cuadro.descubierto or cuadro.mostrar:
                screen.blit(cuadro.imagen_real, (x, y))
            else:
                screen.blit(imagen_oculta, (x, y))
            x += medida_cuadro_h
        y += medida_cuadro_v

    if paused_game == True: # and juegos == True: # PANTALLA DE PAUSA
        game_state = 'Pausado'
        isGame = False
    return isGame, paused_game, game_state, back_window

def completed_1():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window

    pygame.display.set_caption('Completo nivel 1') # Caption - Nombre de la ventana
    screen.blit(fondo_ganador1, (0,0)) # Función que dibuja el fondo
    paused_game = False
    if next_window == True: # Tecla n oprimida
        game_state = 'instruc'
        next_window = False

    if back_window == True: # Tecla b oprimida
        print('intro')
        game_state = 'first_level' 
        back_window = False  
    
    isGame = False # False porque no se encuentra dentro de un juego    

    return game_state, paused_game, isGame, open_game, next_window, back_window

    

def PAUSA(state_before_pause):
    global paused_game
    global game_state
    global cont_game
    global ret_intro
    
   
    pygame.display.set_caption('Pausa') # Caption - Nombre de la ventana
    screen.blit(fondo_pausa, (0,0)) # Función que dibuja el fondo
    if cont_game == True: #continuar juego
        paused_game = False
        cont_game = False
        if state_before_pause == 1:
            game_state = 'first_level'
        if state_before_pause == 2:
            game_state = 'Fst_level'
    if ret_intro == True: #volver a intro memoria
        paused_game = False 
        ret_intro = False
        game_state = 'intro'
    
    return paused_game, game_state, ret_intro, cont_game
if isGame:
    pygame.event.set_grab(True)  # Capturar el cursor dentro de la ventana

while open_game:

    #screen.blit(fondo, (0,0)) # Función que dibuja el fondo
    
    if game_state == 'intro':
        intro()

    if game_state == 'instruc':
        instruc()
    
    if game_state == 'f_step':
        f_step()

    if game_state == 'first_level':
        first_level()
        state_before_pause = 1

    if game_state == 'Fst_level':
        Fst_level()
        state_before_pause = 2
    
    if game_state == 'completed_1':
        completed_1()

    if game_state == 'Pausado': # PANTALLA DE PAUSA
        PAUSA(state_before_pause)
        
    # Event Handler
    for event in pygame.event.get(): # Evento de pygame
        if event.type == pygame.KEYDOWN: # Evento: Tecla presionada
            if event.key == pygame.K_e: # Tecla e para pausar
                paused_game = True
            if event.key == pygame.K_s: # Tecla s para continuar
                next_window = True
            if event.key == pygame.K_a: # Tecla a para atrás
                back_window = True
            if event.key == pygame.K_o: # Tecla o para volver a la intro de memoria
                ret_intro = True
            if event.key == pygame.K_p: # Tecla  para continuar con el juego
                cont_game = True
                # Si hicieron clic y el usuario puede jugar...
            # Primer nivel seleccionar tarjeta con tecla b
            if event.key == pygame.K_b and puede_jugar:
                
                """
                xAbsoluto e yAbsoluto son las coordenadas de la pantalla en donde se hizo
                clic. PyGame no ofrece detección de clic en imagen, por ejemplo. Así que
                se deben hacer ciertos trucos
                """
                # Si el click fue sobre el botón y el juego no se ha iniciado, entonces iniciamos el juego
                xAbsoluto, yAbsoluto = pygame.mouse.get_pos()
                #if boton.collidepoint(event.pos):
                #   if not juego_iniciado:
                #      iniciar_juego()

                #else:
                    # Si no hay juego iniciado, ignoramos el clic
                select = True
                
                if juego_iniciado:
                    iniciar_juego()
                    continue
                """
                Ahora necesitamos a X e Y como índices del arreglo. Los índices no
                son lo mismo que los pixeles, pero sabemos que las imágenes están en un arreglo
                y por lo tanto podemos dividir las coordenadas entre la medida de cada cuadro, redondeando
                hacia abajo, para obtener el índice.
                Por ejemplo, si la medida del cuadro es 100, y el clic es en 140 entonces sabemos que le dieron
                a la segunda imagen porque 140 / 100 es 1.4 y redondeado hacia abajo es 1 (la segunda posición del
                arreglo) lo cual es correcto. Por poner otro ejemplo, si el clic fue en la X 50, al dividir da 0.5 y
                resulta en el índice 0
                """
                x = math.floor(xAbsoluto / medida_cuadro_h)
                y = math.floor(yAbsoluto / medida_cuadro_v)
                # Primero lo primero. Si  ya está mostrada o descubierta, no hacemos nada
                cuadro = cuadros[y][x]
                if cuadro.mostrar or cuadro.descubierto:
                    # continue ignora lo de abajo y deja que el ciclo siga
                    continue
                # Si es la primera vez que tocan la imagen (es decir, no están buscando el par de otra, sino apenas
                # están descubriendo la primera)
                if x1 is None and y1 is None:
                    # Entonces la actual es en la que acaban de dar clic, la mostramos
                    x1 = x
                    y1 = y
                    cuadros[y1][x1].mostrar = True
                    pygame.mixer.Sound.play(sonido_voltear)


                else:
                    # En caso de que ya hubiera una clickeada anteriormente y estemos buscando el par, comparamos...
                    x2 = x
                    y2 = y
                    cuadros[y2][x2].mostrar = True
                    cuadro1 = cuadros[y1][x1]
                    cuadro2 = cuadros[y2][x2]
                    # Si coinciden, entonces a ambas las ponemos en descubiertas:
                    if cuadro1.fuente_imagen == cuadro2.fuente_imagen:
                        cuadros[y1][x1].descubierto = True
                        cuadros[y2][x2].descubierto = True
                        x1 = None
                        x2 = None
                        y1 = None
                        y2 = None
                        acierto_1 = acierto_1 + 1
                        pygame.mixer.Sound.play(sonido_clic)                        
                    else:
                        pygame.mixer.Sound.play(sonido_fracaso)
                        error_1 = error_1 + 1 
                        # Si no coinciden, tenemos que ocultarlas en el plazo de [segundos_mostrar_pieza] segundo(s). Así que establecemos
                        # la bandera. Como esto es un ciclo infinito y asíncrono, podemos usar el tiempo para saber
                        # cuándo fue el tiempo en el que se empezó a ocultar
                        ultimos_segundos = int(time.time())
                        # Hasta que el tiempo se cumpla, el usuario no puede jugar
                        puede_jugar = False
                comprobar_si_gana()
                if ganar1:
                    game_state = 'completed_1'#imagen que diga que ganó y siguiente nivel o cosa 

            # Para el movimiento del cursor

            if event.key == pygame.K_UP and isGame:
                movimiento_y = -velocidad
            if event.key == pygame.K_DOWN and isGame:
                movimiento_y = velocidad
            if event.key == pygame.K_LEFT and isGame:
                movimiento_x = -velocidad
            if event.key == pygame.K_RIGHT and isGame:
                movimiento_x = velocidad
        
        # si se suelta la tecla
        if event.type == pygame.KEYUP and isGame:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN and isGame:
                movimiento_y = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT and isGame:
                movimiento_x = 0

        if isGame:
        # Actualizar la posición del mouse en función del teclado o joystick
            mouse_x, mouse_y = pygame.mouse.get_pos()
            nuevo_mouse_x = mouse_x + movimiento_x
            nuevo_mouse_y = mouse_y + movimiento_y
            
            cursor = pygame.transform.scale(cursor_original,(400,300))
            posx,posy = pygame.mouse.get_pos()
            screen.blit(cursor,((posx-200),(posy-100)))


         #Limitar el movimiento de los cursores dentro de los límites de la pantalla
            if nuevo_mouse_x < 0:
                nuevo_mouse_x = 0
            if nuevo_mouse_x >= screen_width-20:
                nuevo_mouse_x = (screen_width - 20)
            if nuevo_mouse_y < 0:
                nuevo_mouse_y = 0
            if nuevo_mouse_y >= screenheight-50:
                nuevo_mouse_y = (screenheight - 50)

        # Establecer la nueva  del cursor del mouse
            pygame.mouse.set_pos((nuevo_mouse_x, nuevo_mouse_y))



        # Temporizador del primer nivel
        if event.type == timer_event and game_state == 'first_level':
            level_time -= 1 
            timer_text = timer_font.render(str(level_time), True, color_black)
            if level_time <= 0:
                pygame.time.set_timer(timer_event, 0)
                timer_active = False
                game_state = 'Fst_level'
                ##Puedo poner variables para cambiar de nivel o pantallas

        
        # Quit Game
        if event.type == pygame.QUIT: # Si el evento es .QUIT (Darle click en la X de la ventana generada) se deja de ejecutar el while
            open_game = False


    pygame.display.update() # Actualiza Display

pygame.quit() # Se cierra pygame
quit() # Cierra Aplicación