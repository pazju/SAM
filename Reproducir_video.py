
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
