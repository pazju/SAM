import pygame   
from pygame.locals import *
import os
import ATENCION
import results
import teclado
import SLOGICA
import MEMORIA



pygame.init()
pygame.mixer.init() # Inicializar el mezclador porque se van a utilizar sonidos

os.environ['SDL_VIDEO_CENTERED'] = '1' # Después de pygame.init()
info = pygame.display.Info() # Antes de set_mode()
screen_width, screen_height = info.current_w, info.current_h

# COLORS
# https://htmlcolorcodes.com/es/tabla-de-colores/
color_red = (255,0,0)
color_white = (255,255,255)
color_black = (0,0,0)
color_purple = (142,68,173)
color_bluep = (33,97,140)

# SOUNDS

print (screen_width, screen_height)
# DIMENSIONES DISPONIBLES
# Pantalla de mi PC [1366x768]
# Monitor [1920x1080]
# TV 32" [1360x768]

#screen = pygame.display.set_mode((screen_width,screen_height))
screen = pygame.display.set_mode((screen_width , screen_height ))
pygame.display.set_caption('Juego Atención')
clock = pygame.time.Clock()
fps = 60
# game variables


tile_size_x = round(screen_width/20)
tile_size_y = round(screen_height/16)
tiles_x = screen_width/tile_size_x
tiles_y = screen_height/tile_size_y
#tile_size = 100

# Images
inicio_img = pygame.image.load("Assets/menu/inicio.png")
inicio_img = pygame.transform.scale(inicio_img, (tile_size_x*20, tile_size_y*16))
inicio_rect = inicio_img.get_rect(center = (tile_size_x*10,tile_size_y*8))
menu_img = pygame.image.load("Assets/menu/main_menu.png")
menu_img = pygame.transform.scale(menu_img, (tile_size_x*20, tile_size_y*16))
menu_rect = menu_img.get_rect(center = (tile_size_x*10,tile_size_y*8))
sam_img = pygame.image.load("Assets/Character/SPRITES/g0.png")
sam_img = pygame.transform.scale(sam_img, (tile_size_x*2, tile_size_y*2.3))
sam_rect = sam_img.get_rect(center = (tile_size_x*10,tile_size_y*4.9))
off_img = pygame.image.load("Assets/menu/off.png")
off_img = pygame.transform.scale(off_img, (tile_size_x*20, tile_size_y*16))
off_rect = off_img.get_rect(center = (tile_size_x*10,tile_size_y*8))
# continue_img = pygame.image.load("Assets/Icons/Kenney_gameIcons/PNG/Black/2x/fastForward.png")
# exit_img = pygame.image.load("Assets/Icons/Kenney_gameIcons/PNG/Black/2x/exit.png")
# restart_img = pygame.image.load("Assets/Icons/Kenney_gameIcons/PNG/Black/2x/return.png")
# start_img = pygame.image.load("Assets/Icons/Kenney_gameIcons/PNG/Black/2x/next.png")

# Texto en pantalla
def draw_text(text, size, text_col, x, y):
    font = pygame.font.SysFont("adobedevanagaribold", size)
    text_surface = font.render(text, True, text_col)
    text_rect = text_surface.get_rect()
    text_rect.center = (x,y)
    screen.blit(text_surface, text_rect)

# INICIALIZACIÓN MATRICES RESULTADOS
LI = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
PAZ = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
LAU = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
paciente = 'Jugador_1'
level = 'INICIO' # 
run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and level == 'INICIO': # Pantalla Nuevo Jugador
                level = 'JUGADOR'
            if event.key == pygame.K_i and level == 'INICIO': # Pantalla de Apagado
                level = 'APAGADO'    
            if event.key == pygame.K_s and level == 'MAIN_MENU': # Pantalla Nuevo Jugador
                LI = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
                PAZ = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
                LAU = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
                level = 'JUGADOR'
            if event.key == pygame.K_i and level == 'MAIN_MENU': # Pantalla de Apagado
                level = 'APAGADO'
            if event.key == pygame.K_n and level == 'MAIN_MENU': # Iniciar Juego Atención
                level = 'ATENCION'
            if event.key == pygame.K_e and level == 'MAIN_MENU': # Iniciar Juego Memoria
                level = 'MEMORIA'
            if event.key == pygame.K_c and level == 'MAIN_MENU': # Iniciar Juego Secuencia
                level = 'SECUENCIA'
            if event.key == pygame.K_v and level == 'APAGADO': # Volver al Menú Principal
                level = 'MAIN_MENU'    
            if event.key == pygame.K_c and level == 'APAGADO': # Apagar Sistema
                os.system("shutdown /s /t 1")
                run = False 
        if event.type == pygame.QUIT:
            run = False

    if level == 'INICIO':
        screen.blit(inicio_img, inicio_rect) # Fondo Pantalla Final  
        screen.blit(sam_img, sam_rect) # Fondo Pantalla Final 

    if level == 'MAIN_MENU':
        screen.blit(menu_img, menu_rect) # Fondo Pantalla Menu
        screen.blit(sam_img, sam_rect) # Imagen SAM (Personaje) 
    
    if level == 'JUGADOR':
        paciente = teclado.virtual_keyboard()
        level = 'MAIN_MENU'

    if level == 'APAGADO':
        screen.blit(off_img, off_rect) # Fondo Pantalla Apagado
        
    if level == 'ATENCION':
        PAZ = ATENCION.atencion(screen_width,screen_height) # Retorna level = 'MAIN_MENU' y PAZ = [Matriz de Resultados]
        results.results(paciente, LI, PAZ, LAU)
        print(PAZ)
        level = 'MAIN_MENU'
    if level == 'MEMORIA':
        LI = MEMORIA.memoria() # FUNCION JUEGO LIDA
        results.results(paciente, LI, PAZ, LAU)
        print(LI)
        level = 'MAIN_MENU'
    if level == 'SECUENCIA':
        LAU = SLOGICA.secuencia_logica() # FUNCION JUEGO LAU
        results.results(paciente, LI, PAZ, LAU)
        print(LAU)
        level = 'MAIN_MENU'
    
    

    pygame.display.update() ########
        
    
pygame.quit()





