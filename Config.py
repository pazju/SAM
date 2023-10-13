import pygame
pygame.init()

# Configuración de la pantalla
height = pygame.display.Info().current_h
width = pygame.display.Info().current_w
screen = pygame.display.set_mode((width, height))

# Configuración de fuentes
fuente = pygame.font.Font(None, 36)

# Colores 
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Imagen del click para la presentación de las tarjetas
click = pygame.image.load("FONDOS/Señalar.png")
click = pygame.transform.scale(click, (150,150))

# Rectangulos
rectangulo_r = click.get_rect(center=(width*3/8, height*3/8)) #Señala la tarjeta Rojo
rectangulo_a = click.get_rect(center=(width*7/8, height*3/8)) #Señala la tarjeta Amarillo 
rectangulo_v = click.get_rect(center=(width*3/8, height*7/8)) #Señala la tarjeta Verde
rectangulo_b = click.get_rect(center=(width*7/8, height*7/8)) #Señala la tarjeta Azul

rectangulo_rojo = pygame.Rect(0,0 , (width/2),(height/2))
rectangulo_amarillo = pygame.Rect((width/2),0, (width/2),(height/2))
rectangulo_verde = pygame.Rect(0,(height/2), (width/2),(height/2))
rectangulo_azul = pygame.Rect((width/2),(height/2), (width/2),(height/2))

rectangulo_rojo_1 = pygame.Rect(10,10 , (width/2)-10,(height/2)-10)
rectangulo_amarillo_1 = pygame.Rect((width/2)+10,10 , (width/2)-10,(height/2)-10)
rectangulo_verde_1 = pygame.Rect(10,(height/2)+10 , (width/2)-10,(height/2)-10)
rectangulo_azul_1 = pygame.Rect((width/2)+10,(height/2)+10 , (width/2)-10,(height/2)-10)


# Variables de resultados
tiempo_utilizado = 120  # Reemplaza con el valor real
tiempo_restante = 60  # Reemplaza con el valor real
aciertos = 5  # Reemplaza con el valor real
errores = 2  # Reemplaza con el valor real
intentos = 7  # Reemplaza con el valor real
aux_tiempo = 0
aux_intento = 0


#.... Sonidos .............  #
# Nivel 1 
sL0_1 = pygame.mixer.Sound("AUDIOS/intro_1.mp3")
sL0_2 = pygame.mixer.Sound("AUDIOS/intro_2.mp3")
sL0_3 = pygame.mixer.Sound("AUDIOS/Instrucciones.mp3")
sL0_4 = pygame.mixer.Sound("AUDIOS/Intro_personaje.mp3")
sL0_5 = pygame.mixer.Sound("AUDIOS/descripcion_n0.mp3")
sL0_6 = pygame.mixer.Sound("AUDIOS/logro.mp3")
sL0_7 = pygame.mixer.Sound("AUDIOS/Mal.mp3")

sL1_1 = pygame.mixer.Sound('AUDIOS/descripcion_n1.mp3') 