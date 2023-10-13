
import cv2
import pygame
import sys
import time
from Config import *
import Reproducir_video as rv
import os
# Inicialización de pygame
#pygame.init()
# Inicio para reproduccion de sonidos
def secuencia_logica():
    pygame.mixer.init()

    # Variables del cronometro
    fuente_inicio_timer = pygame.font.SysFont("adobedevanageriblod",100)
    tiempo_inicio = 10
    texto_tiempo_inicio = fuente_inicio_timer.render(str(tiempo_inicio),True, WHITE)

    # Variables de duración del nivel
    fuente_timer = pygame.font.SysFont("adobedevanageriblod",100)
    tiempo = 10
    texto_tiempo = fuente_inicio_timer.render(str(tiempo),True, WHITE)

    evento_tiempo = pygame.USEREVENT+1 # ID de evento, en este caso 25 ya que pygame usa los primeros 23
    pygame.time.set_timer(evento_tiempo, 1000)

    timer_activo_inicio = False
    timer_activo = False
    
    # Estados
    estado = 'MENU'
    estado_anterior = 'MENU'

    levelEND_img = pygame.image.load("FONDOS/Fondo Saludarte.png")
    levelEND_img = pygame.transform.scale(levelEND_img, (50,80))
    #levelEND_rect = levelEND_img.get_rect(center = (50,80))


    channel = pygame.mixer.Channel(0)

    # Variables Booleanas

    tiempo_activo = False
    aux = True

    t_roja = False
    t_verde = False
    t_azul = False
    t_amarillo = False

    begin = False
    run = True

    reinicio = False


    # Variables No Boleanas.
    nivel = 0
    intento = 2
    temporal = 0
    temporal_n0 = 0
    velocidad = 0
    unico = 0

    #********** Declaración Matriz de Resultados *************
    matriz = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
    ];


    '''# Imagen del click para la presentación de las tarjetas
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
    rectangulo_azul_1 = pygame.Rect((width/2)+10,(height/2)+10 , (width/2)-10,(height/2)-10)'''

    # Imagenes tarjetas nivel 0
    imagen_n0_1 = pygame.image.load("FONDOS/nivel0_rojo.jpg")
    #imagen_n0_1, rect_imagen_n1_1 = rv.arreglo(imagen_n0_1,1)
    imagen_n0_1, rect_imagen_n0_1 = rv.arreglo(imagen_n0_1,1,width,height)

    imagen_n0_2 = pygame.image.load("FONDOS/nivel0_amarillo.jpg")
    #imagen_n0_2, rect_imagen_n1_2 = rv.arreglo(imagen_n0_2,2)
    imagen_n0_2, rect_imagen_n0_2 = rv.arreglo(imagen_n0_2,2,width,height)

    imagen_n0_3 = pygame.image.load("FONDOS/nivel0_verde.jpg")
    #imagen_n0_3, rect_imagen_n1_3 = rv.arreglo(imagen_n0_3,3)
    imagen_n0_3, rect_imagen_n0_3 = rv.arreglo(imagen_n0_3,3,width,height)

    imagen_n0_4 = pygame.image.load("FONDOS/nivel0_azul.jpg")
    #imagen_n0_4, rect_imagen_n1_4 = rv.arreglo(imagen_n0_4,4)
    imagen_n0_4, rect_imagen_n0_4 = rv.arreglo(imagen_n0_4,4,width,height)


    # Imagenes tarjetas nivel 1
    imagen_n1_1 = pygame.image.load("FONDOS/49.jpg")
    imagen_n1_1, rect_imagen_n1_1 = rv.arreglo(imagen_n1_1,1,width,height)

    imagen_n1_2 = pygame.image.load("FONDOS/50.jpg")
    imagen_n1_2, rect_imagen_n1_2 = rv.arreglo(imagen_n1_2,2,width,height)

    imagen_n1_3 = pygame.image.load("FONDOS/51.jpg")
    imagen_n1_3, rect_imagen_n1_3 = rv.arreglo(imagen_n1_3,3,width,height)

    imagen_n1_4 = pygame.image.load("FONDOS/52.jpg")
    imagen_n1_4, rect_imagen_n1_4 = rv.arreglo(imagen_n1_4,4,width,height)


    # Imagenes tarjetas nivel 2
    imagen_n2_1 = pygame.image.load("FONDOS/54.jpg")
    imagen_n2_1, rect_imagen_n2_1 = rv.arreglo(imagen_n2_1,1,width,height)

    imagen_n2_2 = pygame.image.load("FONDOS/70.jpg")
    imagen_n2_2, rect_imagen_n2_2 = rv.arreglo(imagen_n2_2,2,width,height)

    imagen_n2_3 = pygame.image.load("FONDOS/68.jpg")
    imagen_n2_3, rect_imagen_n2_3 = rv.arreglo(imagen_n2_3,3,width,height)

    imagen_n2_4 = pygame.image.load("FONDOS/69.jpg")
    imagen_n2_4, rect_imagen_n2_4 = rv.arreglo(imagen_n2_4,4,width,height)

    # Imagenes tarjetas nivel 3
    imagen_n3_1 = pygame.image.load("FONDOS/54.jpg")
    imagen_n3_1, rect_imagen_n3_1 = rv.arreglo(imagen_n3_1,1,width,height)

    imagen_n3_2 = pygame.image.load("FONDOS/70.jpg")
    imagen_n3_2, rect_imagen_n3_2 = rv.arreglo(imagen_n3_2,2,width,height)

    imagen_n3_3 = pygame.image.load("FONDOS/71.jpg")
    imagen_n3_3, rect_imagen_n3_3 = rv.arreglo(imagen_n3_3,3,width,height)

    imagen_n3_4 = pygame.image.load("FONDOS/50.jpg")
    imagen_n3_4, rect_imagen_n3_4 = rv.arreglo(imagen_n3_4,4,width,height)


    # Imagenes tarjetas nivel 4
    imagen_n4_1 = pygame.image.load("FONDOS/55.jpg")
    imagen_n4_1, rect_imagen_n4_1 = rv.arreglo(imagen_n4_1,1,width,height)

    imagen_n4_2 = pygame.image.load("FONDOS/58.jpg")
    imagen_n4_2, rect_imagen_n4_2 = rv.arreglo(imagen_n4_2,2,width,height)

    imagen_n4_3 = pygame.image.load("FONDOS/59.jpg")
    imagen_n4_3, rect_imagen_n4_3 = rv.arreglo(imagen_n4_3,3,width,height)

    imagen_n4_4 = pygame.image.load("FONDOS/60.jpg")
    imagen_n4_4, rect_imagen_n4_4 = rv.arreglo(imagen_n4_4,4,width,height)


    # Imagenes tarjetas nivel 5
    imagen_n5_1 = pygame.image.load("FONDOS/61.jpg")
    imagen_n5_1, rect_imagen_n5_1 = rv.arreglo(imagen_n5_1,1,width,height)

    imagen_n5_2 = pygame.image.load("FONDOS/57.jpg")
    imagen_n5_2, rect_imagen_n5_2 = rv.arreglo(imagen_n5_2,2,width,height)

    imagen_n5_3 = pygame.image.load("FONDOS/62.jpg")
    imagen_n5_3, rect_imagen_n5_3 = rv.arreglo(imagen_n5_3,3,width,height)

    imagen_n5_4 = pygame.image.load("FONDOS/60.jpg")
    imagen_n5_4, rect_imagen_n5_4 = rv.arreglo(imagen_n5_4,4,width,height)

    #******+++++++++++++++ Falta ***************
    # Imagenes tarjetas nivel 6
    imagen_n6_1 = pygame.image.load("FONDOS/49.jpg")
    imagen_n6_1, rect_imagen_n6_1 = rv.arreglo(imagen_n6_1,1,width,height)

    imagen_n6_2 = pygame.image.load("FONDOS/50.jpg")
    imagen_n6_2, rect_imagen_n6_2 = rv.arreglo(imagen_n6_2,2,width,height)

    imagen_n6_3 = pygame.image.load("FONDOS/51.jpg")
    imagen_n6_3, rect_imagen_n6_3 = rv.arreglo(imagen_n6_3,3,width,height)

    imagen_n6_4 = pygame.image.load("FONDOS/52.jpg")
    imagen_n6_4, rect_imagen_n6_4 = rv.arreglo(imagen_n6_4,4,width,height)


    # Imagenes tarjetas nivel 7
    imagen_n7_1 = pygame.image.load("FONDOS/54.jpg")
    imagen_n7_1, rect_imagen_n7_1 = rv.arreglo(imagen_n7_1,1,width,height)

    imagen_n7_2 = pygame.image.load("FONDOS/70.jpg")
    imagen_n7_2, rect_imagen_n7_2 = rv.arreglo(imagen_n7_2,2,width,height)

    imagen_n7_3 = pygame.image.load("FONDOS/68.jpg")
    imagen_n7_3, rect_imagen_n7_3 = rv.arreglo(imagen_n7_3,3,width,height)

    imagen_n7_4 = pygame.image.load("FONDOS/69.jpg")
    imagen_n7_4, rect_imagen_n7_4 = rv.arreglo(imagen_n7_4,4,width,height)


    # Imagenes tarjetas nivel 8
    imagen_n8_1 = pygame.image.load("FONDOS/54.jpg")
    imagen_n8_1, rect_imagen_n8_1 = rv.arreglo(imagen_n8_1,1,width,height)

    imagen_n8_2 = pygame.image.load("FONDOS/70.jpg")
    imagen_n8_2, rect_imagen_n8_2 = rv.arreglo(imagen_n8_2,2,width,height)

    imagen_n8_3 = pygame.image.load("FONDOS/71.jpg")
    imagen_n8_3, rect_imagen_n8_3 = rv.arreglo(imagen_n8_3,3,width,height)

    imagen_n8_4 = pygame.image.load("FONDOS/50.jpg")
    imagen_n8_4, rect_imagen_n8_4 = rv.arreglo(imagen_n8_4,4,width,height)


    # Imagenes tarjetas nivel 9
    imagen_n9_1 = pygame.image.load("FONDOS/55.jpg")
    imagen_n9_1, rect_imagen_n9_1 = rv.arreglo(imagen_n9_1,1,width,height)

    imagen_n9_2 = pygame.image.load("FONDOS/58.jpg")
    imagen_n9_2, rect_imagen_n9_2 = rv.arreglo(imagen_n9_2,2,width,height)

    imagen_n9_3 = pygame.image.load("FONDOS/59.jpg")
    imagen_n9_3, rect_imagen_n9_3 = rv.arreglo(imagen_n9_3,3,width,height)

    imagen_n9_4 = pygame.image.load("FONDOS/60.jpg")
    imagen_n9_4, rect_imagen_n9_4 = rv.arreglo(imagen_n9_4,4,width,height)

    # Fondo para los resultados
    resultados = pygame.image.load("FONDOS/result.jpg")
    resultados = pygame.transform.scale(resultados,(width,height))

    # Variables de duración del nivel
    fuente_resultados = pygame.font.SysFont("adobedevanageriblod",200)
    errores = 10
    texto_resultados = fuente_resultados.render(str(errores),True, BLACK)



    aux_estado = 'MENU'

    while (run):

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s: # Cerrar juego con tecla "Q", actualmente
                    run = False
                    return matriz
                if event.key == pygame.K_p:
                    estado = 'PAUSA'
# Reiniciar
                if event.key == pygame.K_o:
                    if (estado == 'RESULTADOS'):
                        reinicio = True
                        estado = estado_anterior
                    if (estado == 'T0'):
                        reinicio = True
                        estado = estado_anterior
                else:
                    reinicio = False

    # Si se arriba o Tarjeta Roja
                if event.key == pygame.K_v:
                    t_roja = True
                else: 
                    t_roja = False

    # Si se arriba o Tarjeta Amarilla
                if event.key == pygame.K_n:
                    t_amarillo = True
                else: 
                    t_amarillo = False

    # Si se arriba o Tarjeta Verde
                if event.key == pygame.K_c:
                    t_verde = True
                else:
                    t_verde = False

    # Si se arriba o Tarjeta Azul
                if event.key == pygame.K_e:
                    t_azul = True
                else: 
                    t_azul = False

    # Si se presiona a se continua
                if (event.key == pygame.K_a):
                    if  estado == 'MENU':
                        estado = 'INTRO'
                    if(estado == 'PAUSA'):
                        estado = estado_anterior
                    if(estado == 'RESULTADOS'):
                        estado = aux_estado

            if event.type == pygame.QUIT:
                run = False
            

            if ((event.type == evento_tiempo) and (begin == True)):
                begin = False
                tiempo_inicio = tiempo_inicio - 1

                if(tiempo_inicio > 0): # Si no se ha acabado el tiempo de inicio ninguna tarjeta será verdadera
                    t_roja = False
                    t_verde = False
                    t_amarillo = False
                    t_azul = False

                #texto_tiempo_inicio = fuente_inicio_timer.render(str(tiempo_inicio),True, BLACK)
                #print(tiempo_inicio)
                if tiempo_inicio <= 0:
                    tiempo_inicio = 0
                    aux = False
                    tiempo_activo = True
                    tiempo = tiempo-1
                    #print("Tiempo:",tiempo)
                    if(tiempo == 0):
                        estado = 'T0'
                        T0 = True
                        tiempo_activo = False
                    else:
                        T0 = False

        if estado == 'PAUSA':
            pygame.mixer.Channel.stop(channel)
            image = pygame.image.load("FONDOS/pausa.jpg").convert()
            imagen = pygame.transform.scale(image, (width,height))
            screen.blit(imagen, (0, 0))
            pygame.display.flip()
            pygame.display.update()
        
        if estado == 'RESULTADOS':
            #rect_resultados = texto_resultados.get_rect(center=screen.get_rect().center)
            #screen.blit(texto_resultados, rect_resultados)
            #reinicio = True

            screen.blit(resultados, (0, 0))

            linea1 = f"Tiempo utilizado: {tiempo_restante}"
            linea2 = f"Tiempo restante: {tiempo_utilizado}"
            linea3 = f"Aciertos: {aciertos}"
            linea4 = f"Errores: {errores}"
            linea5 = f"Número de intentos: {intentos}"

            matriz[nivel][0]= tiempo_restante
            matriz[nivel][1]= tiempo_utilizado
            matriz[nivel][2]= aciertos
            matriz[nivel][3]= errores
            matriz[nivel][4]= intentos

            # Obtener el rectángulo de cada línea de texto
            rect_linea1 = fuente.render(linea1, True, BLACK).get_rect()
            rect_linea2 = fuente.render(linea2, True, BLACK).get_rect()
            rect_linea3 = fuente.render(linea3, True, BLACK).get_rect()
            rect_linea4 = fuente.render(linea4, True, BLACK).get_rect()
            rect_linea5 = fuente.render(linea5, True, BLACK).get_rect()

            # Centrar cada línea de texto en la pantalla
            rect_linea1.center = (width // 2, height// 2 - 100)
            rect_linea2.center = (width // 2, height // 2 - 50)
            rect_linea3.center = (width // 2, height // 2)
            rect_linea4.center = (width // 2, height // 2 + 50)
            rect_linea5.center = (width // 2, height // 2 + 100)

            screen.blit(fuente.render(linea1, True, BLACK), rect_linea1)
            screen.blit(fuente.render(linea2, True, BLACK), rect_linea2)
            screen.blit(fuente.render(linea3, True, BLACK), rect_linea3)
            screen.blit(fuente.render(linea4, True, BLACK), rect_linea4)
            screen.blit(fuente.render(linea5, True, BLACK), rect_linea5)

            pygame.display.flip()
            pygame.display.update()


        if estado == 'MENU':
            estado_anterior = estado
            if (unico == 0):
                unico = 1
                screen.fill(BLACK)
                print("Pantalla negra del Menu")
                pygame.display.update()
                channel.queue(sL0_1)
                #pygame.mixer.music.load('AUDIOS/intro_1.mp3') 
                #pygame.mixer.music.play(1)
                ruta = 'FONDOS/Intro.mp4'
                velocidad = 50
                rv.reproducir_video(ruta, width, height, velocidad)
                pygame.display.update()

                background_image = pygame.image.load("FONDOS/Menu.jpg").convert()
                background_image = pygame.transform.scale(background_image, (width,height))
                channel.queue(sL0_2)
                

            # Dibujar el fondo
            screen.blit(background_image, (0, 0))
            pygame.display.flip()

        if estado == 'INTRO':
            pygame.mixer.Channel.stop(channel)
            estado_anterior = estado
            unico = 2
            temporal = 1
            screen.fill(BLACK)
            print("Pantalla negra de la INTRO")
            pygame.display.update()
            channel.queue(sL0_3)
            '''pygame.mixer.music.load('AUDIOS/Instrucciones.mp3') 
            pygame.mixer.music.play(1)'''
            ruta = 'FONDOS/Instrucciones.mp4'
            velocidad = 25
            rv.reproducir_video(ruta, width, height, velocidad)
            introduccion = False
            nivel_prueba = True
            estado = 'NIVEL_0'
        
        if estado == 'T0':
            pygame.mixer.Channel.stop(channel)
            background_image = pygame.image.load("FONDOS/Fondo_baño.png").convert()
            screen.blit(background_image, (0, 0))
            pygame.display.flip()

    #........... Nivel 0 ..............#

        if estado == 'NIVEL_0':
            nivel = 0
            estado_anterior = estado
            begin = True

            tiempo_mostrar = max(tiempo_inicio, 0)
            texto_tiempo_inicio = fuente_inicio_timer.render(str(tiempo_mostrar), True, WHITE)

            t_mostrar = max(tiempo, 0)
            texto_tiempo = fuente_inicio_timer.render(str(t_mostrar), True, WHITE)

            if(temporal == 1 or reinicio == True):
                pygame.mixer.Channel.stop(channel)
                screen.fill(BLACK)
                pygame.display.update()
                aux = True
                aciertos = 0
                begin = True
                tiempo_activo = False
                intento = 2
                temporal = 2
                velocidad = 15
                tiempo_inicio = 23
                tiempo = 40
                aux_intento = intento
                aux_tiempo = tiempo
                timer_activo_inicio = False
                #print("Entro a la configuración de los timer del nivel 0")
                intro = 'FONDOS/Intro_personaje.mp4'
                channel.queue(sL0_4)
                #channel.queue(sL0_5)
                rv.reproducir_video(intro, width, height, velocidad)
                pygame.mixer.Channel.stop(channel)
                channel.queue(sL0_5)
                reinicio = False
                
                #print ("Entro al temporal = 1 del nivel 0")

            screen.fill(ROJO, rectangulo_rojo)
            screen.fill(AMARILLO, rectangulo_amarillo)
            screen.fill(VERDE, rectangulo_verde)
            screen.fill(AZUL, rectangulo_azul)


            #rv.imagenes(imagen1, imagen2, imagen3, imagen4, width, height)
            
            screen.blit(imagen_n0_1, rect_imagen_n0_1)
            screen.blit(imagen_n0_2, rect_imagen_n0_2)
            screen.blit(imagen_n0_3, rect_imagen_n0_3)
            screen.blit(imagen_n0_4, rect_imagen_n0_4)
            


            #rect_tiempo_inicio = texto_tiempo_inicio.get_rect(center = screen.get_rect().center)
            #rect_timer = texto_tiempo.get_rect(center = (68,46))
            #screen.blit(texto_tiempo_inicio, rect_tiempo_inicio)

            # Mostrar cronometro

            #print("Tiempo inicio",tiempo_inicio)
            # Asegurarse de que el tiempo mostrado no sea negativo
            #texto_tiempo_inicio = fuente_inicio_timer.render(str(tiempo_mostrar), True, WHITE)

            # Dibujar el cronómetro
            if(aux==True):
                rect_tiempo_inicio = texto_tiempo_inicio.get_rect(center=screen.get_rect().center)
                screen.blit(texto_tiempo_inicio, rect_tiempo_inicio)

            if(tiempo_activo == True):
                rect_tiempo = texto_tiempo.get_rect(center=screen.get_rect().center)
                screen.blit(texto_tiempo, rect_tiempo)

            if(16<tiempo_inicio<20):
                screen.blit(click, rectangulo_r)
                pygame.display.update()

            if(10<tiempo_inicio<16):
                screen.blit(click, rectangulo_a)
                pygame.display.update()
                
            if(5<tiempo_inicio<10):
                screen.blit(click, rectangulo_v)
                pygame.display.update()

            if(3<tiempo_inicio<5):
                screen.blit(click, rectangulo_b)
                pygame.display.update()

            if ((t_roja == True) and (tiempo_inicio <= 0) and ((nivel == 0) and (intento>=0))):    
                #print("Selecciono tarjeta Roja") 
                ruta = 'FONDOS/video_7.mp4' 
                #nivel = 1
                aciertos = 1
                #aux_estado = 'NIVEL_1'
                velocidad = 4
                channel.queue(sL0_6)
                rv.reproducir_video(ruta, width, height, velocidad)
                print ("Entro a la roja")
                begin = False
                estado = 'RESULTADOS'
                t_roja = False
            
            
            if ((t_amarillo == True) and (tiempo_inicio <= 0) and  ((nivel == 0) and (intento>=0))):   
                print("Selecciono tarjeta amarilla") 
                t_amarillo = False 
                aciertos = 0
                intento = intento - 1 
                ruta = 'FONDOS/video_6.mp4' 
                channel.queue(sL0_7)
                velocidad = 4
                rv.reproducir_video(ruta, width, height, velocidad)
                

            if ((t_verde == True) and (tiempo_inicio <= 0) and ((nivel == 0) and (intento>=0))):  
                print("Selecciono tarjeta verde") 
                t_verde = False  
                aciertos = 0
                intento = intento - 1
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)
                

            if ((t_azul == True) and (tiempo_inicio <= 0) and ((nivel == 0) and (intento>=0))): 
                print("Selecciono tarjeta azul") 
                t_azul = False
                aciertos = 0
                intento = intento - 1    
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)
                
            if ((intento == 0) or (aciertos == 1)):
                tiempo_utilizado = tiempo # Reemplaza con el valor real
                tiempo_restante = aux_tiempo - tiempo  # Reemplaza con el valor real
                errores = aux_intento - intento  # Reemplaza con el valor real
                intentos = aux_intento # Reemplaza con el valor real
                print(tiempo_utilizado, tiempo_restante, errores, intentos)
                aux_estado = 'NIVEL_1'
                estado = 'RESULTADOS'
            
    #................ NIVEL 1 .................#

        if estado == 'NIVEL_1':
            nivel = 1
            estado_anterior = estado
            begin = True

            tiempo_mostrar = max(tiempo_inicio, 0)
            texto_tiempo_inicio = fuente_inicio_timer.render(str(tiempo_mostrar), True, WHITE)

            t_mostrar = max(tiempo, 0)
            texto_tiempo = fuente_inicio_timer.render(str(t_mostrar), True, WHITE)

            #print ("Inicio nivel 1, tiempo_inicio:",tiempo_inicio,",",tiempo)
            if(temporal == 2 or reinicio == True):
                temporal = 3
                pygame.mixer.Channel.stop(channel)
                screen.fill(BLACK)
                pygame.display.update()
                aux = True
                aciertos = 0
                begin = True
                tiempo_activo = False
                intento = 2
                tiempo_inicio = 26
                tiempo = 20
                #print ("Bucle temporal nivel 1 tiempo_inicio:",tiempo_inicio,",",tiempo)
                aux_intento = intento
                aux_tiempo = tiempo
                timer_activo_inicio = False
                #timer_activo_inicio = True
                #pygame.mixer.music.load('AUDIOS/descripcion_n1.mp3') 
                channel.queue(sL1_1)
            # pygame.mixer.music.play(1)
                pygame.display.update()
                reinicio = False

        # print("Nivel_1",tiempo_inicio)
            
            # Mostrar cronometro
            #begin = True
            '''tiempo_mostrar = max(tiempo_inicio, 0)
            texto_tiempo_inicio = fuente_inicio_timer.render(str(tiempo_mostrar), True, WHITE)

            t_mostrar = max(tiempo, 0)
            texto_tiempo = fuente_inicio_timer.render(str(t_mostrar), True, WHITE)'''

            screen.fill(ROJO, rectangulo_rojo)
            screen.fill(AMARILLO, rectangulo_amarillo)
            screen.fill(VERDE, rectangulo_verde)
            screen.fill(AZUL, rectangulo_azul)
            
            screen.blit(imagen_n1_1, rect_imagen_n1_1)
            screen.blit(imagen_n1_2, rect_imagen_n1_2)
            screen.blit(imagen_n1_3, rect_imagen_n1_3)
            screen.blit(imagen_n1_4, rect_imagen_n1_4)

            # Dibujar el cronómetro
            if(aux == True):
                rect_tiempo_inicio = texto_tiempo_inicio.get_rect(center=screen.get_rect().center)
                screen.blit(texto_tiempo_inicio, rect_tiempo_inicio)
                #print("Entro", tiempo_inicio)

            if(tiempo_activo == True):
                #print("Entro")
                rect_tiempo = texto_tiempo.get_rect(center=screen.get_rect().center)
                screen.blit(texto_tiempo, rect_tiempo)

                
            if(20<=tiempo_inicio<26):
                screen.blit(click, rectangulo_r)
                pygame.display.update()

            if(15<=tiempo_inicio<20):
                screen.blit(click, rectangulo_a)
                pygame.display.update()
                
            if(11<=tiempo_inicio<15):
                screen.blit(click, rectangulo_v)
                pygame.display.update()

            if(7<=tiempo_inicio<11):
                screen.blit(click, rectangulo_b)
                pygame.display.update()
                
            #pygame.display.update()

            if ((t_roja == True) and (nivel == 1) and (intento>=0) and (tiempo_inicio <= 0)):     
                
                t_roja = False
                aciertos = 0
                intento = intento - 1 
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)
            
            if ((t_amarillo == True) and (nivel == 1) and (intento>=0) and (tiempo_inicio <= 0)):   
                t_amarillo = False 
                aciertos = 1
                ruta = 'FONDOS/video_7.mp4' 
                velocidad = 4
                channel.queue(sL0_6)
                rv.reproducir_video(ruta, width, height, velocidad)
                nivel = 1
                nivel_prueba = False
                screen.fill(BLACK)
                #print ("Pantalla negra de t roja del nivel 1")
                pygame.display.update()
                
                

            if ((t_verde == True) and (nivel == 1) and (intento>=0) and (tiempo_inicio <= 0)):  
                t_verde = False  
                aciertos = 0
                intento = intento - 1
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)
                

            if ((t_azul == True) and ((nivel == 1) and (intento>=0)) and (tiempo_inicio <= 0)): 
                t_azul = False
                aciertos = 0
                intento = intento - 1    
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)

            if ((intento == 0) or (aciertos == 1)):
                tiempo_utilizado = tiempo # Reemplaza con el valor real
                tiempo_restante = aux_tiempo - tiempo  # Reemplaza con el valor real
                errores = aux_intento - intento  # Reemplaza con el valor real
                intentos = aux_intento # Reemplaza con el valor real
                print(tiempo_utilizado, tiempo_restante, errores, intentos)
                aux_estado = 'NIVEL_2'
                estado = 'RESULTADOS'
        
    #................ NIVEL 2 .................#
        if estado == 'NIVEL_2':
            nivel = 2
            estado_anterior = estado
            begin = True

            #if(temporal == 1 or reinicio == True):
            tiempo_mostrar = max(tiempo_inicio, 0)
            texto_tiempo_inicio = fuente_inicio_timer.render(str(tiempo_mostrar), True, WHITE)

            t_mostrar = max(tiempo, 0)
            texto_tiempo = fuente_inicio_timer.render(str(t_mostrar), True, WHITE)

            #print ("Inicio nivel 1, tiempo_inicio:",tiempo_inicio,",",tiempo)
            if(temporal == 3 or reinicio == True):
                temporal = 4
                pygame.mixer.Channel.stop(channel)
                screen.fill(BLACK)
                pygame.display.update()
                aux = True
                aciertos = 0
                begin = True
                tiempo_activo = False
                intento = 2
                tiempo_inicio = 26
                tiempo = 20
                #print ("Bucle temporal nivel 1 tiempo_inicio:",tiempo_inicio,",",tiempo)
                aux_intento = intento
                aux_tiempo = tiempo
                timer_activo_inicio = False
                #timer_activo_inicio = True
                #pygame.mixer.music.load('AUDIOS/descripcion_n1.mp3') 
                channel.queue(sL1_1)
            # pygame.mixer.music.play(1)
                pygame.display.update()
                reinicio = False
            
            # Mostrar cronometro

            screen.fill(ROJO, rectangulo_rojo)
            screen.fill(AMARILLO, rectangulo_amarillo)
            screen.fill(VERDE, rectangulo_verde)
            screen.fill(AZUL, rectangulo_azul)
            
            screen.blit(imagen_n2_1, rect_imagen_n2_1)
            screen.blit(imagen_n2_2, rect_imagen_n2_2)
            screen.blit(imagen_n2_3, rect_imagen_n2_3)
            screen.blit(imagen_n2_4, rect_imagen_n2_4)

            # Dibujar el cronómetro
            if(aux == True):
                rect_tiempo_inicio = texto_tiempo_inicio.get_rect(center=screen.get_rect().center)
                screen.blit(texto_tiempo_inicio, rect_tiempo_inicio)
                #print("Entro", tiempo_inicio)

            if(tiempo_activo == True):
                #print("Entro")
                rect_tiempo = texto_tiempo.get_rect(center=screen.get_rect().center)
                screen.blit(texto_tiempo, rect_tiempo)

                
            if(20<=tiempo_inicio<26):
                screen.blit(click, rectangulo_r)
                pygame.display.update()

            if(15<=tiempo_inicio<20):
                screen.blit(click, rectangulo_a)
                pygame.display.update()
                
            if(11<=tiempo_inicio<15):
                screen.blit(click, rectangulo_v)
                pygame.display.update()

            if(7<=tiempo_inicio<11):
                screen.blit(click, rectangulo_b)
                pygame.display.update()
                
            #pygame.display.update()

            if ((t_roja == True) and ((nivel == 2) and (intento>=0))):     
                t_roja = False
                aciertos = 0
                intento = intento - 1 
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)
            
            if ((t_amarillo == True) and ((nivel == 2) and (intento>=0))):   
                t_amarillo = False 
                aciertos = 0
                intento = intento - 1
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)
        

            if ((t_verde == True) and ((nivel == 2) and (intento>=0))):  
                t_verde = False 
                aciertos = 1 
                ruta = 'FONDOS/video_7.mp4' 
                velocidad = 4
                channel.queue(sL0_6)
                rv.reproducir_video(ruta, width, height, velocidad)
                

            if ((t_azul == True) and ((nivel == 2) and (intento>=0))): 
                t_azul = False
                aciertos = 0
                intento = intento - 1    
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)

            if ((intento == 0) or (aciertos == 1)):
                tiempo_utilizado = tiempo # Reemplaza con el valor real
                tiempo_restante = aux_tiempo - tiempo  # Reemplaza con el valor real
                errores = aux_intento - intento  # Reemplaza con el valor real
                intentos = aux_intento # Reemplaza con el valor real
                print(tiempo_utilizado, tiempo_restante, errores, intentos)
                aux_estado = 'NIVEL_3'
                estado = 'RESULTADOS'

    #................ NIVEL 3 .................#
        if estado == 'NIVEL_3':
            nivel = 3
            estado_anterior = estado
            begin = True

            #if(temporal == 1 or reinicio == True):
            tiempo_mostrar = max(tiempo_inicio, 0)
            texto_tiempo_inicio = fuente_inicio_timer.render(str(tiempo_mostrar), True, WHITE)

            t_mostrar = max(tiempo, 0)
            texto_tiempo = fuente_inicio_timer.render(str(t_mostrar), True, WHITE)

            #print ("Inicio nivel 1, tiempo_inicio:",tiempo_inicio,",",tiempo)
            if(temporal == 4 or reinicio == True):
                temporal = 5
                pygame.mixer.Channel.stop(channel)
                screen.fill(BLACK)
                pygame.display.update()
                aux = True
                aciertos = 0
                begin = True
                tiempo_activo = False
                intento = 2
                tiempo_inicio = 26
                tiempo = 20
                #print ("Bucle temporal nivel 1 tiempo_inicio:",tiempo_inicio,",",tiempo)
                aux_intento = intento
                aux_tiempo = tiempo
                timer_activo_inicio = False
                #timer_activo_inicio = True
                #pygame.mixer.music.load('AUDIOS/descripcion_n1.mp3') 
                channel.queue(sL1_1)
            # pygame.mixer.music.play(1)
                pygame.display.update()
                reinicio = False
            
            # Mostrar cronometro

            screen.fill(ROJO, rectangulo_rojo)
            screen.fill(AMARILLO, rectangulo_amarillo)
            screen.fill(VERDE, rectangulo_verde)
            screen.fill(AZUL, rectangulo_azul)
            
            screen.blit(imagen_n3_1, rect_imagen_n3_1)
            screen.blit(imagen_n3_2, rect_imagen_n3_2)
            screen.blit(imagen_n3_3, rect_imagen_n3_3)
            screen.blit(imagen_n3_4, rect_imagen_n3_4)

            # Dibujar el cronómetro
            if(aux == True):
                rect_tiempo_inicio = texto_tiempo_inicio.get_rect(center=screen.get_rect().center)
                screen.blit(texto_tiempo_inicio, rect_tiempo_inicio)
                #print("Entro", tiempo_inicio)

            if(tiempo_activo == True):
                #print("Entro")
                rect_tiempo = texto_tiempo.get_rect(center=screen.get_rect().center)
                screen.blit(texto_tiempo, rect_tiempo)

                
            if(20<=tiempo_inicio<26):
                screen.blit(click, rectangulo_r)
                pygame.display.update()

            if(15<=tiempo_inicio<20):
                screen.blit(click, rectangulo_a)
                pygame.display.update()
                
            if(11<=tiempo_inicio<15):
                screen.blit(click, rectangulo_v)
                pygame.display.update()

            if(7<=tiempo_inicio<11):
                screen.blit(click, rectangulo_b)
                pygame.display.update()
                
            #pygame.display.update()

            if ((t_roja == True) and ((nivel == 3) and (intento>=0)) and (tiempo_inicio <= 0)):     
                t_roja = False
                aciertos = 0
                intento = intento - 1 
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)
            
            if ((t_amarillo == True) and ((nivel == 3) and (intento>=0)) and (tiempo_inicio <= 0)):   
                t_amarillo = False 
                aciertos = 0
                intento = intento - 1
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)
        

            if ((t_verde == True) and ((nivel == 3) and (intento>=0)) and (tiempo_inicio <= 0)):  
                t_verde = False 
                aciertos = 1 
                ruta = 'FONDOS/video_7.mp4' 
                velocidad = 4
                channel.queue(sL0_6)
                rv.reproducir_video(ruta, width, height, velocidad)
                

            if ((t_azul == True) and ((nivel == 3) and (intento>=0)) and (tiempo_inicio <= 0)): 
                t_azul = False
                aciertos = 0
                intento = intento - 1    
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)

            if ((intento == 0) or (aciertos == 1)):
                tiempo_utilizado = tiempo # Reemplaza con el valor real
                tiempo_restante = aux_tiempo - tiempo  # Reemplaza con el valor real
                errores = aux_intento - intento  # Reemplaza con el valor real
                intentos = aux_intento # Reemplaza con el valor real
                print(tiempo_utilizado, tiempo_restante, errores, intentos)
                aux_estado = 'NIVEL_4'
                estado = 'RESULTADOS'

    #................ NIVEL 4 .................#

        if estado == 'NIVEL_4':
            nivel = 4
            estado_anterior = estado
            begin = True

            #if(temporal == 1 or reinicio == True):
            tiempo_mostrar = max(tiempo_inicio, 0)
            texto_tiempo_inicio = fuente_inicio_timer.render(str(tiempo_mostrar), True, WHITE)

            t_mostrar = max(tiempo, 0)
            texto_tiempo = fuente_inicio_timer.render(str(t_mostrar), True, WHITE)

            #print ("Inicio nivel 1, tiempo_inicio:",tiempo_inicio,",",tiempo)
            if(temporal == 5 or reinicio == True):
                temporal = 6
                pygame.mixer.Channel.stop(channel)
                screen.fill(BLACK)
                pygame.display.update()
                aux = True
                aciertos = 0
                begin = True
                tiempo_activo = False
                intento = 2
                tiempo_inicio = 26
                tiempo = 20
                #print ("Bucle temporal nivel 1 tiempo_inicio:",tiempo_inicio,",",tiempo)
                aux_intento = intento
                aux_tiempo = tiempo
                timer_activo_inicio = False
                #timer_activo_inicio = True
                #pygame.mixer.music.load('AUDIOS/descripcion_n1.mp3') 
                channel.queue(sL1_1)
            # pygame.mixer.music.play(1)
                pygame.display.update()
                reinicio = False
            
            # Mostrar cronometro

            screen.fill(ROJO, rectangulo_rojo)
            screen.fill(AMARILLO, rectangulo_amarillo)
            screen.fill(VERDE, rectangulo_verde)
            screen.fill(AZUL, rectangulo_azul)
            
            screen.blit(imagen_n4_1, rect_imagen_n4_1)
            screen.blit(imagen_n4_2, rect_imagen_n4_2)
            screen.blit(imagen_n4_3, rect_imagen_n4_3)
            screen.blit(imagen_n4_4, rect_imagen_n4_4)

            # Dibujar el cronómetro
            if(aux == True):
                rect_tiempo_inicio = texto_tiempo_inicio.get_rect(center=screen.get_rect().center)
                screen.blit(texto_tiempo_inicio, rect_tiempo_inicio)
                #print("Entro", tiempo_inicio)

            if(tiempo_activo == True):
                #print("Entro")
                rect_tiempo = texto_tiempo.get_rect(center=screen.get_rect().center)
                screen.blit(texto_tiempo, rect_tiempo)

                
            if(20<=tiempo_inicio<26):
                screen.blit(click, rectangulo_r)
                pygame.display.update()

            if(15<=tiempo_inicio<20):
                screen.blit(click, rectangulo_a)
                pygame.display.update()
                
            if(11<=tiempo_inicio<15):
                screen.blit(click, rectangulo_v)
                pygame.display.update()

            if(7<=tiempo_inicio<11):
                screen.blit(click, rectangulo_b)
                pygame.display.update()
                
            #pygame.display.update()

            if ((t_roja == True) and ((nivel == 4) and (intento>=0)) and (tiempo_inicio <= 0)):     
                t_roja = False
                aciertos = 0
                intento = intento - 1 
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)
            
            if ((t_amarillo == True) and ((nivel == 4) and (intento>=0)) and (tiempo_inicio <= 0)):   
                t_amarillo = False 
                aciertos = 0
                intento = intento - 1
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)
        

            if ((t_verde == True) and ((nivel == 4) and (intento>=0)) and (tiempo_inicio <= 0)):  
                t_verde = False 
                aciertos = 0
                intento = intento - 1  
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)
                

            if ((t_azul == True) and ((nivel == 4) and (intento>=0)) and (tiempo_inicio <= 0)): 
                t_azul = False
                aciertos = 1
                ruta = 'FONDOS/video_7.mp4' 
                velocidad = 4
                channel.queue(sL0_6)
                rv.reproducir_video(ruta, width, height, velocidad)

            if ((intento == 0) or (aciertos == 1)):
                tiempo_utilizado = tiempo # Reemplaza con el valor real
                tiempo_restante = aux_tiempo - tiempo  # Reemplaza con el valor real
                errores = aux_intento - intento  # Reemplaza con el valor real
                intentos = aux_intento # Reemplaza con el valor real
                print(tiempo_utilizado, tiempo_restante, errores, intentos)
                aux_estado = 'NIVEL_5'
                estado = 'RESULTADOS'

    #................ NIVEL 5 .................#

        if estado == 'NIVEL_5':
            nivel = 5
            estado_anterior = estado
            begin = True

            #if(temporal == 1 or reinicio == True):
            tiempo_mostrar = max(tiempo_inicio, 0)
            texto_tiempo_inicio = fuente_inicio_timer.render(str(tiempo_mostrar), True, WHITE)

            t_mostrar = max(tiempo, 0)
            texto_tiempo = fuente_inicio_timer.render(str(t_mostrar), True, WHITE)

            #print ("Inicio nivel 1, tiempo_inicio:",tiempo_inicio,",",tiempo)
            if(temporal == 6 or reinicio == True):
                temporal = 7
                pygame.mixer.Channel.stop(channel)
                screen.fill(BLACK)
                pygame.display.update()
                aux = True
                aciertos = 0
                begin = True
                tiempo_activo = False
                intento = 2
                tiempo_inicio = 26
                tiempo = 20
                #print ("Bucle temporal nivel 1 tiempo_inicio:",tiempo_inicio,",",tiempo)
                aux_intento = intento
                aux_tiempo = tiempo
                timer_activo_inicio = False
                #timer_activo_inicio = True
                #pygame.mixer.music.load('AUDIOS/descripcion_n1.mp3') 
                channel.queue(sL1_1)
            # pygame.mixer.music.play(1)
                pygame.display.update()
                reinicio = False
            
            # Mostrar cronometro

            screen.fill(ROJO, rectangulo_rojo)
            screen.fill(AMARILLO, rectangulo_amarillo)
            screen.fill(VERDE, rectangulo_verde)
            screen.fill(AZUL, rectangulo_azul)
            
            screen.blit(imagen_n5_1, rect_imagen_n5_1)
            screen.blit(imagen_n5_2, rect_imagen_n5_2)
            screen.blit(imagen_n5_3, rect_imagen_n5_3)
            screen.blit(imagen_n5_4, rect_imagen_n5_4)

            # Dibujar el cronómetro
            if(aux == True):
                rect_tiempo_inicio = texto_tiempo_inicio.get_rect(center=screen.get_rect().center)
                screen.blit(texto_tiempo_inicio, rect_tiempo_inicio)
                #print("Entro", tiempo_inicio)

            if(tiempo_activo == True):
                #print("Entro")
                rect_tiempo = texto_tiempo.get_rect(center=screen.get_rect().center)
                screen.blit(texto_tiempo, rect_tiempo)

                
            if(20<=tiempo_inicio<26):
                screen.blit(click, rectangulo_r)
                pygame.display.update()

            if(15<=tiempo_inicio<20):
                screen.blit(click, rectangulo_a)
                pygame.display.update()
                
            if(11<=tiempo_inicio<15):
                screen.blit(click, rectangulo_v)
                pygame.display.update()

            if(7<=tiempo_inicio<11):
                screen.blit(click, rectangulo_b)
                pygame.display.update()
                
            #pygame.display.update()

            if ((t_roja == True) and ((nivel == 5) and (intento>=0)) and (tiempo_inicio <= 0)):     
                t_roja = False
                aciertos = 0
                intento = intento - 1 
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)
            
            if ((t_amarillo == True) and ((nivel == 5) and (intento>=0)) and (tiempo_inicio <= 0)):   
                t_amarillo = False 
                aciertos = 0
                intento = intento - 1
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)
        

            if ((t_verde == True) and ((nivel == 5) and (intento>=0)) and (tiempo_inicio <= 0)):  
                t_verde = False 
                aciertos = 1
                ruta = 'FONDOS/video_7.mp4' 
                velocidad = 4
                channel.queue(sL0_6)
                rv.reproducir_video(ruta, width, height, velocidad)
                

            if ((t_azul == True) and ((nivel == 5) and (intento>=0)) and (tiempo_inicio <= 0)): 
                t_azul = False
                aciertos = 0
                intento = intento - 1  
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)

            if ((intento == 0) or (aciertos == 1)):
                tiempo_utilizado = tiempo # Reemplaza con el valor real
                tiempo_restante = aux_tiempo - tiempo  # Reemplaza con el valor real
                errores = aux_intento - intento  # Reemplaza con el valor real
                intentos = aux_intento # Reemplaza con el valor real
                print(tiempo_utilizado, tiempo_restante, errores, intentos)
                aux_estado = 'NIVEL_6'
                estado = 'RESULTADOS'

    #................ NIVEL 6 .................#

        if estado == 'NIVEL_6':
            nivel = 6
            estado_anterior = estado
            begin = True

            #if(temporal == 1 or reinicio == True):
            tiempo_mostrar = max(tiempo_inicio, 0)
            texto_tiempo_inicio = fuente_inicio_timer.render(str(tiempo_mostrar), True, WHITE)

            t_mostrar = max(tiempo, 0)
            texto_tiempo = fuente_inicio_timer.render(str(t_mostrar), True, WHITE)

            #print ("Inicio nivel 1, tiempo_inicio:",tiempo_inicio,",",tiempo)
            if(temporal == 7 or reinicio == True):
                temporal = 8
                pygame.mixer.Channel.stop(channel)
                screen.fill(BLACK)
                pygame.display.update()
                aux = True
                aciertos = 0
                begin = True
                tiempo_activo = False
                intento = 2
                tiempo_inicio = 26
                tiempo = 20
                #print ("Bucle temporal nivel 1 tiempo_inicio:",tiempo_inicio,",",tiempo)
                aux_intento = intento
                aux_tiempo = tiempo
                timer_activo_inicio = False
                #timer_activo_inicio = True
                #pygame.mixer.music.load('AUDIOS/descripcion_n1.mp3') 
                channel.queue(sL1_1)
            # pygame.mixer.music.play(1)
                pygame.display.update()
                reinicio = False
            
            # Mostrar cronometro

            screen.fill(ROJO, rectangulo_rojo)
            screen.fill(AMARILLO, rectangulo_amarillo)
            screen.fill(VERDE, rectangulo_verde)
            screen.fill(AZUL, rectangulo_azul)
            
            screen.blit(imagen_n6_1, rect_imagen_n6_1)
            screen.blit(imagen_n6_2, rect_imagen_n6_2)
            screen.blit(imagen_n6_3, rect_imagen_n6_3)
            screen.blit(imagen_n6_4, rect_imagen_n6_4)

            # Dibujar el cronómetro
            if(aux == True):
                rect_tiempo_inicio = texto_tiempo_inicio.get_rect(center=screen.get_rect().center)
                screen.blit(texto_tiempo_inicio, rect_tiempo_inicio)
                #print("Entro", tiempo_inicio)

            if(tiempo_activo == True):
                #print("Entro")
                rect_tiempo = texto_tiempo.get_rect(center=screen.get_rect().center)
                screen.blit(texto_tiempo, rect_tiempo)

                
            if(20<=tiempo_inicio<26):
                screen.blit(click, rectangulo_r)
                pygame.display.update()

            if(15<=tiempo_inicio<20):
                screen.blit(click, rectangulo_a)
                pygame.display.update()
                
            if(11<=tiempo_inicio<15):
                screen.blit(click, rectangulo_v)
                pygame.display.update()

            if(7<=tiempo_inicio<11):
                screen.blit(click, rectangulo_b)
                pygame.display.update()
                
            #pygame.display.update()

            if ((t_roja == True) and ((nivel == 6) and (intento>=0)) and (tiempo_inicio <= 0)):     
                t_roja = False
                aciertos = 0
                intento = intento - 1 
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)
            
            if ((t_amarillo == True) and ((nivel == 6) and (intento>=0)) and (tiempo_inicio <= 0)):   
                t_amarillo = False 
                aciertos = 0
                intento = intento - 1
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)
        

            if ((t_verde == True) and ((nivel == 6) and (intento>=0)) and (tiempo_inicio <= 0)):  
                t_verde = False 
                aciertos = 1
                ruta = 'FONDOS/video_7.mp4' 
                velocidad = 4
                channel.queue(sL0_6)
                rv.reproducir_video(ruta, width, height, velocidad)
                

            if ((t_azul == True) and ((nivel == 6) and (intento>=0)) and (tiempo_inicio <= 0)): 
                t_azul = False
                aciertos = 0
                intento = intento - 1  
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)

            if ((intento == 0) or (aciertos == 1)):
                tiempo_utilizado = tiempo # Reemplaza con el valor real
                tiempo_restante = aux_tiempo - tiempo  # Reemplaza con el valor real
                errores = aux_intento - intento  # Reemplaza con el valor real
                intentos = aux_intento # Reemplaza con el valor real
                print(tiempo_utilizado, tiempo_restante, errores, intentos)
                aux_estado = 'NIVEL_7'
                estado = 'RESULTADOS'

    #................ NIVEL 7 .................#

        if estado == 'NIVEL_7':
            nivel = 7
            estado_anterior = estado
            begin = True

            #if(temporal == 1 or reinicio == True):
            tiempo_mostrar = max(tiempo_inicio, 0)
            texto_tiempo_inicio = fuente_inicio_timer.render(str(tiempo_mostrar), True, WHITE)

            t_mostrar = max(tiempo, 0)
            texto_tiempo = fuente_inicio_timer.render(str(t_mostrar), True, WHITE)

            #print ("Inicio nivel 1, tiempo_inicio:",tiempo_inicio,",",tiempo)
            if(temporal == 8 or reinicio == True):
                temporal = 9
                pygame.mixer.Channel.stop(channel)
                screen.fill(BLACK)
                pygame.display.update()
                aux = True
                aciertos = 0
                begin = True
                tiempo_activo = False
                intento = 2
                tiempo_inicio = 26
                tiempo = 20
                #print ("Bucle temporal nivel 1 tiempo_inicio:",tiempo_inicio,",",tiempo)
                aux_intento = intento
                aux_tiempo = tiempo
                timer_activo_inicio = False
                #timer_activo_inicio = True
                #pygame.mixer.music.load('AUDIOS/descripcion_n1.mp3') 
                channel.queue(sL1_1)
            # pygame.mixer.music.play(1)
                pygame.display.update()
                reinicio = False
            
            # Mostrar cronómetro

            screen.fill(ROJO, rectangulo_rojo)
            screen.fill(AMARILLO, rectangulo_amarillo)
            screen.fill(VERDE, rectangulo_verde)
            screen.fill(AZUL, rectangulo_azul)
            
            screen.blit(imagen_n7_1, rect_imagen_n7_1)
            screen.blit(imagen_n7_2, rect_imagen_n7_2)
            screen.blit(imagen_n7_3, rect_imagen_n7_3)
            screen.blit(imagen_n7_4, rect_imagen_n7_4)

            # Dibujar el cronómetro
            if(aux == True):
                rect_tiempo_inicio = texto_tiempo_inicio.get_rect(center=screen.get_rect().center)
                screen.blit(texto_tiempo_inicio, rect_tiempo_inicio)
                #print("Entro", tiempo_inicio)

            if(tiempo_activo == True):
                #print("Entro")
                rect_tiempo = texto_tiempo.get_rect(center=screen.get_rect().center)
                screen.blit(texto_tiempo, rect_tiempo)

                
            if(20<=tiempo_inicio<26):
                screen.blit(click, rectangulo_r)
                pygame.display.update()

            if(15<=tiempo_inicio<20):
                screen.blit(click, rectangulo_a)
                pygame.display.update()
                
            if(11<=tiempo_inicio<15):
                screen.blit(click, rectangulo_v)
                pygame.display.update()

            if(7<=tiempo_inicio<11):
                screen.blit(click, rectangulo_b)
                pygame.display.update()
                
            #pygame.display.update()

            if ((t_roja == True) and ((nivel == 7) and (intento>=0)) and (tiempo_inicio <= 0)):     
                t_roja = False
                aciertos = 0
                intento = intento - 1 
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)
            
            if ((t_amarillo == True) and ((nivel == 7) and (intento>=0)) and (tiempo_inicio <= 0)):   
                t_amarillo = False 
                aciertos = 0
                intento = intento - 1
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)
        

            if ((t_verde == True) and ((nivel == 7) and (intento>=0)) and (tiempo_inicio <= 0)):  
                t_verde = False 
                aciertos = 1
                ruta = 'FONDOS/video_7.mp4' 
                velocidad = 4
                channel.queue(sL0_6)
                rv.reproducir_video(ruta, width, height, velocidad)
                

            if ((t_azul == True) and ((nivel == 7) and (intento>=0)) and (tiempo_inicio <= 0)): 
                t_azul = False
                aciertos = 0
                intento = intento - 1  
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)

            if ((intento == 0) or (aciertos == 1)):
                tiempo_utilizado = tiempo # Reemplaza con el valor real
                tiempo_restante = aux_tiempo - tiempo  # Reemplaza con el valor real
                errores = aux_intento - intento  # Reemplaza con el valor real
                intentos = aux_intento # Reemplaza con el valor real
                print(tiempo_utilizado, tiempo_restante, errores, intentos)
                aux_estado = 'NIVEL_8'
                estado = 'RESULTADOS'

    #................ NIVEL 8 .................#

        if estado == 'NIVEL_8':
            nivel = 8
            estado_anterior = estado
            begin = True

            #if(temporal == 1 or reinicio == True):
            tiempo_mostrar = max(tiempo_inicio, 0)
            texto_tiempo_inicio = fuente_inicio_timer.render(str(tiempo_mostrar), True, WHITE)

            t_mostrar = max(tiempo, 0)
            texto_tiempo = fuente_inicio_timer.render(str(t_mostrar), True, WHITE)

            #print ("Inicio nivel 1, tiempo_inicio:",tiempo_inicio,",",tiempo)
            if(temporal == 9 or reinicio == True):
                temporal = 10
                pygame.mixer.Channel.stop(channel)
                screen.fill(BLACK)
                pygame.display.update()
                aux = True
                aciertos = 0
                begin = True
                tiempo_activo = False
                intento = 2
                tiempo_inicio = 26
                tiempo = 20
                #print ("Bucle temporal nivel 1 tiempo_inicio:",tiempo_inicio,",",tiempo)
                aux_intento = intento
                aux_tiempo = tiempo
                timer_activo_inicio = False
                #timer_activo_inicio = True
                #pygame.mixer.music.load('AUDIOS/descripcion_n1.mp3') 
                channel.queue(sL1_1)
            # pygame.mixer.music.play(1)
                pygame.display.update()
                reinicio = False
            
            # Mostrar cronómetro

            screen.fill(ROJO, rectangulo_rojo)
            screen.fill(AMARILLO, rectangulo_amarillo)
            screen.fill(VERDE, rectangulo_verde)
            screen.fill(AZUL, rectangulo_azul)
            
            screen.blit(imagen_n8_1, rect_imagen_n8_1)
            screen.blit(imagen_n8_2, rect_imagen_n8_2)
            screen.blit(imagen_n8_3, rect_imagen_n8_3)
            screen.blit(imagen_n8_4, rect_imagen_n8_4)

            # Dibujar el cronómetro
            if(aux == True):
                rect_tiempo_inicio = texto_tiempo_inicio.get_rect(center=screen.get_rect().center)
                screen.blit(texto_tiempo_inicio, rect_tiempo_inicio)
                #print("Entro", tiempo_inicio)

            if(tiempo_activo == True):
                #print("Entro")
                rect_tiempo = texto_tiempo.get_rect(center=screen.get_rect().center)
                screen.blit(texto_tiempo, rect_tiempo)

                
            if(20<=tiempo_inicio<26):
                screen.blit(click, rectangulo_r)
                pygame.display.update()

            if(15<=tiempo_inicio<20):
                screen.blit(click, rectangulo_a)
                pygame.display.update()
                
            if(11<=tiempo_inicio<15):
                screen.blit(click, rectangulo_v)
                pygame.display.update()

            if(7<=tiempo_inicio<11):
                screen.blit(click, rectangulo_b)
                pygame.display.update()
                
            #pygame.display.update()

            if ((t_roja == True) and ((nivel == 8) and (intento>=0)) and (tiempo_inicio <= 0)):     
                t_roja = False
                aciertos = 0
                intento = intento - 1 
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)
            
            if ((t_amarillo == True) and ((nivel == 8) and (intento>=0)) and (tiempo_inicio <= 0)):   
                t_amarillo = False 
                aciertos = 0
                intento = intento - 1
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)
        

            if ((t_verde == True) and ((nivel == 8) and (intento>=0)) and (tiempo_inicio <= 0)):  
                t_verde = False 
                aciertos = 1
                ruta = 'FONDOS/video_7.mp4' 
                velocidad = 4
                channel.queue(sL0_6)
                rv.reproducir_video(ruta, width, height, velocidad)
                

            if ((t_azul == True) and ((nivel == 8) and (intento>=0)) and (tiempo_inicio <= 0)): 
                t_azul = False
                aciertos = 0
                intento = intento - 1  
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)

            if ((intento == 0) or (aciertos == 1)):
                tiempo_utilizado = tiempo # Reemplaza con el valor real
                tiempo_restante = aux_tiempo - tiempo  # Reemplaza con el valor real
                errores = aux_intento - intento  # Reemplaza con el valor real
                intentos = aux_intento # Reemplaza con el valor real
                print(tiempo_utilizado, tiempo_restante, errores, intentos)
                aux_estado = 'NIVEL_9'
                estado = 'RESULTADOS'

    #................ NIVEL 9 .................#

        if estado == 'NIVEL_9':
            nivel = 9
            estado_anterior = estado
            begin = True

            #if(temporal == 1 or reinicio == True):
            tiempo_mostrar = max(tiempo_inicio, 0)
            texto_tiempo_inicio = fuente_inicio_timer.render(str(tiempo_mostrar), True, WHITE)

            t_mostrar = max(tiempo, 0)
            texto_tiempo = fuente_inicio_timer.render(str(t_mostrar), True, WHITE)

            #print ("Inicio nivel 1, tiempo_inicio:",tiempo_inicio,",",tiempo)
            if(temporal == 10 or reinicio == True):
                temporal = 11
                pygame.mixer.Channel.stop(channel)
                screen.fill(BLACK)
                pygame.display.update()
                aux = True
                aciertos = 0
                begin = True
                tiempo_activo = False
                intento = 2
                tiempo_inicio = 26
                tiempo = 20
                #print ("Bucle temporal nivel 1 tiempo_inicio:",tiempo_inicio,",",tiempo)
                aux_intento = intento
                aux_tiempo = tiempo
                timer_activo_inicio = False
                #timer_activo_inicio = True
                #pygame.mixer.music.load('AUDIOS/descripcion_n1.mp3') 
                channel.queue(sL1_1)
            # pygame.mixer.music.play(1)
                pygame.display.update()
                reinicio = False
            
            # Mostrar cronómetro

            screen.fill(ROJO, rectangulo_rojo)
            screen.fill(AMARILLO, rectangulo_amarillo)
            screen.fill(VERDE, rectangulo_verde)
            screen.fill(AZUL, rectangulo_azul)
            
            screen.blit(imagen_n9_1, rect_imagen_n9_1)
            screen.blit(imagen_n9_2, rect_imagen_n9_2)
            screen.blit(imagen_n9_3, rect_imagen_n9_3)
            screen.blit(imagen_n9_4, rect_imagen_n9_4)

            # Dibujar el cronómetro
            if(aux == True):
                rect_tiempo_inicio = texto_tiempo_inicio.get_rect(center=screen.get_rect().center)
                screen.blit(texto_tiempo_inicio, rect_tiempo_inicio)
                #print("Entro", tiempo_inicio)

            if(tiempo_activo == True):
                #print("Entro")
                rect_tiempo = texto_tiempo.get_rect(center=screen.get_rect().center)
                screen.blit(texto_tiempo, rect_tiempo)

                
            if(20<=tiempo_inicio<26):
                screen.blit(click, rectangulo_r)
                pygame.display.update()

            if(15<=tiempo_inicio<20):
                screen.blit(click, rectangulo_a)
                pygame.display.update()
                
            if(11<=tiempo_inicio<15):
                screen.blit(click, rectangulo_v)
                pygame.display.update()

            if(7<=tiempo_inicio<11):
                screen.blit(click, rectangulo_b)
                pygame.display.update()
                
            #pygame.display.update()

            if ((t_roja == True) and ((nivel == 9) and (intento>=0)) and (tiempo_inicio <= 0)):     
                t_roja = False
                aciertos = 0
                intento = intento - 1 
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)
            
            if ((t_amarillo == True) and ((nivel == 9) and (intento>=0)) and (tiempo_inicio <= 0)):   
                t_amarillo = False 
                aciertos = 0
                intento = intento - 1
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)
        

            if ((t_verde == True) and ((nivel == 9) and (intento>=0)) and (tiempo_inicio <= 0)):  
                t_verde = False 
                aciertos = 1
                ruta = 'FONDOS/video_7.mp4' 
                velocidad = 4
                channel.queue(sL0_6)
                rv.reproducir_video(ruta, width, height, velocidad)
                

            if ((t_azul == True) and ((nivel == 9) and (intento>=0)) and (tiempo_inicio <= 0)): 
                t_azul = False
                aciertos = 0
                intento = intento - 1  
                ruta = 'FONDOS/video_6.mp4' 
                velocidad = 4
                channel.queue(sL0_7)
                rv.reproducir_video(ruta, width, height, velocidad)

            if ((intento == 0) or (aciertos == 1)):
                tiempo_utilizado = tiempo # Reemplaza con el valor real
                tiempo_restante = aux_tiempo - tiempo  # Reemplaza con el valor real
                errores = aux_intento - intento  # Reemplaza con el valor real
                intentos = aux_intento # Reemplaza con el valor real
                print(tiempo_utilizado, tiempo_restante, errores, intentos)
                aux_estado = 'FIN'
                estado = 'RESULTADOS'

        pygame.display.update()

    return(matriz)

#resultado = secuencia_logica()

