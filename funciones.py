import pygame
import math # Redondear
import time # Permite generar un loop durante un timpo establecido (Para que las tarjetas se volteen solas de nuevo si están mal)
import cv2

pygame.init() 
pygame.font.init() # Inicializar fuentes a utilizar
pygame.mixer.init() 

#Ajuste de la pantalla
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption('Juego Memoria')

#screen_width, screen_height = 800, 450
#screen = pygame.display.set_mode((screen_width, screen_height))
LI = [[0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0]]
#level = 'INICIO'
# Colores
# https://htmlcolorcodes.com/es/tabla-de-colores/
color_red = (255,0,0)
color_white = (255,255,255)
color_black = (0,0,0)
color_fondo = (52, 78, 91)
color_menta = (72, 201, 176)
color_azul_claro = (169,223,191)
color_rosado = (250, 219, 216)
color_amarillo = (247, 220, 111)


# Fuentes y Tamaños
font = pygame.font.SysFont("consolas", 40)
#print(pygame.font.get_fonts()) # Comando para ver las fuentes disponibles


# Variables de Juego / Estados
open_game = True # Variable de Inicio
paused_game = False
game_state = 'intro'
#game_state = 'exp_protesis2'
state_before_pause = 0
actual_state = 0
actual_state_board = 0
actual_matrix = 0
original_matrix = 0
actual_board = 0
isGame = False
yes_no_question = False
yes = False
no = False
next_window = False
back_window = False
level_check = False
cont_game = False
ret_intro = False
aux_cronometro = False
aux_cronometro2 = False
aux_cronometro3 = False
aux_cronometro4 = False
aux_cronometro5= False
aux_cronometro6 = False
aux_cronometro7 = False
aux_cronometro8 = False
aux_cronometro9 = False
aux_cronometro10 = False
prueba = False
prueba2 = False
prueba3 = False
prueba4 = False
prueba5 = False
prueba6 = False
prueba7 = False
prueba8 = False
prueba9 = False
prueba10 = False
#####
reinicio = False
# ERRORES 
error_1 = 0
error_2 = 0
error_3 = 0
error_4 = 0
error_5 = 0
error_6 = 0
error_7 = 0
error_8 = 0
error_9 = 0
error_10 = 0

#ACIERTOS 
acierto_1 = 0
acierto_2 = 0
acierto_3 = 0
acierto_4 = 0
acierto_5 = 0
acierto_6 = 0
acierto_7 = 0
acierto_8 = 0
acierto_9 = 0
acierto_10 = 0
# GANADORES
ganar1 = False
ganar2 = False
ganar3 = False
ganar4 = False
ganar5 = False
ganar6 = False
ganar7 = False
ganar8 = False
ganar9 = False
ganar10 = False

ganar_rein1 = 0
ganar_reinicio2 = 0
ganar_reinicio3 = 0
ganar_reinicio4 = 0
ganar_reinicio5 = 0
ganar_reinicio6 = 0
ganar_reinicio7 = 0
ganar_reinicio8 = 0
ganar_reinicio9 = 0
ganar_reinicio10 = 0

#Perdedores
perder2 = False
perder3 = False
perder4 = False
perder5 = False
perder6 = False
perder7 = False
perder8 = False
perder9 = False
perder10 = False
#Cepillos
cepillos2 = 3
cepillos3 = 3
cepillos4 = 3
cepillos5 = 3
cepillos6 = 3
cepillos7 = 3
cepillos8 = 3
cepillos9 = 3
cepillos10 = 3
#Personaje
sam = 0
sami = 0
samuel = 0
samantha = 0 
s1 = False
s2 = False
s3 = False
s4 = False

# CRONOMETROS y temporizadores

# Temporizador  primer nivel
timer_font = pygame.font.SysFont("freemono.ttf", 100)
level_time = 20 # 20s
timer_text = timer_font.render(str(level_time), True, color_black)
timer_event = pygame.USEREVENT+1 # Evento de Usuario + 1 (USEREVENT 25 - ID) 
timer_active = False # Variable para controlar si el temporizador está o no activo
# Temporizador  Segundo nivel
timer_font_2 = pygame.font.SysFont("freemono.ttf", 100)
level_time_2 = 15 # 15s
timer_text_2 = timer_font_2.render(str(level_time_2), True, color_black)
timer_event_2 = pygame.USEREVENT+1 # Evento de Usuario + 1 (USEREVENT 25 - ID) 
timer_active_2 = False # Variable para controlar si el temporizador está o no activo
# Temporizador  Tercer nivel
timer_font_3 = pygame.font.SysFont("freemono.ttf", 100)
level_time_3 = 15 # 15s
timer_text_3 = timer_font_3.render(str(level_time_3), True, color_black)
timer_event_3 = pygame.USEREVENT+1 # Evento de Usuario + 1 (USEREVENT 25 - ID) 
timer_active_3 = False # Variable para controlar si el temporizador está o no activo
# Temporizador  Cuarto nivel
timer_font_4 = pygame.font.SysFont("freemono.ttf", 100)
level_time_4 = 15 # 15s
timer_text_4 = timer_font_4.render(str(level_time_4), True, color_black)
timer_event_4 = pygame.USEREVENT+1 # Evento de Usuario + 1 (USEREVENT 25 - ID) 
timer_active_4 = False # Variable para controlar si el temporizador está o no activo
# Temporizador  quinto nivel
timer_font_5 = pygame.font.SysFont("freemono.ttf", 100)
level_time_5 = 20 # 20s
timer_text_5 = timer_font_5.render(str(level_time_5), True, color_black)
timer_event_5 = pygame.USEREVENT+1 # Evento de Usuario + 1 (USEREVENT 25 - ID) 
timer_active_5 = False # Variable para controlar si el temporizador está o no activo
# Temporizador  Sexto nivel
timer_font_6 = pygame.font.SysFont("freemono.ttf", 100)
level_time_6 = 20 # 20s
timer_text_6 = timer_font_6.render(str(level_time_6), True, color_black)
timer_event_6 = pygame.USEREVENT+1 # Evento de Usuario + 1 (USEREVENT 25 - ID) 
timer_active_6 = False # Variable para controlar si el temporizador está o no activo
# Temporizador  Septimo nivel
timer_font_7 = pygame.font.SysFont("freemono.ttf", 100)
level_time_7 = 20 # 20s
timer_text_7 = timer_font_7.render(str(level_time_7), True, color_black)
timer_event_7 = pygame.USEREVENT+1 # Evento de Usuario + 1 (USEREVENT 25 - ID) 
timer_active_7 = False # Variable para controlar si el temporizador está o no activo
# Temporizador  Octavo nivel
timer_font_8 = pygame.font.SysFont("freemono.ttf", 100)
level_time_8 = 20 # 20s
timer_text_8 = timer_font_8.render(str(level_time_8), True, color_black)
timer_event_8 = pygame.USEREVENT+1 # Evento de Usuario + 1 (USEREVENT 25 - ID) 
timer_active_8 = False # Variable para controlar si el temporizador está o no activo
# Temporizador  Noveno nivel
timer_font_9 = pygame.font.SysFont("freemono.ttf", 100)
level_time_9 = 20 # 20s
timer_text_9 = timer_font_2.render(str(level_time_9), True, color_black)
timer_event_9 = pygame.USEREVENT+1 # Evento de Usuario + 1 (USEREVENT 25 - ID) 
timer_active_9 = False # Variable para controlar si el temporizador está o no activo
# Temporizador  Decimo nivel
timer_font_10 = pygame.font.SysFont("freemono.ttf", 100)
level_time_10 = 20 # 20s
timer_text_10 = timer_font_2.render(str(level_time_10), True, color_black)
timer_event_10 = pygame.USEREVENT+1 # Evento de Usuario + 1 (USEREVENT 25 - ID) 
timer_active_10 = False # Variable para controlar si el temporizador está o no activo

# Cronometro primer nivel
start_time = 0 #0s
start_timer_text = timer_font.render(str(start_time), True, color_black)
start_timer_event = pygame.USEREVENT+1 # Evento de Usuario + 1 (USEREVENT 25 - ID) 
start_timer_active = False # Variable para controlar si el temporizador está o no activo
used_time_1 = 0
unused_time_1 = 0
time_limit_1 = 240

# Cronometro segundo nivel
start_time_2 = 0 #0s
start_timer_text_2 = timer_font.render(str(start_time_2), True, color_black)
start_timer_event_2 = pygame.USEREVENT+1 # Evento de Usuario + 1 (USEREVENT 25 - ID) 
start_timer_active_2 = False # Variable para controlar si el temporizador está o no activo
used_time_2 = 0
unused_time_2 = 0
time_limit_2 = 60

# Cronometro tercer nivel
start_time_3 = 0 #0s
start_timer_text_3 = timer_font.render(str(start_time_3), True, color_black)
start_timer_event_3 = pygame.USEREVENT+1 # Evento de Usuario + 1 (USEREVENT 25 - ID) 
start_timer_active_3 = False # Variable para controlar si el temporizador está o no activo
used_time_3 = 0
unused_time_3 = 0
time_limit_3 = 60

# Cronometro cuarto nivel
start_time_4 = 0 #0s
start_timer_text_4 = timer_font.render(str(start_time_4), True, color_black)
start_timer_event_4 = pygame.USEREVENT+1 # Evento de Usuario + 1 (USEREVENT 25 - ID) 
start_timer_active_4 = False # Variable para controlar si el temporizador está o no activo
used_time_4 = 0
unused_time_4 = 0
time_limit_4 = 60

# Cronometro quinto nivel
start_time_5 = 0 #0s
start_timer_text_5 = timer_font.render(str(start_time_5), True, color_black)
start_timer_event_5 = pygame.USEREVENT+1 # Evento de Usuario + 1 (USEREVENT 25 - ID) 
start_timer_active_5 = False # Variable para controlar si el temporizador está o no activo
used_time_5 = 0
unused_time_5 = 0
time_limit_5 = 120

# Cronometro sexto nivel
start_time_6 = 0 #0s
start_timer_text_6 = timer_font.render(str(start_time_6), True, color_black)
start_timer_event_6 = pygame.USEREVENT+1 # Evento de Usuario + 1 (USEREVENT 25 - ID) 
start_timer_active_6 = False # Variable para controlar si el temporizador está o no activo
used_time_6 = 0
unused_time_6 = 0
time_limit_6 = 120

# Cronometro septimo nivel
start_time_7 = 0 #0s
start_timer_text_7 = timer_font.render(str(start_time_7), True, color_black)
start_timer_event_7 = pygame.USEREVENT+1 # Evento de Usuario + 1 (USEREVENT 25 - ID) 
start_timer_active_7 = False # Variable para controlar si el temporizador está o no activo
used_time_7 = 0
unused_time_7 = 0
time_limit_7 = 120

# Cronometro octavo nivel
start_time_8 = 0 #0s
start_timer_text_8 = timer_font.render(str(start_time_8), True, color_black)
start_timer_event_8 = pygame.USEREVENT+1 # Evento de Usuario + 1 (USEREVENT 25 - ID) 
start_timer_active_8 = False # Variable para controlar si el temporizador está o no activo
used_time_8 = 0
unused_time_8 = 0
time_limit_8 = 120

# Cronometro noveno nivel
start_time_9 = 0 #0s
start_timer_text_9 = timer_font.render(str(start_time_9), True, color_black)
start_timer_event_9 = pygame.USEREVENT+1 # Evento de Usuario + 1 (USEREVENT 25 - ID) 
start_timer_active_9 = False # Variable para controlar si el temporizador está o no activo
used_time_9 = 0
unused_time_9 = 0
time_limit_9 = 240

# Cronometro decimo nivel
start_time_10 = 0 #0s
start_timer_text_10 = timer_font.render(str(start_time_10), True, color_black)
start_timer_event_10 = pygame.USEREVENT+1 # Evento de Usuario + 1 (USEREVENT 25 - ID) 
start_timer_active_10 = False # Variable para controlar si el temporizador está o no activo
used_time_10 = 0
unused_time_10 = 0
time_limit_10 = 240

# Movimiento del cursor
pointer = pygame.image.load("F_LEVEL/pointer.png")
velocidad = 15 # pixeles que se moveran en cada dirección
movimiento_x = 0 
movimiento_y = 0
posX, posY = 0, 0
pygame.mouse.set_visible(False)#Ocultar el cursor 
#Variable de los audios
audio_in = 1
audio_inst = 1
audioinst_tut1 = 1
audio_level = 1
audio_cont = 1
audio_sel = 1
audio_persona = 1
audio_fin = 1
audio_tar1 = 1
audio_qp = 1
audio_qp2 = 1
audio_ind = 1
audio_tablero = 1
audio_resultados = 1

# Variable audios tarjetas
s_primero = 1
s_segundo = 1
s_wrong2_1 = 1
s_wrong2_2 = 1
s_tercero = 1
s_wrong3_1 = 1
s_wrong3_2 = 1
s_wrong3_3 = 1
s_cuarto = 1
s_wrong4_1 = 1
s_wrong4_2 = 1
s_wrong4_3 = 1
s_wrong4_4 = 1
s_quinto = 1
s_wrong5_1 = 1
s_wrong5_2 = 1
s_wrong5_3 = 1
s_sexto = 1
s_wrong6_1 = 1
s_wrong6_2 = 1
s_wrong6_3 = 1
s_wrong6_4 = 1
s_wrong6_5 = 1
s_septimo = 1
s_wrong7_1 = 1
s_wrong7_2 = 1
s_wrong7_3 = 1
s_wrong7_4 = 1
s_octavo = 1
s_wrong8_1 = 1
s_wrong8_2 = 1
s_wrong8_3 = 1
s_wrong8_4 = 1
s_wrong8_5 = 1
s_wrong8_6 = 1
s_noveno = 1
s_wrong9_1 = 1
s_wrong9_2 = 1
s_wrong9_3 = 1
s_wrong9_4 = 1
s_wrong9_5 = 1
s_decimo = 1
s_wrong10_1 = 1
s_wrong10_2 = 1
s_wrong10_3 = 1
s_wrong10_4 = 1
s_wrong10_5 = 1
s_wrong10_6 = 1

class Cuadro:
    def __init__(self, fuente_imagen):
        self.mostrar = False
        self.descubierto = False
        """
        Una cosa es la fuente de la imagen (es decir, el nombre del archivo) y otra
        la imagen lista para ser pintada por PyGame
        La fuente la necesitamos para más tarde, comparar las tarjetas
        """
        cantidad_columnas_fst = 5
        tam_imgs_fst_cls = screen_width//cantidad_columnas_fst
        self.fuente_imagen = fuente_imagen # Fuente: nombre de la img. para hacer la comparación
        self.imagen_real = pygame.transform.scale(pygame.image.load(fuente_imagen), (tam_imgs_fst_cls, tam_imgs_fst_cls))

cuadros = [
    [Cuadro("F_LEVEL/crema.png"), Cuadro("F_LEVEL/agua.png"), Cuadro("F_LEVEL/crema.png"), Cuadro("F_LEVEL/enjuague.png"),Cuadro("F_LEVEL/cepillo.png")],
    [Cuadro("F_LEVEL/hilo.png"), Cuadro("F_LEVEL/agua.png"), Cuadro("F_LEVEL/hilo.png"), Cuadro("F_LEVEL/cepillo.png"),Cuadro("F_LEVEL/enjuague.png")],  
]

class Cuadro2:
    def __init__(self2, fuente_imagen2):
        self2.mostrar2 = False
        self2.descubierto2 = False
        """
        Una cosa es la fuente de la imagen (es decir, el nombre del archivo) y otra
        la imagen lista para ser pintada por PyGame
        La fuente la necesitamos para más tarde, comparar las tarjetas
        """
        tam_imgs_scnd = screen_width//3
        self2.fuente_imagen2 = fuente_imagen2 # Fuente: nombre de la img. para hacer la comparación
        self2.imagen_real2 = pygame.transform.scale(pygame.image.load(fuente_imagen2), (tam_imgs_scnd, tam_imgs_scnd))
cuadros2 =[[Cuadro2("IMG_2L/segundo.png"), Cuadro2("IMG_2L/wrong2_1.png"), Cuadro2("IMG_2L/wrong2_2.png")]]

class Cuadro3:
    def __init__(self3, fuente_imagen3):
        self3.mostrar3 = False
        self3.descubierto3 = False
        """
        Una cosa es la fuente de la imagen (es decir, el nombre del archivo) y otra
        la imagen lista para ser pintada por PyGame
        La fuente la necesitamos para más tarde, comparar las tarjetas
        """
        tam_imgs_thrd = screen_height//2
        self3.fuente_imagen3 = fuente_imagen3 # Fuente: nombre de la img. para hacer la comparación
        self3.imagen_real3 = pygame.transform.scale(pygame.image.load(fuente_imagen3), (tam_imgs_thrd, tam_imgs_thrd))
cuadros3 =[[Cuadro3("IMG_3L/tercero.png"), Cuadro3("IMG_3L/wrong3_1.png")], 
           [Cuadro3("IMG_3L/wrong3_2.png"), Cuadro3("IMG_3L/wrong3_3.png")]]
class Cuadro4:
    def __init__(self4, fuente_imagen4):
        self4.mostrar4 = False
        self4.descubierto4 = False
        """
        Una cosa es la fuente de la imagen (es decir, el nombre del archivo) y otra
        la imagen lista para ser pintada por PyGame
        La fuente la necesitamos para más tarde, comparar las
             tarjetas
        """
        tam_imgs_frth = screen_width//3.5
        self4.fuente_imagen4 = fuente_imagen4 # Fuente: nombre de la img. para hacer la comparación
        self4.imagen_real4 = pygame.transform.scale(pygame.image.load(fuente_imagen4), (tam_imgs_frth, tam_imgs_frth))
cuadros4 =[[Cuadro4("IMG_4L/cuarto.png"), Cuadro4("IMG_4L/wrong4_1.png"), Cuadro4("IMG_4L/wrong4_2.png")], 
           [Cuadro4("IMG_4L/wrong4_3.png"),Cuadro4("IMG_4L/cuarto.png"), Cuadro4("IMG_4L/wrong4_4.png")]]

class Cuadro5:
    def __init__(self5, fuente_imagen5):
        self5.mostrar5 = False
        self5.descubierto5 = False
        """
        Una cosa es la fuente de la imagen (es decir, el nombre del archivo) y otra
        la imagen lista para ser pintada por PyGame
        La fuente la necesitamos para más tarde, comparar las tarjetas
        """
        tam_imgs_ffth = screen_width//3.5
        self5.fuente_imagen5 = fuente_imagen5 # Fuente: nombre de la img. para hacer la comparación
        self5.imagen_real5 = pygame.transform.scale(pygame.image.load(fuente_imagen5), (tam_imgs_ffth, tam_imgs_ffth))
cuadros5 =[[Cuadro5("IMG_5L/quinto.png"), Cuadro5("IMG_5L/wrong5_1.png"), Cuadro5("IMG_5L/quinto.png")],
           [Cuadro5("IMG_5L/wrong5_2.png"), Cuadro5("IMG_5L/wrong5_3.png"), Cuadro5("IMG_5L/quinto.png")]]

class Cuadro6:
    def __init__(self6, fuente_imagen6):
        self6.mostrar6 = False
        self6.descubierto6 = False
        """
        Una cosa es la fuente de la imagen (es decir, el nombre del archivo) y otra
        la imagen lista para ser pintada por PyGame
        La fuente la necesitamos para más tarde, comparar las tarjetas
        """
        tam_imgs_sxth = screen_width//4
        self6.fuente_imagen6 = fuente_imagen6 # Fuente: nombre de la img. para hacer la comparación
        self6.imagen_real6 = pygame.transform.scale(pygame.image.load(fuente_imagen6), (tam_imgs_sxth, tam_imgs_sxth))
cuadros6 =[[Cuadro6("IMG_6L/sexto.png"), Cuadro6("IMG_6L/wrong6_1.png"), Cuadro6("IMG_6L/wrong6_2.png"),Cuadro6("IMG_6L/wrong6_3.png")],
           [Cuadro6("IMG_6L/wrong6_4.png"), Cuadro6("IMG_6L/sexto.png"), Cuadro6("IMG_6L/wrong6_5.png"), Cuadro6("IMG_6L/sexto.png")]]

class Cuadro7:
    def __init__(self7, fuente_imagen7):
        self7.mostrar7 = False
        self7.descubierto7 = False
        """
        Una cosa es la fuente de la imagen (es decir, el nombre del archivo) y otra
        la imagen lista para ser pintada por PyGame
        La fuente la necesitamos para más tarde, comparar las tarjetas
        """
        tam_imgs_svn = screen_width//4
        self7.fuente_imagen7 = fuente_imagen7 # Fuente: nombre de la img. para hacer la comparación
        self7.imagen_real7 = pygame.transform.scale(pygame.image.load(fuente_imagen7), (tam_imgs_svn, tam_imgs_svn))
cuadros7 =[[Cuadro7("IMG_7L/septimo.png"), Cuadro7("IMG_7L/septimo.png"), Cuadro7("IMG_7L/wrong7_1.png"),Cuadro7("IMG_7L/wrong7_2.png")],
           [Cuadro7("IMG_7L/wrong7_3.png"), Cuadro7("IMG_7L/septimo.png"), Cuadro7("IMG_7L/septimo.png"), Cuadro7("IMG_7L/wrong7_4.png")]]

class Cuadro8:
    def __init__(self8, fuente_imagen8):
        self8.mostrar8 = False
        self8.descubierto8 = False
        """
        Una cosa es la fuente de la imagen (es decir, el nombre del archivo) y otra
        la imagen lista para ser pintada por PyGame
        La fuente la necesitamos para más tarde, comparar las tarjetas
        """
        tam_imgs_eighth = screen_width//5
        self8.fuente_imagen8 = fuente_imagen8 # Fuente: nombre de la img. para hacer la comparación
        self8.imagen_real8 = pygame.transform.scale(pygame.image.load(fuente_imagen8), (tam_imgs_eighth, tam_imgs_eighth))
cuadros8 =[[Cuadro8("IMG_8L/wrong8_1.png"), Cuadro8("IMG_8L/wrong8_2.png"), Cuadro8("IMG_8L/octavo.png"),Cuadro8("IMG_8L/wrong8_3.png"),Cuadro8("IMG_8L/octavo.png")],
           [Cuadro8("IMG_8L/wrong8_4.png"), Cuadro8("IMG_8L/octavo.png"), Cuadro8("IMG_8L/wrong8_5.png"), Cuadro8("IMG_8L/wrong8_6.png"),Cuadro8("IMG_8L/octavo.png")]]

class Cuadro9:
    def __init__(self9, fuente_imagen9):
        self9.mostrar9 = False
        self9.descubierto9 = False
        """
        Una cosa es la fuente de la imagen (es decir, el nombre del archivo) y otra
        la imagen lista para ser pintada por PyGame
        La fuente la necesitamos para más tarde, comparar las tarjetas
        """
        tam_imgs_nine = screen_width//5
        self9.fuente_imagen9 = fuente_imagen9 # Fuente: nombre de la img. para hacer la comparación
        self9.imagen_real9 = pygame.transform.scale(pygame.image.load(fuente_imagen9), (tam_imgs_nine, tam_imgs_nine))
cuadros9 =[[Cuadro9("IMG_9L/noveno.png"), Cuadro9("IMG_9L/wrong9_1.png"), Cuadro9("IMG_9L/wrong9_2.png"),Cuadro9("IMG_9L/noveno.png"),Cuadro9("IMG_9L/wrong9_3.png")],
           [Cuadro9("IMG_9L/noveno.png"), Cuadro9("IMG_9L/wrong9_4.png"), Cuadro9("IMG_9L/noveno.png"), Cuadro9("IMG_9L/wrong9_5.png"),Cuadro9("IMG_9L/noveno.png")]]

class Cuadro10:
    def __init__(self10, fuente_imagen10):
        self10.mostrar10 = False
        self10.descubierto10 = False
        """
        Una cosa es la fuente de la imagen (es decir, el nombre del archivo) y otra
        la imagen lista para ser pintada por PyGame
        La fuente la necesitamos para más tarde, comparar las tarjetas
        """
        tam_imgs_tnth = screen_width//5.464
        self10.fuente_imagen10 = fuente_imagen10 # Fuente: nombre de la img. para hacer la comparación
        self10.imagen_real10 = pygame.transform.scale(pygame.image.load(fuente_imagen10), (tam_imgs_tnth, tam_imgs_tnth))
cuadros10 =[[Cuadro10("IMG_10L/wrong1_1.png"), Cuadro10("IMG_10L/wrong1_2.png"), Cuadro10("IMG_10L/decimo.png"), Cuadro10("IMG_10L/decimo.png")],
           [Cuadro10("IMG_10L/decimo.png"), Cuadro10("IMG_10L/wrong1_3.png"), Cuadro10("IMG_10L/decimo.png"), Cuadro10("IMG_10L/wrong1_4.png")],
           [Cuadro10("IMG_10L/wrong1_5.png"), Cuadro10("IMG_10L/decimo.png"), Cuadro10("IMG_10L/wrong1_6.png"), Cuadro10("IMG_10L/decimo.png")]]


# Imagen cuando la figura está oculta
cantidad_columnas = len(cuadros[0])
tam_imgs_fst = screen_width//cantidad_columnas
segundos_mostrar_pieza = 2  # Segundos para ocultar la pieza si no es la correcta
segundos_mostrar_pieza2 = 2  # Segundos para ocultar la pieza si no es la correcta
segundos_mostrar_pieza3 = 2  # Segundos para ocultar la pieza si no es la correcta
segundos_mostrar_pieza4 = 2  # Segundos para ocultar la pieza si no es la correcta
segundos_mostrar_pieza5 = 2  # Segundos para ocultar la pieza si no es la correcta
segundos_mostrar_pieza6 = 2  # Segundos para ocultar la pieza si no es la correcta
segundos_mostrar_pieza7 = 2  # Segundos para ocultar la pieza si no es la correcta
segundos_mostrar_pieza8 = 2  # Segundos para ocultar la pieza si no es la correcta
segundos_mostrar_pieza9 = 2  # Segundos para ocultar la pieza si no es la correcta
segundos_mostrar_pieza10 = 2  # Segundos para ocultar la pieza si no es la correcta
# Imágenes primer nivel
imagen_oculta = pygame.transform.scale(pygame.image.load("F_LEVEL/oculta.png"), (tam_imgs_fst, tam_imgs_fst))
agua = pygame.transform.scale(pygame.image.load("F_LEVEL/agua.png").convert_alpha(), (tam_imgs_fst, tam_imgs_fst))
cepillo = pygame.transform.scale(pygame.image.load("F_LEVEL/cepillo.png").convert_alpha(), (tam_imgs_fst, tam_imgs_fst)) 
crema = pygame.transform.scale(pygame.image.load("F_LEVEL/crema.png").convert_alpha(), (tam_imgs_fst, tam_imgs_fst)) 
hilo = pygame.transform.scale(pygame.image.load("F_LEVEL/hilo.png").convert_alpha(), (tam_imgs_fst, tam_imgs_fst))
enjuague = pygame.transform.scale(pygame.image.load("F_LEVEL/enjuague.png").convert_alpha(), (tam_imgs_fst, tam_imgs_fst))
#Imágenes segundo nivel
tam2 = screen_width//3
imagen_oculta2 = pygame.transform.scale(pygame.image.load("F_LEVEL/oculta2.png"), (tam2, tam2))
correct2 = pygame.transform.scale(pygame.image.load("IMG_2L/segundo.png").convert_alpha(),(tam2,tam2))
wrong2_1 = pygame.transform.scale(pygame.image.load("IMG_2L/wrong2_1.png").convert_alpha(),(tam2,tam2))
wrong2_2 = pygame.transform.scale(pygame.image.load("IMG_2L/wrong2_2.png").convert_alpha(),(tam2,tam2))
#Imágenes tercer nivel
tam3 =screen_height//2
imagen_oculta3 = pygame.transform.scale(pygame.image.load("F_LEVEL/oculta3.png"), (tam3, tam3))
correct3 = pygame.transform.scale(pygame.image.load("IMG_3L/tercero.png").convert_alpha(),(tam3,tam3))
wrong3_1 = pygame.transform.scale(pygame.image.load("IMG_3L/wrong3_1.png").convert_alpha(),(tam3,tam3))
wrong3_2 = pygame.transform.scale(pygame.image.load("IMG_3L/wrong3_2.png").convert_alpha(),(tam3,tam3))
wrong3_3 = pygame.transform.scale(pygame.image.load("IMG_3L/wrong3_3.png").convert_alpha(),(tam3,tam3))
#Imágenes cuarto nivel
tam4 = screen_width//3.5
imagen_oculta4 = pygame.transform.scale(pygame.image.load("F_LEVEL/oculta4.png"), (tam4, tam4))
correct4 = pygame.transform.scale(pygame.image.load("IMG_4L/cuarto.png").convert_alpha(),(tam4,tam4))
wrong4_1 = pygame.transform.scale(pygame.image.load("IMG_4L/wrong4_1.png").convert_alpha(),(tam4,tam4))
wrong4_2 = pygame.transform.scale(pygame.image.load("IMG_4L/wrong4_2.png").convert_alpha(),(tam4,tam4))
wrong4_3 = pygame.transform.scale(pygame.image.load("IMG_4L/wrong4_3.png").convert_alpha(),(tam4,tam4))
wrong4_4 = pygame.transform.scale(pygame.image.load("IMG_4L/wrong4_4.png").convert_alpha(),(tam4,tam4))
#Imágenes quinto nivel
tam5 = screen_width//3.5
imagen_oculta5 = pygame.transform.scale(pygame.image.load("F_LEVEL/oculta5.png"), (tam5, tam5))
correct5 = pygame.transform.scale(pygame.image.load("IMG_5L/quinto.png").convert_alpha(),(tam5,tam5))
wrong5_1 = pygame.transform.scale(pygame.image.load("IMG_5L/wrong5_1.png").convert_alpha(),(tam5,tam5))
wrong5_2 = pygame.transform.scale(pygame.image.load("IMG_5L/wrong5_2.png").convert_alpha(),(tam5,tam5))
wrong5_3 = pygame.transform.scale(pygame.image.load("IMG_5L/wrong5_3.png").convert_alpha(),(tam5,tam5))

#Imágenes sexto nivel
tam6 = screen_width//4
imagen_oculta6 = pygame.transform.scale(pygame.image.load("F_LEVEL/oculta6.png"), (tam6, tam6))
correct6 = pygame.transform.scale(pygame.image.load("IMG_6L/sexto.png").convert_alpha(),(tam6,tam6))
wrong6_1 = pygame.transform.scale(pygame.image.load("IMG_6L/wrong6_1.png").convert_alpha(),(tam6,tam6))
wrong6_2 = pygame.transform.scale(pygame.image.load("IMG_6L/wrong6_2.png").convert_alpha(),(tam6,tam6))
wrong6_3 = pygame.transform.scale(pygame.image.load("IMG_6L/wrong6_3.png").convert_alpha(),(tam6,tam6))
wrong6_4 = pygame.transform.scale(pygame.image.load("IMG_6L/wrong6_4.png").convert_alpha(),(tam6,tam6))
wrong6_5 = pygame.transform.scale(pygame.image.load("IMG_6L/wrong6_5.png").convert_alpha(),(tam6,tam6))
#Imágenes septimo nivel
tam7 = screen_width//4
imagen_oculta7 = pygame.transform.scale(pygame.image.load("F_LEVEL/oculta7.png"), (tam7, tam7))
correct7 = pygame.transform.scale(pygame.image.load("IMG_7L/septimo.png").convert_alpha(),(tam7,tam7))
wrong7_1 = pygame.transform.scale(pygame.image.load("IMG_7L/wrong7_1.png").convert_alpha(),(tam7,tam7))
wrong7_2 = pygame.transform.scale(pygame.image.load("IMG_7L/wrong7_2.png").convert_alpha(),(tam7,tam7))
wrong7_3 = pygame.transform.scale(pygame.image.load("IMG_7L/wrong7_3.png").convert_alpha(),(tam7,tam7))
wrong7_4 = pygame.transform.scale(pygame.image.load("IMG_7L/wrong7_4.png").convert_alpha(),(tam7,tam7))
#Imágenes octavo nivel
tam8 = screen_width//5
imagen_oculta8 = pygame.transform.scale(pygame.image.load("F_LEVEL/oculta8.png"), (tam8, tam8))
correct8 = pygame.transform.scale(pygame.image.load("IMG_8L/octavo.png").convert_alpha(),(tam8,tam8))
wrong8_1 = pygame.transform.scale(pygame.image.load("IMG_8L/wrong8_1.png").convert_alpha(),(tam8,tam8))
wrong8_2 = pygame.transform.scale(pygame.image.load("IMG_8L/wrong8_2.png").convert_alpha(),(tam8,tam8))
wrong8_3 = pygame.transform.scale(pygame.image.load("IMG_8L/wrong8_3.png").convert_alpha(),(tam8,tam8))
wrong8_4 = pygame.transform.scale(pygame.image.load("IMG_8L/wrong8_4.png").convert_alpha(),(tam8,tam8))
wrong8_5 = pygame.transform.scale(pygame.image.load("IMG_8L/wrong8_5.png").convert_alpha(),(tam8,tam8))
wrong8_6 = pygame.transform.scale(pygame.image.load("IMG_8L/wrong8_6.png").convert_alpha(),(tam8,tam8))
#Imágenes noveno nivel
tam9 = screen_width//5
imagen_oculta9 = pygame.transform.scale(pygame.image.load("F_LEVEL/oculta9.png"), (tam9, tam9))
correct9 = pygame.transform.scale(pygame.image.load("IMG_9L/noveno.png").convert_alpha(),(tam9,tam9))
wrong9_1 = pygame.transform.scale(pygame.image.load("IMG_9L/wrong9_1.png").convert_alpha(),(tam9,tam9))
wrong9_2 = pygame.transform.scale(pygame.image.load("IMG_9L/wrong9_2.png").convert_alpha(),(tam9,tam9))
wrong9_3 = pygame.transform.scale(pygame.image.load("IMG_9L/wrong9_3.png").convert_alpha(),(tam9,tam9))
wrong9_4 = pygame.transform.scale(pygame.image.load("IMG_9L/wrong9_4.png").convert_alpha(),(tam9,tam9))
wrong9_5 = pygame.transform.scale(pygame.image.load("IMG_9L/wrong9_5.png").convert_alpha(),(tam9,tam9))
#Imágenes decimo nivel
tam10 = screen_width//5.464
imagen_oculta10 = pygame.transform.scale(pygame.image.load("F_LEVEL/oculta10.png"), (tam10, tam10))
correct1 = pygame.transform.scale(pygame.image.load("IMG_10L/decimo.png").convert_alpha(),(tam10, tam10))
wrong1_1 = pygame.transform.scale(pygame.image.load("IMG_10L/wrong1_1.png").convert_alpha(),(tam10, tam10))
wrong1_2 = pygame.transform.scale(pygame.image.load("IMG_10L/wrong1_2.png").convert_alpha(),(tam10, tam10))
wrong1_3 = pygame.transform.scale(pygame.image.load("IMG_10L/wrong1_3.png").convert_alpha(),(tam10, tam10))
wrong1_4 = pygame.transform.scale(pygame.image.load("IMG_10L/wrong1_4.png").convert_alpha(),(tam10, tam10))
wrong1_5 = pygame.transform.scale(pygame.image.load("IMG_10L/wrong1_5.png").convert_alpha(),(tam10, tam10))
wrong1_6 = pygame.transform.scale(pygame.image.load("IMG_10L/wrong1_6.png").convert_alpha(),(tam10, tam10))
# Los sonidos a utilizar
sonido_fondo = pygame.mixer.Sound("F_LEVEL/fondo.wav")
sonido_clic = pygame.mixer.Sound("F_LEVEL/clic.mp3")
sonido_exito = pygame.mixer.Sound("F_LEVEL/ganador.mp3")
sonido_fracaso = pygame.mixer.Sound("F_LEVEL/equivocado.mp3")
sonido_voltear = pygame.mixer.Sound("F_LEVEL/voltear.mp3")
sonido_intro = pygame.mixer.Sound("F_LEVEL/intro.mp3")
sonido_instruc = pygame.mixer.Sound("F_LEVEL/instruc.mp3")
sonido_resultados = pygame.mixer.Sound("F_LEVEL/resultados.mp3")
sonido_resultados1 = pygame.mixer.Sound("F_LEVEL/resultados1.mp3")
tar_1 = pygame.mixer.Sound("F_LEVEL/tar_1.mp3")
#Tutoriales
cont_rut = pygame.mixer.Sound("Edicion/Audios/cont_rutina.mp3")
sonido_inst1 = pygame.mixer.Sound("Edicion/Audios/instruc.mp3")
q_protesis = pygame.mixer.Sound("Edicion/Audios/q_usa_protesis.mp3")
q_protesis2 = pygame.mixer.Sound("Edicion/Audios/q_protesis2.mp3")
protesis_1 = pygame.mixer.Sound("Edicion/Audios/1_protesis.mp3")
protesis_2 = pygame.mixer.Sound("Edicion/Audios/2_protesis_colocar.mp3")
sel_personaje = pygame.mixer.Sound("Edicion/Audios/sel_personaje.mp3")
ver_tablero = pygame.mixer.Sound("Edicion/Audios/tiempo_memorizar.mp3")
exp1 = pygame.mixer.Sound("Edicion/Audios/insumos.mp3")
exp2 = pygame.mixer.Sound("Edicion/Audios/1_enjuagar_agua.mp3")
exp3 = pygame.mixer.Sound("Edicion/Audios/2_sujetar_hilo.mp3")
exp4 = pygame.mixer.Sound("Edicion/Audios/3_hilo_c.mp3")
exp5 = pygame.mixer.Sound("Edicion/Audios/4_ubicar_cepillo.mp3")
exp6 = pygame.mixer.Sound("Edicion/Audios/5_circulos_cepillo.mp3")
exp7 = pygame.mixer.Sound("Edicion/Audios/6_enjuagar_crema.mp3")
exp8 = pygame.mixer.Sound("Edicion/Audios/7_buches_enjuague.mp3")
#Ganar y perder
completed = pygame.mixer.Sound("F_LEVEL/completed.mp3")
tiempo_agotado = pygame.mixer.Sound("F_LEVEL/perder_tiempo.mp3")
puntos_agotados = pygame.mixer.Sound("F_LEVEL/perder_puntos.mp3")
sonido_fin = pygame.mixer.Sound("F_LEVEL/audio_fin.mp3")
sonido_ind = pygame.mixer.Sound("Edicion/Audios/ind_niveles.mp3")
#Nombres
sam_name = pygame.mixer.Sound("Edicion/Audios/sam.mp3")
sami_name = pygame.mixer.Sound("Edicion/Audios/sami.mp3")
samuel_name = pygame.mixer.Sound("Edicion/Audios/samuel.mp3")
samantha_name = pygame.mixer.Sound("Edicion/Audios/samantha.mp3")





# Sonidos tarjetas en tableros
#segundo nivel
sn_wrong2_1 = pygame.mixer.Sound("AUDIO_CARDS/wrong2_1.mp3")
sn_wrong2_2 = pygame.mixer.Sound("AUDIO_CARDS/wrong2_2.mp3")
#Tercer nivel
sn_wrong3_1 = pygame.mixer.Sound("AUDIO_CARDS/wrong3_1.mp3")
sn_wrong3_2 = pygame.mixer.Sound("AUDIO_CARDS/wrong3_2.mp3")
sn_wrong3_3 = pygame.mixer.Sound("AUDIO_CARDS/wrong3_3.mp3")
#Cuarto nivel
sn_wrong4_1 = pygame.mixer.Sound("AUDIO_CARDS/wrong4_1.mp3")
sn_wrong4_2 = pygame.mixer.Sound("AUDIO_CARDS/wrong4_2.mp3")
sn_wrong4_3 = pygame.mixer.Sound("AUDIO_CARDS/wrong4_3.mp3")
sn_wrong4_4 = pygame.mixer.Sound("AUDIO_CARDS/wrong4_4.mp3")
#Quinto nivel
sn_wrong5_1 = pygame.mixer.Sound("AUDIO_CARDS/wrong5_1.mp3")
sn_wrong5_2 = pygame.mixer.Sound("AUDIO_CARDS/wrong5_2.mp3")
sn_wrong5_3 = pygame.mixer.Sound("AUDIO_CARDS/wrong5_3.mp3")
#Sexto nivel
sn_wrong6_1 = pygame.mixer.Sound("AUDIO_CARDS/wrong6_1.mp3")
sn_wrong6_2 = pygame.mixer.Sound("AUDIO_CARDS/wrong6_2.mp3")
sn_wrong6_3 = pygame.mixer.Sound("AUDIO_CARDS/wrong6_3.mp3")
sn_wrong6_4 = pygame.mixer.Sound("AUDIO_CARDS/wrong6_4.mp3")
sn_wrong6_5 = pygame.mixer.Sound("AUDIO_CARDS/wrong6_5.mp3")
#Septimo nivel
sn_wrong7_1 = pygame.mixer.Sound("AUDIO_CARDS/wrong7_1.mp3")
sn_wrong7_2 = pygame.mixer.Sound("AUDIO_CARDS/wrong7_2.mp3")
sn_wrong7_3 = pygame.mixer.Sound("AUDIO_CARDS/wrong7_3.mp3")
sn_wrong7_4 = pygame.mixer.Sound("AUDIO_CARDS/wrong7_4.mp3")
#Octavo nivel
sn_wrong8_1 = pygame.mixer.Sound("AUDIO_CARDS/wrong8_1.mp3")
sn_wrong8_2 = pygame.mixer.Sound("AUDIO_CARDS/wrong8_2.mp3")
sn_wrong8_3 = pygame.mixer.Sound("AUDIO_CARDS/wrong8_3.mp3")
sn_wrong8_4 = pygame.mixer.Sound("AUDIO_CARDS/wrong8_4.mp3")
sn_wrong8_5 = pygame.mixer.Sound("AUDIO_CARDS/wrong8_5.mp3")
sn_wrong8_6 = pygame.mixer.Sound("AUDIO_CARDS/wrong8_6.mp3")
#Noveno nivel
sn_wrong9_1 = pygame.mixer.Sound("AUDIO_CARDS/wrong9_1.mp3")
sn_wrong9_2 = pygame.mixer.Sound("AUDIO_CARDS/wrong9_2.mp3")
sn_wrong9_3 = pygame.mixer.Sound("AUDIO_CARDS/wrong9_3.mp3")
sn_wrong9_4 = pygame.mixer.Sound("AUDIO_CARDS/wrong9_4.mp3")
sn_wrong9_5 = pygame.mixer.Sound("AUDIO_CARDS/wrong9_5.mp3")
#Decimo nivel
sn_wrong10_1 = pygame.mixer.Sound("AUDIO_CARDS/wrong10_1.mp3")
sn_wrong10_2 = pygame.mixer.Sound("AUDIO_CARDS/wrong10_2.mp3")
sn_wrong10_3 = pygame.mixer.Sound("AUDIO_CARDS/wrong10_3.mp3")
sn_wrong10_4 = pygame.mixer.Sound("AUDIO_CARDS/wrong10_4.mp3")
sn_wrong10_5 = pygame.mixer.Sound("AUDIO_CARDS/wrong10_5.mp3")
sn_wrong10_6 = pygame.mixer.Sound("AUDIO_CARDS/wrong10_6.mp3")

# Banderas primer nivel
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

#Banderas segundo nivel
ultimos_segundos_2 = None
puede_jugar_2 = True 
juego_iniciado_2 = False
x1_2 = None
y1_2 = None
#Banderas tercer nivel
ultimos_segundos_3 = None
puede_jugar_3 = True 
juego_iniciado_3 = False
x1_3 = None
y1_3 = None
#Banderas cuarto nivel
ultimos_segundos_4 = None
puede_jugar_4 = True 
juego_iniciado_4 = False
x1_4 = None
y1_4 = None
#Banderas quinto nivel
ultimos_segundos_5 = None
puede_jugar_5 = True 
juego_iniciado_5 = False
x1_5 = None
y1_5 = None
#Banderas sexto nivel
ultimos_segundos_6 = None
puede_jugar_6 = True 
juego_iniciado_6 = False
x1_6 = None
y1_6 = None
#Banderas septimo nivel
ultimos_segundos_7 = None
puede_jugar_7 = True 
juego_iniciado_7 = False
x1_7 = None
y1_7 = None
#Banderas octavo nivel
ultimos_segundos_8 = None
puede_jugar_8 = True 
juego_iniciado_8 = False
x1_8 = None
y1_8 = None
#Banderas noveno nivel
ultimos_segundos_9 = None
puede_jugar_9 = True 
juego_iniciado_9 = False
x1_9 = None
y1_9 = None
#Banderas décimo nivel
ultimos_segundos_10 = None
puede_jugar_10 = True 
juego_iniciado_10 = False
x1_10 = None
y1_10 = None

#Imágenes para mostrar y explicar (lo que el paciente debe memorizar)
level_images = {
    1: "IMG_LEVEL/segundo.png",
    2: "IMG_LEVEL/tercero.png",
    3: "IMG_LEVEL/cuarto.png",
    4: "IMG_LEVEL/quinto.png",
    5: "IMG_LEVEL/sexto.png",
    6: "IMG_LEVEL/septimo.png",
    7: "IMG_LEVEL/octavo.png",
    8: "IMG_LEVEL/noveno.png",
    9: "IMG_LEVEL/decimo.png"
}
#Audios de las imágenes para mostrar y explicar (lo que el paciente debe memorizar)
#card_channel = None
stop_audio = 0
level_audios = {
    1: pygame.mixer.Sound("AUDIO_LEVEL/segundo.mp3"),
    2: pygame.mixer.Sound("AUDIO_LEVEL/tercero.mp3"),
    3: pygame.mixer.Sound("AUDIO_LEVEL/cuarto.mp3"),
    4: pygame.mixer.Sound("AUDIO_LEVEL/quinto.mp3"),
    5: pygame.mixer.Sound("AUDIO_LEVEL/sexto.mp3"),
    6: pygame.mixer.Sound("AUDIO_LEVEL/septimo.mp3"),
    7: pygame.mixer.Sound("AUDIO_LEVEL/octavo.mp3"),
    8: pygame.mixer.Sound("AUDIO_LEVEL/noveno.mp3"),
    9: pygame.mixer.Sound("AUDIO_LEVEL/decimo.mp3")
}

# Lista de matrices para los juegos
matrix_level = {
    1: [[correct2, wrong2_1, wrong2_2]],
    2: [[correct3, wrong3_1],
        [wrong3_2, wrong3_3]],
    3: [[correct4, wrong4_1, wrong4_2],
        [wrong4_3, correct4, wrong4_4]],
    4: [[correct5, wrong5_1, correct5],
        [wrong5_2, wrong5_3, correct5]],
    5: [[correct6, wrong6_1, wrong6_2, wrong6_3],
        [wrong6_4, correct6, wrong6_5, correct6]],
    6: [[correct7, correct7, wrong7_1, wrong7_2],
        [wrong7_3, correct7, correct7, wrong7_4]],
    7: [[wrong8_1, wrong8_2, correct8, wrong8_3, correct8],
        [wrong8_4, correct8, wrong8_5, wrong8_6, correct8]],
    8: [[correct9, wrong9_1, wrong9_2, correct9, wrong9_3],
        [correct9, wrong9_4, correct9, wrong9_5, correct9]],
    9: [[wrong1_1, wrong1_2, correct1, correct1],
        [correct1, wrong1_3, correct1, wrong1_4],
        [wrong1_5, correct1, wrong1_6, correct1]]
}


# IMAGENES FONDOS
fondo = pygame.transform.scale(pygame.image.load("FONDOS_LI/inicio.png").convert_alpha(), (screen_width, screen_height))
fondo_instruc = pygame.transform.scale(pygame.image.load("FONDOS_LI/instruc.png").convert_alpha(), (screen_width, screen_height))
fondo_pausa = pygame.transform.scale(pygame.image.load("FONDOS_LI/pausa.png").convert_alpha(), (screen_width, screen_height))
fondo_tarjetas = pygame.transform.scale(pygame.image.load("FONDOS_LI/fondo_tarjetas.png").convert_alpha(), (screen_width, screen_height))
fondo_resultados = pygame.transform.scale(pygame.image.load("FONDOS_LI/resultados.png").convert_alpha(), (screen_width, screen_height))
fondo_resultados1 = pygame.transform.scale(pygame.image.load("FONDOS_LI/resultados_fst_p.png").convert_alpha(), (screen_width, screen_height))
fondo1 = pygame.transform.scale(pygame.image.load("F_LEVEL/fondo1.png").convert_alpha(), (screen_width, screen_height))
fondo_cont_rut = pygame.transform.scale(pygame.image.load("FONDOS_LI/cont_rutina.png").convert_alpha(), (screen_width, screen_height))
fondo_sel_per = pygame.transform.scale(pygame.image.load("FONDOS_LI/sel_personaje.png").convert_alpha(), (screen_width, screen_height))
fondo_fin = pygame.transform.scale(pygame.image.load("FONDOS_LI/fin.png").convert_alpha(), (screen_width, screen_height))
fondo_tar1 = pygame.transform.scale(pygame.image.load("FONDOS_LI/tarjeta1.png").convert_alpha(), (screen_width, screen_height))
fondo_ind = pygame.transform.scale(pygame.image.load("FONDOS_LI/ind_niveles.png").convert_alpha(), (screen_width, screen_height))

#VIDEOS 
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
# FUNCIONES JUEGO / PANTALLAS / MENÚS
def reproducir_video_tut(ruta, vel):
    global screen_width, screen_height
    cap = cv2.VideoCapture(ruta)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (screen_width , screen_height ))
            cv2.namedWindow('Frame',cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty('Frame',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            cv2.imshow('Frame', frame)
            if cv2.waitKey(vel) & 0xFF == ord('a'):
        
                    break
        else: 
            break
    cap.release()
    cv2.destroyAllWindows()
    pygame.display.update()


def reproducir_video(ruta, vel):
    global screen_width, screen_height
    cap = cv2.VideoCapture(ruta)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (screen_width , screen_height ))
            cv2.namedWindow('Frame',cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty('Frame',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            cv2.imshow('Frame', frame)
            if cv2.waitKey(vel) & 0xFF == ord('q'):
        
                    break
        else: 
            break
    cap.release()
    cv2.destroyAllWindows()
    pygame.display.update()


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
    global audio_in

    pygame.display.set_caption('Introducción Memoria') # Caption - Nombre de la ventana
    screen.blit(fondo, (0,0)) # Función que dibuja el fondo
    paused_game = False

    channel = pygame.mixer.Channel(0)
    audio_intro = pygame.mixer.Sound(sonido_intro)
    if audio_in == 1:
        channel.queue(audio_intro)
        audio_in = 0

    if next_window == True: # Tecla n oprimida
        print('instruc')
        game_state = 'instruc'
        next_window = False
        channel.stop()
        audio_in = 1

    if back_window == True: # Tecla b oprimida
        print('Salir')
        open_game = False
        back_window = False
        channel.stop()
        audio_in = 1
    isGame = False # False porque no se encuentra dentro de un juego

    return game_state, paused_game, isGame, open_game, next_window, back_window

def instruc():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window
    global audio_inst, audioinst_tut1

    pygame.display.set_caption('Instrucciones Memoria') # Caption - Nombre de la ventana
    screen.blit(fondo_instruc, (0,0)) # Función que dibuja el fondo
    paused_game = False
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(sonido_instruc)
    if audio_inst == 1:
        channel.queue(audio_instruc)
        audio_inst = 0


    if next_window == True: # Tecla n oprimida
        game_state = 'f_step'
        next_window = False
        channel.stop()
        audio_inst = 1

    if back_window == True: # Tecla b oprimida
        game_state = 'intro'  
        back_window = False  
        channel.stop()
        audio_inst = 1
    
    isGame = False # False porque no se encuentra dentro de un juego    
    
    return game_state, paused_game, isGame, open_game, next_window, back_window

def f_step():
    global game_state
    global isGame
    global audioinst_tut1, next_window
    isGame = False
    pygame.display.set_caption('Tutorial') # Caption - Nombre de la ventana
    instruc = 'VIDEOS/tutorial1.mp4'
    vel = 20
    channel= pygame.mixer.Channel(1)
    audio_tut1 = pygame.mixer.Sound(sonido_inst1)
    channel.queue(audio_tut1)
    reproducir_video_tut(instruc, vel)
    pygame.mixer.Channel.stop(channel)
    game_state = 'personaje'
    return game_state, next_window

def q_nivel_prueba():
    global game_state, screen_height, screen_width
    global isGame
    global paused_game
    global yes_no_question, yes, no, back_window, next_window
    global ganar_reinicio2
    global q_protesis, audio_qp
    isGame = False
    next_window = False
    yes_no_question = True
    paused_game = False
    pygame.display.update()
    nivel_prueba = pygame.transform.scale(pygame.image.load("FONDOS_LI/usa_protesis.png").convert_alpha(), (screen_width, screen_height))
    screen.blit(nivel_prueba, (0,0)) # Función que dibuja el fondo
    
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(q_protesis)
    if audio_qp == 1:
        channel.queue(audio_instruc)
        audio_qp = 0

    if yes == True: # Tecla n oprimida
        game_state = 'video_protesis1'
        yes = False
        yes_no_question = False
        channel.stop()
        audio_qp =1 

    if no == True: # Tecla b oprimida
        game_state = 'video_enjuague_agua'  
        no = False  
        yes_no_question = False
        channel.stop()
        audio_qp = 1
    
    if back_window == True:
        game_state = 'intro'
        back_window = False
        yes_no_question = False
        channel.stop()
        audio_qp = 1

    return yes, no, yes_no_question, isGame, paused_game, back_window

def video_protesis1():
    global game_state
    global isGame
    global audioinst_tut1, next_window
    isGame = False
    pygame.display.set_caption('Tutorial') # Caption - Nombre de la ventana
    instruc = 'VIDEOS/exp3.mp4'
    vel = 20
    channel= pygame.mixer.Channel(1)
    audio_tut1 = pygame.mixer.Sound(protesis_1)
    channel.queue(audio_tut1)
    reproducir_video(instruc, vel)
    pygame.mixer.Channel.stop(channel)
    game_state = 'cont_rutina'
    return game_state, next_window

def video_instrumentos():
    global game_state
    global isGame
    global audioinst_tut1, next_window
    isGame = False
    pygame.display.set_caption('Tutorial') # Caption - Nombre de la ventana
    instruc = 'VIDEOS/exp_1.mp4'
    vel = 20
    channel= pygame.mixer.Channel(1)
    audio_tut1 = pygame.mixer.Sound(exp1)
    channel.queue(audio_tut1)
    reproducir_video(instruc, vel)
    pygame.mixer.Channel.stop(channel)
    game_state = 'q_nivel_prueba'
    return game_state, next_window

def cont_rutina():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window
    global audio_cont, cont_rut
    pygame.display.update()
    screen.blit(fondo_cont_rut, (0,0)) # Función que dibuja el fondo
    paused_game = False
    channel= pygame.mixer.Channel(1)
    back_window = False

    audio_cont_rut = pygame.mixer.Sound(cont_rut)
    if audio_cont == 1:
        channel.queue(audio_cont_rut)
        audio_cont = 0

    if next_window == True: # Tecla n oprimida
        game_state = 'video_enjuague_agua'
        next_window = False
        channel.stop()
        audio_cont = 1
    
    isGame = False # False porque no se encuentra dentro de un juego    
    
    return game_state, paused_game, isGame, open_game, next_window, back_window

def personaje():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window
    global audio_sel, sel_personaje, s1, s2, s3, s4, samuel, sam, samantha, sami, audio_persona

    screen.blit(fondo_sel_per, (0,0)) # Función que dibuja el fondo
    paused_game = False
    back_window = False
    channel= pygame.mixer.Channel(1)
    sel_persona = pygame.mixer.Sound(sel_personaje)
    
    if audio_sel == 1:
        channel.queue(sel_persona)
        audio_sel = 0

    if s1 == True:
        sam = 1
        samuel = 0
        samantha = 0
        sami = 0
        s1 = False
        s2 = False
        s3 = False
        s4 = False
        name = sam_name
        if audio_persona == 1:
            channel.queue(name)
            audio_persona = 0

    if s2 == True:
        samuel = 1
        sam = 0
        samantha = 0
        sami = 0
        s1 = False
        s2 = False
        s3 = False
        s4 = False
        name = samuel_name
        if audio_persona == 1:
            channel.queue(name)
            audio_persona = 0
    if s3 == True:
        samantha = 1
        sam = 0
        samuel = 0
        sami = 0
        s1 = False
        s2 = False
        s3 = False
        s4 = False
        name = samantha_name
        if audio_persona == 1:
            channel.queue(name)
            audio_persona = 0
    if s4 == True:
        sami = 1
        sam = 0
        samuel = 0
        samantha = 0
        s1 = False
        s2 = False
        s3 = False
        s4 = False
        name = sami_name
        if audio_persona == 1:
            channel.queue(name)
            audio_persona = 0

    if next_window == True and (sam == 1 or samuel ==1 or sami == 1 or samantha == 1): # Tecla n oprimida
        game_state = 'video_instrumentos'
        next_window = False
        channel.stop()
        audio_sel = 1
        audio_persona = 1
    
    isGame = False # False porque no se encuentra dentro de un juego    
    
    return game_state, paused_game, isGame, open_game, next_window, back_window, s1, s2, s3, s4, samuel, sam, samantha, sami
  
def video_enjuague_agua():
    global game_state
    global isGame
    global next_window
    global sam, samantha, samuel, sami
    isGame = False
    pygame.display.set_caption('Tutorial') # Caption - Nombre de la ventana
    if sam == 1:
        instruc = 'VIDEOS/sam_exp2.mp4'
    if samuel == 1:
        instruc = 'VIDEOS/samuel_exp2.mp4'
    if samantha == 1:
        instruc = 'VIDEOS/samantha_exp2.mp4'
    if sami == 1:
        instruc = 'VIDEOS/sami_exp2.mp4'
    vel = 20
    channel= pygame.mixer.Channel(1)
    audio_tut1 = pygame.mixer.Sound(exp2)
    channel.queue(audio_tut1)
    reproducir_video(instruc, vel)
    pygame.mixer.Channel.stop(channel)
    game_state = 'id_niveles'
    return game_state, next_window

def video_sostener_hilo():
    global game_state
    global isGame
    global next_window
    isGame = False
    pygame.display.set_caption('Tutorial') # Caption - Nombre de la ventana
    instruc = 'VIDEOS/exp5.mp4'
    vel = 30
    channel= pygame.mixer.Channel(1)
    audio_tut1 = pygame.mixer.Sound(exp3)
    channel.queue(audio_tut1)
    reproducir_video(instruc, vel)
    pygame.mixer.Channel.stop(channel)
    game_state = 'thirdcard'
    return game_state, next_window

def video_mover_hilo():
    global game_state
    global isGame
    global next_window
    isGame = False
    pygame.display.set_caption('Tutorial') # Caption - Nombre de la ventana
    instruc = 'VIDEOS/exp4.mp4'
    vel = 25
    channel= pygame.mixer.Channel(1)
    audio_tut1 = pygame.mixer.Sound(exp4)
    channel.queue(audio_tut1)
    reproducir_video(instruc, vel)
    pygame.mixer.Channel.stop(channel)
    game_state = 'fourthcard'
    return game_state, next_window

def video_ubicar_cepillo():
    global game_state
    global isGame
    global next_window
    isGame = False
    pygame.display.set_caption('Tutorial') # Caption - Nombre de la ventana
    instruc = 'VIDEOS/exp6_1.mp4'
    vel = 20
    channel= pygame.mixer.Channel(1)
    audio_tut1 = pygame.mixer.Sound(exp5)
    channel.queue(audio_tut1)
    reproducir_video(instruc, vel)
    pygame.mixer.Channel.stop(channel)
    game_state = 'seventhcard'
    return game_state, next_window

def video_cepillar_circulos():
    global game_state
    global isGame
    global next_window
    isGame = False
    pygame.display.set_caption('Tutorial') # Caption - Nombre de la ventana
    instruc = 'VIDEOS/exp6_2.mp4'
    vel = 20
    channel= pygame.mixer.Channel(1)
    audio_tut1 = pygame.mixer.Sound(exp6)
    channel.queue(audio_tut1)
    reproducir_video(instruc, vel)
    pygame.mixer.Channel.stop(channel)
    game_state = 'eighthcard'
    return game_state, next_window

def video_enjuague_crema():
    global game_state
    global isGame
    global next_window
    global sam, samantha, samuel, sami
    isGame = False
    pygame.display.set_caption('Tutorial') # Caption - Nombre de la ventana
    if sam == 1:
        instruc = 'VIDEOS/sam_exp7.mp4'
    if samuel == 1:
        instruc = 'VIDEOS/samuel_exp7.mp4'
    if samantha == 1:
        instruc = 'VIDEOS/samantha_exp7.mp4'
    if sami == 1:
        instruc = 'VIDEOS/sami_exp7.mp4'
    vel = 20
    channel= pygame.mixer.Channel(1)
    audio_tut1 = pygame.mixer.Sound(exp7)
    channel.queue(audio_tut1)
    reproducir_video(instruc, vel)
    pygame.mixer.Channel.stop(channel)
    game_state = 'tenthcard'
    return game_state, next_window

def video_enjuague_bucal():
    global game_state
    global isGame
    global next_window
    global sam, samantha, samuel, sami
    isGame = False
    pygame.display.set_caption('Tutorial') # Caption - Nombre de la ventana
    if sam == 1:
        instruc = 'VIDEOS/sam_exp8.mp4'
    if samuel == 1:
        instruc = 'VIDEOS/samuel_exp8.mp4'
    if samantha == 1:
        instruc = 'VIDEOS/samantha_exp8.mp4'
    if sami == 1:
        instruc = 'VIDEOS/sami_exp8.mp4'
    vel = 20
    channel= pygame.mixer.Channel(1)
    audio_tut1 = pygame.mixer.Sound(exp8)
    channel.queue(audio_tut1)
    reproducir_video(instruc, vel)
    pygame.mixer.Channel.stop(channel)
    game_state = 'exp_protesis2'
    return game_state, next_window

def exp_protesis2():
    global game_state, screen_height, screen_width
    global isGame
    global paused_game
    global yes_no_question, yes, no, back_window, next_window
    global ganar_reinicio2
    global q_protesis2, audio_qp2
    isGame = False
    next_window = False
    yes_no_question = True
    paused_game = False
    back_window = False
    pygame.display.update()
    nivel_prueba = pygame.transform.scale(pygame.image.load("FONDOS_LI/usa_protesis2.png").convert_alpha(), (screen_width, screen_height))
    screen.blit(nivel_prueba, (0,0)) # Función que dibuja el fondo
    
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(q_protesis2)
    if audio_qp2 == 1:
        channel.queue(audio_instruc)
        audio_qp2 = 0
    if yes == True: # Tecla n oprimida
        game_state = 'exp_prot2'
        yes = False
        yes_no_question = False
        channel.stop()
        audio_qp2 =1 

    if no == True: # Tecla b oprimida
        game_state = 'first_level_card'  
        no = False  
        yes_no_question = False
        channel.stop()
        audio_qp2 = 1

    return yes, no, yes_no_question, isGame, paused_game, back_window

def first_level_card():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window
    global audio_tar1, tar_1
    pygame.display.update()
    screen.blit(fondo_tar1, (0,0)) # Función que dibuja el fondo
    paused_game = False
    back_window = False

    channel= pygame.mixer.Channel(1)
    audio_tar = pygame.mixer.Sound(tar_1)
    if audio_tar1 == 1:
        channel.queue(audio_tar)
        audio_tar1 = 0

    if next_window == True: # Tecla n oprimida
        game_state = 'first_level'
        next_window = False
        channel.stop()
        audio_tar1 =1
    
    isGame = False # False porque no se encuentra dentro de un juego    
    
    return game_state, paused_game, isGame, open_game, next_window, back_window

def id_niveles():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window
    global sonido_ind, audio_ind
    pygame.display.update()
    screen.blit(fondo_ind, (0,0)) # Función que dibuja el fondo
    paused_game = False
    back_window = False

    channel= pygame.mixer.Channel(1)
    audio_tar = pygame.mixer.Sound(sonido_ind)
    if audio_ind == 1:
        channel.queue(audio_tar)
        audio_ind = 0

    if next_window == True: # Tecla n oprimida
        game_state = 'secondcard'
        next_window = False
        channel.stop()
        audio_ind =1
    
    isGame = False # False porque no se encuentra dentro de un juego    
    
    return game_state, paused_game, isGame, open_game, next_window, back_window

def exp_prot2():
    global game_state
    global isGame
    global next_window
    isGame = False
    pygame.display.set_caption('Tutorial') # Caption - Nombre de la ventana
    instruc = 'VIDEOS/exp9.mp4'
    vel = 20
    channel= pygame.mixer.Channel(1)
    audio_tut1 = pygame.mixer.Sound(protesis_2)
    channel.queue(audio_tut1)
    reproducir_video(instruc, vel)
    pygame.mixer.Channel.stop(channel)
    game_state = 'first_level_card'
    return game_state, next_window

def juego_fin():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window
    global audio_fin, sonido_fin
    next_window = False
    screen.blit(fondo_fin, (0,0)) # Función que dibuja el fondo
    paused_game = False
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(sonido_fin)
    if audio_fin == 1:
        channel.queue(audio_instruc)
        audio_fin = 0

    if back_window == True: # Tecla b oprimida
        open_game = False
        channel.stop()
        audio_fin = 1 
        back_window = False  
        
    isGame = False # False porque no se encuentra dentro de un juego    
    
    return game_state, paused_game, isGame, open_game, next_window, back_window


#-------------------- Primer Nivel ----------------------------------------

def ocultar_todos_los_cuadros():
    for fila in cuadros:
        for cuadro in fila:
            cuadro.mostrar = False
            cuadro.descubierto = False

# Determina si se gana, reinicia el juego y suena la pista correspondiente
def comprobar_si_gana():
    global acierto_1, used_time_1, unused_time_1
    global game_state
    global ganar1, juego_iniciado, time_limit_1
    if gana():
        used_time_1 =  start_time
        unused_time_1 =  time_limit_1 - start_time
        ganar1 = True
        juego_iniciado = False

    return acierto_1, game_state, ganar1, puede_jugar, juego_iniciado, LI

def gana():
    for fila in cuadros:
        for cuadro in fila:
            if not cuadro.descubierto:
                return False
    return True

# Reproduce el sonido de click para que empiece, modifica el juego iniciado
def iniciar_juego():
    global juego_iniciado
    #global automatico
    #pygame.mixer.Sound.play(sonido_clic)
    #automatico = pygame.MOUSEBUTTONDOWN

    ocultar_todos_los_cuadros()
    juego_iniciado = True



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
    global screen_height
    global timer_text, level_time, timer_active
    global puede_jugar, reinicio, ganar1
    global start_timer_active, aux_cronometro
    global x1, x2, y1, y2, ganar_rein1, acierto_1, error_1, unused_time_1, used_time_1, tar_1, audio_tablero
    pygame.display.set_caption('first_level') # Caption - Nombre de la ventana
    pygame.display.update()
    screen.fill(color_azul_claro) 
    #########################################################
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(ver_tablero)
    if audio_tablero == 1:
        channel.queue(audio_instruc)
        audio_tablero = 0
    #########################################################
    aux_cronometro = True
    isGame = False # Bandera que indica estado de juego activo, lo que implica que se puede pausar o no
    paused_game = False
    puede_jugar = True
    reinicio = False
    acierto_1 = 0
    error_1 = 0
    unused_time_1 = 0
    used_time_1 = 0
    #start_timer_active = False
    #Para que al estar en esta pantalla sea seguro que el juego se reinicia y queda en el estado inicial
    ocultar_todos_los_cuadros()
    ganar1 = False
    if not ganar_rein1 == 0:
        x1 = None
        x2 = None
        y1 = None
        y2 = None

    image_matrix = [ [crema, agua, crema, enjuague, cepillo],  [hilo, agua, hilo, cepillo, enjuague]]
    rows = len(image_matrix)
    cols = len(image_matrix[0])
    image_width = image_matrix[0][0].get_width()
    image_height = image_matrix[0][0].get_height()
    padding_x = (screen_width - (cols * image_width)) // (cols + 1)
    padding_y = (screen_height - (rows * image_height)) // (rows + 1)
    timer_rect = timer_text.get_rect(center = ((screen_width/2),(screen_height/2))) # Centro de la pantalla: center = screen.get_rect().center
    

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

    return (isGame, paused_game, game_state, next_window, back_window, timer_text, level_time,  puede_jugar, reinicio, ganar1, 
            aux_cronometro, timer_active, x1, y1, x2, y2, ganar_rein1, acierto_1, error_1, used_time_1, unused_time_1)


def Fst_level():
    global isGame
    global game_state
    global paused_game
    global segundos_mostrar_pieza
    global cuadros
    global imagen_oculta
    global puede_jugar
    global ultimos_segundos
    global x1, y1, x2, y2, posX, posY, ganar_rein1
    global reinicio, ret_intro, cont_game, next_window, back_window
    global timer_font, start_time, start_timer_text, start_timer_event, start_timer_active
    global prueba, acierto_1, error_1, ganar1, aux_cronometro

    #pygame.mouse.set_visible(True)# Hacer visible el cursor   

    pygame.display.set_caption('Fst_level') # Caption - Nombre de la ventana
    screen.fill(color_azul_claro) 
    isGame = True # Bandera que indica estado de juego activo, lo que implica que se puede pausar
    ret_intro = False
    cont_game = False
    reinicio = False
    next_window = False
    back_window = False

    medida_cuadro_h = screen_width/len(cuadros[0])  # Medida de la imagen en pixeles
    medida_cuadro_v = screen_height/len(cuadros) # Medida de la imagen en pixeles

    timer_rect = start_timer_text.get_rect(center = ((screen_width/2),(screen_height/2)))
    if not start_timer_active and game_state == 'Fst_level':
        start_time = 0
        pygame.time.set_timer(start_timer_event, 1000)
        start_timer_active = True

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
    screen.fill(color_azul_claro)
    # Banderas para saber en dónde dibujar las imágenes
    cuadros_rows = len(cuadros)
    cuadros_cols = len(cuadros[0])
    image_cuadros = cuadros[0][0].imagen_real
    image_cuadros_width = image_cuadros.get_width()
    image_cuadros_height = image_cuadros.get_height()
    x_offset = (screen_width - (cuadros_cols*image_cuadros_width))//(cuadros_cols + 1)
    y_offset = (screen_height - (cuadros_rows*image_cuadros_height))//(cuadros_rows + 1)

    y =  y_offset
    # Recorrer los cuadros
    for fila in cuadros:
        x = x_offset
        for cuadro in fila:
            """
            Si está descubierto o se debe mostrar, dibujamos la imagen real. Si no,
            dibujamos la imagen oculta
            """
            if cuadro.descubierto or cuadro.mostrar:
                screen.blit(cuadro.imagen_real, (x, y))
                screen.blit(start_timer_text, timer_rect)

            else:
                screen.blit(imagen_oculta, (x, y))
                screen.blit(start_timer_text, timer_rect)

            x += medida_cuadro_h
        y += medida_cuadro_v
    
    

    if prueba == True: 
        """
        xAbsoluto e yAbsoluto son las coordenadas de la pantalla en donde se hizo
        clic. PyGame no ofrece detección de clic en imagen, por ejemplo. Así que
        se deben hacer ciertos trucos
        """
        # Si el click fue sobre el botón y el juego no se ha iniciado, entonces iniciamos el juego
        xAbsoluto = posX
        yAbsoluto = posY
        #if boton.collidepoint(event.pos):
        #   if not juego_iniciado:
        #      iniciar_juego()

        #else:
            # Si no hay juego iniciado, ignoramos el clic
        
        if juego_iniciado:
            iniciar_juego()
            return
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
        x_rel = xAbsoluto - x_offset 
        y_rel = yAbsoluto - y_offset 
        
        x_cuadro = math.floor(x_rel / medida_cuadro_h)
        y_cuadro = math.floor(y_rel / medida_cuadro_v)
        
        # Primero lo primero. Si  ya está mostrada o descubierta, no hacemos nada
        if 0 <= x_cuadro < cuadros_cols and 0 <= y_cuadro < cuadros_rows:
            cuadro = cuadros[y_cuadro][x_cuadro]
            if cuadro.mostrar or cuadro.descubierto:
                # continue ignora lo de abajo y deja que el ciclo siga
                return
            # Si es la primera vez que tocan la imagen (es decir, no están buscando el par de otra, sino apenas
            # están descubriendo la primera)
            if x1 is None and y1 is None:
                # Entonces la actual es en la que acaban de dar clic, la mostramos
                x1 = x_cuadro
                y1 = y_cuadro
                cuadros[y1][x1].mostrar = True
                pygame.mixer.Sound.play(sonido_voltear)

            else:
                # En caso de que ya hubiera una clickeada anteriormente y estemos buscando el par, comparamos...
                x2 = x_cuadro
                y2 = y_cuadro
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
                game_state = 'recompensa_1'#imagen que diga que ganó  y siguiente nivel o cosa 
            prueba = False  

    if paused_game == True: # and juegos == True: # PANTALLA DE PAUSA
        game_state = 'Pausado'
        isGame = False
    return isGame, paused_game, game_state, back_window, reinicio, ret_intro, cont_game, prueba, acierto_1, error_1, ganar1, aux_cronometro

def recompensa_1():
    global game_state
    global isGame
    isGame = False
    pygame.display.set_caption('Ganador1') # Caption - Nombre de la ventana
    instruc = 'VIDEOS/ganar_10.mp4'
    vel = 20
    pygame.mixer.Sound.play(completed)
    reproducir_video(instruc, vel)
    game_state = 'completed_1'
    return game_state

def completed_1():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window
    global reinicio
    global puede_jugar
    global ganar1
    #global aux_cronometro
    global acierto_1, error_1, unused_time_1, used_time_1, ganar_rein1
    global audio_resultados
    
    pygame.display.set_caption('Completo nivel 1') # Caption - Nombre de la ventana
    screen.blit(fondo_resultados, (0,0)) # Función que dibuja el fondo
    correct_text = font.render(str(acierto_1), True, color_black)
    mistake_text = font.render(str(error_1), True, color_black)
    used_time_text = font.render( str(used_time_1), True, color_black)
    unused_time_text = font.render(str(unused_time_1), True, color_black)
    
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(sonido_resultados)
    if audio_resultados == 1:
        channel.queue(audio_instruc)
        audio_resultados = 0
    
    screen.blit(correct_text, ((screen_width//1.91), (screen_height//3.55)))
    screen.blit(mistake_text, ((screen_width//1.993), (screen_height//2.59)))
    screen.blit(used_time_text, ((screen_width//1.597), (screen_height//2.077)))
    screen.blit(unused_time_text, ((screen_width//1.597), (screen_height//1.717)))

    paused_game = False


    if reinicio == True:
        puede_jugar = True
        ocultar_todos_los_cuadros()
        game_state = 'first_level'
        reinicio = False
        ganar1 = False
        back_window = False
        next_window = False
        #aux_cronometro = True 
        acierto_1 = 0
        error_1 = 0
        unused_time_1 = 0
        used_time_1 = 0
        ganar_rein1 +=1
        channel.stop()
        audio_resultados = 1

    if next_window == True: # Tecla n oprimida
        game_state = 'juego_fin'
        next_window = False
        channel.stop()
        audio_resultados = 1

    if back_window == True: # Tecla b oprimida
        back_window = False  
        open_game = False
        ganar_rein1 +=1
        channel.stop()
        audio_resultados = 1

    isGame = False # False porque no se encuentra dentro de un juego    

    return game_state, paused_game, isGame, open_game, next_window, back_window, reinicio, puede_jugar, ganar1,  acierto_1, error_1, unused_time_1, used_time_1, ganar_rein1

def reflection_1():
    global game_state
    global isGame
    isGame = False
    pygame.display.set_caption('Ganador1') # Caption - Nombre de la ventana
    instruc = 'VIDEOS/perder_tiempo.mp4'
    vel =20
    pygame.mixer.Sound.play(tiempo_agotado)
    reproducir_video(instruc, vel)
    game_state = 'uncompleted_1'
    return game_state

def uncompleted_1():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window
    global reinicio
    global puede_jugar
    global ganar1, ganar_rein1
    global aux_cronometro
    global acierto_1, error_1, unused_time_1, used_time_1, start_time
    global audio_resultados
    
    pygame.display.set_caption('No completo nivel 1') # Caption - Nombre de la ventana
    screen.blit(fondo_resultados1, (0,0)) # Función que dibuja el fondo
    
    
    correct_text = font.render(str(acierto_1), True, color_black)
    mistake_text = font.render(str(error_1), True, color_black)
    used_time_text = font.render(str(used_time_1), True, color_black)
    unused_time_text = font.render(str(unused_time_1), True, color_black)
    
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(sonido_resultados1)
    if audio_resultados == 1:
        channel.queue(audio_instruc)
        audio_resultados = 0

    screen.blit(correct_text, ((screen_width//1.91), (screen_height//3.55)))
    screen.blit(mistake_text, ((screen_width//1.993), (screen_height//2.59)))
    screen.blit(used_time_text, ((screen_width//1.597), (screen_height//2.077)))
    screen.blit(unused_time_text, ((screen_width//1.597), (screen_height//1.717)))

    paused_game = False
    next_window = False
    back_window = False

    if reinicio == True:
        puede_jugar = True
        ocultar_todos_los_cuadros()
        game_state = 'first_level'
        reinicio = False
        ganar1 = False
        back_window = False
        next_window = False 
        aux_cronometro = True
        acierto_1 = 0
        error_1 = 0
        unused_time_1 = 0
        used_time_1 = 0
        ganar_rein1 = 0#######################################################
        channel.stop()
        audio_resultados = 1

    '''if next_window == True: # Tecla n oprimida
        game_state = 'secondcard'
        next_window = False'''

    '''if back_window == True: # Tecla b oprimida
        back_window = False 
        open_game = False
        ganar_rein1 = 0'''
    
    isGame = False # False porque no se encuentra dentro de un juego    

    return game_state, paused_game, isGame, open_game, next_window, back_window, reinicio, puede_jugar, ganar1, aux_cronometro, acierto_1, error_1, unused_time_1, used_time_1, ganar_rein1


############################## Carta objetivo ##############################################
def level_card(actual_state):
    global audio_level, stop_audio
    global screen_width, screen_height
    global level_audios, level_images
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window
    global reinicio
    global audio_tablero
    #Funcion para definir la tarjeta según el nivel
    pygame.display.update()
    back_window =  False
    ########
    audio_tablero = 1    

    image_path = level_images[actual_state]
    image = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(), (screen_height, screen_height))
    audio_path = level_audios[actual_state]
    card_channel = pygame.mixer.Channel(0) 
    audio = pygame.mixer.Sound(audio_path)
    image_w = image.get_width()/2
    image_h = image.get_height()/2
    if audio_level == 1:
        card_channel.queue(audio)
        audio_level = 0
    if stop_audio == 1 :
        card_channel.stop()
        audio_level = 1
        stop_audio = 0     

    screen.blit(fondo_tarjetas, (0,0))
    screen.blit(image,(((screen_width/2)-image_w), ((screen_height/2)-image_h)))

    if next_window == True: # Tecla n oprimida
        next_window = False
        card_channel.stop()
        stop_audio = 1
        if actual_state == 1:
            game_state = 'second_level'
        if actual_state == 2:
            game_state = 'third_level'
        if actual_state == 3:
            game_state = 'fourth_level'
        if actual_state == 4:
            game_state = 'fifth_level'
        if actual_state == 5:
            game_state = 'sixth_level'
        if actual_state == 6:
            game_state = 'seventh_level'
        if actual_state == 7:
            game_state = 'eighth_level'
        if actual_state == 8:
            game_state = 'ninth_level'
        if actual_state == 9:
            game_state = 'tenth_level'


    if reinicio == True: # Tecla b oprimida
        reinicio = False  
        card_channel.stop()
        stop_audio = 1
        if actual_state == 1:
            game_state = 'secondcard'
        if actual_state == 2:
            game_state = 'thirdcard'
        if actual_state == 3:
            game_state = 'fourthcard'
        if actual_state == 4:
            game_state = 'fifthcard'
        if actual_state == 5:
            game_state = 'sixthcard'
        if actual_state == 6:
            game_state = 'seventhcard'
        if actual_state == 7:
            game_state = 'eighthcard'
        if actual_state == 8:
            game_state = 'ninthcard'
        if actual_state == 9:
            game_state = 'tenthcard'
    
    isGame = False # False porque no se encuentra dentro de un juego    
    
    return game_state, paused_game, isGame, open_game, next_window, back_window, reinicio, actual_state, audio_tablero
    

###################################  Segundo Nivel #####################################
def ocultar_todos_los_cuadros_2():
    for fila in cuadros2:
        for cuadro in fila:
            cuadro.mostrar2 = False
            cuadro.descubierto2 = False

# Determina si se gana, reinicia el juego y suena la pista correspondiente
def comprobar_si_gana2():
    global acierto_2, used_time_2, unused_time_2
    global game_state
    global ganar2, juego_iniciado_2, time_limit_2, perder2
    global error_2, ganar_reinicio2

    if gana2():
        used_time_2 =  start_time_2
        unused_time_2 =  time_limit_2 - used_time_2
        ganar2 = True
        juego_iniciado_2 = False

    if error_2 == 3 or used_time_2 == time_limit_2:
        used_time_2 =  start_time_2
        unused_time_2 =  time_limit_2 - used_time_2
        perder2 = True
        juego_iniciado_2 = False
        ganar_reinicio2 = 0
    return acierto_2, game_state, ganar2, juego_iniciado_2, perder2, error_2, ganar_reinicio2
        
        
# Regresa False si al menos un cuadro NO está descubierto. True en caso de que absolutamente todos estén descubiertos
# Recorre todas las filas de la matriz y en caso de que alguno no esté descubierto retorna a falso, de lo contrario pasa a true
def gana2():
    if not acierto_2 == 1: 
        return False
    return True


# Reproduce el sonido de click para que empiece, modifica el juego iniciado 
def iniciar_juego2():
    global juego_iniciado_2
    #global automatico
    #pygame.mixer.Sound.play(sonido_clic)
    #automatico = pygame.MOUSEBUTTONDOWN
    ocultar_todos_los_cuadros_2()
    juego_iniciado_2 = True

# Función para dibujar los cepillos en la pantalla
def draw_points(cepillos):
    cepillo_image = pygame.transform.scale(pygame.image.load("puntos/punto3.png"), (100, 100))
    cepillo_width, cepillo_height = cepillo_image.get_size()
    x_offset = (screen_width*0.16032)  # Ajusta la posición x donde quieres que aparezcan los cepillos

    for i in range(cepillos):
        x = x_offset + i * (cepillo_width + 5)  # Espacio entre los cepillos
        y = (screen_height*0.02864)  # Ajusta la posición y donde quieres que aparezcan los cepillos
        screen.blit(cepillo_image, (x, y))

def second_level():  
    global isGame
    global game_state
    global paused_game
    global screen_width
    global screen_height
    global timer_text_2, level_time_2, timer_active_2, aux_cronometro2
    global puede_jugar_2, reinicio, ganar2, perder2
    global acierto_2, error_2, used_time_2, unused_time_2 
    global x1_2, y1_2
    global actual_matrix, ganar_reinicio2, cepillos2, audio_tablero
    pygame.display.set_caption('_') # Caption - Nombre de la ventana
    screen.fill(color_rosado)
    isGame = False # Bandera que indica estado de juego activo, lo que implica que se puede pausar o no
    paused_game = False
    puede_jugar_2 = True
    reinicio = False
    aux_cronometro2 = True
    acierto_2 = 0
    error_2 = 0
    unused_time_2 = 0
    used_time_2 = 0
    cepillos2 = 3
    ######################
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(ver_tablero)
    if audio_tablero == 1:
        channel.queue(audio_instruc)
        audio_tablero = 0
    ######################
    if not ganar_reinicio2 == 0:
            x1_2 = None
            y1_2 = None

    #start_timer_active = False
    #Para que al estar en esta pantalla sea seguro que el juego se reinicia y queda en el estado inicial
    ocultar_todos_los_cuadros_2()
    ganar2 = False
    perder2 = False
    actual_matrix = 1
    image_matrix = matrix_level[actual_matrix]
    rows = len(image_matrix)
    cols = len(image_matrix[0])
    image_width = image_matrix[0][0].get_width()
    image_height = image_matrix[0][0].get_height()
    padding_x = (screen_width - (cols * image_width)) // (cols + 1)
    #padding_y = (screen_height - (rows * image_height)) // (rows + 1)
    padding_y = ((screen_height * 0.1927)+ 40 )
    timer_rect_2 = timer_text_2.get_rect(topleft = ((screen_width*0.7738),(screen_height*0.05859))) # Centro de la pantalla: center = screen.get_rect().center
    

    for i in range(rows):
        for j in range(cols):
            x = padding_x + j * (image_width + padding_x)
            y = padding_y + i * (image_height + padding_y)
            screen.blit(image_matrix[i][j], (x, y))
            #center_text(first_level_text,100) # Texto
            screen.blit(timer_text_2, timer_rect_2) 
    
    if not timer_active_2 and game_state == 'second_level':
        level_time_2 = 15
        pygame.time.set_timer(timer_event_2, 1000) # set_timer crea una acción cada 1s
        timer_active_2 = True

    return isGame, paused_game, game_state, next_window, back_window, timer_text_2, level_time_2,  puede_jugar_2, reinicio, ganar2, perder2, timer_active_2, x1_2, y1_2, aux_cronometro2, acierto_2, error_2, used_time_2, unused_time_2, cepillos2



def Scnd_level():
    global isGame
    global game_state
    global paused_game
    global segundos_mostrar_pieza2
    global cuadros2
    global imagen_oculta2
    global puede_jugar_2
    global ultimos_segundos_2
    global x1_2, y1_2, posX, posY, carta2
    global reinicio, ret_intro, cont_game, next_window, back_window
    global timer_font_2, start_time_2, start_timer_text_2, start_timer_event_2, start_timer_active_2
    global prueba2, acierto_2, error_2, ganar2, aux_cronometro2, perder2
    global cepillos2
    global ganar_reinicio2
    global s_wrong2_1, sn_wrong2_1, s_wrong2_2, sn_wrong2_2

    #pygame.mouse.set_visible(True)# Hacer visible el cursor   

    pygame.display.set_caption('Scnd_level') # Caption - Nombre de la ventana
    isGame = True # Bandera que indica estado de juego activo, lo que implica que se puede pausar
    ret_intro = False
    cont_game = False
    reinicio = False
    next_window = False
    back_window = False

    medida_cuadro_h = screen_width/len(cuadros2[0])  # Medida de la imagen en pixeles
    medida_cuadro_v = screen_height/len(cuadros2) # Medida de la imagen en pixeles

    timer_rect = start_timer_text_2.get_rect(topleft = ((screen_width*0.7738),(screen_height*0.05859)))
    if not start_timer_active_2 and game_state == 'Scnd_level':
        start_time_2 = 0
        pygame.time.set_timer(start_timer_event_2, 1000)
        start_timer_active_2 = True

    ahora = int(time.time())
    # Y aquí usamos la bandera del tiempo, de nuevo. Si los segundos actuales menos los segundos
    # en los que se empezó el ocultamiento son mayores a los segundos en los que se muestra la pieza, entonces
    # se ocultan las dos tarjetas y se reinician las banderas
    if ultimos_segundos_2 is not None and ahora - ultimos_segundos_2 >= segundos_mostrar_pieza2:
        cuadros2[y1_2][x1_2].mostrar2 = False
        
        #cuadros2[y2_2][x2_2].mostrar2 = False
        x1_2 = None
        y1_2 = None
        #x2_2 = None
        #y2_2 = None
        ultimos_segundos_2 = None
        # En este momento el usuario ya puede hacer clic de nuevo pues las imágenes ya estarán ocultas
        puede_jugar_2 = True

    if not ganar_reinicio2 == 0:
        x1_2 = None
        y1_2 = None



    # Hacer toda la pantalla blanca
    screen.fill(color_rosado)
    # Banderas para saber en dónde dibujar las imágenes
    cuadros_rows = len(cuadros2)
    cuadros_cols = len(cuadros2[0])
    image_cuadros = cuadros2[0][0].imagen_real2
    image_cuadros_width = image_cuadros.get_width()
    image_cuadros_height = image_cuadros.get_height()
    x_offset = (screen_width - (cuadros_cols*image_cuadros_width))//(cuadros_cols + 1)
    y_offset = (screen_height - (cuadros_rows*image_cuadros_height))//(cuadros_rows + 1)
    #y_offset =((screen_height * 0.1927)+ 40 )
    y =  y_offset
    # Recorrer los cuadros
    for fila in cuadros2:
        x = x_offset
        
        for cuadro in fila:
            """
            Si está descubierto o se debe mostrar, dibujamos la imagen real. Si no,
            dibujamos la imagen oculta
            """
            if cuadro.descubierto2 or cuadro.mostrar2:
                screen.blit(cuadro.imagen_real2, (x, y))
                screen.blit(start_timer_text_2, timer_rect)
                

            else:
                screen.blit(imagen_oculta2, (x, y))
                screen.blit(start_timer_text_2, timer_rect)


            x += medida_cuadro_h
        y += medida_cuadro_v

    draw_points(cepillos2)
    
    if prueba2 == True: 
        """
        xAbsoluto e yAbsoluto son las coordenadas de la pantalla en donde se hizo
        clic. PyGame no ofrece detección de clic en imagen, por ejemplo. Así que
        se deben hacer ciertos trucos
        """
        # Si el click fue sobre el botón y el juego no se ha iniciado, entonces iniciamos el juego
        xAbsoluto = posX
        yAbsoluto = posY
        #if boton.collidepoint(event.pos):
        #   if not juego_iniciado:
        #      iniciar_juego()

        #else:
            # Si no hay juego iniciado, ignoramos el clic
        
        if juego_iniciado_2:
            iniciar_juego2()
            return
        
        x_rel = xAbsoluto - x_offset 
        y_rel = yAbsoluto - y_offset 
        
        x_cuadro = math.floor(x_rel / medida_cuadro_h)
        y_cuadro = math.floor(y_rel / medida_cuadro_v)
           
        # Primero lo primero. Si  ya está mostrada o descubierta, no hacemos nada
        if 0 <= x_cuadro < cuadros_cols and 0 <= y_cuadro < cuadros_rows:
            cuadro = cuadros2[y_cuadro][x_cuadro]
            if cuadro.mostrar2 or cuadro.descubierto2:
                # continue ignora lo de abajo y deja que el ciclo siga
                return
            # Si es la primera vez que tocan la imagen (es decir, no están buscando el par de otra, sino apenas
            # están descubriendo la primera)
            if x1_2 is None and y1_2 is None:# or acierto_2 == 1:
                # Entonces la actual es en la que acaban de dar clic, la mostramos
                x1_2 = x_cuadro
                y1_2 = y_cuadro
                cuadros2[y1_2][x1_2].mostrar2 = True
                pygame.mixer.Sound.play(sonido_voltear)
            
            cuadro1 = cuadros2[y1_2][x1_2]
            if cuadro1.fuente_imagen2 == "IMG_2L/segundo.png":
                cuadros2[y1_2][x1_2].descubierto2 = True
                acierto_2 = acierto_2 + 1
                pygame.mixer.Sound.play(sonido_clic)                        
            if not cuadro1.fuente_imagen2 == "IMG_2L/segundo.png":
                if cuadro1.fuente_imagen2 == "IMG_2L/wrong2_1.png":
                    if s_wrong2_1 == 1:
                        pygame.mixer.Sound.play(sn_wrong2_1)
                        s_wrong2_1 = 0
                if cuadro1.fuente_imagen2 == "IMG_2L/wrong2_2.png":
                    if s_wrong2_2 == 1:
                        pygame.mixer.Sound.play(sn_wrong2_2)
                        s_wrong2_2 = 0
                s_wrong2_1 = 1 
                s_wrong2_2 = 1
                #cuadros2[y1_2][x1_2].descubierto2 = False
                #pygame.mixer.Sound.play(sonido_fracaso)
                error_2 = error_2 + 1 
                ultimos_segundos_2 = int(time.time())
                ganar_reinicio2 = 0
                cepillos2 = cepillos2 -1


            comprobar_si_gana2()
                
          
            if ganar2:
                game_state = 'recompensa_2'#imagen que diga que ganó  y siguiente nivel o cosa 
            if perder2:
                game_state = 'reflection_2'
            prueba2 = False  
            


    if paused_game == True: # and juegos == True: # PANTALLA DE PAUSA
        game_state = 'Pausado'
        isGame = False
    return isGame, paused_game, game_state, back_window, reinicio, ret_intro, cont_game, prueba2, acierto_2, error_2, ganar2, aux_cronometro2, perder2, puede_jugar_2, ganar_reinicio2, cepillos2, sn_wrong2_1,s_wrong2_1, s_wrong2_2, sn_wrong2_2

def recompensa_2():
    global game_state
    global isGame
    isGame = False
    pygame.display.set_caption('Ganador1') # Caption - Nombre de la ventana
    instruc = 'VIDEOS/ganar_1.mp4'
    vel = 20
    pygame.mixer.Sound.play(completed)
    reproducir_video(instruc,vel)
    game_state = 'completed_2'
    return game_state

def completed_2():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window
    global reinicio
    global puede_jugar_2
    global ganar2, perder2, x1_2,y1_2
    global acierto_2, error_2, unused_time_2, used_time_2
    global ganar_reinicio2
    global audio_resultados
    
    pygame.display.set_caption('Completo nivel 2') # Caption - Nombre de la ventana
    screen.blit(fondo_resultados, (0,0)) # Función que dibuja el fondo
    correct_text = font.render(str(acierto_2), True, color_black)
    mistake_text = font.render(str(error_2), True, color_black)
    used_time_text = font.render( str(used_time_2), True, color_black)
    unused_time_text = font.render(str(unused_time_2), True, color_black)
    
    ######################
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(sonido_resultados)
    if audio_resultados == 1:
        channel.queue(audio_instruc)
        audio_resultados = 0
    ######################
    
    screen.blit(correct_text, ((screen_width//1.91), (screen_height//3.55)))
    screen.blit(mistake_text, ((screen_width//1.993), (screen_height//2.59)))
    screen.blit(used_time_text, ((screen_width//1.597), (screen_height//2.077)))
    screen.blit(unused_time_text, ((screen_width//1.597), (screen_height//1.717)))

    paused_game = False


    if reinicio == True:
        puede_jugar_2 = True
        ocultar_todos_los_cuadros_2()
        game_state = 'secondcard'
        reinicio = False
        ganar2 = False
        perder2 =  False
        back_window = False
        next_window = False
        #aux_cronometro = True 
        acierto_2 = 0
        error_2 = 0
        unused_time_2 = 0
        used_time_2 = 0
        #x1_2 = None
        #y1_2 = None
        ganar_reinicio2 +=1
        channel.stop()
        audio_resultados = 1

    if next_window == True: # Tecla n oprimida
        game_state = 'video_sostener_hilo'
        next_window = False
        ganar_reinicio2 +=1
        channel.stop()
        audio_resultados = 1
        

    if back_window == True: # Tecla b oprimida
        paused_game = False 
        back_window = False
        open_game = False
        ganar_reinicio2 +=1
        channel.stop()
        audio_resultados = 1
    
    isGame = False # False porque no se encuentra dentro de un juego    

    return game_state, paused_game, isGame, open_game, next_window, back_window, reinicio, puede_jugar_2, ganar2,  acierto_2, error_2, unused_time_2, used_time_2, perder2, x1_2, y1_2, ganar_reinicio2

def reflection_2():
    global game_state
    global isGame, used_time_2, time_limit_2
    isGame = False
    pygame.display.set_caption('Perder2') # Caption - Nombre de la ventana
    if used_time_2 == time_limit_2:
        instruc = 'VIDEOS/perder_tiempo.mp4'
        pygame.mixer.Sound.play(tiempo_agotado)
    else:
        instruc = 'VIDEOS/perder_puntos.mp4'
        pygame.mixer.Sound.play(puntos_agotados)
    vel = 20
    reproducir_video(instruc,vel)
    game_state = 'uncompleted_2'
    return game_state

def uncompleted_2():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window
    global reinicio
    global puede_jugar_2
    global ganar2, perder2
    global aux_cronometro2
    global acierto_2, error_2, unused_time_2, used_time_2, start_time_2, x1_2, y1_2
    global ganar_reinicio2
    global audio_resultados
    
    pygame.display.set_caption('No completo nivel 2') # Caption - Nombre de la ventana
    screen.blit(fondo_resultados, (0,0)) # Función que dibuja el fondo
    
    
    correct_text = font.render(str(acierto_2), True, color_black)
    mistake_text = font.render(str(error_2), True, color_black)
    used_time_text = font.render(str(used_time_2), True, color_black)
    unused_time_text = font.render(str(unused_time_2), True, color_black)
    ######################
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(sonido_resultados)
    if audio_resultados == 1:
        channel.queue(audio_instruc)
        audio_resultados = 0
    ######################
    screen.blit(correct_text, ((screen_width//1.91), (screen_height//3.55)))
    screen.blit(mistake_text, ((screen_width//1.993), (screen_height//2.59)))
    screen.blit(used_time_text, ((screen_width//1.597), (screen_height//2.077)))
    screen.blit(unused_time_text, ((screen_width//1.597), (screen_height//1.717)))

    paused_game = False

    if reinicio == True:
        puede_jugar_2 = True
        ocultar_todos_los_cuadros_2()
        game_state = 'secondcard'
        reinicio = False
        ganar2 = False
        perder2 = False
        back_window = False
        next_window = False 
        aux_cronometro2 = True
        acierto_2 = 0
        error_2 = 0
        unused_time_2 = 0
        used_time_2 = 0
        #x1_2 = None
        #y1_2 = None
        ganar_reinicio2 = 0
        channel.stop()
        audio_resultados = 1


    if next_window == True: # Tecla n oprimida
        game_state = 'video_sostener_hilo'
        next_window = False
        ganar_reinicio2 = 0
        channel.stop()
        audio_resultados = 1

    if back_window == True: # Tecla b oprimida
        paused_game = False 
        back_window = False
        open_game = False
        ganar_reinicio2 = 0
        channel.stop()
        audio_resultados = 1
         
    
    isGame = False # False porque no se encuentra dentro de un juego    

    return game_state, paused_game, isGame, open_game, next_window, back_window, reinicio, puede_jugar_2, ganar2, aux_cronometro2, acierto_2, error_2, unused_time_2, used_time_2, x1_2, y1_2, ganar_reinicio2


############################################## Tercer Nivel ###################################
def ocultar_todos_los_cuadros_3():
    for fila in cuadros3:
        for cuadro in fila:
            cuadro.mostrar3 = False
            cuadro.descubierto3 = False

# Determina si se gana, reinicia el juego y suena la pista correspondiente
def comprobar_si_gana3():
    global acierto_3, used_time_3, unused_time_3
    global game_state
    global ganar3, juego_iniciado_3, time_limit_3, perder3
    global error_3, ganar_reinicio3

    if gana3():
        used_time_3 =  start_time_3
        unused_time_3 =  time_limit_3 - used_time_3
        ganar3 = True
        juego_iniciado_3 = False

    if error_3 == 3 or used_time_3 == time_limit_3:
        used_time_3 =  start_time_3
        unused_time_3 =  time_limit_3 - used_time_3
        perder3 = True
        juego_iniciado_3 = False
        ganar_reinicio3 = 0
    return acierto_3, game_state, ganar3, juego_iniciado_3, perder3, error_3, ganar_reinicio3
        
        
# Regresa False si al menos un cuadro NO está descubierto. True en caso de que absolutamente todos estén descubiertos
# Recorre todas las filas de la matriz y en caso de que alguno no esté descubierto retorna a falso, de lo contrario pasa a true
def gana3():
    if not acierto_3 == 1: 
        return False
    return True


# Reproduce el sonido de click para que empiece, modifica el juego iniciado 
def iniciar_juego3():
    global juego_iniciado_3
    #global automatico
    #pygame.mixer.Sound.play(sonido_clic)
    #automatico = pygame.MOUSEBUTTONDOWN
    ocultar_todos_los_cuadros_3()
    juego_iniciado_3 = True

# Función para dibujar los cepillos en la pantalla
def draw_points2(cepillos):
    cepillo_image = pygame.transform.scale(pygame.image.load("puntos/punto2.png"), (100, 100))
    cepillo_width, cepillo_height = cepillo_image.get_size()
    x_offset = 10 # Ajusta la posición x donde quieres que aparezcan los cepillos

    for i in range(cepillos):
        x = x_offset + i * (cepillo_width + 5)  # Espacio entre los cepillos
        y = 10  # Ajusta la posición y donde quieres que aparezcan los cepillos
        screen.blit(cepillo_image, (x, y))

def third_level():  
    global isGame
    global game_state
    global paused_game
    global screen_width
    global screen_height
    global timer_text_3, level_time_3, timer_active_3, aux_cronometro3
    global puede_jugar_3, reinicio, ganar3, perder3
    global acierto_3, error_3, used_time_3, unused_time_3 
    global x1_3, y1_3
    global actual_matrix, ganar_reinicio3, cepillos3
    global audio_tablero
    pygame.display.set_caption('_') # Caption - Nombre de la ventana
    screen.fill(color_rosado)
    isGame = False # Bandera que indica estado de juego activo, lo que implica que se puede pausar o no
    paused_game = False
    puede_jugar_3 = True
    reinicio = False
    aux_cronometro3 = True
    acierto_3 = 0
    error_3 = 0
    unused_time_3 = 0
    used_time_3 = 0
    cepillos3 = 3
    ######################
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(ver_tablero)
    if audio_tablero == 1:
        channel.queue(audio_instruc)
        audio_tablero = 0
    ######################
    if not ganar_reinicio3 == 0:
            x1_3 = None
            y1_3 = None

    #start_timer_active = False
    #Para que al estar en esta pantalla sea seguro que el juego se reinicia y queda en el estado inicial
    ocultar_todos_los_cuadros_3()
    ganar3 = False
    perder3 = False
    actual_matrix = 2
    image_matrix = matrix_level[actual_matrix]
    rows = len(image_matrix)
    cols = len(image_matrix[0])
    image_width = image_matrix[0][0].get_width()
    image_height = image_matrix[0][0].get_height()
    padding_x = (screen_width - (cols * image_width)) // (cols + 1)
    padding_y = (screen_height - (rows * image_height)) // (rows + 1)
    timer_rect_3 = timer_text_3.get_rect(center = ((screen_width/2),(screen_height/2))) # Centro de la pantalla: center = screen.get_rect().center

    for i in range(rows):
        for j in range(cols):
            x = padding_x + j * (image_width + padding_x)
            y = padding_y + i * (image_height + padding_y)
            screen.blit(image_matrix[i][j], (x, y))
            #center_text(first_level_text,100) # Texto
            screen.blit(timer_text_3, timer_rect_3) 
    
    if not timer_active_3 and game_state == 'third_level':
        level_time_3 = 15
        pygame.time.set_timer(timer_event_3, 1000) # set_timer crea una acción cada 1s
        timer_active_3 = True

    return isGame, paused_game, game_state, next_window, back_window, timer_text_3, level_time_3,  puede_jugar_3, reinicio, ganar3, perder3, timer_active_3, x1_3, y1_3, aux_cronometro3, acierto_3, error_3, used_time_3, unused_time_3, cepillos3



def Thrd_level():
    global isGame
    global game_state
    global paused_game
    global segundos_mostrar_pieza3
    global cuadros3
    global imagen_oculta3
    global puede_jugar_3
    global ultimos_segundos_3
    global x1_3, y1_3, posX, posY
    global reinicio, ret_intro, cont_game, next_window, back_window
    global timer_font_3, start_time_3, start_timer_text_3, start_timer_event_3, start_timer_active_3
    global prueba3, acierto_3, error_3, ganar3, aux_cronometro3, perder3
    global cepillos3
    global ganar_reinicio3, cepillos3
    global s_wrong3_1, s_wrong3_2,s_wrong3_3, sn_wrong3_1, sn_wrong3_2, sn_wrong3_3
    #pygame.mouse.set_visible(True)# Hacer visible el cursor   

    pygame.display.set_caption('Thrd_level') # Caption - Nombre de la ventana
    isGame = True # Bandera que indica estado de juego activo, lo que implica que se puede pausar
    ret_intro = False
    cont_game = False
    reinicio = False
    next_window = False
    back_window = False

    medida_cuadro_h = screen_width/len(cuadros3[0])  # Medida de la imagen en pixeles
    medida_cuadro_v = screen_height/len(cuadros3) # Medida de la imagen en pixeles

    timer_rect3 = start_timer_text_3.get_rect(center = ((screen_width/2),(screen_height/2)))
    if not start_timer_active_3 and game_state == 'Thrd_level':
        start_time_3 = 0
        pygame.time.set_timer(start_timer_event_3, 1000)
        start_timer_active_3 = True

    ahora = int(time.time())
    # Y aquí usamos la bandera del tiempo, de nuevo. Si los segundos actuales menos los segundos
    # en los que se empezó el ocultamiento son mayores a los segundos en los que se muestra la pieza, entonces
    # se ocultan las dos tarjetas y se reinician las banderas
    if ultimos_segundos_3 is not None and ahora - ultimos_segundos_3 >= segundos_mostrar_pieza3:
        cuadros3[y1_3][x1_3].mostrar3 = False
        
        #cuadros2[y2_2][x2_2].mostrar2 = False
        x1_3 = None
        y1_3 = None
        #x2_2 = None
        #y2_2 = None
        ultimos_segundos_3 = None
        # En este momento el usuario ya puede hacer clic de nuevo pues las imágenes ya estarán ocultas
        puede_jugar_3 = True

    if not ganar_reinicio3 == 0:
        x1_3 = None
        y1_3 = None



    # Hacer toda la pantalla blanca
    screen.fill(color_rosado)
    # Banderas para saber en dónde dibujar las imágenes
    cuadros_rows = len(cuadros3)
    cuadros_cols = len(cuadros3[0])
    image_cuadros = cuadros3[0][0].imagen_real3
    image_cuadros_width = image_cuadros.get_width()
    image_cuadros_height = image_cuadros.get_height()
    x_offset = (screen_width - (cuadros_cols*image_cuadros_width))//(cuadros_cols + 1)
    y_offset = (screen_height - (cuadros_rows*image_cuadros_height))//(cuadros_rows + 1)
    
    y =  y_offset
    # Recorrer los cuadros
    for fila in cuadros3:
        x = x_offset
        for cuadro in fila:
            """
            Si está descubierto o se debe mostrar, dibujamos la imagen real. Si no,
            dibujamos la imagen oculta
            """
            if cuadro.descubierto3 or cuadro.mostrar3:
                screen.blit(cuadro.imagen_real3, (x, y))
                screen.blit(start_timer_text_3, timer_rect3)
                

            else:
                screen.blit(imagen_oculta3, (x, y))
                screen.blit(start_timer_text_3, timer_rect3)


            x += medida_cuadro_h
        y += medida_cuadro_v
        

    draw_points2(cepillos3)
    
    if prueba3 == True: 
        """
        xAbsoluto e yAbsoluto son las coordenadas de la pantalla en donde se hizo
        clic. PyGame no ofrece detección de clic en imagen, por ejemplo. Así que
        se deben hacer ciertos trucos
        """
        # Si el click fue sobre el botón y el juego no se ha iniciado, entonces iniciamos el juego
        xAbsoluto = posX 
        yAbsoluto = posY 
        #if boton.collidepoint(event.pos):
        #   if not juego_iniciado:
        #      iniciar_juego()

        #else:
            # Si no hay juego iniciado, ignoramos el clic
        
        if juego_iniciado_3:
            iniciar_juego3()
            return
        
        x_rel = xAbsoluto - x_offset 
        y_rel = yAbsoluto - y_offset 
 
        
        x_cuadro = math.floor(x_rel / medida_cuadro_h)
        y_cuadro = math.floor(y_rel / medida_cuadro_v)
        
           
        # Primero lo primero. Si  ya está mostrada o descubierta, no hacemos nada
        if 0 <= x_cuadro < cuadros_cols and 0 <= y_cuadro < cuadros_rows:
            cuadro = cuadros3[y_cuadro][x_cuadro]

            if cuadro.mostrar3 or cuadro.descubierto3:
                # continue ignora lo de abajo y deja que el ciclo siga
                return
            # Si es la primera vez que tocan la imagen (es decir, no están buscando el par de otra, sino apenas
            # están descubriendo la primera)
            if x1_3 is None and y1_3 is None:# or acierto_2 == 1:
                # Entonces la actual es en la que acaban de dar clic, la mostramos
                x1_3 = x_cuadro
                y1_3 = y_cuadro
                cuadros3[y1_3][x1_3].mostrar3 = True
                pygame.mixer.Sound.play(sonido_voltear)
            
            cuadro1 = cuadros3[y1_3][x1_3]
            if cuadro1.fuente_imagen3 == "IMG_3L/tercero.png":
                cuadros2[y1_3][x1_3].descubierto3 = True
                acierto_3 = acierto_3 + 1
                pygame.mixer.Sound.play(sonido_clic)                        
            if not cuadro1.fuente_imagen3 == "IMG_3L/tercero.png":
                if cuadro1.fuente_imagen3 == "IMG_3L/wrong3_1.png":
                    if s_wrong3_1 == 1:
                        pygame.mixer.Sound.play(sn_wrong3_1)
                        s_wrong3_1 = 0
                if cuadro1.fuente_imagen3 == "IMG_3L/wrong3_2.png":
                    if s_wrong3_2 == 1:
                        pygame.mixer.Sound.play(sn_wrong3_2)
                        s_wrong3_2 = 0
                if cuadro1.fuente_imagen3 == "IMG_3L/wrong3_3.png":
                    if s_wrong3_3 == 1:
                        pygame.mixer.Sound.play(sn_wrong3_3)
                        s_wrong3_3 = 0
                s_wrong3_1 = 1
                s_wrong3_2 = 1
                s_wrong3_3 = 1 
                error_3 = error_3 + 1 
                ultimos_segundos_3 = int(time.time())
                ganar_reinicio3 = 0
                cepillos3 = cepillos3 -1
            comprobar_si_gana3()
                
          
            if ganar3:
                game_state = 'recompensa_3'#imagen que diga que ganó  y siguiente nivel o cosa 
            if perder3:
                game_state = 'reflection_3'
            prueba3 = False  
            


    if paused_game == True: # and juegos == True: # PANTALLA DE PAUSA
        game_state = 'Pausado'
        isGame = False
    return (isGame, paused_game, game_state, back_window, reinicio, ret_intro, cont_game,
             prueba3, acierto_3, error_3, ganar3, aux_cronometro3, perder3, puede_jugar_3, ganar_reinicio3, 
             cepillos3, s_wrong3_1, s_wrong3_2, s_wrong3_3)

def recompensa_3():
    global game_state
    global isGame
    isGame = False
    pygame.display.set_caption('Ganador1') # Caption - Nombre de la ventana
    instruc = 'VIDEOS/ganar_2.mp4'
    vel = 20
    pygame.mixer.Sound.play(completed)
    reproducir_video(instruc,vel)
    game_state = 'completed_3'
    return game_state

def completed_3():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window
    global reinicio
    global puede_jugar_3
    global ganar3, perder3, x1_3,y1_3
    #global aux_cronometro
    global acierto_3, error_3, unused_time_3, used_time_3
    global ganar_reinicio3
    global audio_resultados
    
    pygame.display.set_caption('Completo nivel 3') # Caption - Nombre de la ventana
    screen.blit(fondo_resultados, (0,0)) # Función que dibuja el fondo
    correct_text = font.render(str(acierto_3), True, color_black)
    mistake_text = font.render(str(error_3), True, color_black)
    used_time_text = font.render( str(used_time_3), True, color_black)
    unused_time_text = font.render(str(unused_time_3), True, color_black)
    ######################
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(sonido_resultados)
    if audio_resultados == 1:
        channel.queue(audio_instruc)
        audio_resultados = 0
    ######################
    
    screen.blit(correct_text, ((screen_width//1.91), (screen_height//3.55)))
    screen.blit(mistake_text, ((screen_width//1.993), (screen_height//2.59)))
    screen.blit(used_time_text, ((screen_width//1.597), (screen_height//2.077)))
    screen.blit(unused_time_text, ((screen_width//1.597), (screen_height//1.717)))

    paused_game = False


    if reinicio == True:
        puede_jugar_3 = True
        ocultar_todos_los_cuadros_3()
        game_state = 'thirdcard'
        reinicio = False
        ganar3 = False
        perder3 =  False
        back_window = False
        next_window = False
        #aux_cronometro = True 
        acierto_3 = 0
        error_3 = 0
        unused_time_3 = 0
        used_time_3 = 0
        #x1_2 = None
        #y1_2 = None
        ganar_reinicio3 +=1
        channel.stop()
        audio_resultados = 1

    if next_window == True: # Tecla n oprimida
        game_state = 'video_mover_hilo'
        next_window = False
        ganar_reinicio3 +=1
        channel.stop()
        audio_resultados = 1
        

    if back_window == True: # Tecla b oprimida
        paused_game = False 
        back_window = False
        open_game = False
        ganar_reinicio3 +=1
        channel.stop()
        audio_resultados = 1
    
    isGame = False # False porque no se encuentra dentro de un juego    

    return game_state, paused_game, isGame, open_game, next_window, back_window, reinicio, puede_jugar_3, ganar3,  acierto_3, error_3, unused_time_3, used_time_3, perder3, x1_3, y1_3, ganar_reinicio3

def reflection_3():
    global game_state
    global isGame, used_time_3, time_limit_3
    isGame = False
    pygame.display.set_caption('Perder3') # Caption - Nombre de la ventana
    if used_time_3 == time_limit_3:
        instruc = 'VIDEOS/perder_tiempo.mp4'
        pygame.mixer.Sound.play(tiempo_agotado)
    else:
        instruc = 'VIDEOS/perder_puntos.mp4'
        pygame.mixer.Sound.play(puntos_agotados)
    vel = 20
    reproducir_video(instruc,vel)
    game_state = 'uncompleted_3'
    return game_state

def uncompleted_3():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window
    global reinicio
    global puede_jugar_3
    global ganar3, perder3
    global aux_cronometro3
    global acierto_3, error_3, unused_time_3, used_time_3, start_time_3, x1_3, y1_3
    global ganar_reinicio3
    global audio_resultados
    
    pygame.display.set_caption('No completo nivel 3') # Caption - Nombre de la ventana
    screen.blit(fondo_resultados, (0,0)) # Función que dibuja el fondo
    
    
    correct_text = font.render(str(acierto_3), True, color_black)
    mistake_text = font.render(str(error_3), True, color_black)
    used_time_text = font.render(str(used_time_3), True, color_black)
    unused_time_text = font.render(str(unused_time_3), True, color_black)
    
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(sonido_resultados)
    if audio_resultados == 1:
        channel.queue(audio_instruc)
        audio_resultados = 0

    screen.blit(correct_text, ((screen_width//1.91), (screen_height//3.55)))
    screen.blit(mistake_text, ((screen_width//1.993), (screen_height//2.59)))
    screen.blit(used_time_text, ((screen_width//1.597), (screen_height//2.077)))
    screen.blit(unused_time_text, ((screen_width//1.597), (screen_height//1.717)))

    paused_game = False

    if reinicio == True:
        puede_jugar_3 = True
        ocultar_todos_los_cuadros_3()
        game_state = 'thirdcard'
        reinicio = False
        ganar3 = False
        perder3 = False
        back_window = False
        next_window = False 
        aux_cronometro3 = True
        acierto_3 = 0
        error_3 = 0
        unused_time_3 = 0
        used_time_3 = 0
        ganar_reinicio3 = 0
        channel.stop()
        audio_resultados = 1


    if next_window == True: # Tecla n oprimida
        game_state = 'video_mover_hilo'
        next_window = False
        ganar_reinicio3 = 0
        channel.stop()
        audio_resultados = 1
        

    if back_window == True: # Tecla b oprimida
        paused_game = False 
        back_window = False
        open_game = False
        ganar_reinicio3 = 0
        channel.stop()
        audio_resultados = 1
         
    
    isGame = False # False porque no se encuentra dentro de un juego    

    return game_state, paused_game, isGame, open_game, next_window, back_window, reinicio, puede_jugar_3, ganar3, aux_cronometro3, acierto_3, error_3, unused_time_3, used_time_3, x1_3, y1_3, ganar_reinicio3



####################################### Cuarto Nivel ############################################FALTA
def ocultar_todos_los_cuadros_4():
    for fila in cuadros4:
        for cuadro in fila:
            cuadro.mostrar4 = False
            cuadro.descubierto4 = False

# Determina si se gana, reinicia el juego y suena la pista correspondiente
def comprobar_si_gana4():
    global acierto_4, used_time_4, unused_time_4
    global game_state
    global ganar4, juego_iniciado_4, time_limit_4, perder4
    global error_4, ganar_reinicio4, x1_4, y1_4

    if gana4():
        used_time_4 =  start_time_4
        unused_time_4 =  time_limit_4 - used_time_4
        ganar4 = True
        juego_iniciado_4 = False

    if error_4 == 3 or used_time_4 == time_limit_4:
        used_time_4 =  start_time_4
        unused_time_4 =  time_limit_4 - used_time_4
        perder4 = True
        juego_iniciado_4 = False
        ganar_reinicio4 = 0

    return acierto_4, game_state, ganar4, juego_iniciado_4, perder4, error_4, ganar_reinicio4, x1_4, y1_4
        
        
# Regresa False si al menos un cuadro NO está descubierto. True en caso de que absolutamente todos estén descubiertos
# Recorre todas las filas de la matriz y en caso de que alguno no esté descubierto retorna a falso, de lo contrario pasa a true
def gana4():
    if not acierto_4 == 2: 
        return False
    return True



# Reproduce el sonido de click para que empiece, modifica el juego iniciado 
def iniciar_juego4():
    global juego_iniciado_4
    #global automatico
    #pygame.mixer.Sound.play(sonido_clic)
    #automatico = pygame.MOUSEBUTTONDOWN
    ocultar_todos_los_cuadros_4()
    juego_iniciado_4 = True

# Función para dibujar los cepillos en la pantalla
def draw_points3(cepillos):
    cepillo_image = pygame.transform.scale(pygame.image.load("puntos/punto1.png"), (100, 100))
    cepillo_width, cepillo_height = cepillo_image.get_size()
    x_offset = 10  # Ajusta la posición x donde quieres que aparezcan los cepillos

    for i in range(cepillos):
        x = x_offset + i * (cepillo_width + 5)  # Espacio entre los cepillos
        y = 10  # Ajusta la posición y donde quieres que aparezcan los cepillos
        screen.blit(cepillo_image, (x, y))

def fourth_level():  
    global isGame
    global game_state
    global paused_game
    global screen_width
    global screen_height
    global timer_text_4, level_time_4, timer_active_4, aux_cronometro4
    global puede_jugar_4, reinicio, ganar4, perder4
    global acierto_4, error_4, used_time_4, unused_time_4 
    global x1_4, y1_4
    global actual_matrix, ganar_reinicio4, cepillos4
    global audio_tablero
    pygame.display.set_caption('_') # Caption - Nombre de la ventana
    screen.fill(color_azul_claro) 
    isGame = False # Bandera que indica estado de juego activo, lo que implica que se puede pausar o no
    paused_game = False
    puede_jugar_4 = True
    reinicio = False
    aux_cronometro4 = True
    acierto_4 = 0
    error_4 = 0
    unused_time_4 = 0
    used_time_4 = 0
    cepillos4 = 3
    ######################
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(ver_tablero)
    if audio_tablero == 1:
        channel.queue(audio_instruc)
        audio_tablero = 0
    ######################
    if not ganar_reinicio4 == 0:
            x1_4 = None
            y1_4 = None

    #start_timer_active = False
    #Para que al estar en esta pantalla sea seguro que el juego se reinicia y queda en el estado inicial
    ocultar_todos_los_cuadros_4()
    ganar4 = False
    perder4 = False
    actual_matrix = 3
    image_matrix = matrix_level[actual_matrix]
    rows = len(image_matrix)
    cols = len(image_matrix[0])
    image_width = image_matrix[0][0].get_width()
    image_height = image_matrix[0][0].get_height()
    padding_x = (screen_width - (cols * image_width)) // (cols + 1)
    padding_y = (screen_height - (rows * image_height)) // (rows + 1)
    timer_rect_4 = timer_text_4.get_rect(center = ((screen_width/2),(screen_height/2))) # Centro de la pantalla: center = screen.get_rect().center
    

    for i in range(rows):
        for j in range(cols):
            x = padding_x + j * (image_width + padding_x)
            y = padding_y + i * (image_height + padding_y)
            screen.blit(image_matrix[i][j], (x, y))
            #center_text(first_level_text,100) # Texto
            screen.blit(timer_text_4, timer_rect_4) 
    
    if not timer_active_4 and game_state == 'fourth_level':
        level_time_4 = 15
        pygame.time.set_timer(timer_event_4, 1000) # set_timer crea una acción cada 1s
        timer_active_4 = True

    return isGame, paused_game, game_state, next_window, back_window, timer_text_4, level_time_4,  puede_jugar_4, reinicio, ganar4, perder4, timer_active_4, x1_4, y1_4, aux_cronometro4, acierto_4, error_4, used_time_4, unused_time_4, cepillos4



def Frth_level():
    global isGame
    global game_state
    global paused_game
    global segundos_mostrar_pieza4
    global cuadros4
    global imagen_oculta4
    global puede_jugar_4
    global ultimos_segundos_4
    global x1_4, y1_4, posX, posY
    global reinicio, ret_intro, cont_game, next_window, back_window
    global timer_font_4, start_time_4, start_timer_text_4, start_timer_event_4, start_timer_active_4
    global prueba4, acierto_4, error_4, ganar4, aux_cronometro4, perder4
    global cepillos4
    global ganar_reinicio4, cepillos4
    global s_wrong4_1, s_wrong4_2, s_wrong4_3, s_wrong4_4, sn_wrong4_1, sn_wrong4_2, sn_wrong4_3, sn_wrong4_4
    #pygame.mouse.set_visible(True)# Hacer visible el cursor   

    pygame.display.set_caption('Frth_level') # Caption - Nombre de la ventana
    screen.fill(color_azul_claro) 
    isGame = True # Bandera que indica estado de juego activo, lo que implica que se puede pausar
    ret_intro = False
    cont_game = False
    reinicio = False
    next_window = False
    back_window = False

    medida_cuadro_h = screen_width/len(cuadros4[0])  # Medida de la imagen en pixeles
    medida_cuadro_v = screen_height/len(cuadros4) # Medida de la imagen en pixeles

    timer_rect4 = start_timer_text_4.get_rect(center = ((screen_width/2),(screen_height/2)))
    if not start_timer_active_4 and game_state == 'Frth_level':
        start_time_4 = 0
        pygame.time.set_timer(start_timer_event_4, 1000)
        start_timer_active_4 = True

    ahora = int(time.time())
    # Y aquí usamos la bandera del tiempo, de nuevo. Si los segundos actuales menos los segundos
    # en los que se empezó el ocultamiento son mayores a los segundos en los que se muestra la pieza, entonces
    # se ocultan las dos tarjetas y se reinician las banderas
    if ultimos_segundos_4 is not None and ahora - ultimos_segundos_4 >= segundos_mostrar_pieza4:
        cuadros4[y1_4][x1_4].mostrar4 = False
        
        #cuadros2[y2_2][x2_2].mostrar2 = False
        x1_4 = None
        y1_4 = None
        #x2_2 = None
        #y2_2 = None
        ultimos_segundos_4 = None
        # En este momento el usuario ya puede hacer clic de nuevo pues las imágenes ya estarán ocultas
        puede_jugar_4 = True

    if not ganar_reinicio4 == 0:
        x1_4 = None
        y1_4 = None



    # Hacer toda la pantalla blanca
    screen.fill(color_azul_claro)
    # Banderas para saber en dónde dibujar las imágenes
    cuadros_rows = len(cuadros4)
    cuadros_cols = len(cuadros4[0])
    image_cuadros = cuadros4[0][0].imagen_real4
    image_cuadros_width = image_cuadros.get_width()
    image_cuadros_height = image_cuadros.get_height()
    x_offset = (screen_width - (cuadros_cols*image_cuadros_width))//(cuadros_cols + 1)
    y_offset = (screen_height - (cuadros_rows*image_cuadros_height))//(cuadros_rows + 1)

    y =  y_offset
    # Recorrer los cuadros
    for fila in cuadros4:
        x = x_offset
        for cuadro in fila:
            """
            Si está descubierto o se debe mostrar, dibujamos la imagen real. Si no,
            dibujamos la imagen oculta
            """
            if cuadro.descubierto4 or cuadro.mostrar4:
                screen.blit(cuadro.imagen_real4, (x, y))
                screen.blit(start_timer_text_4, timer_rect4)
                

            else:
                screen.blit(imagen_oculta4, (x, y))
                screen.blit(start_timer_text_4, timer_rect4)


            x += medida_cuadro_h
        y += medida_cuadro_v

    draw_points3(cepillos4)
    
    if prueba4 == True: 
        """
        xAbsoluto e yAbsoluto son las coordenadas de la pantalla en donde se hizo
        clic. PyGame no ofrece detección de clic en imagen, por ejemplo. Así que
        se deben hacer ciertos trucos
        """
        # Si el click fue sobre el botón y el juego no se ha iniciado, entonces iniciamos el juego
        xAbsoluto = posX
        yAbsoluto = posY
        #if boton.collidepoint(event.pos):
        #   if not juego_iniciado:
        #      iniciar_juego()

        #else:
            # Si no hay juego iniciado, ignoramos el clic
        
        if juego_iniciado_4:
            iniciar_juego4()
            return
        
        x_rel = xAbsoluto - x_offset 
        y_rel = yAbsoluto - y_offset 
        
        x_cuadro = math.floor(x_rel / medida_cuadro_h)
        y_cuadro = math.floor(y_rel / medida_cuadro_v)
        
        # Primero lo primero. Si  ya está mostrada o descubierta, no hacemos nada
        if 0 <= x_cuadro < cuadros_cols and 0 <= y_cuadro < cuadros_rows:
            cuadro = cuadros4[y_cuadro][x_cuadro]
            if cuadro.mostrar4 or cuadro.descubierto4:
                # continue ignora lo de abajo y deja que el ciclo siga
                return
            # Si es la primera vez que tocan la imagen (es decir, no están buscando el par de otra, sino apenas
            # están descubriendo la primera)
            if x1_4 is None and y1_4 is None:# or acierto_2 == 1:
                # Entonces la actual es en la que acaban de dar clic, la mostramos
                x1_4 = x_cuadro
                y1_4 = y_cuadro
                cuadros4[y1_4][x1_4].mostrar4 = True
                pygame.mixer.Sound.play(sonido_voltear)
            
            cuadro1 = cuadros4[y1_4][x1_4]
            if cuadro1.fuente_imagen4 == "IMG_4L/cuarto.png":
                cuadros4[y1_4][x1_4].descubierto4 = True
                acierto_4 = acierto_4 + 1                    
                pygame.mixer.Sound.play(sonido_clic) 
                ganar_reinicio4 = 1
            if not cuadro1.fuente_imagen4 == "IMG_4L/cuarto.png":
                if cuadro1.fuente_imagen4 == "IMG_4L/wrong4_1.png":
                    if s_wrong4_1 == 1:
                        pygame.mixer.Sound.play(sn_wrong4_1)
                        s_wrong4_1 = 0
                if cuadro1.fuente_imagen4 == "IMG_4L/wrong4_2.png":
                    if s_wrong4_2 == 1:
                        pygame.mixer.Sound.play(sn_wrong4_2)
                        s_wrong4_2 = 0
                if cuadro1.fuente_imagen4 == "IMG_4L/wrong4_3.png":
                    if s_wrong4_3 == 1:
                        pygame.mixer.Sound.play(sn_wrong4_3)
                        s_wrong4_3 = 0
                if cuadro1.fuente_imagen4 == "IMG_4L/wrong4_4.png":
                    if s_wrong4_4 == 1:
                        pygame.mixer.Sound.play(sn_wrong4_4)
                        s_wrong4_4 = 0
                s_wrong4_1 = 1
                s_wrong4_2 = 1
                s_wrong4_3 = 1
                s_wrong4_4 = 1 

                error_4 = error_4 + 1 
                ultimos_segundos_4 = int(time.time())
                ganar_reinicio4 = 0
                cepillos4 = cepillos4 -1
            comprobar_si_gana4()
                
          
            if ganar4:
                game_state = 'recompensa_4'#imagen que diga que ganó  y siguiente nivel o cosa 
            if perder4:
                game_state = 'reflection_4'
            prueba4 = False  
            


    if paused_game == True: # and juegos == True: # PANTALLA DE PAUSA
        game_state = 'Pausado'
        isGame = False
    return (isGame, paused_game, game_state, back_window, reinicio, ret_intro, cont_game, 
            prueba4, acierto_4, error_4, ganar4, aux_cronometro4, perder4, puede_jugar_4, ganar_reinicio4, cepillos4,
            s_wrong4_1, s_wrong4_2, s_wrong4_3, s_wrong4_4)

def recompensa_4():
    global game_state
    global isGame
    isGame = False
    pygame.display.set_caption('Ganador4') # Caption - Nombre de la ventana
    instruc = 'VIDEOS/ganar_3.mp4'
    vel = 20
    pygame.mixer.Sound.play(completed)
    reproducir_video(instruc,vel)
    game_state = 'completed_4'
    return game_state

def completed_4():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window
    global reinicio
    global puede_jugar_4
    global ganar4, perder4, x1_4,y1_4
    global acierto_4, error_4, unused_time_4, used_time_4
    global ganar_reinicio4
    global audio_resultados
    
    pygame.display.set_caption('Completo nivel 4') # Caption - Nombre de la ventana
    screen.blit(fondo_resultados, (0,0)) # Función que dibuja el fondo
    correct_text = font.render(str(acierto_4), True, color_black)
    mistake_text = font.render(str(error_4), True, color_black)
    used_time_text = font.render( str(used_time_4), True, color_black)
    unused_time_text = font.render(str(unused_time_4), True, color_black)
   
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(sonido_resultados)
    if audio_resultados == 1:
        channel.queue(audio_instruc)
        audio_resultados = 0
  
    screen.blit(correct_text, ((screen_width//1.91), (screen_height//3.55)))
    screen.blit(mistake_text, ((screen_width//1.993), (screen_height//2.59)))
    screen.blit(used_time_text, ((screen_width//1.597), (screen_height//2.077)))
    screen.blit(unused_time_text, ((screen_width//1.597), (screen_height//1.717)))

    paused_game = False


    if reinicio == True:
        puede_jugar_4 = True
        ocultar_todos_los_cuadros_4()
        game_state = 'fourthcard'
        reinicio = False
        ganar4 = False
        perder4 =  False
        back_window = False
        next_window = False
        #aux_cronometro = True 
        acierto_4 = 0
        error_4 = 0
        unused_time_4 = 0
        used_time_4 = 0
        #x1_2 = None
        #y1_2 = None
        ganar_reinicio4 +=1
        channel.stop()
        audio_resultados = 1

    if next_window == True: # Tecla n oprimida
        game_state = 'fifthcard'
        next_window = False
        channel.stop()
        audio_resultados = 1
        
        

    if back_window == True: # Tecla b oprimida
        paused_game = False 
        back_window = False
        open_game = False
        ganar_reinicio4 +=1
        channel.stop()
        audio_resultados = 1
    
    isGame = False # False porque no se encuentra dentro de un juego    

    return game_state, paused_game, isGame, open_game, next_window, back_window, reinicio, puede_jugar_4, ganar4,  acierto_4, error_4, unused_time_4, used_time_4, perder4, x1_4, y1_4, ganar_reinicio4

def reflection_4():
    global game_state
    global isGame, used_time_4, time_limit_4
    isGame = False
    pygame.display.set_caption('Perder4') # Caption - Nombre de la ventana
    if used_time_4 == time_limit_4:
        instruc = 'VIDEOS/perder_tiempo.mp4'
        pygame.mixer.Sound.play(tiempo_agotado)
    else:
        instruc = 'VIDEOS/perder_puntos.mp4'
        pygame.mixer.Sound.play(puntos_agotados)
    vel = 20
    reproducir_video(instruc,vel)
    game_state = 'uncompleted_4'
    return game_state

def uncompleted_4():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window
    global reinicio
    global puede_jugar_4
    global ganar4, perder4
    global aux_cronometro4
    global acierto_4, error_4, unused_time_4, used_time_4, start_time_4, x1_4, y1_4
    global ganar_reinicio4
    global audio_resultados
    pygame.display.set_caption('No completo nivel 4') # Caption - Nombre de la ventana
    screen.blit(fondo_resultados, (0,0)) # Función que dibuja el fondo
    
    
    correct_text = font.render(str(acierto_4), True, color_black)
    mistake_text = font.render(str(error_4), True, color_black)
    used_time_text = font.render(str(used_time_4), True, color_black)
    unused_time_text = font.render(str(unused_time_4), True, color_black)
    
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(sonido_resultados)
    if audio_resultados == 1:
        channel.queue(audio_instruc)
        audio_resultados = 0

    screen.blit(correct_text, ((screen_width//1.91), (screen_height//3.55)))
    screen.blit(mistake_text, ((screen_width//1.993), (screen_height//2.59)))
    screen.blit(used_time_text, ((screen_width//1.597), (screen_height//2.077)))
    screen.blit(unused_time_text, ((screen_width//1.597), (screen_height//1.717)))

    paused_game = False

    if reinicio == True:
        puede_jugar_4 = True
        ocultar_todos_los_cuadros_4()
        game_state = 'fourthcard'##### CAMBIAR
        reinicio = False
        ganar4 = False
        perder4 = False
        back_window = False
        next_window = False 
        aux_cronometro4 = True
        acierto_4 = 0
        error_4 = 0
        unused_time_4 = 0
        used_time_4 = 0
        ganar_reinicio4 = 0
        channel.stop()
        audio_resultados = 1

    if next_window == True: # Tecla n oprimida
        game_state = 'fifthcard'
        next_window = False
        channel.stop()
        audio_resultados = 1

    if back_window == True: # Tecla b oprimida
        paused_game = False 
        back_window = False
        open_game = False
        ganar_reinicio4 = 0
        channel.stop()
        audio_resultados = 1
    
    isGame = False # False porque no se encuentra dentro de un juego    

    return game_state, paused_game, isGame, open_game, next_window, back_window, reinicio, puede_jugar_4, ganar4, aux_cronometro4, acierto_4, error_4, unused_time_4, used_time_4, x1_4, y1_4, ganar_reinicio4

#######################################Quinto Nivel###############################################
def ocultar_todos_los_cuadros_5():
    for fila in cuadros5:
        for cuadro in fila:
            cuadro.mostrar5 = False
            cuadro.descubierto5 = False

# Determina si se gana, reinicia el juego y suena la pista correspondiente
def comprobar_si_gana5():
    global acierto_5, used_time_5, unused_time_5
    global game_state
    global ganar5, juego_iniciado_5, time_limit_5, perder5
    global error_5, ganar_reinicio5

    if gana5():
        used_time_5 =  start_time_5
        unused_time_5 =  time_limit_5 - used_time_5
        ganar5 = True
        juego_iniciado_5 = False

    if error_5 == 3 or used_time_5 == time_limit_5:
        used_time_5 =  start_time_5
        unused_time_5 =  time_limit_5 - used_time_5
        perder5 = True
        juego_iniciado_5 = False
        ganar_reinicio5 = 0

    return acierto_5, game_state, ganar5, juego_iniciado_5, perder5, error_5, ganar_reinicio5
        
        
# Regresa False si al menos un cuadro NO está descubierto. True en caso de que absolutamente todos estén descubiertos
# Recorre todas las filas de la matriz y en caso de que alguno no esté descubierto retorna a falso, de lo contrario pasa a true
def gana5():
    if not acierto_5 == 3: 
        return False
    return True



# Reproduce el sonido de click para que empiece, modifica el juego iniciado 
def iniciar_juego5():
    global juego_iniciado_5
    #global automatico
    #pygame.mixer.Sound.play(sonido_clic)
    #automatico = pygame.MOUSEBUTTONDOWN
    ocultar_todos_los_cuadros_5()
    juego_iniciado_5 = True

# Función para dibujar los cepillos en la pantalla
def draw_points4(cepillos):
    cepillo_image = pygame.transform.scale(pygame.image.load("puntos/punto3.png"), (100, 100))
    cepillo_width, cepillo_height = cepillo_image.get_size()
    x_offset = 10  # Ajusta la posición x donde quieres que aparezcan los cepillos

    for i in range(cepillos):
        x = x_offset + i * (cepillo_width + 5)  # Espacio entre los cepillos
        y = 10  # Ajusta la posición y donde quieres que aparezcan los cepillos
        screen.blit(cepillo_image, (x, y))

def fifth_level():  
    global isGame
    global game_state
    global paused_game
    global screen_width
    global screen_height
    global timer_text_5, level_time_5, timer_active_5, aux_cronometro5
    global puede_jugar_5, reinicio, ganar5, perder5
    global acierto_5, error_5, used_time_5, unused_time_5
    global x1_5, y1_5
    global actual_matrix, ganar_reinicio5, cepillos5
    global audio_tablero
    pygame.display.set_caption('_') # Caption - Nombre de la ventana
    screen.fill(color_rosado) 
    isGame = False # Bandera que indica estado de juego activo, lo que implica que se puede pausar o no
    paused_game = False
    puede_jugar_5 = True
    reinicio = False
    aux_cronometro5 = True
    acierto_5 = 0
    error_5 = 0
    unused_time_5 = 0
    used_time_5 = 0
    cepillos5 = 3
    ######################
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(ver_tablero)
    if audio_tablero == 1:
        channel.queue(audio_instruc)
        audio_tablero = 0
    ######################
    if not ganar_reinicio5 == 0:
            x1_5 = None
            y1_5 = None

    #start_timer_active = False
    #Para que al estar en esta pantalla sea seguro que el juego se reinicia y queda en el estado inicial
    ocultar_todos_los_cuadros_5()
    ganar5 = False
    perder5 = False
    actual_matrix = 4
    image_matrix = matrix_level[actual_matrix]
    rows = len(image_matrix)
    cols = len(image_matrix[0])
    image_width = image_matrix[0][0].get_width()
    image_height = image_matrix[0][0].get_height()
    padding_x = (screen_width - (cols * image_width)) // (cols + 1)
    padding_y = (screen_height - (rows * image_height)) // (rows + 1)
    timer_rect_5 = timer_text_5.get_rect(center = ((screen_width/2),(screen_height/2))) # Centro de la pantalla: center = screen.get_rect().center
    

    for i in range(rows):
        for j in range(cols):
            x = padding_x + j * (image_width + padding_x)
            y = padding_y + i * (image_height + padding_y)
            screen.blit(image_matrix[i][j], (x, y))
            #center_text(first_level_text,100) # Texto
            screen.blit(timer_text_5, timer_rect_5) 
    
    if not timer_active_5 and game_state == 'fifth_level':
        level_time_5 = 20 # 20s
        pygame.time.set_timer(timer_event_5, 1000) # set_timer crea una acción cada 1s
        timer_active_5 = True

    return (isGame, paused_game, game_state, next_window, back_window, 
            timer_text_5, level_time_5,  puede_jugar_5, reinicio, ganar5, perder5, timer_active_5, 
            x1_5, y1_5, aux_cronometro5, acierto_5, error_5, used_time_5, unused_time_5, cepillos5)



def Ffth_level():
    global isGame
    global game_state
    global paused_game
    global segundos_mostrar_pieza5
    global cuadros5
    global imagen_oculta5
    global puede_jugar_5
    global ultimos_segundos_5
    global x1_5, y1_5, posX, posY
    global reinicio, ret_intro, cont_game, next_window, back_window
    global timer_font_5, start_time_5, start_timer_text_5, start_timer_event_5, start_timer_active_5
    global prueba5, acierto_5, error_5, ganar5, aux_cronometro5, perder5
    global cepillos5
    global ganar_reinicio5, cepillos5
    global s_wrong5_1, s_wrong5_2, s_wrong5_3, sn_wrong5_1, sn_wrong5_2, sn_wrong5_3
    #pygame.mouse.set_visible(True)# Hacer visible el cursor   

    pygame.display.set_caption('Ffth_level') # Caption - Nombre de la ventana
    screen.fill(color_rosado) 
    isGame = True # Bandera que indica estado de juego activo, lo que implica que se puede pausar
    ret_intro = False
    cont_game = False
    reinicio = False
    next_window = False
    back_window = False

    medida_cuadro_h = screen_width/len(cuadros5[0])  # Medida de la imagen en pixeles
    medida_cuadro_v = screen_height/len(cuadros5) # Medida de la imagen en pixeles

    timer_rect5 = start_timer_text_5.get_rect(center = ((screen_width/2),(screen_height/2)))
    if not start_timer_active_5 and game_state == 'Ffth_level':
        start_time_5 = 0
        pygame.time.set_timer(start_timer_event_5, 1000)
        start_timer_active_5 = True

    ahora = int(time.time())
    # Y aquí usamos la bandera del tiempo, de nuevo. Si los segundos actuales menos los segundos
    # en los que se empezó el ocultamiento son mayores a los segundos en los que se muestra la pieza, entonces
    # se ocultan las dos tarjetas y se reinician las banderas
    if ultimos_segundos_5 is not None and ahora - ultimos_segundos_5 >= segundos_mostrar_pieza5:
        cuadros5[y1_5][x1_5].mostrar5 = False
        #cuadros2[y2_2][x2_2].mostrar2 = False
        x1_5 = None
        y1_5 = None
        #x2_2 = None
        #y2_2 = None
        ultimos_segundos_5 = None
        # En este momento el usuario ya puede hacer clic de nuevo pues las imágenes ya estarán ocultas
        puede_jugar_5 = True

    


    if not ganar_reinicio5 == 0:
        x1_5 = None
        y1_5 = None



    # Hacer toda la pantalla blanca
    screen.fill(color_rosado)
    # Banderas para saber en dónde dibujar las imágenes
    cuadros_rows = len(cuadros5)
    cuadros_cols = len(cuadros5[0])
    image_cuadros = cuadros5[0][0].imagen_real5
    image_cuadros_width = image_cuadros.get_width()
    image_cuadros_height = image_cuadros.get_height()
    x_offset = (screen_width - (cuadros_cols*image_cuadros_width))//(cuadros_cols + 1)
    y_offset = (screen_height - (cuadros_rows*image_cuadros_height))//(cuadros_rows + 1)

    y =  y_offset
    # Recorrer los cuadros
    for fila in cuadros5:
        x = x_offset
        for cuadro in fila:
            """
            Si está descubierto o se debe mostrar, dibujamos la imagen real. Si no,
            dibujamos la imagen oculta
            """
            if cuadro.descubierto5 or cuadro.mostrar5:
                screen.blit(cuadro.imagen_real5, (x, y))
                screen.blit(start_timer_text_5, timer_rect5)

            else:
                screen.blit(imagen_oculta5, (x, y))
                screen.blit(start_timer_text_5, timer_rect5)


            x += medida_cuadro_h
        y += medida_cuadro_v

    draw_points4(cepillos5)
    

    
    if prueba5 == True: 
        """
        xAbsoluto e yAbsoluto son las coordenadas de la pantalla en donde se hizo
        clic. PyGame no ofrece detección de clic en imagen, por ejemplo. Así que
        se deben hacer ciertos trucos
        """
        # Si el click fue sobre el botón y el juego no se ha iniciado, entonces iniciamos el juego
        xAbsoluto = posX
        yAbsoluto = posY
        #if boton.collidepoint(event.pos):
        #   if not juego_iniciado:
        #      iniciar_juego()

        #else:
            # Si no hay juego iniciado, ignoramos el clic
        
        if juego_iniciado_5:
            iniciar_juego5()
            return
        
        x_rel = xAbsoluto - x_offset 
        y_rel = yAbsoluto - y_offset 
        
        x_cuadro = math.floor(x_rel / medida_cuadro_h)
        y_cuadro = math.floor(y_rel / medida_cuadro_v)
        
        # Primero lo primero. Si  ya está mostrada o descubierta, no hacemos nada
        if 0 <= x_cuadro < cuadros_cols and 0 <= y_cuadro < cuadros_rows:
            cuadro = cuadros5[y_cuadro][x_cuadro]
            if cuadro.mostrar5 or cuadro.descubierto5:
                # continue ignora lo de abajo y deja que el ciclo siga
                return
            # Si es la primera vez que tocan la imagen (es decir, no están buscando el par de otra, sino apenas
            # están descubriendo la primera)

            if x1_5 is None and y1_5 is None:# or acierto_2 == 1:
                # Entonces la actual es en la que acaban de dar clic, la mostramos
                x1_5 = x_cuadro
                y1_5 = y_cuadro
                cuadros5[y1_5][x1_5].mostrar5 = True
                pygame.mixer.Sound.play(sonido_voltear)  
                
            cuadro1 = cuadros5[y1_5][x1_5]
            if cuadro1.fuente_imagen5 == "IMG_5L/quinto.png":
                cuadros5[y1_5][x1_5].descubierto5 = True
                acierto_5 = acierto_5 + 1                    
                pygame.mixer.Sound.play(sonido_clic) 
                ganar_reinicio5 = 1
            if not cuadro1.fuente_imagen5 == "IMG_5L/quinto.png":
                if cuadro1.fuente_imagen5 == "IMG_5L/wrong5_1.png":
                    if s_wrong5_1 == 1:
                        pygame.mixer.Sound.play(sn_wrong5_1)
                        s_wrong5_1 = 0
                if cuadro1.fuente_imagen5 == "IMG_5L/wrong5_2.png":
                    if s_wrong5_2 == 1:
                        pygame.mixer.Sound.play(sn_wrong5_2)
                        s_wrong5_2 = 0
                if cuadro1.fuente_imagen5 == "IMG_5L/wrong5_3.png":
                    if s_wrong5_3 == 1:
                        pygame.mixer.Sound.play(sn_wrong5_3)
                        s_wrong5_3 = 0
                s_wrong5_1 = 1
                s_wrong5_2 = 1
                s_wrong5_3 = 1
                error_5 = error_5 + 1 
                ultimos_segundos_5 = int(time.time())
                ganar_reinicio5 = 0
                cepillos5 = cepillos5 -1
            comprobar_si_gana5()
                
          
            if ganar5:
                game_state = 'recompensa_5'#imagen que diga que ganó  y siguiente nivel o cosa 
            if perder5:
                game_state = 'reflection_5'
            prueba5 = False  
        


    if paused_game == True: # and juegos == True: # PANTALLA DE PAUSA
            game_state = 'Pausado'
            isGame = False
        
    return (isGame, paused_game, game_state, back_window, reinicio, ret_intro, cont_game, 
            prueba5, acierto_5, error_5, ganar5, aux_cronometro5, perder5, puede_jugar_5, ganar_reinicio5, cepillos5,
            s_wrong5_1, s_wrong5_2, s_wrong5_3)

def recompensa_5():
    global game_state
    global isGame
    isGame = False
    pygame.display.set_caption('Ganador5') # Caption - Nombre de la ventana
    instruc = 'VIDEOS/ganar_4.mp4'
    vel = 20
    pygame.mixer.Sound.play(completed)
    reproducir_video(instruc,vel)
    game_state = 'completed_5'
    return game_state

def completed_5():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window
    global reinicio
    global puede_jugar_5
    global ganar5, perder5, x1_5,y1_5
    global acierto_5, error_5, unused_time_5, used_time_5
    global ganar_reinicio5
    global audio_resultados
    
    pygame.display.set_caption('Completo nivel 5') # Caption - Nombre de la ventana
    screen.blit(fondo_resultados, (0,0)) # Función que dibuja el fondo
    correct_text = font.render(str(acierto_5), True, color_black)
    mistake_text = font.render(str(error_5), True, color_black)
    used_time_text = font.render( str(used_time_5), True, color_black)
    unused_time_text = font.render(str(unused_time_5), True, color_black)
    
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(sonido_resultados)
    if audio_resultados == 1:
        channel.queue(audio_instruc)
        audio_resultados = 0

    screen.blit(correct_text, ((screen_width//1.91), (screen_height//3.55)))
    screen.blit(mistake_text, ((screen_width//1.993), (screen_height//2.59)))
    screen.blit(used_time_text, ((screen_width//1.597), (screen_height//2.077)))
    screen.blit(unused_time_text, ((screen_width//1.597), (screen_height//1.717)))

    paused_game = False


    if reinicio == True:
        puede_jugar_5 = True
        ocultar_todos_los_cuadros_5()
        game_state = 'fifthcard'######CAMBIAR
        reinicio = False
        ganar5 = False
        perder5 =  False
        back_window = False
        next_window = False
        #aux_cronometro = True 
        acierto_5 = 0
        error_5 = 0
        unused_time_5 = 0
        used_time_5 = 0
        #x1_2 = None
        #y1_2 = None
        ganar_reinicio5 +=1
        channel.stop()
        audio_resultados = 1


    if next_window == True: # Tecla n oprimida
        game_state = 'sixthcard'
        next_window = False
        channel.stop()
        audio_resultados = 1
        

    if back_window == True: # Tecla b oprimida
        paused_game = False 
        back_window = False
        open_game = False
        ganar_reinicio5 +=1
        channel.stop()
        audio_resultados = 1
    
    isGame = False # False porque no se encuentra dentro de un juego    

    return (game_state, paused_game, isGame, open_game, next_window, back_window, reinicio, 
            puede_jugar_5, ganar5,  acierto_5, error_5, unused_time_5, used_time_5, perder5, x1_5, y1_5, ganar_reinicio5)

def reflection_5():
    global game_state
    global isGame, used_time_5, time_limit_5
    isGame = False
    pygame.display.set_caption('Perder5') # Caption - Nombre de la ventana
    if used_time_5 == time_limit_5:
        instruc = 'VIDEOS/perder_tiempo.mp4'
        pygame.mixer.Sound.play(tiempo_agotado)
    else:
        instruc = 'VIDEOS/perder_puntos.mp4'
        pygame.mixer.Sound.play(puntos_agotados)
    vel = 20
    reproducir_video(instruc,vel)
    game_state = 'uncompleted_5'
    return game_state

def uncompleted_5():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window
    global reinicio
    global puede_jugar_5
    global ganar5, perder5
    global aux_cronometro5
    global acierto_5, error_5, unused_time_5, used_time_5, start_time_5, x1_5, y1_5
    global ganar_reinicio5
    global audio_resultados
    
    pygame.display.set_caption('No completo nivel 5') # Caption - Nombre de la ventana
    screen.blit(fondo_resultados, (0,0)) # Función que dibuja el fondo
    
    
    correct_text = font.render(str(acierto_5), True, color_black)
    mistake_text = font.render(str(error_5), True, color_black)
    used_time_text = font.render(str(used_time_5), True, color_black)
    unused_time_text = font.render(str(unused_time_5), True, color_black)
    
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(sonido_resultados)
    if audio_resultados == 1:
        channel.queue(audio_instruc)
        audio_resultados = 0

    screen.blit(correct_text, ((screen_width//1.91), (screen_height//3.55)))
    screen.blit(mistake_text, ((screen_width//1.993), (screen_height//2.59)))
    screen.blit(used_time_text, ((screen_width//1.597), (screen_height//2.077)))
    screen.blit(unused_time_text, ((screen_width//1.597), (screen_height//1.717)))

    paused_game = False

    if reinicio == True:
        puede_jugar_5 = True
        ocultar_todos_los_cuadros_5()
        game_state = 'fifthcard'##### CAMBIAR
        reinicio = False
        ganar5 = False
        perder5 = False
        back_window = False
        next_window = False 
        aux_cronometro5 = True
        acierto_5 = 0
        error_5 = 0
        unused_time_5 = 0
        used_time_5 = 0
        ganar_reinicio5 = 0
        channel.stop()
        audio_resultados = 1


    if next_window == True: # Tecla n oprimida
        game_state = 'sixthcard'
        next_window = False
        channel.stop()
        audio_resultados = 1

    if back_window == True: # Tecla b oprimida
        paused_game = False 
        back_window = False
        open_game = False
        ganar_reinicio5 = 0
        channel.stop()
        audio_resultados = 1
    
    isGame = False # False porque no se encuentra dentro de un juego    

    return (game_state, paused_game, isGame, open_game, next_window, back_window, reinicio, 
            puede_jugar_5, ganar5, aux_cronometro5, acierto_5, error_5, unused_time_5, used_time_5, x1_5, y1_5, ganar_reinicio5)

####################################### Sexto Nivel ################################################
def ocultar_todos_los_cuadros_6():
    for fila in cuadros6:
        for cuadro in fila:
            cuadro.mostrar6 = False
            cuadro.descubierto6 = False

# Determina si se gana, reinicia el juego y suena la pista correspondiente
def comprobar_si_gana6():
    global acierto_6, used_time_6, unused_time_6
    global game_state
    global ganar6, juego_iniciado_6, time_limit_6, perder6
    global error_6, ganar_reinicio6

    if gana6():
        used_time_6 =  start_time_6
        unused_time_6 =  time_limit_6 - used_time_6
        ganar6 = True
        juego_iniciado_6 = False

    if error_6 == 3 or used_time_6 == time_limit_6:
        used_time_6 =  start_time_6
        unused_time_6 =  time_limit_6 - used_time_6
        perder6 = True
        juego_iniciado_6 = False
        ganar_reinicio6 = 0

    return acierto_6, game_state, ganar6, juego_iniciado_6, perder6, error_6, ganar_reinicio6
        
        
# Regresa False si al menos un cuadro NO está descubierto. True en caso de que absolutamente todos estén descubiertos
# Recorre todas las filas de la matriz y en caso de que alguno no esté descubierto retorna a falso, de lo contrario pasa a true
def gana6():
    if not acierto_6 == 3: 
        return False
    return True



# Reproduce el sonido de click para que empiece, modifica el juego iniciado 
def iniciar_juego6():
    global juego_iniciado_6
    #global automatico
    #pygame.mixer.Sound.play(sonido_clic)
    #automatico = pygame.MOUSEBUTTONDOWN
    ocultar_todos_los_cuadros_6()
    juego_iniciado_6 = True

# Función para dibujar los cepillos en la pantalla
def draw_points5(cepillos):
    cepillo_image = pygame.transform.scale(pygame.image.load("puntos/punto1.png"), (100, 100))
    cepillo_width, cepillo_height = cepillo_image.get_size()
    x_offset = 10  # Ajusta la posición x donde quieres que aparezcan los cepillos

    for i in range(cepillos):
        x = x_offset + i * (cepillo_width + 5)  # Espacio entre los cepillos
        y = 10  # Ajusta la posición y donde quieres que aparezcan los cepillos
        screen.blit(cepillo_image, (x, y))

def sixth_level():  
    global isGame
    global game_state
    global paused_game
    global screen_width
    global screen_height
    global timer_text_6, level_time_6, timer_active_6, aux_cronometro6
    global puede_jugar_6, reinicio, ganar6, perder6
    global acierto_6, error_6, used_time_6, unused_time_6
    global x1_6, y1_6
    global actual_matrix, ganar_reinicio6, cepillos6
    global audio_tablero
    pygame.display.set_caption('_') # Caption - Nombre de la ventana
    screen.fill(color_rosado) 
    isGame = False # Bandera que indica estado de juego activo, lo que implica que se puede pausar o no
    paused_game = False
    puede_jugar_6 = True
    reinicio = False
    aux_cronometro6 = True
    acierto_6 = 0
    error_6 = 0
    unused_time_6 = 0
    used_time_6 = 0
    cepillos6 = 3

    ######################
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(ver_tablero)
    if audio_tablero == 1:
        channel.queue(audio_instruc)
        audio_tablero = 0
    ######################

    if not ganar_reinicio6 == 0:
            x1_6 = None
            y1_6 = None

    #start_timer_active = False
    #Para que al estar en esta pantalla sea seguro que el juego se reinicia y queda en el estado inicial
    ocultar_todos_los_cuadros_6()
    ganar6 = False
    perder6 = False
    actual_matrix = 5
    image_matrix = matrix_level[actual_matrix]
    rows = len(image_matrix)
    cols = len(image_matrix[0])
    image_width = image_matrix[0][0].get_width()
    image_height = image_matrix[0][0].get_height()
    padding_x = (screen_width - (cols * image_width)) // (cols + 1)
    padding_y = (screen_height - (rows * image_height)) // (rows + 1)
    timer_rect_6 = timer_text_6.get_rect(center = ((screen_width/2),(screen_height/2))) # Centro de la pantalla: center = screen.get_rect().center
    

    for i in range(rows):
        for j in range(cols):
            x = padding_x + j * (image_width + padding_x)
            y = padding_y + i * (image_height + padding_y)
            screen.blit(image_matrix[i][j], (x, y))
            #center_text(first_level_text,100) # Texto
            screen.blit(timer_text_6, timer_rect_6) 
    
    if not timer_active_6 and game_state == 'sixth_level':
        level_time_6 = 20 # 20s
        pygame.time.set_timer(timer_event_6, 1000) # set_timer crea una acción cada 1s
        timer_active_6 = True

    return (isGame, paused_game, game_state, next_window, back_window, 
            timer_text_6, level_time_6,  puede_jugar_6, reinicio, ganar6, perder6, timer_active_6, 
            x1_6, y1_6, aux_cronometro6, acierto_6, error_6, used_time_6, unused_time_6, cepillos6)



def Sxth_level():
    global isGame
    global game_state
    global paused_game
    global segundos_mostrar_pieza6
    global cuadros6
    global imagen_oculta6
    global puede_jugar_6
    global ultimos_segundos_6
    global x1_6, y1_6, posX, posY
    global reinicio, ret_intro, cont_game, next_window, back_window
    global timer_font_6, start_time_6, start_timer_text_6, start_timer_event_6, start_timer_active_6
    global prueba6, acierto_6, error_6, ganar6, aux_cronometro6, perder6
    global cepillos6
    global ganar_reinicio6, cepillos6
    global s_wrong6_1, s_wrong6_2, s_wrong6_3, s_wrong6_4, s_wrong6_5
    global sn_wrong6_1, sn_wrong6_2, sn_wrong6_3, sn_wrong6_4, sn_wrong6_5
    #pygame.mouse.set_visible(True)# Hacer visible el cursor   

    pygame.display.set_caption('Sxth_level') # Caption - Nombre de la ventana
    screen.fill(color_amarillo) 
    isGame = True # Bandera que indica estado de juego activo, lo que implica que se puede pausar
    ret_intro = False
    cont_game = False
    reinicio = False
    next_window = False
    back_window = False

    medida_cuadro_h = screen_width/len(cuadros6[0])  # Medida de la imagen en pixeles
    medida_cuadro_v = screen_height/len(cuadros6) # Medida de la imagen en pixeles

    timer_rect6 = start_timer_text_6.get_rect(center = ((screen_width/2),(screen_height/2)))
    if not start_timer_active_6 and game_state == 'Sxth_level':
        start_time_6 = 0
        pygame.time.set_timer(start_timer_event_6, 1000)
        start_timer_active_6 = True

    ahora = int(time.time())
    # Y aquí usamos la bandera del tiempo, de nuevo. Si los segundos actuales menos los segundos
    # en los que se empezó el ocultamiento son mayores a los segundos en los que se muestra la pieza, entonces
    # se ocultan las dos tarjetas y se reinician las banderas
    if ultimos_segundos_6 is not None and ahora - ultimos_segundos_6 >= segundos_mostrar_pieza6:
        cuadros6[y1_6][x1_6].mostrar6 = False
        
        #cuadros2[y2_2][x2_2].mostrar2 = False
        x1_6 = None
        y1_6 = None
        #x2_2 = None
        #y2_2 = None
        ultimos_segundos_6 = None
        # En este momento el usuario ya puede hacer clic de nuevo pues las imágenes ya estarán ocultas
        puede_jugar_6 = True

    if not ganar_reinicio6 == 0:
        x1_6 = None
        y1_6 = None



    # Hacer toda la pantalla blanca
    screen.fill(color_rosado)
    # Banderas para saber en dónde dibujar las imágenes
    cuadros_rows = len(cuadros6)
    cuadros_cols = len(cuadros6[0])
    image_cuadros = cuadros6[0][0].imagen_real6
    image_cuadros_width = image_cuadros.get_width()
    image_cuadros_height = image_cuadros.get_height()
    x_offset = (screen_width - (cuadros_cols*image_cuadros_width))//(cuadros_cols + 1)
    y_offset = (screen_height - (cuadros_rows*image_cuadros_height))//(cuadros_rows + 1)

    y =  y_offset
    # Recorrer los cuadros
    for fila in cuadros6:
        x = x_offset
        for cuadro in fila:
            """
            Si está descubierto o se debe mostrar, dibujamos la imagen real. Si no,
            dibujamos la imagen oculta
            """
            if cuadro.descubierto6 or cuadro.mostrar6:
                screen.blit(cuadro.imagen_real6, (x, y))
                screen.blit(start_timer_text_6, timer_rect6)
                

            else:
                screen.blit(imagen_oculta6, (x, y))
                screen.blit(start_timer_text_6, timer_rect6)


            x += medida_cuadro_h
        y += medida_cuadro_v

    draw_points5(cepillos6)
    
    if prueba6 == True: 
        """
        xAbsoluto e yAbsoluto son las coordenadas de la pantalla en donde se hizo
        clic. PyGame no ofrece detección de clic en imagen, por ejemplo. Así que
        se deben hacer ciertos trucos
        """
        # Si el click fue sobre el botón y el juego no se ha iniciado, entonces iniciamos el juego
        xAbsoluto = posX
        yAbsoluto = posY
        #if boton.collidepoint(event.pos):
        #   if not juego_iniciado:
        #      iniciar_juego()

        #else:
            # Si no hay juego iniciado, ignoramos el clic
        
        if juego_iniciado_6:
            iniciar_juego6()
            return
        
        x_rel = xAbsoluto - x_offset 
        y_rel = yAbsoluto - y_offset 
        
        x_cuadro = math.floor(x_rel / medida_cuadro_h)
        y_cuadro = math.floor(y_rel / medida_cuadro_v)
        
        # Primero lo primero. Si  ya está mostrada o descubierta, no hacemos nada
        if 0 <= x_cuadro < cuadros_cols and 0 <= y_cuadro < cuadros_rows:
            cuadro = cuadros6[y_cuadro][x_cuadro]
            if cuadro.mostrar6 or cuadro.descubierto6:
                # continue ignora lo de abajo y deja que el ciclo siga
                return
            # Si es la primera vez que tocan la imagen (es decir, no están buscando el par de otra, sino apenas
            # están descubriendo la primera)
            if x1_6 is None and y1_6 is None:# or acierto_2 == 1:
                # Entonces la actual es en la que acaban de dar clic, la mostramos
                x1_6 = x_cuadro
                y1_6 = y_cuadro
                cuadros6[y1_6][x1_6].mostrar6 = True
                pygame.mixer.Sound.play(sonido_voltear)
            
            cuadro1 = cuadros6[y1_6][x1_6]
            if cuadro1.fuente_imagen6 == "IMG_6L/sexto.png":
                cuadros6[y1_6][x1_6].descubierto6 = True
                acierto_6 = acierto_6 + 1                    
                pygame.mixer.Sound.play(sonido_clic) 
                ganar_reinicio6 = 1
            if not cuadro1.fuente_imagen6 == "IMG_6L/sexto.png":
                if cuadro1.fuente_imagen6 == "IMG_6L/wrong6_1.png":
                    if s_wrong6_1 == 1:
                        pygame.mixer.Sound.play(sn_wrong6_1)
                        s_wrong6_1 = 0
                if cuadro1.fuente_imagen6 == "IMG_6L/wrong6_2.png":
                    if s_wrong6_2 == 1:
                        pygame.mixer.Sound.play(sn_wrong6_2)
                        s_wrong6_2 = 0
                if cuadro1.fuente_imagen6 == "IMG_6L/wrong6_3.png":
                    if s_wrong6_3 == 1:
                        pygame.mixer.Sound.play(sn_wrong6_3)
                        s_wrong6_3 = 0
                if cuadro1.fuente_imagen6 == "IMG_6L/wrong6_4.png":
                    if s_wrong6_4 == 1:
                        pygame.mixer.Sound.play(sn_wrong6_4)
                        s_wrong6_4 = 0
                if cuadro1.fuente_imagen6 == "IMG_6L/wrong6_5.png":
                    if s_wrong6_5 == 1:
                        pygame.mixer.Sound.play(sn_wrong6_5)
                        s_wrong6_5 = 0
                s_wrong6_1 = 1
                s_wrong6_2 = 1
                s_wrong6_3 = 1
                s_wrong6_4 = 1
                s_wrong6_5 = 1
                error_6 = error_6 + 1 
                ultimos_segundos_6 = int(time.time())
                ganar_reinicio6 = 0
                cepillos6 = cepillos6 -1
            comprobar_si_gana6()
                
          
            if ganar6:
                game_state = 'recompensa_6'#imagen que diga que ganó  y siguiente nivel o cosa 
            if perder6:
                game_state = 'reflection_6'
            prueba6 = False  
            


    if paused_game == True: # and juegos == True: # PANTALLA DE PAUSA
        game_state = 'Pausado'
        isGame = False
    return (isGame, paused_game, game_state, back_window, reinicio, ret_intro, cont_game, 
            prueba6, acierto_6, error_6, ganar6, aux_cronometro6, perder6, puede_jugar_6, ganar_reinicio6, cepillos6,
            s_wrong6_1, s_wrong6_2, s_wrong6_3, s_wrong6_4, s_wrong6_5)

def recompensa_6():
    global game_state
    global isGame
    isGame = False
    pygame.display.set_caption('Ganador6') # Caption - Nombre de la ventana
    instruc = 'VIDEOS/ganar_5.mp4'
    vel = 20
    pygame.mixer.Sound.play(completed)
    reproducir_video(instruc,vel)
    game_state = 'completed_6'
    return game_state

def completed_6():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window
    global reinicio
    global puede_jugar_6
    global ganar6, perder6, x1_6,y1_6
    #global aux_cronometro
    global acierto_6, error_6, unused_time_6, used_time_6
    global ganar_reinicio6
    global audio_resultados
    
    pygame.display.set_caption('Completo nivel 6') # Caption - Nombre de la ventana
    screen.blit(fondo_resultados, (0,0)) # Función que dibuja el fondo
    correct_text = font.render(str(acierto_6), True, color_black)
    mistake_text = font.render(str(error_6), True, color_black)
    used_time_text = font.render( str(used_time_6), True, color_black)
    unused_time_text = font.render(str(unused_time_6), True, color_black)
    
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(sonido_resultados)
    if audio_resultados == 1:
        channel.queue(audio_instruc)
        audio_resultados = 0

    screen.blit(correct_text, ((screen_width//1.91), (screen_height//3.55)))
    screen.blit(mistake_text, ((screen_width//1.993), (screen_height//2.59)))
    screen.blit(used_time_text, ((screen_width//1.597), (screen_height//2.077)))
    screen.blit(unused_time_text, ((screen_width//1.597), (screen_height//1.717)))

    paused_game = False


    if reinicio == True:
        puede_jugar_6 = True
        ocultar_todos_los_cuadros_6()
        game_state = 'sixthcard'######CAMBIAR
        reinicio = False
        ganar6 = False
        perder6 =  False
        back_window = False
        next_window = False
        #aux_cronometro = True 
        acierto_6 = 0
        error_6 = 0
        unused_time_6 = 0
        used_time_6 = 0
        #x1_2 = None
        #y1_2 = None
        ganar_reinicio6 +=1
        channel.stop()
        audio_resultados = 1

    if next_window == True: # Tecla n oprimida
        game_state = 'video_ubicar_cepillo'
        next_window = False
        channel.stop()
        audio_resultados = 1
        
        

    if back_window == True: # Tecla b oprimida
        paused_game = False 
        back_window = False
        open_game = False
        ganar_reinicio6 +=1
        channel.stop()
        audio_resultados = 1
    
    isGame = False # False porque no se encuentra dentro de un juego    

    return (game_state, paused_game, isGame, open_game, next_window, back_window, reinicio, 
            puede_jugar_6, ganar6,  acierto_6, error_6, unused_time_6, used_time_6, perder6, x1_6, y1_6, ganar_reinicio6)

def reflection_6():
    global game_state
    global isGame, used_time_6, time_limit_6
    isGame = False
    pygame.display.set_caption('Perder6') # Caption - Nombre de la ventana
    if used_time_6 == time_limit_6:
        instruc = 'VIDEOS/perder_tiempo.mp4'
        pygame.mixer.Sound.play(tiempo_agotado)
    else:
        instruc = 'VIDEOS/perder_puntos.mp4'
        pygame.mixer.Sound.play(puntos_agotados)
    vel = 20
    reproducir_video(instruc,vel)
    game_state = 'uncompleted_6'
    return game_state

def uncompleted_6():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window
    global reinicio
    global puede_jugar_6
    global ganar6, perder6
    global aux_cronometro6
    global acierto_6, error_6, unused_time_6, used_time_6, start_time_6, x1_6, y1_6
    global ganar_reinicio6
    global audio_resultados
    
    pygame.display.set_caption('No completo nivel 6') # Caption - Nombre de la ventana
    screen.blit(fondo_resultados, (0,0)) # Función que dibuja el fondo
    
    
    correct_text = font.render(str(acierto_6), True, color_black)
    mistake_text = font.render(str(error_6), True, color_black)
    used_time_text = font.render(str(used_time_6), True, color_black)
    unused_time_text = font.render(str(unused_time_6), True, color_black)
    
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(sonido_resultados)
    if audio_resultados == 1:
        channel.queue(audio_instruc)
        audio_resultados = 0

    screen.blit(correct_text, ((screen_width//1.91), (screen_height//3.55)))
    screen.blit(mistake_text, ((screen_width//1.993), (screen_height//2.59)))
    screen.blit(used_time_text, ((screen_width//1.597), (screen_height//2.077)))
    screen.blit(unused_time_text, ((screen_width//1.597), (screen_height//1.717)))

    paused_game = False

    if reinicio == True:
        puede_jugar_6 = True
        ocultar_todos_los_cuadros_6()
        game_state = 'sixthcard'##### CAMBIAR
        reinicio = False
        ganar6 = False
        perder6 = False
        back_window = False
        next_window = False 
        aux_cronometro6 = True
        acierto_6 = 0
        error_6 = 0
        unused_time_6 = 0
        used_time_6 = 0
        ganar_reinicio6 = 0
        channel.stop()
        audio_resultados = 1


    if next_window == True: # Tecla n oprimida
        game_state = 'video_ubicar_cepillo'
        next_window = False
        channel.stop()
        audio_resultados = 1

    if back_window == True: # Tecla b oprimida
        paused_game = False 
        back_window = False
        open_game = False
        ganar_reinicio6 = 0
        channel.stop()
        audio_resultados = 1
         
    
    isGame = False # False porque no se encuentra dentro de un juego    

    return (game_state, paused_game, isGame, open_game, next_window, back_window, reinicio, 
            puede_jugar_6, ganar6, aux_cronometro6, acierto_6, error_6, unused_time_6, used_time_6, x1_6, y1_6, ganar_reinicio6)
####################################### Septimo Nivel ##############################################
def ocultar_todos_los_cuadros_7():
    for fila in cuadros7:
        for cuadro in fila:
            cuadro.mostrar7 = False
            cuadro.descubierto7 = False

# Determina si se gana, reinicia el juego y suena la pista correspondiente
def comprobar_si_gana7():
    global acierto_7, used_time_7, unused_time_7
    global game_state
    global ganar7, juego_iniciado_7, time_limit_7, perder7
    global error_7, ganar_reinicio7

    if gana7():
        used_time_7 =  start_time_7
        unused_time_7 =  time_limit_7 - used_time_7
        ganar7 = True
        juego_iniciado_7 = False

    if error_7 == 3 or used_time_7 == time_limit_7:
        used_time_7 =  start_time_7
        unused_time_7 =  time_limit_7 - used_time_7
        perder7 = True
        juego_iniciado_7 = False
        ganar_reinicio7 = 0

    return acierto_7, game_state, ganar7, juego_iniciado_7, perder7, error_7, ganar_reinicio7
        
        
# Regresa False si al menos un cuadro NO está descubierto. True en caso de que absolutamente todos estén descubiertos
# Recorre todas las filas de la matriz y en caso de que alguno no esté descubierto retorna a falso, de lo contrario pasa a true
def gana7():
    if not acierto_7 == 4: 
        return False
    return True



# Reproduce el sonido de click para que empiece, modifica el juego iniciado 
def iniciar_juego7():
    global juego_iniciado_7
    #global automatico
    #pygame.mixer.Sound.play(sonido_clic)
    #automatico = pygame.MOUSEBUTTONDOWN
    ocultar_todos_los_cuadros_7()
    juego_iniciado_7 = True

# Función para dibujar los cepillos en la pantalla
def draw_points6(cepillos):
    cepillo_image = pygame.transform.scale(pygame.image.load("puntos/punto2.png"), (100, 100))
    cepillo_width, cepillo_height = cepillo_image.get_size()
    x_offset = 10  # Ajusta la posición x donde quieres que aparezcan los cepillos

    for i in range(cepillos):
        x = x_offset + i * (cepillo_width + 5)  # Espacio entre los cepillos
        y = 10  # Ajusta la posición y donde quieres que aparezcan los cepillos
        screen.blit(cepillo_image, (x, y))

def seventh_level():  
    global isGame
    global game_state
    global paused_game
    global screen_width
    global screen_height
    global timer_text_7, level_time_7, timer_active_7, aux_cronometro7
    global puede_jugar_7, reinicio, ganar7, perder7
    global acierto_7, error_7, used_time_7, unused_time_7
    global x1_7, y1_7
    global actual_matrix, ganar_reinicio7, cepillos7
    global audio_tablero
    pygame.display.set_caption('_') # Caption - Nombre de la ventana
    screen.fill(color_azul_claro) 
    isGame = False # Bandera que indica estado de juego activo, lo que implica que se puede pausar o no
    paused_game = False
    puede_jugar_7 = True
    reinicio = False
    aux_cronometro7 = True
    acierto_7 = 0
    error_7 = 0
    unused_time_7 = 0
    used_time_7 = 0
    cepillos7 = 3
    ######################
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(ver_tablero)
    if audio_tablero == 1:
        channel.queue(audio_instruc)
        audio_tablero = 0
    ######################
    if not ganar_reinicio7 == 0:
            x1_7 = None
            y1_7 = None

    #start_timer_active = False
    #Para que al estar en esta pantalla sea seguro que el juego se reinicia y queda en el estado inicial
    ocultar_todos_los_cuadros_7()
    ganar7 = False
    perder7 = False
    actual_matrix = 6
    image_matrix = matrix_level[actual_matrix]
    rows = len(image_matrix)
    cols = len(image_matrix[0])
    image_width = image_matrix[0][0].get_width()
    image_height = image_matrix[0][0].get_height()
    padding_x = (screen_width - (cols * image_width)) // (cols + 1)
    padding_y = (screen_height - (rows * image_height)) // (rows + 1)
    timer_rect_7 = timer_text_7.get_rect(center = ((screen_width/2),(screen_height/2))) # Centro de la pantalla: center = screen.get_rect().center
    

    for i in range(rows):
        for j in range(cols):
            x = padding_x + j * (image_width + padding_x)
            y = padding_y + i * (image_height + padding_y)
            screen.blit(image_matrix[i][j], (x, y))
            #center_text(first_level_text,100) # Texto
            screen.blit(timer_text_7, timer_rect_7) 
    
    if not timer_active_7 and game_state == 'seventh_level':
        level_time_7 = 20 # 20s
        pygame.time.set_timer(timer_event_7, 1000) # set_timer crea una acción cada 1s
        timer_active_7 = True

    return (isGame, paused_game, game_state, next_window, back_window, 
            timer_text_7, level_time_7,  puede_jugar_7, reinicio, ganar7, perder7, timer_active_7, 
            x1_7, y1_7, aux_cronometro7, acierto_7, error_7, used_time_7, unused_time_7, cepillos7)



def Svnth_level():
    global isGame
    global game_state
    global paused_game
    global segundos_mostrar_pieza7
    global cuadros7
    global imagen_oculta7
    global puede_jugar_7
    global ultimos_segundos_7
    global x1_7, y1_7, posX, posY
    global reinicio, ret_intro, cont_game, next_window, back_window
    global timer_font_7, start_time_7, start_timer_text_7, start_timer_event_7, start_timer_active_7
    global prueba7, acierto_7, error_7, ganar7, aux_cronometro7, perder7
    global ganar_reinicio7, cepillos7
    global s_wrong7_1, s_wrong7_2, s_wrong7_3, s_wrong7_4
    global sn_wrong7_1, sn_wrong7_2, sn_wrong7_3, sn_wrong7_4
    #pygame.mouse.set_visible(True)# Hacer visible el cursor   

    pygame.display.set_caption('Svnth_level') # Caption - Nombre de la ventana
    screen.fill(color_azul_claro) 
    isGame = True # Bandera que indica estado de juego activo, lo que implica que se puede pausar
    ret_intro = False
    cont_game = False
    reinicio = False
    next_window = False
    back_window = False

    medida_cuadro_h = screen_width/len(cuadros7[0])  # Medida de la imagen en pixeles
    medida_cuadro_v = screen_height/len(cuadros7) # Medida de la imagen en pixeles

    timer_rect7 = start_timer_text_7.get_rect(center = ((screen_width/2),(screen_height/2)))
    if not start_timer_active_7 and game_state == 'Svnth_level':
        start_time_7 = 0
        pygame.time.set_timer(start_timer_event_7, 1000)
        start_timer_active_7 = True

    ahora = int(time.time())
    # Y aquí usamos la bandera del tiempo, de nuevo. Si los segundos actuales menos los segundos
    # en los que se empezó el ocultamiento son mayores a los segundos en los que se muestra la pieza, entonces
    # se ocultan las dos tarjetas y se reinician las banderas
    if ultimos_segundos_7 is not None and ahora - ultimos_segundos_7 >= segundos_mostrar_pieza7:
        cuadros7[y1_7][x1_7].mostrar7 = False
        
        #cuadros2[y2_2][x2_2].mostrar2 = False
        x1_7 = None
        y1_7 = None
        #x2_2 = None
        #y2_2 = None
        ultimos_segundos_7 = None
        # En este momento el usuario ya puede hacer clic de nuevo pues las imágenes ya estarán ocultas
        puede_jugar_7 = True

    if not ganar_reinicio7 == 0:
        x1_7 = None
        y1_7 = None



    # Hacer toda la pantalla blanca
    screen.fill(color_azul_claro)
    # Banderas para saber en dónde dibujar las imágenes
    cuadros_rows = len(cuadros7)
    cuadros_cols = len(cuadros7[0])
    image_cuadros = cuadros7[0][0].imagen_real7
    image_cuadros_width = image_cuadros.get_width()
    image_cuadros_height = image_cuadros.get_height()
    x_offset = (screen_width - (cuadros_cols*image_cuadros_width))//(cuadros_cols + 1)
    y_offset = (screen_height - (cuadros_rows*image_cuadros_height))//(cuadros_rows + 1)

    y =  y_offset
    # Recorrer los cuadros
    for fila in cuadros7:
        x = x_offset
        for cuadro in fila:
            """
            Si está descubierto o se debe mostrar, dibujamos la imagen real. Si no,
            dibujamos la imagen oculta
            """
            if cuadro.descubierto7 or cuadro.mostrar7:
                screen.blit(cuadro.imagen_real7, (x, y))
                screen.blit(start_timer_text_7, timer_rect7)
                

            else:
                screen.blit(imagen_oculta7, (x, y))
                screen.blit(start_timer_text_7, timer_rect7)


            x += medida_cuadro_h
        y += medida_cuadro_v

    draw_points6(cepillos7)
    
    if prueba7 == True: 
        """
        xAbsoluto e yAbsoluto son las coordenadas de la pantalla en donde se hizo
        clic. PyGame no ofrece detección de clic en imagen, por ejemplo. Así que
        se deben hacer ciertos trucos
        """
        # Si el click fue sobre el botón y el juego no se ha iniciado, entonces iniciamos el juego
        xAbsoluto = posX
        yAbsoluto = posY
        #if boton.collidepoint(event.pos):
        #   if not juego_iniciado:
        #      iniciar_juego()

        #else:
            # Si no hay juego iniciado, ignoramos el clic
        
        if juego_iniciado_7:
            iniciar_juego7()
            return
        
        x_rel = xAbsoluto - x_offset 
        y_rel = yAbsoluto - y_offset 
        
        x_cuadro = math.floor(x_rel / medida_cuadro_h)
        y_cuadro = math.floor(y_rel / medida_cuadro_v)
        
        # Primero lo primero. Si  ya está mostrada o descubierta, no hacemos nada
        if 0 <= x_cuadro < cuadros_cols and 0 <= y_cuadro < cuadros_rows:
            cuadro = cuadros7[y_cuadro][x_cuadro]
            if cuadro.mostrar7 or cuadro.descubierto7:
                # continue ignora lo de abajo y deja que el ciclo siga
                return
            # Si es la primera vez que tocan la imagen (es decir, no están buscando el par de otra, sino apenas
            # están descubriendo la primera)
            if x1_7 is None and y1_7 is None:# or acierto_2 == 1:
                # Entonces la actual es en la que acaban de dar clic, la mostramos
                x1_7 = x_cuadro
                y1_7 = y_cuadro
                cuadros7[y1_7][x1_7].mostrar7 = True
                pygame.mixer.Sound.play(sonido_voltear)
            
            cuadro1 = cuadros7[y1_7][x1_7]
            if cuadro1.fuente_imagen7 == "IMG_7L/septimo.png":
                cuadros7[y1_7][x1_7].descubierto7 = True
                acierto_7 = acierto_7 + 1                    
                pygame.mixer.Sound.play(sonido_clic) 
                ganar_reinicio7 = 1
            if not cuadro1.fuente_imagen7 == "IMG_7L/septimo.png":
                if cuadro1.fuente_imagen7 == "IMG_7L/wrong7_1.png":
                    if s_wrong7_1 == 1:
                        pygame.mixer.Sound.play(sn_wrong7_1)
                        s_wrong7_1 = 0
                if cuadro1.fuente_imagen7 == "IMG_7L/wrong7_2.png":
                    if s_wrong7_2 == 1:
                        pygame.mixer.Sound.play(sn_wrong7_2)
                        s_wrong7_2 = 0
                if cuadro1.fuente_imagen7 == "IMG_7L/wrong7_3.png":
                    if s_wrong7_3 == 1:
                        pygame.mixer.Sound.play(sn_wrong7_3)
                        s_wrong7_3 = 0
                if cuadro1.fuente_imagen7 == "IMG_7L/wrong7_4.png":
                    if s_wrong7_4 == 1:
                        pygame.mixer.Sound.play(sn_wrong7_4)
                        s_wrong7_4 = 0
                s_wrong7_1 = 1 
                s_wrong7_2 = 1  
                s_wrong7_3 = 1  
                s_wrong7_4 = 1       
                error_7 = error_7 + 1 
                ultimos_segundos_7 = int(time.time())
                ganar_reinicio7 = 0
                cepillos7 = cepillos7 -1
            comprobar_si_gana7()
                
          
            if ganar7:
                game_state = 'recompensa_7'#imagen que diga que ganó  y siguiente nivel o cosa 
            if perder7:
                game_state = 'reflection_7'
            prueba7 = False  
            


    if paused_game == True: # and juegos == True: # PANTALLA DE PAUSA
        game_state = 'Pausado'
        isGame = False
    return (isGame, paused_game, game_state, back_window, reinicio, ret_intro, cont_game, 
            prueba7, acierto_7, error_7, ganar7, aux_cronometro7, perder7, puede_jugar_7, ganar_reinicio7, cepillos7,
            s_wrong7_1, s_wrong7_2, s_wrong7_3, s_wrong7_4)

def recompensa_7():
    global game_state
    global isGame
    isGame = False
    pygame.display.set_caption('Ganador7') # Caption - Nombre de la ventana
    instruc = 'VIDEOS/ganar_6.mp4'
    vel = 20
    pygame.mixer.Sound.play(completed)
    reproducir_video(instruc,vel)
    game_state = 'completed_7'
    return game_state

def completed_7():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window
    global reinicio
    global puede_jugar_7
    global ganar7, perder7, x1_7,y1_7
    #global aux_cronometro
    global acierto_7, error_7, unused_time_7, used_time_7
    global ganar_reinicio7
    global audio_resultados
    
    pygame.display.set_caption('Completo nivel 7') # Caption - Nombre de la ventana
    screen.blit(fondo_resultados, (0,0)) # Función que dibuja el fondo
    correct_text = font.render(str(acierto_7), True, color_black)
    mistake_text = font.render(str(error_7), True, color_black)
    used_time_text = font.render( str(used_time_7), True, color_black)
    unused_time_text = font.render(str(unused_time_7), True, color_black)
    
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(sonido_resultados)
    if audio_resultados == 1:
        channel.queue(audio_instruc)
        audio_resultados = 0
    
    screen.blit(correct_text, ((screen_width//1.91), (screen_height//3.55)))
    screen.blit(mistake_text, ((screen_width//1.993), (screen_height//2.59)))
    screen.blit(used_time_text, ((screen_width//1.597), (screen_height//2.077)))
    screen.blit(unused_time_text, ((screen_width//1.597), (screen_height//1.717)))

    paused_game = False


    if reinicio == True:
        puede_jugar_7 = True
        ocultar_todos_los_cuadros_7()
        game_state = 'seventhcard'######CAMBIAR
        reinicio = False
        ganar7 = False
        perder7 =  False
        back_window = False
        next_window = False
        #aux_cronometro = True 
        acierto_7 = 0
        error_7 = 0
        unused_time_7 = 0
        used_time_7 = 0
        #x1_2 = None
        #y1_2 = None
        ganar_reinicio7 +=1
        channel.stop()
        audio_resultados = 1

    if next_window == True: # Tecla n oprimida
        game_state = 'video_cepillar_circulos'
        next_window = False
        channel.stop()
        audio_resultados = 1
        

    if back_window == True: # Tecla b oprimida
        paused_game = False 
        back_window = False
        open_game = False
        ganar_reinicio7 +=1
        channel.stop()
        audio_resultados = 1
    
    isGame = False # False porque no se encuentra dentro de un juego    

    return (game_state, paused_game, isGame, open_game, next_window, back_window, reinicio, 
            puede_jugar_7, ganar7,  acierto_7, error_7, unused_time_7, used_time_7, perder7, x1_7, y1_7, ganar_reinicio7)

def reflection_7():
    global game_state
    global isGame, used_time_7, time_limit_7
    isGame = False
    pygame.display.set_caption('Perder7') # Caption - Nombre de la ventana
    if used_time_7 == time_limit_7:
        instruc = 'VIDEOS/perder_tiempo.mp4'
        pygame.mixer.Sound.play(tiempo_agotado)
    else:
        instruc = 'VIDEOS/perder_puntos.mp4'
        pygame.mixer.Sound.play(puntos_agotados)
    vel = 20
    reproducir_video(instruc,vel)
    game_state = 'uncompleted_7'
    return game_state

def uncompleted_7():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window
    global reinicio
    global puede_jugar_7
    global ganar7, perder7
    global aux_cronometro7
    global acierto_7, error_7, unused_time_7, used_time_7, start_time_7, x1_7, y1_7
    global ganar_reinicio7
    global audio_resultados

    pygame.display.set_caption('No completo nivel 7') # Caption - Nombre de la ventana
    screen.blit(fondo_resultados, (0,0)) # Función que dibuja el fondo
    
    
    correct_text = font.render(str(acierto_7), True, color_black)
    mistake_text = font.render(str(error_7), True, color_black)
    used_time_text = font.render(str(used_time_7), True, color_black)
    unused_time_text = font.render(str(unused_time_7), True, color_black)
    
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(sonido_resultados)
    if audio_resultados == 1:
        channel.queue(audio_instruc)
        audio_resultados = 0

    screen.blit(correct_text, ((screen_width//1.91), (screen_height//3.55)))
    screen.blit(mistake_text, ((screen_width//1.993), (screen_height//2.59)))
    screen.blit(used_time_text, ((screen_width//1.597), (screen_height//2.077)))
    screen.blit(unused_time_text, ((screen_width//1.597), (screen_height//1.717)))

    paused_game = False

    if reinicio == True:
        puede_jugar_7 = True
        ocultar_todos_los_cuadros_7()
        game_state = 'seventhcard'##### CAMBIAR
        reinicio = False
        ganar7 = False
        perder7 = False
        back_window = False
        next_window = False 
        aux_cronometro7 = True
        acierto_7 = 0
        error_7 = 0
        unused_time_7 = 0
        used_time_7 = 0
        ganar_reinicio7 = 0
        channel.stop()
        audio_resultados = 1


    if next_window == True: # Tecla n oprimida
        game_state = 'video_cepillar_circulos'
        next_window = False
        channel.stop()
        audio_resultados = 1
        

    if back_window == True: # Tecla b oprimida
        paused_game = False 
        back_window = False
        open_game = False
        ganar_reinicio7 = 0
        channel.stop()
        audio_resultados = 1
    
    isGame = False # False porque no se encuentra dentro de un juego    

    return (game_state, paused_game, isGame, open_game, next_window, back_window, reinicio, 
            puede_jugar_7, ganar7, aux_cronometro7, acierto_7, error_7, unused_time_7, used_time_7, x1_7, y1_7, ganar_reinicio7)
####################################### Octavo Nivel ###############################################
def ocultar_todos_los_cuadros_8():
    for fila in cuadros8:
        for cuadro in fila:
            cuadro.mostrar8 = False
            cuadro.descubierto8 = False

# Determina si se gana, reinicia el juego y suena la pista correspondiente
def comprobar_si_gana8():
    global acierto_8, used_time_8, unused_time_8
    global game_state
    global ganar8, juego_iniciado_8, time_limit_8, perder8
    global error_8, ganar_reinicio8

    if gana8():
        used_time_8 =  start_time_8
        unused_time_8 =  time_limit_8 - used_time_8
        ganar8 = True
        juego_iniciado_8 = False

    if error_8 == 3 or used_time_8 == time_limit_8:
        used_time_8 =  start_time_8
        unused_time_8 =  time_limit_8 - used_time_8
        perder8 = True
        juego_iniciado_8 = False
        ganar_reinicio8 = 0

    return acierto_8, game_state, ganar8, juego_iniciado_8, perder8, error_8, ganar_reinicio8
        
        
# Regresa False si al menos un cuadro NO está descubierto. True en caso de que absolutamente todos estén descubiertos
# Recorre todas las filas de la matriz y en caso de que alguno no esté descubierto retorna a falso, de lo contrario pasa a true
def gana8():
    if not acierto_8 == 4: 
        return False
    return True



# Reproduce el sonido de click para que empiece, modifica el juego iniciado 
def iniciar_juego8():
    global juego_iniciado_8
    #global automatico
    #pygame.mixer.Sound.play(sonido_clic)
    #automatico = pygame.MOUSEBUTTONDOWN
    ocultar_todos_los_cuadros_8()
    juego_iniciado_8 = True

# Función para dibujar los cepillos en la pantalla
def draw_points7(cepillos):
    cepillo_image = pygame.transform.scale(pygame.image.load("puntos/punto3.png"), (100, 100))
    cepillo_width, cepillo_height = cepillo_image.get_size()
    x_offset = 10  # Ajusta la posición x donde quieres que aparezcan los cepillos

    for i in range(cepillos):
        x = x_offset + i * (cepillo_width + 5)  # Espacio entre los cepillos
        y = 10  # Ajusta la posición y donde quieres que aparezcan los cepillos
        screen.blit(cepillo_image, (x, y))

def eighth_level():  
    global isGame
    global game_state
    global paused_game
    global screen_width
    global screen_height
    global timer_text_8, level_time_8, timer_active_8, aux_cronometro8
    global puede_jugar_8, reinicio, ganar8, perder8
    global acierto_8, error_8, used_time_8, unused_time_8
    global x1_8, y1_8
    global actual_matrix, ganar_reinicio8, cepillos8
    global audio_tablero
    pygame.display.set_caption('_') # Caption - Nombre de la ventana
    screen.fill(color_white) 
    isGame = False # Bandera que indica estado de juego activo, lo que implica que se puede pausar o no
    paused_game = False
    puede_jugar_8 = True
    reinicio = False
    aux_cronometro8 = True
    acierto_8 = 0
    error_8 = 0
    unused_time_8 = 0
    used_time_8 = 0
    cepillos8 = 3
    ######################
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(ver_tablero)
    if audio_tablero == 1:
        channel.queue(audio_instruc)
        audio_tablero = 0
    ######################
    if not ganar_reinicio8 == 0:
            x1_8 = None
            y1_8 = None

    #start_timer_active = False
    #Para que al estar en esta pantalla sea seguro que el juego se reinicia y queda en el estado inicial
    ocultar_todos_los_cuadros_8()
    ganar8 = False
    perder8 = False
    actual_matrix = 7
    image_matrix = matrix_level[actual_matrix]
    rows = len(image_matrix)
    cols = len(image_matrix[0])
    image_width = image_matrix[0][0].get_width()
    image_height = image_matrix[0][0].get_height()
    padding_x = (screen_width - (cols * image_width)) // (cols + 1)
    padding_y = (screen_height - (rows * image_height)) // (rows + 1)
    timer_rect_8 = timer_text_8.get_rect(center = ((screen_width/2),(screen_height/2))) # Centro de la pantalla: center = screen.get_rect().center
    

    for i in range(rows):
        for j in range(cols):
            x = padding_x + j * (image_width + padding_x)
            y = padding_y + i * (image_height + padding_y)
            screen.blit(image_matrix[i][j], (x, y))
            #center_text(first_level_text,100) # Texto
            screen.blit(timer_text_8, timer_rect_8) 
    
    if not timer_active_8 and game_state == 'eighth_level':
        level_time_8 = 20 # 20s
        pygame.time.set_timer(timer_event_8, 1000) # set_timer crea una acción cada 1s
        timer_active_8 = True

    return (isGame, paused_game, game_state, next_window, back_window, 
            timer_text_8, level_time_8,  puede_jugar_8, reinicio, ganar8, perder8, timer_active_8, 
            x1_8, y1_8, aux_cronometro8, acierto_8, error_8, used_time_8, unused_time_8, cepillos8)



def Eighth_level():
    global isGame
    global game_state
    global paused_game
    global segundos_mostrar_pieza8
    global cuadros8
    global imagen_oculta8
    global puede_jugar_8
    global ultimos_segundos_8
    global x1_8, y1_8, posX, posY
    global reinicio, ret_intro, cont_game, next_window, back_window
    global timer_font_8, start_time_8, start_timer_text_8, start_timer_event_8, start_timer_active_8
    global prueba8, acierto_8, error_8, ganar8, aux_cronometro8, perder8
    global ganar_reinicio8, cepillos8
    global s_wrong8_1, s_wrong8_2, s_wrong8_3, s_wrong8_4, s_wrong8_5, s_wrong8_6
    global sn_wrong8_1, sn_wrong8_2, sn_wrong8_3, sn_wrong8_4, sn_wrong8_5, sn_wrong8_6
    #pygame.mouse.set_visible(True)# Hacer visible el cursor   

    pygame.display.set_caption('Eighth_level') # Caption - Nombre de la ventana
    screen.fill(color_white) 
    isGame = True # Bandera que indica estado de juego activo, lo que implica que se puede pausar
    ret_intro = False
    cont_game = False
    reinicio = False
    next_window = False
    back_window = False

    medida_cuadro_h = screen_width/len(cuadros8[0])  # Medida de la imagen en pixeles
    medida_cuadro_v = screen_height/len(cuadros8) # Medida de la imagen en pixeles

    timer_rect8 = start_timer_text_8.get_rect(center = ((screen_width/2),(screen_height/2)))
    if not start_timer_active_8 and game_state == 'Eighth_level':
        start_time_8 = 0
        pygame.time.set_timer(start_timer_event_8, 1000)
        start_timer_active_8 = True

    ahora = int(time.time())
    # Y aquí usamos la bandera del tiempo, de nuevo. Si los segundos actuales menos los segundos
    # en los que se empezó el ocultamiento son mayores a los segundos en los que se muestra la pieza, entonces
    # se ocultan las dos tarjetas y se reinician las banderas
    if ultimos_segundos_8 is not None and ahora - ultimos_segundos_8 >= segundos_mostrar_pieza8:
        cuadros8[y1_8][x1_8].mostrar8 = False
        
        #cuadros2[y2_2][x2_2].mostrar2 = False
        x1_8 = None
        y1_8= None
        #x2_2 = None
        #y2_2 = None
        ultimos_segundos_8 = None
        # En este momento el usuario ya puede hacer clic de nuevo pues las imágenes ya estarán ocultas
        puede_jugar_8 = True

    if not ganar_reinicio8 == 0:
        x1_8 = None
        y1_8 = None



    # Hacer toda la pantalla blanca
    screen.fill(color_white)
    # Banderas para saber en dónde dibujar las imágenes
    cuadros_rows = len(cuadros8)
    cuadros_cols = len(cuadros8[0])
    image_cuadros = cuadros8[0][0].imagen_real8
    image_cuadros_width = image_cuadros.get_width()
    image_cuadros_height = image_cuadros.get_height()
    x_offset = (screen_width - (cuadros_cols*image_cuadros_width))//(cuadros_cols + 1)
    y_offset = (screen_height - (cuadros_rows*image_cuadros_height))//(cuadros_rows + 1)

    y =  y_offset
    # Recorrer los cuadros
    for fila in cuadros8:
        x = x_offset
        for cuadro in fila:
            """
            Si está descubierto o se debe mostrar, dibujamos la imagen real. Si no,
            dibujamos la imagen oculta
            """
            if cuadro.descubierto8 or cuadro.mostrar8:
                screen.blit(cuadro.imagen_real8, (x, y))
                screen.blit(start_timer_text_8, timer_rect8)
                

            else:
                screen.blit(imagen_oculta8, (x, y))
                screen.blit(start_timer_text_8, timer_rect8)


            x += medida_cuadro_h
        y += medida_cuadro_v

    draw_points7(cepillos8)
    
    if prueba8 == True: 
        """
        xAbsoluto e yAbsoluto son las coordenadas de la pantalla en donde se hizo
        clic. PyGame no ofrece detección de clic en imagen, por ejemplo. Así que
        se deben hacer ciertos trucos
        """
        # Si el click fue sobre el botón y el juego no se ha iniciado, entonces iniciamos el juego
        xAbsoluto = posX
        yAbsoluto = posY
        #if boton.collidepoint(event.pos):
        #   if not juego_iniciado:
        #      iniciar_juego()

        #else:
            # Si no hay juego iniciado, ignoramos el clic
        
        if juego_iniciado_8:
            iniciar_juego8()
            return
        
        x_rel = xAbsoluto - x_offset 
        y_rel = yAbsoluto - y_offset 
        
        x_cuadro = math.floor(x_rel / medida_cuadro_h)
        y_cuadro = math.floor(y_rel / medida_cuadro_v)
        
        # Primero lo primero. Si  ya está mostrada o descubierta, no hacemos nada
        if 0 <= x_cuadro < cuadros_cols and 0 <= y_cuadro < cuadros_rows:
            cuadro = cuadros8[y_cuadro][x_cuadro]
            if cuadro.mostrar8 or cuadro.descubierto8:
                # continue ignora lo de abajo y deja que el ciclo siga
                return
            # Si es la primera vez que tocan la imagen (es decir, no están buscando el par de otra, sino apenas
            # están descubriendo la primera)
            if x1_8 is None and y1_8 is None:# or acierto_2 == 1:
                # Entonces la actual es en la que acaban de dar clic, la mostramos
                x1_8 = x_cuadro
                y1_8 = y_cuadro
                cuadros8[y1_8][x1_8].mostrar8 = True
                pygame.mixer.Sound.play(sonido_voltear)
            
            cuadro1 = cuadros8[y1_8][x1_8]
            if cuadro1.fuente_imagen8 == "IMG_8L/octavo.png":
                cuadros8[y1_8][x1_8].descubierto8 = True
                acierto_8 = acierto_8 + 1                    
                pygame.mixer.Sound.play(sonido_clic) 
                ganar_reinicio8 = 1
            if not cuadro1.fuente_imagen8 == "IMG_8L/octavo.png":
                if cuadro1.fuente_imagen8 == "IMG_8L/wrong8_1.png":
                    if s_wrong8_1 == 1:
                        pygame.mixer.Sound.play(sn_wrong8_1)
                        s_wrong8_1 = 0
                if cuadro1.fuente_imagen8 == "IMG_8L/wrong8_2.png":
                    if s_wrong8_2 == 1:
                        pygame.mixer.Sound.play(sn_wrong8_2)
                        s_wrong8_2 = 0
                if cuadro1.fuente_imagen8 == "IMG_8L/wrong8_3.png":
                    if s_wrong8_3 == 1:
                        pygame.mixer.Sound.play(sn_wrong8_3)
                        s_wrong8_3 = 0
                if cuadro1.fuente_imagen8 == "IMG_8L/wrong8_4.png":
                    if s_wrong8_4 == 1:
                        pygame.mixer.Sound.play(sn_wrong8_4)
                        s_wrong8_4 = 0
                if cuadro1.fuente_imagen8 == "IMG_8L/wrong8_5.png":
                    if s_wrong8_5 == 1:
                        pygame.mixer.Sound.play(sn_wrong8_5)
                        s_wrong8_5 = 0
                if cuadro1.fuente_imagen8 == "IMG_8L/wrong8_6.png":
                    if s_wrong8_6 == 1:
                        pygame.mixer.Sound.play(sn_wrong8_6)
                        s_wrong8_6 = 0
                s_wrong8_1 = 1
                s_wrong8_2 = 1
                s_wrong8_3 = 1
                s_wrong8_4 = 1
                s_wrong8_5 = 1
                s_wrong8_6 = 1

                error_8 = error_8 + 1 
                ultimos_segundos_8 = int(time.time())
                ganar_reinicio8 = 0
                cepillos8 = cepillos8 -1
            comprobar_si_gana8()
                
          
            if ganar8:
                game_state = 'recompensa_8'#imagen que diga que ganó  y siguiente nivel o cosa 
            if perder8:
                game_state = 'reflection_8'
            prueba8 = False  
            


    if paused_game == True: # and juegos == True: # PANTALLA DE PAUSA
        game_state = 'Pausado'
        isGame = False
    return (isGame, paused_game, game_state, back_window, reinicio, ret_intro, cont_game, 
            prueba8, acierto_8, error_8, ganar8, aux_cronometro8, perder8, puede_jugar_8, ganar_reinicio8, cepillos8, 
            s_wrong8_1, s_wrong8_2, s_wrong8_3, s_wrong8_4, s_wrong8_5, s_wrong8_6)

def recompensa_8():
    global game_state
    global isGame
    isGame = False
    pygame.display.set_caption('Ganador8') # Caption - Nombre de la ventana
    instruc = 'VIDEOS/ganar_7.mp4'
    vel = 20
    pygame.mixer.Sound.play(completed)
    reproducir_video(instruc,vel)
    game_state = 'completed_8'
    return game_state

def completed_8():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window
    global reinicio
    global puede_jugar_8
    global ganar8, perder8, x1_8,y1_8
    #global aux_cronometro
    global acierto_8, error_8, unused_time_8, used_time_8
    global ganar_reinicio8
    global audio_resultados
    
    pygame.display.set_caption('Completo nivel 8') # Caption - Nombre de la ventana
    screen.blit(fondo_resultados, (0,0)) # Función que dibuja el fondo
    correct_text = font.render(str(acierto_8), True, color_black)
    mistake_text = font.render(str(error_8), True, color_black)
    used_time_text = font.render( str(used_time_8), True, color_black)
    unused_time_text = font.render(str(unused_time_8), True, color_black)
    
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(sonido_resultados)
    if audio_resultados == 1:
        channel.queue(audio_instruc)
        audio_resultados = 0

    screen.blit(correct_text, ((screen_width//1.91), (screen_height//3.55)))
    screen.blit(mistake_text, ((screen_width//1.993), (screen_height//2.59)))
    screen.blit(used_time_text, ((screen_width//1.597), (screen_height//2.077)))
    screen.blit(unused_time_text, ((screen_width//1.597), (screen_height//1.717)))

    paused_game = False


    if reinicio == True:
        puede_jugar_8 = True
        ocultar_todos_los_cuadros_8()
        game_state = 'eighthcard'######CAMBIAR
        reinicio = False
        ganar8 = False
        perder8 =  False
        back_window = False
        next_window = False
        #aux_cronometro = True 
        acierto_8 = 0
        error_8 = 0
        unused_time_8 = 0
        used_time_8 = 0
        #x1_2 = None
        #y1_2 = None
        ganar_reinicio8 +=1
        channel.stop()
        audio_resultados = 1

    if next_window == True: # Tecla n oprimida
        game_state = 'ninthcard'
        next_window = False
        channel.stop()
        audio_resultados = 1
        

    if back_window == True: # Tecla b oprimida
        paused_game = False 
        back_window = False
        open_game = False
        ganar_reinicio8 +=1
        channel.stop()
        audio_resultados = 1
    
    isGame = False # False porque no se encuentra dentro de un juego    

    return (game_state, paused_game, isGame, open_game, next_window, back_window, reinicio, 
            puede_jugar_8, ganar8,  acierto_8, error_8, unused_time_8, used_time_8, perder8, x1_8, y1_8, ganar_reinicio8)

def reflection_8():
    global game_state
    global isGame, used_time_8, time_limit_8
    isGame = False
    pygame.display.set_caption('Perder8') # Caption - Nombre de la ventana
    if used_time_8 == time_limit_8:
        instruc = 'VIDEOS/perder_tiempo.mp4'
        pygame.mixer.Sound.play(tiempo_agotado)
    else:
        instruc = 'VIDEOS/perder_puntos.mp4'
        pygame.mixer.Sound.play(puntos_agotados)
    vel = 20
    reproducir_video(instruc,vel)
    game_state = 'uncompleted_8'
    return game_state

def uncompleted_8():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window
    global reinicio
    global puede_jugar_8
    global ganar8, perder8
    global aux_cronometro8
    global acierto_8, error_8, unused_time_8, used_time_8, start_time_8, x1_8, y1_8
    global ganar_reinicio8
    global audio_resultados
    
    pygame.display.set_caption('No completo nivel 8') # Caption - Nombre de la ventana
    screen.blit(fondo_resultados, (0,0)) # Función que dibuja el fondo
    
    
    correct_text = font.render(str(acierto_8), True, color_black)
    mistake_text = font.render(str(error_8), True, color_black)
    used_time_text = font.render(str(used_time_8), True, color_black)
    unused_time_text = font.render(str(unused_time_8), True, color_black)
    
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(sonido_resultados)
    if audio_resultados == 1:
        channel.queue(audio_instruc)
        audio_resultados = 0

    screen.blit(correct_text, ((screen_width//1.91), (screen_height//3.55)))
    screen.blit(mistake_text, ((screen_width//1.993), (screen_height//2.59)))
    screen.blit(used_time_text, ((screen_width//1.597), (screen_height//2.077)))
    screen.blit(unused_time_text, ((screen_width//1.597), (screen_height//1.717)))

    paused_game = False

    if reinicio == True:
        puede_jugar_8 = True
        ocultar_todos_los_cuadros_8()
        game_state = 'eighthcard'##### CAMBIAR
        reinicio = False
        ganar8= False
        perder8 = False
        back_window = False
        next_window = False 
        aux_cronometro8 = True
        acierto_8 = 0
        error_8 = 0
        unused_time_8 = 0
        used_time_8 = 0
        ganar_reinicio8 = 0
        channel.stop()
        audio_resultados = 1


    if next_window == True: # Tecla n oprimida
        game_state = 'ninthcard'
        next_window = False
        channel.stop()
        audio_resultados = 1

    if back_window == True: # Tecla b oprimida
        paused_game = False 
        back_window = False
        open_game = False
        ganar_reinicio8 = 0
        channel.stop()
        audio_resultados = 1
         
    
    isGame = False # False porque no se encuentra dentro de un juego    

    return (game_state, paused_game, isGame, open_game, next_window, back_window, reinicio, 
            puede_jugar_8, ganar8, aux_cronometro8, acierto_8, error_8, unused_time_8, used_time_8, x1_8, y1_8, ganar_reinicio8)

####################################### Noveno Nivel ###############################################
def ocultar_todos_los_cuadros_9():
    for fila in cuadros9:
        for cuadro in fila:
            cuadro.mostrar9 = False
            cuadro.descubierto9 = False

# Determina si se gana, reinicia el juego y suena la pista correspondiente
def comprobar_si_gana9():
    global acierto_9, used_time_9, unused_time_9
    global game_state
    global ganar9, juego_iniciado_9, time_limit_9, perder9
    global error_9, ganar_reinicio9

    if gana9():
        used_time_9 =  start_time_9
        unused_time_9 =  time_limit_9 - used_time_9
        ganar9 = True
        juego_iniciado_9 = False

    if error_9 == 3 or used_time_9 == time_limit_9:
        used_time_9 =  start_time_9
        unused_time_9 =  time_limit_9 - used_time_9
        perder9 = True
        juego_iniciado_9 = False
        ganar_reinicio9 = 0

    return acierto_9, game_state, ganar9, juego_iniciado_9, perder9, error_9, ganar_reinicio9
        
        
# Regresa False si al menos un cuadro NO está descubierto. True en caso de que absolutamente todos estén descubiertos
# Recorre todas las filas de la matriz y en caso de que alguno no esté descubierto retorna a falso, de lo contrario pasa a true
def gana9():
    if not acierto_9 == 5: 
        return False
    return True



# Reproduce el sonido de click para que empiece, modifica el juego iniciado 
def iniciar_juego9():
    global juego_iniciado_9
    #global automatico
    #pygame.mixer.Sound.play(sonido_clic)
    #automatico = pygame.MOUSEBUTTONDOWN
    ocultar_todos_los_cuadros_9()
    juego_iniciado_9 = True

# Función para dibujar los cepillos en la pantalla
def draw_points8(cepillos):
    cepillo_image = pygame.transform.scale(pygame.image.load("puntos/punto1.png"), (100, 100))
    cepillo_width, cepillo_height = cepillo_image.get_size()
    x_offset = 10  # Ajusta la posición x donde quieres que aparezcan los cepillos

    for i in range(cepillos):
        x = x_offset + i * (cepillo_width + 5)  # Espacio entre los cepillos
        y = 10  # Ajusta la posición y donde quieres que aparezcan los cepillos
        screen.blit(cepillo_image, (x, y))

def ninth_level():  
    global isGame
    global game_state
    global paused_game
    global screen_width
    global screen_height
    global timer_text_9, level_time_9, timer_active_9, aux_cronometro9
    global puede_jugar_9, reinicio, ganar9, perder9
    global acierto_9, error_9, used_time_9, unused_time_9
    global x1_9, y1_9
    global actual_matrix, ganar_reinicio9, cepillos9
    global audio_tablero
    pygame.display.set_caption('_') # Caption - Nombre de la ventana
    screen.fill(color_azul_claro) 
    isGame = False # Bandera que indica estado de juego activo, lo que implica que se puede pausar o no
    paused_game = False
    puede_jugar_9 = True
    reinicio = False
    aux_cronometro9 = True
    acierto_9 = 0
    error_9 = 0
    unused_time_9 = 0
    used_time_9 = 0
    cepillos9 = 3
    ######################
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(ver_tablero)
    if audio_tablero == 1:
        channel.queue(audio_instruc)
        audio_tablero = 0
    ######################
    if not ganar_reinicio9 == 0:
            x1_9 = None
            y1_9 = None

    #start_timer_active = False
    #Para que al estar en esta pantalla sea seguro que el juego se reinicia y queda en el estado inicial
    ocultar_todos_los_cuadros_9()
    ganar9 = False
    perder9 = False
    actual_matrix = 8
    image_matrix = matrix_level[actual_matrix]
    rows = len(image_matrix)
    cols = len(image_matrix[0])
    image_width = image_matrix[0][0].get_width()
    image_height = image_matrix[0][0].get_height()
    padding_x = (screen_width - (cols * image_width)) // (cols + 1)
    padding_y = (screen_height - (rows * image_height)) // (rows + 1)
    timer_rect_9 = timer_text_9.get_rect(center = ((screen_width/2),(screen_height/2))) # Centro de la pantalla: center = screen.get_rect().center
    

    for i in range(rows):
        for j in range(cols):
            x = padding_x + j * (image_width + padding_x)
            y = padding_y + i * (image_height + padding_y)
            screen.blit(image_matrix[i][j], (x, y))
            #center_text(first_level_text,100) # Texto
            screen.blit(timer_text_9, timer_rect_9)
    
    if not timer_active_9 and game_state == 'ninth_level':
        level_time_9 = 20 # 20s
        pygame.time.set_timer(timer_event_9, 1000) # set_timer crea una acción cada 1s
        timer_active_9 = True

    return (isGame, paused_game, game_state, next_window, back_window, 
            timer_text_9, level_time_9,  puede_jugar_9, reinicio, ganar9, perder9, timer_active_9, 
            x1_9, y1_9, aux_cronometro9, acierto_9, error_9, used_time_9, unused_time_9, cepillos9)



def Nnth_level():
    global isGame
    global game_state
    global paused_game
    global segundos_mostrar_pieza9
    global cuadros9
    global imagen_oculta9
    global puede_jugar_9
    global ultimos_segundos_9
    global x1_9, y1_9, posX, posY
    global reinicio, ret_intro, cont_game, next_window, back_window
    global timer_font_9, start_time_9, start_timer_text_9, start_timer_event_9, start_timer_active_9
    global prueba9, acierto_9, error_9, ganar9, aux_cronometro9, perder9
    global ganar_reinicio9, cepillos9
    global s_wrong9_1, s_wrong9_2, s_wrong9_3, s_wrong9_4, s_wrong9_5
    global sn_wrong9_1, sn_wrong9_2, sn_wrong9_3, sn_wrong9_4, sn_wrong9_5
    #pygame.mouse.set_visible(True)# Hacer visible el cursor   

    pygame.display.set_caption('Nnth_level') # Caption - Nombre de la ventana
    screen.fill(color_azul_claro) 
    isGame = True # Bandera que indica estado de juego activo, lo que implica que se puede pausar
    ret_intro = False
    cont_game = False
    reinicio = False
    next_window = False
    back_window = False

    medida_cuadro_h = screen_width/len(cuadros9[0])  # Medida de la imagen en pixeles
    medida_cuadro_v = screen_height/len(cuadros9) # Medida de la imagen en pixeles

    timer_rect9 = start_timer_text_9.get_rect(center = ((screen_width/2),(screen_height/2)))
    if not start_timer_active_9 and game_state == 'Nnth_level':
        start_time_9 = 0
        pygame.time.set_timer(start_timer_event_9, 1000)
        start_timer_active_9 = True

    ahora = int(time.time())
    # Y aquí usamos la bandera del tiempo, de nuevo. Si los segundos actuales menos los segundos
    # en los que se empezó el ocultamiento son mayores a los segundos en los que se muestra la pieza, entonces
    # se ocultan las dos tarjetas y se reinician las banderas
    if ultimos_segundos_9 is not None and ahora - ultimos_segundos_9 >= segundos_mostrar_pieza9:
        cuadros9[y1_9][x1_9].mostrar9 = False
        
        #cuadros2[y2_2][x2_2].mostrar2 = False
        x1_9 = None
        y1_9 = None
        #x2_2 = None
        #y2_2 = None
        ultimos_segundos_9 = None
        # En este momento el usuario ya puede hacer clic de nuevo pues las imágenes ya estarán ocultas
        puede_jugar_9 = True

    if not ganar_reinicio9 == 0:
        x1_9 = None
        y1_9 = None



    # Hacer toda la pantalla blanca
    screen.fill(color_azul_claro)
    # Banderas para saber en dónde dibujar las imágenes
    cuadros_rows = len(cuadros9)
    cuadros_cols = len(cuadros9[0])
    image_cuadros = cuadros9[0][0].imagen_real9
    image_cuadros_width = image_cuadros.get_width()
    image_cuadros_height = image_cuadros.get_height()
    x_offset = (screen_width - (cuadros_cols*image_cuadros_width))//(cuadros_cols + 1)
    y_offset = (screen_height - (cuadros_rows*image_cuadros_height))//(cuadros_rows + 1)

    y =  y_offset
    # Recorrer los cuadros
    for fila in cuadros9:
        x = x_offset
        for cuadro in fila:
            """
            Si está descubierto o se debe mostrar, dibujamos la imagen real. Si no,
            dibujamos la imagen oculta
            """
            if cuadro.descubierto9 or cuadro.mostrar9:
                screen.blit(cuadro.imagen_real9, (x, y))
                screen.blit(start_timer_text_9, timer_rect9)
                

            else:
                screen.blit(imagen_oculta9, (x, y))
                screen.blit(start_timer_text_9, timer_rect9)


            x += medida_cuadro_h
        y += medida_cuadro_v

    draw_points8(cepillos9)
    
    if prueba9 == True: 
        """
        xAbsoluto e yAbsoluto son las coordenadas de la pantalla en donde se hizo
        clic. PyGame no ofrece detección de clic en imagen, por ejemplo. Así que
        se deben hacer ciertos trucos
        """
        # Si el click fue sobre el botón y el juego no se ha iniciado, entonces iniciamos el juego
        xAbsoluto = posX
        yAbsoluto = posY
        #if boton.collidepoint(event.pos):
        #   if not juego_iniciado:
        #      iniciar_juego()

        #else:
            # Si no hay juego iniciado, ignoramos el clic
        
        if juego_iniciado_9:
            iniciar_juego9()
            return
        
        x_rel = xAbsoluto - x_offset 
        y_rel = yAbsoluto - y_offset 
        
        x_cuadro = math.floor(x_rel / medida_cuadro_h)
        y_cuadro = math.floor(y_rel / medida_cuadro_v)
        
        # Primero lo primero. Si  ya está mostrada o descubierta, no hacemos nada
        if 0 <= x_cuadro < cuadros_cols and 0 <= y_cuadro < cuadros_rows:
            cuadro = cuadros9[y_cuadro][x_cuadro]
            if cuadro.mostrar9 or cuadro.descubierto9:
                # continue ignora lo de abajo y deja que el ciclo siga
                return
            # Si es la primera vez que tocan la imagen (es decir, no están buscando el par de otra, sino apenas
            # están descubriendo la primera)
            if x1_9 is None and y1_9 is None:# or acierto_2 == 1:
                # Entonces la actual es en la que acaban de dar clic, la mostramos
                x1_9 = x_cuadro
                y1_9 = y_cuadro
                cuadros9[y1_9][x1_9].mostrar9 = True
                pygame.mixer.Sound.play(sonido_voltear)
            
            cuadro1 = cuadros9[y1_9][x1_9]
            if cuadro1.fuente_imagen9 == "IMG_9L/noveno.png":
                cuadros9[y1_9][x1_9].descubierto9 = True
                acierto_9 = acierto_9 + 1                    
                pygame.mixer.Sound.play(sonido_clic) 
                ganar_reinicio9 = 1
            if not cuadro1.fuente_imagen9 == "IMG_9L/noveno.png":
                if cuadro1.fuente_imagen9 == "IMG_9L/wrong9_1.png":
                    if s_wrong9_1 == 1:
                        pygame.mixer.Sound.play(sn_wrong9_1)
                        s_wrong9_1 = 0
                if cuadro1.fuente_imagen9 == "IMG_9L/wrong9_2.png":
                    if s_wrong9_2 == 1:
                        pygame.mixer.Sound.play(sn_wrong9_2)
                        s_wrong9_2 = 0
                if cuadro1.fuente_imagen9 == "IMG_9L/wrong9_3.png":
                    if s_wrong9_3 == 1:
                        pygame.mixer.Sound.play(sn_wrong9_3)
                        s_wrong9_3 = 0
                if cuadro1.fuente_imagen9 == "IMG_9L/wrong9_4.png":
                    if s_wrong9_4 == 1:
                        pygame.mixer.Sound.play(sn_wrong9_4)
                        s_wrong9_4 = 0
                if cuadro1.fuente_imagen9 == "IMG_9L/wrong9_5.png":
                    if s_wrong9_5 == 1:
                        pygame.mixer.Sound.play(sn_wrong9_5)
                        s_wrong9_5 = 0
                s_wrong9_1 = 1
                s_wrong9_2 = 1
                s_wrong9_3 = 1
                s_wrong9_4 = 1
                s_wrong9_5 = 1
                error_9 = error_9 + 1 
                ultimos_segundos_9 = int(time.time())
                ganar_reinicio9 = 0
                cepillos9 = cepillos9 -1
            comprobar_si_gana9()
                
          
            if ganar9:
                game_state = 'recompensa_9'#imagen que diga que ganó  y siguiente nivel o cosa 
            if perder9:
                game_state = 'reflection_9'
            prueba9 = False  
            


    if paused_game == True: # and juegos == True: # PANTALLA DE PAUSA
        game_state = 'Pausado'
        isGame = False
    return (isGame, paused_game, game_state, back_window, reinicio, ret_intro, cont_game, 
            prueba9, acierto_9, error_9, ganar9, aux_cronometro9, perder9, puede_jugar_9, ganar_reinicio9, cepillos9, 
            s_wrong9_1, s_wrong9_2, s_wrong9_3, s_wrong9_4, s_wrong9_5 )

def recompensa_9():
    global game_state
    global isGame
    isGame = False
    pygame.display.set_caption('Ganador9') # Caption - Nombre de la ventana
    instruc = 'VIDEOS/ganar_8.mp4'
    vel = 20
    pygame.mixer.Sound.play(completed)
    reproducir_video(instruc,vel)
    game_state = 'completed_9'
    return game_state

def completed_9():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window
    global reinicio
    global puede_jugar_9
    global ganar9, perder9, x1_9,y1_9
    #global aux_cronometro
    global acierto_9, error_9, unused_time_9, used_time_9
    global ganar_reinicio9
    global audio_resultados
    
    pygame.display.set_caption('Completo nivel 9') # Caption - Nombre de la ventana
    screen.blit(fondo_resultados, (0,0)) # Función que dibuja el fondo
    correct_text = font.render(str(acierto_9), True, color_black)
    mistake_text = font.render(str(error_9), True, color_black)
    used_time_text = font.render( str(used_time_9), True, color_black)
    unused_time_text = font.render(str(unused_time_9), True, color_black)
    
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(sonido_resultados)
    if audio_resultados == 1:
        channel.queue(audio_instruc)
        audio_resultados = 0

    screen.blit(correct_text, ((screen_width//1.91), (screen_height//3.55)))
    screen.blit(mistake_text, ((screen_width//1.993), (screen_height//2.59)))
    screen.blit(used_time_text, ((screen_width//1.597), (screen_height//2.077)))
    screen.blit(unused_time_text, ((screen_width//1.597), (screen_height//1.717)))

    paused_game = False


    if reinicio == True:
        puede_jugar_9 = True
        ocultar_todos_los_cuadros_9()
        game_state = 'ninthcard'######CAMBIAR
        reinicio = False
        ganar8 = False
        perder8 =  False
        back_window = False
        next_window = False
        #aux_cronometro = True 
        acierto_9 = 0
        error_9 = 0
        unused_time_9 = 0
        used_time_9 = 0
        #x1_2 = None
        #y1_2 = None
        ganar_reinicio9 +=1
        channel.stop()
        audio_resultados = 1

    if next_window == True: # Tecla n oprimida
        game_state = 'video_enjuague_crema'
        next_window = False
        channel.stop()
        audio_resultados = 1

    if back_window == True: # Tecla b oprimida
        paused_game = False 
        back_window = False
        open_game = False
        ganar_reinicio9 +=1
        channel.stop()
        audio_resultados = 1
    
    isGame = False # False porque no se encuentra dentro de un juego    

    return (game_state, paused_game, isGame, open_game, next_window, back_window, reinicio, 
            puede_jugar_9, ganar9,  acierto_9, error_9, unused_time_9, used_time_9, perder9, x1_9, y1_9, ganar_reinicio9)

def reflection_9():
    global game_state
    global isGame, used_time_9, time_limit_9
    isGame = False
    pygame.display.set_caption('Perder9') # Caption - Nombre de la ventana
    if used_time_9 == time_limit_9:
        instruc = 'VIDEOS/perder_tiempo.mp4'
        pygame.mixer.Sound.play(tiempo_agotado)
    else:
        instruc = 'VIDEOS/perder_puntos.mp4'
        pygame.mixer.Sound.play(puntos_agotados)
    vel = 20
    reproducir_video(instruc,vel)
    game_state = 'uncompleted_9'
    return game_state

def uncompleted_9():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window
    global reinicio
    global puede_jugar_9
    global ganar9, perder9
    global aux_cronometro9
    global acierto_9, error_9, unused_time_9, used_time_9, start_time_9, x1_9, y1_9
    global ganar_reinicio9
    global audio_resultados
    
    pygame.display.set_caption('No completo nivel 9') # Caption - Nombre de la ventana
    screen.blit(fondo_resultados, (0,0)) # Función que dibuja el fondo
    
    
    correct_text = font.render(str(acierto_9), True, color_black)
    mistake_text = font.render(str(error_9), True, color_black)
    used_time_text = font.render(str(used_time_9), True, color_black)
    unused_time_text = font.render(str(unused_time_9), True, color_black)
    
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(sonido_resultados)
    if audio_resultados == 1:
        channel.queue(audio_instruc)
        audio_resultados = 0

    screen.blit(correct_text, ((screen_width//1.91), (screen_height//3.55)))
    screen.blit(mistake_text, ((screen_width//1.993), (screen_height//2.59)))
    screen.blit(used_time_text, ((screen_width//1.597), (screen_height//2.077)))
    screen.blit(unused_time_text, ((screen_width//1.597), (screen_height//1.717)))

    paused_game = False

    if reinicio == True:
        puede_jugar_9 = True
        ocultar_todos_los_cuadros_9()
        game_state = 'ninthcard'##### CAMBIAR
        reinicio = False
        ganar9= False
        perder9 = False
        back_window = False
        next_window = False 
        aux_cronometro9 = True
        acierto_9 = 0
        error_9 = 0
        unused_time_9 = 0
        used_time_9 = 0
        ganar_reinicio9 = 0
        channel.stop()
        audio_resultados = 1

    if next_window == True: # Tecla n oprimida
        game_state = 'video_enjuague_crema'
        next_window = False
        channel.stop()
        audio_resultados = 1

    if back_window == True: # Tecla b oprimida
        paused_game = False 
        back_window = False
        open_game = False
        channel.stop()
        audio_resultados = 1
         
    
    isGame = False # False porque no se encuentra dentro de un juego    

    return (game_state, paused_game, isGame, open_game, next_window, back_window, reinicio, 
            puede_jugar_9, ganar9, aux_cronometro9, acierto_9, error_9, unused_time_9, used_time_9, x1_9, y1_9, ganar_reinicio9)

####################################### Decimo Nivel ###############################################
def ocultar_todos_los_cuadros_10():
    for fila in cuadros10:
        for cuadro in fila:
            cuadro.mostrar10 = False
            cuadro.descubierto10 = False

# Determina si se gana, reinicia el juego y suena la pista correspondiente
def comprobar_si_gana10():
    global acierto_10, used_time_10, unused_time_10
    global game_state
    global ganar10, juego_iniciado_10, time_limit_10, perder10
    global error_10, ganar_reinicio10

    if gana10():
        used_time_10 =  start_time_10
        unused_time_10 =  time_limit_10 - used_time_10
        ganar10 = True
        juego_iniciado_10 = False

    if error_10 == 3 or used_time_10 == time_limit_10:
        used_time_10 =  start_time_10
        unused_time_10 =  time_limit_10 - used_time_10
        perder10 = True
        juego_iniciado_10 = False
        ganar_reinicio10 = 0

    return acierto_10, game_state, ganar10, juego_iniciado_10, perder10, error_10, ganar_reinicio10
        
        
# Regresa False si al menos un cuadro NO está descubierto. True en caso de que absolutamente todos estén descubiertos
# Recorre todas las filas de la matriz y en caso de que alguno no esté descubierto retorna a falso, de lo contrario pasa a true
def gana10():
    if not acierto_10 == 6: 
        return False
    return True



# Reproduce el sonido de click para que empiece, modifica el juego iniciado 
def iniciar_juego10():
    global juego_iniciado_10
    #global automatico
    #pygame.mixer.Sound.play(sonido_clic)
    #automatico = pygame.MOUSEBUTTONDOWN
    ocultar_todos_los_cuadros_10()
    juego_iniciado_10 = True

# Función para dibujar los cepillos en la pantalla
def draw_points9(cepillos):
    cepillo_image = pygame.transform.scale(pygame.image.load("puntos/punto2.png"), (100, 100))
    cepillo_width, cepillo_height = cepillo_image.get_size()
    x_offset = 10  # Ajusta la posición x donde quieres que aparezcan los cepillos

    for i in range(cepillos):
        x = x_offset + i * (cepillo_width + 5)  # Espacio entre los cepillos
        y = 10  # Ajusta la posición y donde quieres que aparezcan los cepillos
        screen.blit(cepillo_image, (x, y))

def tenth_level():  
    global isGame
    global game_state
    global paused_game
    global screen_width
    global screen_height
    global timer_text_10, level_time_10, timer_active_10, aux_cronometro10
    global puede_jugar_10, reinicio, ganar10, perder10
    global acierto_10, error_10, used_time_10, unused_time_10
    global x1_10, y1_10
    global actual_matrix, ganar_reinicio10, cepillos10
    global audio_tablero
    pygame.display.set_caption('_') # Caption - Nombre de la ventana
    screen.fill(color_azul_claro) 
    isGame = False # Bandera que indica estado de juego activo, lo que implica que se puede pausar o no
    paused_game = False
    puede_jugar_10 = True
    reinicio = False
    aux_cronometro10 = True
    acierto_10 = 0
    error_10 = 0
    unused_time_10 = 0
    used_time_10 = 0
    cepillos10 = 3
    ######################
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(ver_tablero)
    if audio_tablero == 1:
        channel.queue(audio_instruc)
        audio_tablero = 0
    ######################
    if not ganar_reinicio10 == 0:
            x1_10 = None
            y1_10 = None

    #start_timer_active = False
    #Para que al estar en esta pantalla sea seguro que el juego se reinicia y queda en el estado inicial
    ocultar_todos_los_cuadros_10()
    ganar10 = False
    perder10 = False
    actual_matrix = 9
    image_matrix = matrix_level[actual_matrix]
    rows = len(image_matrix)
    cols = len(image_matrix[0])
    image_width = image_matrix[0][0].get_width()
    image_height = image_matrix[0][0].get_height()
    padding_x = (screen_width - (cols * image_width)) // (cols + 1)
    padding_y = (screen_height - (rows * image_height)) // (rows + 1)
    timer_rect_10 = timer_text_10.get_rect(center = ((screen_width/2),(screen_height/2))) # Centro de la pantalla: center = screen.get_rect().center
    

    for i in range(rows):
        for j in range(cols):
            x = padding_x + j * (image_width + padding_x)
            y = padding_y + i * (image_height + padding_y)
            screen.blit(image_matrix[i][j], (x, y))
            #center_text(first_level_text,100) # Texto
            screen.blit(timer_text_10, timer_rect_10)
    
    if not timer_active_10 and game_state == 'tenth_level':
        level_time_10 = 20 # 20s
        pygame.time.set_timer(timer_event_10, 1000) # set_timer crea una acción cada 1s
        timer_active_10 = True

    return (isGame, paused_game, game_state, next_window, back_window, 
            timer_text_10, level_time_10,  puede_jugar_10, reinicio, ganar10, perder10, timer_active_10, 
            x1_10, y1_10, aux_cronometro10, acierto_10, error_10, used_time_10, unused_time_10, cepillos10)



def Tnth_level():
    global isGame
    global game_state
    global paused_game
    global segundos_mostrar_pieza10
    global cuadros10
    global imagen_oculta10
    global puede_jugar_10
    global ultimos_segundos_10
    global x1_10, y1_10, posX, posY
    global reinicio, ret_intro, cont_game, next_window, back_window
    global timer_font_10, start_time_10, start_timer_text_10, start_timer_event_10, start_timer_active_10
    global prueba10, acierto_10, error_10, ganar10, aux_cronometro10, perder10
    global ganar_reinicio10, cepillos10
    global s_wrong10_1, s_wrong10_2, s_wrong10_3, s_wrong10_4, s_wrong10_5, s_wrong10_6
    global sn_wrong10_1, sn_wrong10_2, sn_wrong10_3, sn_wrong10_4, sn_wrong10_5, sn_wrong10_6
    #pygame.mouse.set_visible(True)# Hacer visible el cursor   

    pygame.display.set_caption('Tnth_level') # Caption - Nombre de la ventana
    screen.fill(color_azul_claro) 
    isGame = True # Bandera que indica estado de juego activo, lo que implica que se puede pausar
    ret_intro = False
    cont_game = False
    reinicio = False
    next_window = False
    back_window = False

    medida_cuadro_h = screen_width/len(cuadros10[0])  # Medida de la imagen en pixeles
    medida_cuadro_v = screen_height/len(cuadros10) # Medida de la imagen en pixeles

    timer_rect10 = start_timer_text_10.get_rect(center = ((screen_width/2),(screen_height/2)))
    if not start_timer_active_10 and game_state == 'Tnth_level':
        start_time_10 = 0
        pygame.time.set_timer(start_timer_event_10, 1000)
        start_timer_active_10 = True

    ahora = int(time.time())
    # Y aquí usamos la bandera del tiempo, de nuevo. Si los segundos actuales menos los segundos
    # en los que se empezó el ocultamiento son mayores a los segundos en los que se muestra la pieza, entonces
    # se ocultan las dos tarjetas y se reinician las banderas
    if ultimos_segundos_10 is not None and ahora - ultimos_segundos_10 >= segundos_mostrar_pieza10:
        cuadros10[y1_10][x1_10].mostrar10 = False
        
        #cuadros2[y2_2][x2_2].mostrar2 = False
        x1_10 = None
        y1_10 = None
        #x2_2 = None
        #y2_2 = None
        ultimos_segundos_10 = None
        # En este momento el usuario ya puede hacer clic de nuevo pues las imágenes ya estarán ocultas
        puede_jugar_10 = True

    if not ganar_reinicio10 == 0:
        x1_10 = None
        y1_10 = None



    # Hacer toda la pantalla blanca
    screen.fill(color_azul_claro)
    # Banderas para saber en dónde dibujar las imágenes
    cuadros_rows = len(cuadros10)
    cuadros_cols = len(cuadros10[0])
    image_cuadros = cuadros10[0][0].imagen_real10
    image_cuadros_width = image_cuadros.get_width()
    image_cuadros_height = image_cuadros.get_height()
    x_offset = (screen_width - (cuadros_cols*image_cuadros_width))//(cuadros_cols + 1)
    y_offset = (screen_height - (cuadros_rows*image_cuadros_height))//(cuadros_rows + 1)

    y =  y_offset
    # Recorrer los cuadros
    for fila in cuadros10:
        x = x_offset
        for cuadro in fila:
            """
            Si está descubierto o se debe mostrar, dibujamos la imagen real. Si no,
            dibujamos la imagen oculta
            """
            if cuadro.descubierto10 or cuadro.mostrar10:
                screen.blit(cuadro.imagen_real10, (x, y))
                screen.blit(start_timer_text_10, timer_rect10)
                

            else:
                screen.blit(imagen_oculta10, (x, y))
                screen.blit(start_timer_text_10, timer_rect10)


            x += medida_cuadro_h
        y += medida_cuadro_v

    draw_points9(cepillos10)
    
    if prueba10 == True: 
        """
        xAbsoluto e yAbsoluto son las coordenadas de la pantalla en donde se hizo
        clic. PyGame no ofrece detección de clic en imagen, por ejemplo. Así que
        se deben hacer ciertos trucos
        """
        # Si el click fue sobre el botón y el juego no se ha iniciado, entonces iniciamos el juego
        xAbsoluto = posX
        yAbsoluto = posY
        #if boton.collidepoint(event.pos):
        #   if not juego_iniciado:
        #      iniciar_juego()

        #else:
            # Si no hay juego iniciado, ignoramos el clic
        
        if juego_iniciado_10:
            iniciar_juego10()
            return
        
        x_rel = xAbsoluto - x_offset 
        y_rel = yAbsoluto - y_offset 
        
        x_cuadro = math.floor(x_rel / medida_cuadro_h)
        y_cuadro = math.floor(y_rel / medida_cuadro_v)
        
        # Primero lo primero. Si  ya está mostrada o descubierta, no hacemos nada
        if 0 <= x_cuadro < cuadros_cols and 0 <= y_cuadro < cuadros_rows:
            cuadro = cuadros10[y_cuadro][x_cuadro]
            if cuadro.mostrar10 or cuadro.descubierto10:
                # continue ignora lo de abajo y deja que el ciclo siga
                return
            # Si es la primera vez que tocan la imagen (es decir, no están buscando el par de otra, sino apenas
            # están descubriendo la primera)
            if x1_10 is None and y1_10 is None:# or acierto_2 == 1:
                # Entonces la actual es en la que acaban de dar clic, la mostramos
                x1_10 = x_cuadro
                y1_10 = y_cuadro
                cuadros10[y1_10][x1_10].mostrar10 = True
                pygame.mixer.Sound.play(sonido_voltear)
            
            cuadro1 = cuadros10[y1_10][x1_10]
            if cuadro1.fuente_imagen10 == "IMG_10L/decimo.png":
                cuadros10[y1_10][x1_10].descubierto10 = True
                acierto_10 = acierto_10 + 1                    
                pygame.mixer.Sound.play(sonido_clic) 
                ganar_reinicio10 = 1
            if not cuadro1.fuente_imagen10 == "IMG_10L/decimo.png":
                if cuadro1.fuente_imagen10 == "IMG_10L/wrong1_1.png":
                    if s_wrong10_1 == 1:
                        pygame.mixer.Sound.play(sn_wrong10_1)
                        s_wrong10_1 = 0
                if cuadro1.fuente_imagen10 == "IMG_10L/wrong1_2.png":
                    if s_wrong10_2 == 1:
                        pygame.mixer.Sound.play(sn_wrong10_2)
                        s_wrong10_2 = 0
                if cuadro1.fuente_imagen10 == "IMG_10L/wrong1_3.png":
                    if s_wrong10_3 == 1:
                        pygame.mixer.Sound.play(sn_wrong10_3)
                        s_wrong10_3 = 0
                if cuadro1.fuente_imagen10 == "IMG_10L/wrong1_4.png":
                    if s_wrong10_4 == 1:
                        pygame.mixer.Sound.play(sn_wrong10_4)
                        s_wrong10_4 = 0
                if cuadro1.fuente_imagen10 == "IMG_10L/wrong1_5.png":
                    if s_wrong10_5 == 1:
                        pygame.mixer.Sound.play(sn_wrong10_5)
                        s_wrong10_5 = 0
                if cuadro1.fuente_imagen10 == "IMG_10L/wrong1_6.png":
                    if s_wrong10_6 == 1:
                        pygame.mixer.Sound.play(sn_wrong10_6)
                        s_wrong10_6 = 0
                s_wrong10_1 = 1
                s_wrong10_2 = 1
                s_wrong10_3 = 1
                s_wrong10_4 = 1
                s_wrong10_5 = 1
                s_wrong10_6 = 1
                error_10 = error_10 + 1 
                ultimos_segundos_10 = int(time.time())
                ganar_reinicio10 = 0
                cepillos10 = cepillos10 -1
            comprobar_si_gana10()
                
          
            if ganar10:
                game_state = 'recompensa_10'#imagen que diga que ganó  y siguiente nivel o cosa 
            if perder10:
                game_state = 'reflection_10'
            prueba10 = False  
            


    if paused_game == True: # and juegos == True: # PANTALLA DE PAUSA
        game_state = 'Pausado'
        isGame = False
    return (isGame, paused_game, game_state, back_window, reinicio, ret_intro, cont_game, 
            prueba10, acierto_10, error_10, ganar10, aux_cronometro10, perder10, puede_jugar_10, ganar_reinicio10, cepillos10,
            s_wrong10_1, s_wrong10_2, s_wrong10_3, s_wrong10_4, s_wrong10_5, s_wrong10_6)

def recompensa_10():
    global game_state
    global isGame
    isGame = False
    pygame.display.set_caption('Ganador10') # Caption - Nombre de la ventana
    instruc = 'VIDEOS/ganar_9.mp4'
    vel = 25
    pygame.mixer.Sound.play(completed)
    reproducir_video(instruc,vel)
    game_state = 'completed_10'
    return game_state

def completed_10():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window
    global reinicio
    global puede_jugar_10
    global ganar10, perder10, x1_10,y1_10
    #global aux_cronometro
    global acierto_10, error_10, unused_time_10, used_time_10
    global ganar_reinicio10
    global audio_resultados
    
    pygame.display.set_caption('Completo nivel 10') # Caption - Nombre de la ventana
    screen.blit(fondo_resultados, (0,0)) # Función que dibuja el fondo
    correct_text = font.render(str(acierto_10), True, color_black)
    mistake_text = font.render(str(error_10), True, color_black)
    used_time_text = font.render( str(used_time_10), True, color_black)
    unused_time_text = font.render(str(unused_time_10), True, color_black)
    
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(sonido_resultados)
    if audio_resultados == 1:
        channel.queue(audio_instruc)
        audio_resultados = 0
    
    screen.blit(correct_text, ((screen_width//1.91), (screen_height//3.55)))
    screen.blit(mistake_text, ((screen_width//1.993), (screen_height//2.59)))
    screen.blit(used_time_text, ((screen_width//1.597), (screen_height//2.077)))
    screen.blit(unused_time_text, ((screen_width//1.597), (screen_height//1.717)))

    paused_game = False


    if reinicio == True:
        puede_jugar_10 = True
        ocultar_todos_los_cuadros_10()
        game_state = 'tenthcard'######CAMBIAR
        reinicio = False
        ganar10 = False
        perder10 =  False
        back_window = False
        next_window = False
        #aux_cronometro = True 
        acierto_10 = 0
        error_10 = 0
        unused_time_10 = 0
        used_time_10 = 0
        #x1_2 = None
        #y1_2 = None
        ganar_reinicio10 +=1
        channel.stop()
        audio_resultados = 1

    if next_window == True: # Tecla n oprimida
        game_state = 'video_enjuague_bucal'
        next_window = False
        channel.stop()
        audio_resultados = 1
        

    if back_window == True: # Tecla b oprimida
        paused_game = False 
        back_window = False
        open_game = False
        ganar_reinicio10 +=1
        channel.stop()
        audio_resultados = 1
    
    isGame = False # False porque no se encuentra dentro de un juego    

    return (game_state, paused_game, isGame, open_game, next_window, back_window, reinicio, 
            puede_jugar_10, ganar10,  acierto_10, error_10, unused_time_10, used_time_10, perder10, x1_10, y1_10, ganar_reinicio10)

def reflection_10():
    global game_state
    global isGame, used_time_10, time_limit_10
    isGame = False
    pygame.display.set_caption('Perder10') # Caption - Nombre de la ventana
    if used_time_10 == time_limit_10:
        instruc = 'VIDEOS/perder_tiempo.mp4'
        pygame.mixer.Sound.play(tiempo_agotado)
    else:
        instruc = 'VIDEOS/perder_puntos.mp4'
        pygame.mixer.Sound.play(puntos_agotados)
    vel = 20
    reproducir_video(instruc,vel)
    game_state = 'uncompleted_10'
    return game_state

def uncompleted_10():
    global open_game
    global game_state
    global paused_game
    global isGame
    global next_window
    global back_window
    global reinicio
    global puede_jugar_10
    global ganar10, perder10
    global aux_cronometro10
    global acierto_10, error_10, unused_time_10, used_time_10, start_time_10, x1_10, y1_10
    global ganar_reinicio10
    global audio_resultados
    pygame.display.set_caption('No completo nivel 10') # Caption - Nombre de la ventana
    screen.blit(fondo_resultados, (0,0)) # Función que dibuja el fondo
    
    
    correct_text = font.render(str(acierto_10), True, color_black)
    mistake_text = font.render(str(error_10), True, color_black)
    used_time_text = font.render(str(used_time_10), True, color_black)
    unused_time_text = font.render(str(unused_time_10), True, color_black)
    
    channel= pygame.mixer.Channel(1)
    audio_instruc = pygame.mixer.Sound(sonido_resultados)
    if audio_resultados == 1:
        channel.queue(audio_instruc)
        audio_resultados = 0

    screen.blit(correct_text, ((screen_width//1.91), (screen_height//3.55)))
    screen.blit(mistake_text, ((screen_width//1.993), (screen_height//2.59)))
    screen.blit(used_time_text, ((screen_width//1.597), (screen_height//2.077)))
    screen.blit(unused_time_text, ((screen_width//1.597), (screen_height//1.717)))

    paused_game = False

    if reinicio == True:
        puede_jugar_10 = True
        ocultar_todos_los_cuadros_10()
        game_state = 'tenthcard'##### CAMBIAR
        reinicio = False
        ganar10= False
        perder10 = False
        back_window = False
        next_window = False 
        aux_cronometro10 = True
        acierto_10 = 0
        error_10 = 0
        unused_time_10 = 0
        used_time_10 = 0
        ganar_reinicio10 = 0
        channel.stop()
        audio_resultados = 1


    if next_window == True: # Tecla n oprimida
        game_state = 'video_enjuague_bucal'
        next_window = False
        channel.stop()
        audio_resultados = 1
        

    if back_window == True: # Tecla b oprimida
        paused_game = False 
        back_window = False
        open_game = False
        ganar_reinicio10 = 0
        channel.stop()
        audio_resultados = 1
         
    
    isGame = False # False porque no se encuentra dentro de un juego    

    return (game_state, paused_game, isGame, open_game, next_window, back_window, reinicio, 
            puede_jugar_10, ganar10, aux_cronometro10, acierto_10, error_10, unused_time_10, used_time_10, x1_10, y1_10, ganar_reinicio10)

#######################################FIN NIVELES###############################################

####################################### PAUSA ###############################################
def pausa(state_before_pause):
    global paused_game
    global game_state
    global cont_game
    global ret_intro
    global back_window
    global next_window
    global open_game, reinicio
    global puede_jugar, aux_cronometro, ganar1, acierto_1, error_1, unused_time_1, used_time_1, x1, y1, x2, y2, ganar_rein1
    global ganar2, acierto_2, error_2, unused_time_2, used_time_2, puede_jugar_2, perder2, x1_2, y1_2, ganar_reinicio2, aux_cronometro2
    global ganar3, acierto_3, error_3, unused_time_3, used_time_3, puede_jugar_3, perder3, x1_3, y1_3, ganar_reinicio3, aux_cronometro3
    global ganar4, acierto_4, error_4, unused_time_4, used_time_4, puede_jugar_4, perder4, x1_4, y1_4, ganar_reinicio4, aux_cronometro4
    global ganar5, acierto_5, error_5, unused_time_5, used_time_5, puede_jugar_5, perder5, x1_5, y1_5, ganar_reinicio5, aux_cronometro5
    global ganar6, acierto_6, error_6, unused_time_6, used_time_6, puede_jugar_6, perder6, x1_6, y1_6, ganar_reinicio6, aux_cronometro6
    global ganar7, acierto_7, error_7, unused_time_7, used_time_7, puede_jugar_7, perder7, x1_7, y1_7, ganar_reinicio7, aux_cronometro7
    global ganar8, acierto_8, error_8, unused_time_8, used_time_8, puede_jugar_8, perder8, x1_8, y1_8, ganar_reinicio8, aux_cronometro8
    global ganar9, acierto_9, error_9, unused_time_9, used_time_9, puede_jugar_9, perder9, x1_9, y1_9, ganar_reinicio9, aux_cronometro9
    global ganar10, acierto_10, error_10, unused_time_10, used_time_10, puede_jugar_10, perder10, x1_10, y1_10, ganar_reinicio10, aux_cronometro10
   
    pygame.display.set_caption('Pausa') # Caption - Nombre de la ventana
    screen.blit(fondo_pausa, (0,0)) # Función que dibuja el fondo

    if next_window == True: #continuar juego
        paused_game = False
        next_window = False
        if state_before_pause == 1:
            game_state = 'Fst_level'
        if state_before_pause == 2:
            game_state = 'Scnd_level'
        if state_before_pause == 3:
            game_state = 'Thrd_level'
        if state_before_pause == 4:
            if not ganar_reinicio4 == 0:
                x1_4 = None
                y1_4 = None
            game_state = 'Frth_level'
        if state_before_pause == 5:
            if not ganar_reinicio5 == 0:
                x1_5 = None
                y1_5 = None
            game_state = 'Ffth_level'
        if state_before_pause == 6:
            if not ganar_reinicio6 == 0:
                x1_6 = None
                y1_6 = None
            game_state = 'Sxth_level'
        if state_before_pause == 7:
            if not ganar_reinicio7 == 0:
                x1_7 = None
                y1_7 = None
            game_state = 'Svnth_level'
        if state_before_pause == 8:
            if not ganar_reinicio8 == 0:
                x1_8 = None
                y1_8 = None
            game_state = 'Eighth_level'
        if state_before_pause == 9:
            if not ganar_reinicio9 == 0:
                x1_9 = None
                y1_9 = None
            game_state = 'Nnth_level'
        if state_before_pause == 10:
            if not ganar_reinicio10 == 0:
                x1_10 = None
                y1_10 = None
            game_state = 'Tnth_level'
        


    if back_window == True: #volver a intro memoria
        if state_before_pause == 1:
            paused_game = False 
            back_window = False
            open_game = False
            used_time_1 =  start_time
            unused_time_1 =  time_limit_1 - start_time
        if state_before_pause == 2:
            paused_game = False 
            back_window = False
            open_game = False
            used_time_2 =  start_time_3
            unused_time_2 =  time_limit_2 - start_time_2
        if state_before_pause == 3:
            paused_game = False 
            back_window = False
            open_game = False
            used_time_3 =  start_time_3
            unused_time_3 =  time_limit_3 - start_time_3
        if state_before_pause == 4:
            paused_game = False 
            back_window = False
            open_game = False
            used_time_4 =  start_time_4
            unused_time_4 =  time_limit_4 - start_time_4
        if state_before_pause == 5:
            paused_game = False 
            back_window = False
            open_game = False
            used_time_5 =  start_time_5
            unused_time_5 =  time_limit_5 - start_time_5
        if state_before_pause == 6:
            paused_game = False 
            back_window = False
            open_game = False
            used_time_6 =  start_time_6
            unused_time_6 =  time_limit_6 - start_time_6
        if state_before_pause == 7:
            paused_game = False 
            back_window = False
            open_game = False
            used_time_7 =  start_time_7
            unused_time_7 =  time_limit_7 - start_time_7
        if state_before_pause == 8:
            paused_game = False 
            back_window = False
            open_game = False
            used_time_8 =  start_time_8
            unused_time_8 =  time_limit_8 - start_time_8
        if state_before_pause == 9:
            paused_game = False 
            back_window = False
            open_game = False
            used_time_9 =  start_time_9
            unused_time_9 =  time_limit_9 - start_time_9
        if state_before_pause == 10:
            paused_game = False 
            back_window = False
            open_game = False
            used_time_10 =  start_time_10
            unused_time_10 =  time_limit_10 - start_time_10

    if reinicio == True:
        paused_game = False
        if state_before_pause == 1:
            puede_jugar = True
            ocultar_todos_los_cuadros()
            game_state = 'first_level'
            reinicio = False
            ganar1 = False
            back_window = False
            next_window = False
            aux_cronometro = True 
            acierto_1 = 0
            error_1 = 0
            used_time_1 = 0
            unused_time_1 = 0
            ganar_rein1 += 1

        if state_before_pause == 2:
            puede_jugar_2 = True
            ocultar_todos_los_cuadros_2()
            game_state = 'secondcard'
            reinicio = False
            ganar2 = False
            perder2 = False
            back_window = False
            next_window = False
            aux_cronometro2 = True 
            acierto_2 = 0
            error_2 = 0
            used_time_2 = 0
            unused_time_2 = 0
            ganar_reinicio2 = 0
        if state_before_pause == 3:
            puede_jugar_3 = True
            ocultar_todos_los_cuadros_3()
            game_state = 'thirdcard'
            reinicio = False
            ganar3 = False
            perder3 = False
            back_window = False
            next_window = False
            aux_cronometro3 = True 
            acierto_3 = 0
            error_3 = 0
            used_time_3 = 0
            unused_time_3 = 0
            ganar_reinicio3 = 0
        if state_before_pause == 4:
            puede_jugar_4 = True
            if not ganar_reinicio4 == 0:
                x1_4 = None
                y1_4 = None
            ocultar_todos_los_cuadros_4()
            game_state = 'fourthcard'
            reinicio = False
            ganar4 = False
            perder4 = False
            back_window = False
            next_window = False
            aux_cronometro4 = True 
            acierto_4 = 0
            error_4 = 0
            used_time_4 = 0
            unused_time_4 = 0
            ganar_reinicio4 = 0
        if state_before_pause == 5:
            puede_jugar_5 = True
            if not ganar_reinicio5 == 0:
                x1_5 = None
                y1_5 = None
            ocultar_todos_los_cuadros_5()
            game_state = 'fifthcard'
            reinicio = False
            ganar5 = False
            perder5 = False
            back_window = False
            next_window = False
            aux_cronometro5 = True 
            acierto_5 = 0
            error_5 = 0
            used_time_5 = 0
            unused_time_5 = 0
            ganar_reinicio5 = 0
        if state_before_pause == 6:
            puede_jugar_6 = True
            if not ganar_reinicio6 == 0:
                x1_6 = None
                y1_6 = None
            ocultar_todos_los_cuadros_6()
            game_state = 'sixthcard'
            reinicio = False
            ganar6 = False
            perder6 = False
            back_window = False
            next_window = False
            aux_cronometro6 = True 
            acierto_6 = 0
            error_6 = 0
            used_time_6 = 0
            unused_time_6 = 0
            ganar_reinicio6 = 0
        if state_before_pause == 7:
            puede_jugar_7 = True
            if not ganar_reinicio7 == 0:
                x1_7 = None
                y1_7 = None
            ocultar_todos_los_cuadros_7()
            game_state = 'seventhcard'
            reinicio = False
            ganar7 = False
            perder7 = False
            back_window = False
            next_window = False
            aux_cronometro7 = True 
            acierto_7 = 0
            error_7 = 0
            used_time_7 = 0
            unused_time_7 = 0
            ganar_reinicio7 = 0
        if state_before_pause == 8:
            puede_jugar_8 = True
            if not ganar_reinicio8 == 0:
                x1_8 = None
                y1_8 = None
            ocultar_todos_los_cuadros_8()
            game_state = 'eighthcard'
            reinicio = False
            ganar8 = False
            perder8 = False
            back_window = False
            next_window = False
            aux_cronometro8 = True 
            acierto_8 = 0
            error_8 = 0
            used_time_8 = 0
            unused_time_8 = 0
            ganar_reinicio8 = 0
        if state_before_pause == 9:
            puede_jugar_9 = True
            if not ganar_reinicio8 == 0:
                x1_9 = None
                y1_9 = None
            ocultar_todos_los_cuadros_9()
            game_state = 'ninthcard'
            reinicio = False
            ganar9 = False
            perder9 = False
            back_window = False
            next_window = False
            aux_cronometro9 = True 
            acierto_9 = 0
            error_9 = 0
            used_time_9 = 0
            unused_time_9 = 0
            ganar_reinicio9 = 0
        if state_before_pause == 10:
            puede_jugar_10 = True
            if not ganar_reinicio10 == 0:
                x1_10 = None
                y1_10 = None
            ocultar_todos_los_cuadros_10()
            game_state = 'tenthcard'
            reinicio = False
            ganar10 = False
            perder10 = False
            back_window = False
            next_window = False
            aux_cronometro10 = True 
            acierto_10 = 0
            error_10 = 0
            used_time_10 = 0
            unused_time_10 = 0
            ganar_reinicio10 = 0

    return (paused_game, game_state, ret_intro, cont_game, open_game, back_window, puede_jugar, ganar_rein1,
            aux_cronometro, reinicio, ganar1, acierto_1, error_1, used_time_1, unused_time_1,
            ganar2, acierto_2, error_2, used_time_2, unused_time_2, puede_jugar_2, perder2, ganar_reinicio2, 
            ganar3, acierto_3, error_3, used_time_3, unused_time_3, puede_jugar_3, perder3, ganar_reinicio3, 
            ganar4, acierto_4, error_4, used_time_4, unused_time_4, puede_jugar_4, perder4, ganar_reinicio4, x1_4, y1_4, 
            ganar5, acierto_5, error_5, used_time_5, unused_time_5, puede_jugar_5, perder5, ganar_reinicio5, x1_5, y1_5,
            ganar6, acierto_6, error_6, used_time_6, unused_time_6, puede_jugar_6, perder6, ganar_reinicio6, x1_6, y1_6,
            ganar7, acierto_7, error_7, used_time_7, unused_time_7, puede_jugar_7, perder7, ganar_reinicio7, x1_7, y1_7,
            ganar8, acierto_8, error_8, used_time_8, unused_time_8, puede_jugar_8, perder8, ganar_reinicio8, x1_8, y1_8,
            ganar9, acierto_9, error_9, used_time_9, unused_time_9, puede_jugar_9, perder9, ganar_reinicio9, x1_9, y1_9,
            ganar10, acierto_10, error_10, used_time_10, unused_time_10, puede_jugar_10, perder10, ganar_reinicio10, x1_10, y1_10)

def resultados():
    global LI, resultado
    global acierto_1, error_1, used_time_1, unused_time_1
    global acierto_2, error_2, used_time_2, unused_time_2
    global acierto_3, error_3, used_time_3, unused_time_3
    global acierto_4, error_4, used_time_4, unused_time_4
    global acierto_5, error_5, used_time_5, unused_time_5
    global acierto_6, error_6, used_time_6, unused_time_6
    global acierto_7, error_7, used_time_7, unused_time_7
    global acierto_8, error_8, used_time_8, unused_time_8
    global acierto_9, error_9, used_time_9, unused_time_9
    global acierto_10, error_10, used_time_10, unused_time_10

    LI[0][0] = acierto_2
    LI[0][1] = error_2
    LI[0][2] = used_time_2
    LI[0][3] = unused_time_2

    LI[1][0] = acierto_3
    LI[1][1] = error_3
    LI[1][2] = used_time_3
    LI[1][3] = unused_time_3

    LI[2][0] = acierto_4
    LI[2][1] = error_4
    LI[2][2] = used_time_4
    LI[2][3] = unused_time_4

    LI[3][0] = acierto_5
    LI[3][1] = error_5
    LI[3][2] = used_time_5
    LI[3][3] = unused_time_5

    LI[4][0] = acierto_6
    LI[4][1] = error_6
    LI[4][2] = used_time_6
    LI[4][3] = unused_time_6

    LI[5][0] = acierto_7
    LI[5][1] = error_7
    LI[5][2] = used_time_7
    LI[5][3] = unused_time_7

    LI[6][0] = acierto_8
    LI[6][1] = error_8
    LI[6][2] = used_time_8
    LI[6][3] = unused_time_8

    LI[7][0] = acierto_9
    LI[7][1] = error_9
    LI[7][2] = used_time_9
    LI[7][3] = unused_time_9

    LI[8][0] = acierto_10
    LI[8][1] = error_10
    LI[8][2] = used_time_10
    LI[8][3] = unused_time_10

    LI[9][0] = acierto_1
    LI[9][1] = error_1
    LI[9][2] = used_time_1
    LI[9][3] = unused_time_1

    resultado = str(LI) 
    return resultado
    
def reiniciar_variables():
    global open_game, game_state, sam, samuel, samantha, sami
    global start_timer_active, acierto_1, error_1, used_time_1, unused_time_1
    global start_timer_active_2, acierto_2, error_2, used_time_2, unused_time_2
    global start_timer_active_3, acierto_3, error_3, used_time_3, unused_time_3
    global start_timer_active_4, acierto_4, error_4, used_time_4, unused_time_4
    global start_timer_active_5, acierto_5, error_5, used_time_5, unused_time_5
    global start_timer_active_6, acierto_6, error_6, used_time_6, unused_time_6
    global start_timer_active_7, acierto_7, error_7, used_time_7, unused_time_7
    global start_timer_active_8, acierto_8, error_8, used_time_8, unused_time_8
    global start_timer_active_9, acierto_9, error_9, used_time_9, unused_time_9
    global start_timer_active_10, acierto_10, error_10, used_time_10, unused_time_10
    global ganar_reinicio2, x1_2, y1_2

    open_game = True
    game_state ='intro'

    sam = 0
    sami = 0
    samuel = 0 
    samantha = 0 

    #game_state = 'second_level'
    start_timer_active = False
    start_timer_active_2 = False
    start_timer_active_3 = False
    start_timer_active_4 = False
    start_timer_active_5 = False
    start_timer_active_6 = False
    start_timer_active_7 = False
    start_timer_active_8 = False
    start_timer_active_9 = False
    start_timer_active_10 = False

    acierto_1 = 0
    acierto_2 = 0
    acierto_3 = 0
    acierto_4 = 0
    acierto_5 = 0
    acierto_6 = 0
    acierto_7 = 0
    acierto_8 = 0
    acierto_9 = 0
    acierto_10 = 0

    error_1 = 0
    error_2 = 0
    error_3 = 0
    error_4 = 0
    error_5 = 0
    error_6 = 0
    error_7 = 0
    error_8 = 0
    error_9 = 0
    error_10 = 0

    used_time_1 = 0
    used_time_2 = 0
    used_time_3 = 0
    used_time_4 = 0
    used_time_5 = 0
    used_time_6 = 0
    used_time_7 = 0
    used_time_8 = 0
    used_time_9 = 0
    used_time_10 = 0

    unused_time_1 = 0
    unused_time_2 = 0
    unused_time_3 = 0
    unused_time_4 = 0
    unused_time_5 = 0
    unused_time_6 = 0
    unused_time_7 = 0
    unused_time_8 = 0
    unused_time_9 = 0
    unused_time_10 = 0



    return(open_game, game_state,sam, samuel, samantha, sami, 
           start_timer_active, acierto_1, error_1, used_time_1, unused_time_1,
           start_timer_active_2, acierto_2, error_2, used_time_2, unused_time_2,
           start_timer_active_3, acierto_3, error_3, used_time_3, unused_time_3,
           start_timer_active_4, acierto_4, error_4, used_time_4, unused_time_4,
           start_timer_active_5, acierto_5, error_5, used_time_5, unused_time_5,
           start_timer_active_6, acierto_6, error_6, used_time_6, unused_time_6,
           start_timer_active_7, acierto_7, error_7, used_time_7, unused_time_7,
           start_timer_active_8, acierto_8, error_8, used_time_8, unused_time_8,
           start_timer_active_9, acierto_9, error_9, used_time_9, unused_time_9,
           start_timer_active_10, acierto_10, error_10, used_time_10, unused_time_10)
