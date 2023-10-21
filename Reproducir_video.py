
import cv2
import pygame
from moviepy.editor import *
from Config import *


def reproducir_video(ruta, width, height, velocidad):
    cap = cv2.VideoCapture(ruta)

    while cap.isOpened():
    # Capture frame-by-frame
        ret, frame = cap.read()

        # If the frame is read correctly, ret will be True
        if ret:
            # Resize the frame to the new dimensions
            
            frame = cv2.resize(frame, (width, height))
            cv2.namedWindow('Frame',cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty('Frame',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

            # Display the resulting frame
            cv2.imshow('Frame', frame)

            # Ajusta el tiempo de espera para acelerar la reproducción (más pequeño = más rápido)
            if cv2.waitKey(velocidad) & 0xFF == ord('a'):
                break
        else:
        # Break the loop if there are no more frames to read
            break

    # Release the video capture object
    cap.release()

    # Close all the frames
    cv2.destroyAllWindows()

    pygame.display.update()

def imagenes(imagen1, imagen2, imagen3, imagen4, width, height):

    screen = pygame.display.set_mode((width, height))

    imagen_1 = 0
    imagen_2 = 0
    imagen_3 = 0
    imagen_4 = 0

    # Escalar las imágenes al tamaño deseado
    imagen1 = pygame.transform.scale(imagen1, ((width/2)-20,(height/2)-20))
    imagen2 = pygame.transform.scale(imagen2, ((width/2)-20,(height/2)-20))
    imagen3 = pygame.transform.scale(imagen3, ((width/2)-20,(height/2)-20))
    imagen4 = pygame.transform.scale(imagen4, ((width/2)-20,(height/2)-20))

    # Definir los rectángulos y sus posiciones
    rectangulo_rojo = pygame.Rect(imagen_1,imagen_1 , (width/2)-imagen_1,(height/2)-imagen_1)
    rectangulo_amarillo = pygame.Rect((width/2)+imagen_2,imagen_2, (width/2)-imagen_2,(height/2)-imagen_2)
    rectangulo_verde = pygame.Rect(imagen_3,(height/2)+imagen_3, (width/2)-imagen_3,(height/2)-imagen_3)
    rectangulo_azul = pygame.Rect((width/2)+imagen_4,(height/2)+imagen_4, (width/2)-imagen_4,(height/2)-imagen_4)

    rectangulo_rojo_1 = pygame.Rect(10,10 , (width/2)-10,(height/2)-10)
    rectangulo_amarillo_1 = pygame.Rect((width/2)+10,10 , (width/2)-10,(height/2)-10)
    rectangulo_verde_1 = pygame.Rect(10,(height/2)+10 , (width/2)-10,(height/2)-10)
    rectangulo_azul_1 = pygame.Rect((width/2)+10,(height/2)+10 , (width/2)-10,(height/2)-10)

    screen.fill(ROJO, rectangulo_rojo)
    screen.fill(AMARILLO, rectangulo_amarillo)
    screen.fill(VERDE, rectangulo_verde)
    screen.fill(AZUL, rectangulo_azul)

    screen.blit(imagen1, rectangulo_rojo_1)
    screen.blit(imagen2, rectangulo_amarillo_1)
    screen.blit(imagen3, rectangulo_verde_1)
    screen.blit(imagen4, rectangulo_azul_1)

    #pygame.display.flip()

def level_image(imagen1, imagen2, imagen3, imagen4, width, height):

    screen = pygame.display.set_mode((width, height))

    imagen_1 = 0
    imagen_2 = 0
    imagen_3 = 0
    imagen_4 = 0

    # Escalar las imágenes al tamaño deseado
    imagen1 = pygame.transform.scale(imagen1, ((width/2)-20,(height/2)-20))
    imagen2 = pygame.transform.scale(imagen2, ((width/2)-20,(height/2)-20))
    imagen3 = pygame.transform.scale(imagen3, ((width/2)-20,(height/2)-20))
    imagen4 = pygame.transform.scale(imagen4, ((width/2)-20,(height/2)-20))

    # Definir los rectángulos y sus posiciones
    rectangulo_rojo = pygame.Rect(imagen_1,imagen_1 , (width/2)-imagen_1,(height/2)-imagen_1)
    rectangulo_amarillo = pygame.Rect((width/2)+imagen_2,imagen_2, (width/2)-imagen_2,(height/2)-imagen_2)
    rectangulo_verde = pygame.Rect(imagen_3,(height/2)+imagen_3, (width/2)-imagen_3,(height/2)-imagen_3)
    rectangulo_azul = pygame.Rect((width/2)+imagen_4,(height/2)+imagen_4, (width/2)-imagen_4,(height/2)-imagen_4)

    rectangulo_rojo_1 = pygame.Rect(10,10 , (width/2)-10,(height/2)-10)
    rectangulo_amarillo_1 = pygame.Rect((width/2)+10,10 , (width/2)-10,(height/2)-10)
    rectangulo_verde_1 = pygame.Rect(10,(height/2)+10 , (width/2)-10,(height/2)-10)
    rectangulo_azul_1 = pygame.Rect((width/2)+10,(height/2)+10 , (width/2)-10,(height/2)-10)

    screen.fill(ROJO, rectangulo_rojo)
    screen.fill(AMARILLO, rectangulo_amarillo)
    screen.fill(VERDE, rectangulo_verde)
    screen.fill(AZUL, rectangulo_azul)

    screen.blit(imagen1, rectangulo_rojo_1)
    screen.blit(imagen2, rectangulo_amarillo_1)
    screen.blit(imagen3, rectangulo_verde_1)
    screen.blit(imagen4, rectangulo_azul_1)

    #pygame.display.flip()

def rep_video(ruta, width, height):
    clip = VideoFileClip(ruta).resize((width, height))
    ipython_display(clip,maxduration=10000000)
    pygame.mixer.music.load('Instrucciones.mp3') 
    pygame.mixer.music.play(1)
    clip.preview()
    pygame.display.update()


def arreglo(imagen, place, width, height):
    imagen = pygame.transform.scale(imagen, ((width/2)-20,(height/2)-20))

    if (place == 1):
        rect = pygame.Rect(10,10 , (width/2)-10,(height/2)-10)

    if (place == 2):
        rect = pygame.Rect((width/2)+10,10 , (width/2)-10,(height/2)-10)
    
    if (place == 3):
        rect =  pygame.Rect(10,(height/2)+10 , (width/2)-10,(height/2)-10)
    
    if (place == 4):
        rect = pygame.Rect((width/2)+10,(height/2)+10 , (width/2)-10,(height/2)-10)
    
    return imagen, rect

def rectangulos(width, height):

    #screen = pygame.display.set_mode((width, height))

    rectangulo_rojo = pygame.Rect(0,0 , (width/2),(height/2))
    rectangulo_amarillo = pygame.Rect((width/2),0, (width/2),(height/2))
    rectangulo_verde = pygame.Rect(0,(height/2), (width/2),(height/2))
    rectangulo_azul = pygame.Rect((width/2),(height/2), (width/2),(height/2))

    screen.fill(ROJO, rectangulo_rojo)
    screen.fill(AMARILLO, rectangulo_amarillo)
    screen.fill(VERDE, rectangulo_verde)
    screen.fill(AZUL, rectangulo_azul)
