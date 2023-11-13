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
# Nivel 0
sL0_1 = pygame.mixer.Sound("AUDIOS/synthesize (53).mp3")
sL0_2 = pygame.mixer.Sound("AUDIOS/Instrucciones.mp3")
sL0_3 = pygame.mixer.Sound("AUDIOS/synthesize (70).mp3")
sL0_4 = pygame.mixer.Sound("AUDIOS/synthesize (5).mp3")
# Tarjetas
sL0_5 = pygame.mixer.Sound("AUDIOS/synthesize (6).mp3")
sL0_6 = pygame.mixer.Sound("AUDIOS/synthesize (7).mp3")
sL0_7 = pygame.mixer.Sound("AUDIOS/synthesize (8).mp3")
sL0_8 = pygame.mixer.Sound("AUDIOS/synthesize (9).mp3")

# Se acabó el tiempo
sL0_9 = pygame.mixer.Sound("AUDIOS/synthesize (10).mp3")

# Nivel 1
sL1_1 = pygame.mixer.Sound("AUDIOS/synthesize (11).mp3")
# Tarjetas
sL1_2 = pygame.mixer.Sound("AUDIOS/synthesize (12).mp3")
sL1_3 = pygame.mixer.Sound("AUDIOS/synthesize (13).mp3")
sL1_4 = pygame.mixer.Sound("AUDIOS/synthesize (14).mp3")
sL1_5 = pygame.mixer.Sound("AUDIOS/synthesize (15).mp3")

# Nivel 2
sL2_1 = pygame.mixer.Sound("AUDIOS/synthesize (16).mp3")
# Tarjetas
sL2_2 = pygame.mixer.Sound("AUDIOS/synthesize (17).mp3")
sL2_3 = pygame.mixer.Sound("AUDIOS/synthesize (18).mp3")
sL2_4 = pygame.mixer.Sound("AUDIOS/synthesize (19).mp3")
sL2_5 = pygame.mixer.Sound("AUDIOS/synthesize (20).mp3")

# Nivel 3
sL3_1 = pygame.mixer.Sound("AUDIOS/synthesize (80).mp3")
# Tarjetas
sL3_2 = pygame.mixer.Sound("AUDIOS/synthesize (22).mp3")
sL3_3 = pygame.mixer.Sound("AUDIOS/synthesize (23).mp3")
sL3_4 = pygame.mixer.Sound("AUDIOS/synthesize (72).mp3")
sL3_5 = pygame.mixer.Sound("AUDIOS/synthesize (25).mp3")

# Nivel 4
sL4_1 = pygame.mixer.Sound("AUDIOS/synthesize (73).mp3")
# Tarjetas
sL4_2 = pygame.mixer.Sound("AUDIOS/synthesize (27).mp3")
sL4_3 = pygame.mixer.Sound("AUDIOS/synthesize (28).mp3")
sL4_4 = pygame.mixer.Sound("AUDIOS/synthesize (29).mp3")
sL4_5 = pygame.mixer.Sound("AUDIOS/synthesize (30).mp3")

# Nivel 5
sL5_1 = pygame.mixer.Sound("AUDIOS/synthesize (81).mp3")
# Tarjetas
sL5_2 = pygame.mixer.Sound("AUDIOS/synthesize (32).mp3")
sL5_3 = pygame.mixer.Sound("AUDIOS/synthesize (33).mp3")
sL5_4 = pygame.mixer.Sound("AUDIOS/synthesize (34).mp3")
sL5_5 = pygame.mixer.Sound("AUDIOS/synthesize (33).mp3")

# Nivel 6
sL6_1 = pygame.mixer.Sound("AUDIOS/synthesize (75).mp3")
# Tarjetas
sL6_2 = pygame.mixer.Sound("AUDIOS/synthesize (36).mp3")
sL6_3 = pygame.mixer.Sound("AUDIOS/synthesize (37).mp3")
sL6_4 = pygame.mixer.Sound("AUDIOS/synthesize (38).mp3")
sL6_5 = pygame.mixer.Sound("AUDIOS/synthesize (39).mp3")

# Nivel 7
sL7_1 = pygame.mixer.Sound("AUDIOS/synthesize (76).mp3")
# Tarjetas
sL7_2 = pygame.mixer.Sound("AUDIOS/synthesize (40).mp3")
sL7_3 = pygame.mixer.Sound("AUDIOS/synthesize (41).mp3")
sL7_4 = pygame.mixer.Sound("AUDIOS/synthesize (42).mp3")
sL7_5 = pygame.mixer.Sound("AUDIOS/synthesize (43).mp3")

# Nivel 8
sL8_1 = pygame.mixer.Sound("AUDIOS/synthesize (77).mp3")
# Tarjetas
sL8_2 = pygame.mixer.Sound("AUDIOS/synthesize (45).mp3")
sL8_3 = pygame.mixer.Sound("AUDIOS/synthesize (46).mp3")
sL8_4 = pygame.mixer.Sound("AUDIOS/synthesize (47).mp3")
sL8_5 = pygame.mixer.Sound("AUDIOS/synthesize (48).mp3")

# Nivel 9
sL9_1 = pygame.mixer.Sound("AUDIOS/synthesize (78).mp3")
# Tarjetas
sL9_2 = pygame.mixer.Sound("AUDIOS/synthesize (49).mp3")
sL9_3 = pygame.mixer.Sound("AUDIOS/synthesize (50).mp3")
sL9_4 = pygame.mixer.Sound("AUDIOS/synthesize (51).mp3")
sL9_5 = pygame.mixer.Sound("AUDIOS/synthesize (52).mp3")
sL_10 = pygame.mixer.Sound("AUDIOS/synthesize (82).mp3") 
