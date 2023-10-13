#   LIBRERIAS PROYECTO
import pygame
#   LIBRERIAS PROYECTO

# BOTONES
class Button():
    def __init__(self, x, y, image, scale):    # self, ejes xy, la imagen
        width = image.get_width() # Obtiene el ancho de la imagen cargada
        #print(width)
        height = image.get_height() # Obtiene el alto de la imagen cargada
        #print(height)
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale))) 
        self.rect = self.image.get_rect(center = (x,y)) # Obtener rectángulo de la imagen
        #self.rect.topleft = (x,y) # Posición rectángulo
        self.clicked = False # Estado de inicio botones, sin click

    def draw(self, surface): # Método de dibujo
        action = False #Variable
        # Obtener Posición Mouse
        pos = pygame.mouse.get_pos()
        # print(pos) # Imprime Posición Mouse

        # Verificar Mouse sobre img y condición de click
        if self.rect.collidepoint(pos): # Pregunta si el mouse está colisionando con el rectángulo
            #print ('Colisión') # Test de colisión
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: # Se debe escoger el botón del mouse (El izquierdo es 0)
                # print('Click') # Prueba Click, se debe ajustar para que al dar click solo se obtenga 1 click
                self.clicked = True
                # print('Click')
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False # Se reinicia la Condición del Click


        # Dibuja el botón en la pantalla
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action # Retorna el valor de action False o True para realizar acciones dependiendo del click sobre el botón
