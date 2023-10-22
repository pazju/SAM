import pygame   
from pygame.locals import *
import player
import world
import background
#import button
import cv2

def atencion(screen_width, screen_height):
    pygame.init()
    pygame.mixer.init() # Inicializar el mezclador porque se van a utilizar sonidos

    # os.environ['SDL_VIDEO_CENTERED'] = '1' # Después de pygame.init()
    # info = pygame.display.Info() # Antes de set_mode()
    # screen_width, screen_height = screen_width, info.current_height

    # COLORS
    # https://htmlcolorcodes.com/es/tabla-de-colores/
    color_red = (255,0,0)
    color_white = (255,255,255)
    color_black = (0,0,0)
    color_purple = (142,68,173)
    color_bluep = (33,97,140)


    # SOUNDS
    sIntro = pygame.mixer.Sound("Assets/Sounds/AUDIO_INTRO_SAM.mp3")
    sTuto_1 = pygame.mixer.Sound("Assets/Sounds/AUDIO_TUTORIAL.mp3")
    sTuto_2 = pygame.mixer.Sound("Assets/Sounds/AUDIO_TUTORIAL_2.mp3")

    sL1_1 = pygame.mixer.Sound("Assets/Sounds/LEVEL_1/audio_level_1_1.mp3")
    sL1_2 = pygame.mixer.Sound("Assets/Sounds/LEVEL_1/audio_level_1_2.mp3")
    sL1_3 = pygame.mixer.Sound("Assets/Sounds/LEVEL_1/audio_level_1_3.mp3")
    sL1_4 = pygame.mixer.Sound("Assets/Sounds/LEVEL_1/audio_level_1_4.mp3")
    sL1_5 = pygame.mixer.Sound("Assets/Sounds/LEVEL_1/audio_level_end.mp3")

    sL2_1 = pygame.mixer.Sound("Assets/Sounds/LEVEL_2/audio_level_2_1.mp3")
    sL2_2 = pygame.mixer.Sound("Assets/Sounds/LEVEL_2/audio_level_2_2.mp3")
    sL2_3 = pygame.mixer.Sound("Assets/Sounds/LEVEL_2/audio_level_2_3.mp3")
    sL2_4 = pygame.mixer.Sound("Assets/Sounds/LEVEL_2/audio_level_2_4.mp3")
    sL2_5 = pygame.mixer.Sound("Assets/Sounds/LEVEL_2/audio_level_2_5.mp3")
    sL2_6 = pygame.mixer.Sound("Assets/Sounds/LEVEL_2/audio_level_2_6.mp3")
    sL2_7 = pygame.mixer.Sound("Assets/Sounds/LEVEL_2/audio_level_2_7.mp3")
    sL2_8 = pygame.mixer.Sound("Assets/Sounds/LEVEL_1/audio_level_end.mp3")

    sL3_1 = pygame.mixer.Sound("Assets/Sounds/LEVEL_3/audio_level_3_1.mp3")
    sL3_2 = pygame.mixer.Sound("Assets/Sounds/LEVEL_3/audio_level_3_2.mp3")
    sL3_3 = pygame.mixer.Sound("Assets/Sounds/LEVEL_3/audio_level_3_3.mp3")
    sL3_4 = pygame.mixer.Sound("Assets/Sounds/LEVEL_3/audio_level_3_4.mp3")
    sL3_5 = pygame.mixer.Sound("Assets/Sounds/LEVEL_3/audio_level_3_5.mp3")
    sL3_6 = pygame.mixer.Sound("Assets/Sounds/LEVEL_3/audio_level_3_6.mp3")
    sL3_7 = pygame.mixer.Sound("Assets/Sounds/LEVEL_3/audio_level_3_7.mp3")
    sL3_8 = pygame.mixer.Sound("Assets/Sounds/LEVEL_3/audio_level_3_8.mp3")
    sL3_9 = pygame.mixer.Sound("Assets/Sounds/LEVEL_3/audio_level_3_9.mp3")
    sL3_10 = pygame.mixer.Sound("Assets/Sounds/LEVEL_3/audio_level_3_10.mp3")
    sL3_11 = pygame.mixer.Sound("Assets/Sounds/LEVEL_3/audio_level_3_11.mp3")
    sL3_12 = pygame.mixer.Sound("Assets/Sounds/LEVEL_1/audio_level_end.mp3")

    sL4_1 = pygame.mixer.Sound("Assets/Sounds/LEVEL_4/audio_level_4_1.mp3")
    sL4_2 = pygame.mixer.Sound("Assets/Sounds/LEVEL_4/audio_level_4_2.mp3")
    sL4_3 = pygame.mixer.Sound("Assets/Sounds/LEVEL_4/audio_level_4_3.mp3")
    sL4_4 = pygame.mixer.Sound("Assets/Sounds/LEVEL_4/audio_level_4_4.mp3")
    sL4_5 = pygame.mixer.Sound("Assets/Sounds/LEVEL_4/audio_level_4_5.mp3")
    sL4_6 = pygame.mixer.Sound("Assets/Sounds/LEVEL_4/audio_level_4_6.mp3")
    sL4_7 = pygame.mixer.Sound("Assets/Sounds/LEVEL_4/audio_level_4_7.mp3")
    sL4_8 = pygame.mixer.Sound("Assets/Sounds/LEVEL_4/audio_level_4_8.mp3")
    sL4_9 = pygame.mixer.Sound("Assets/Sounds/LEVEL_4/audio_level_4_9.mp3")
    sL4_10 = pygame.mixer.Sound("Assets/Sounds/LEVEL_4/audio_level_4_10.mp3")
    sL4_11 = pygame.mixer.Sound("Assets/Sounds/LEVEL_4/audio_level_4_11.mp3")
    sL4_12 = pygame.mixer.Sound("Assets/Sounds/LEVEL_1/audio_level_end.mp3")

    sL5_1 = pygame.mixer.Sound("Assets/Sounds/LEVEL_5/audio_level_5_1.mp3")
    sL5_2 = pygame.mixer.Sound("Assets/Sounds/LEVEL_5/audio_level_5_2.mp3")
    sL5_3 = pygame.mixer.Sound("Assets/Sounds/LEVEL_5/audio_level_5_3.mp3")
    sL5_4 = pygame.mixer.Sound("Assets/Sounds/LEVEL_5/audio_level_5_4.mp3")
    sL5_5 = pygame.mixer.Sound("Assets/Sounds/LEVEL_5/audio_level_5_5.mp3")
    sL5_6 = pygame.mixer.Sound("Assets/Sounds/LEVEL_5/audio_level_5_6.mp3")
    sL5_7 = pygame.mixer.Sound("Assets/Sounds/LEVEL_5/audio_level_5_7.mp3")
    sL5_8 = pygame.mixer.Sound("Assets/Sounds/LEVEL_5/audio_level_5_8.mp3")
    sL5_9 = pygame.mixer.Sound("Assets/Sounds/LEVEL_1/audio_level_end.mp3")

    sEnd= pygame.mixer.Sound("Assets/Sounds/END/end.mp3")

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
    timer_font = pygame.font.SysFont("adobedevanagaribold", 30)
    begin_timer_font = pygame.font.SysFont("adobedevanagaribold", 100)
    begin_time = 8 # 5 segundos para iniciar
    level_time = 121 # 2 minutes (121)
    timer_text = timer_font.render(str(level_time), True, color_white)
    timer_event = pygame.USEREVENT+1 # Evento de Usuario + 1 (USEREVENT 25 - ID) 
    pygame.time.set_timer(timer_event, 1000) # set_timer crea una acción cada 1s
    print(pygame.font.get_fonts()) ################### IMPRESIÓN FUENTES (SELECCIONAR LA MEJOR)

    # 20 cuadros de ancho y 16 de alto de dimensiones [tile_size_x * tile_size_y]
    # if screen_width == 1920:    # 1920/20 = 96, 1080/16 = 67.5
    #     tile_size_x = 96
    #     tile_size_y = 67.5
    #     tiles_x = screen_width/tile_size_x
    #     tiles_y = screen_height/tile_size_y
        
    # elif screen_width <= 1366:   # 1360/20 = 68, 768/16 = 48
    #     tile_size_x = 68
    #     tile_size_y = 48
    #     tiles_x = screen_width/tile_size_x
    #     tiles_y = screen_height/tile_size_y


    tile_size_x = round(screen_width/20)
    tile_size_y = round(screen_height/16)
    tiles_x = screen_width/tile_size_x
    tiles_y = screen_height/tile_size_y
    #tile_size = 100

    # Images
    # https://sierrassets.itch.io/pixel-art-furniture-pack
    # https://opengameart.org/content/platformer-pack-redux-360-assets
    sam_img = pygame.image.load("Assets/Character/SPRITES/g0.png")
    sam_img = pygame.transform.scale(sam_img, (tile_size_x*5, tile_size_y*5.4))
    sam_rect = sam_img.get_rect(center = (tile_size_x*10,tile_size_y*7))

    clock_img = pygame.image.load("Assets/Background/clock.png") # https://www.freepng.es/png-i0i6aj/download.html
    clock_img = pygame.transform.scale(clock_img, (tile_size_x*0.8, tile_size_y*0.8)) # Tamaño de la imagen
    clock_rect = clock_img.get_rect(center = (tile_size_x*19,tile_size_y*0.6))

    #cesta_img = pygame.image.load("Assets/Background/cesta.png")# https://www.freepng.es/png-vlgbg1/
    cesta_img = pygame.image.load("Assets/Icons/Kenney_gameIcons/PNG/Black/2x/shoppingBasket.png")# www.kenney.nl
    cesta_img = pygame.transform.scale(cesta_img, (tile_size_x*1.5, tile_size_y*1.5)) # Tamaño de la imagen
    cesta_rect = cesta_img.get_rect(center = (tile_size_x, tile_size_y*0.9))

    cesta_end_img = pygame.transform.scale(cesta_img, (tile_size_x, tile_size_y))
    cesta_end_rect = cesta_end_img.get_rect(center = (tile_size_x*10, tile_size_y*10))

    arrowUp_img = pygame.image.load("Assets/Icons/Kenney_gameIcons/PNG/Black/1x/arrowUp.png")
    arrowUp_rect = arrowUp_img.get_rect(center = (tile_size_x*5.5,tile_size_y*4.5))
    arrowUp_rect2 = arrowUp_img.get_rect(center = (tile_size_x*2.8,tile_size_y*5))

    water_img = pygame.image.load("Assets/Water/02/Water__05.png")
    water_img = pygame.transform.scale(water_img, (tile_size_x*2, tile_size_y*2))
    water_rect = water_img.get_rect(center = (tile_size_x*7,tile_size_y*5))

    caution_img = pygame.image.load("Assets/Rewards/caution.png")
    caution_img = pygame.transform.scale(caution_img, (tile_size_x*1.1, tile_size_y*1.1))
    caution_rect = caution_img.get_rect(center = (tile_size_x*12.5,tile_size_y*6))

    tapete_img = pygame.image.load("Assets/Rewards/tapete_b.png")
    tapete_img = pygame.transform.scale(tapete_img, (tile_size_x*2, tile_size_y*4))
    tapete_rect = tapete_img.get_rect(center = (tile_size_x*15.5,tile_size_y*7))


    levelEND_img = pygame.image.load("Assets/Background/blue_land.png")
    levelEND_img = pygame.transform.scale(levelEND_img, (tile_size_x*20, tile_size_y*16))
    levelEND_rect = levelEND_img.get_rect(center = (tile_size_x*10,tile_size_y*8))

    final_img = pygame.image.load("Assets/Background/final.png")
    final_img = pygame.transform.scale(final_img, (tile_size_x*20, tile_size_y*16))
    final_rect = final_img.get_rect(center = (tile_size_x*10,tile_size_y*8))

    levelOneR_img = pygame.image.load("Assets/Rewards/cepillo_azul.png")
    levelOneR_img  = pygame.transform.scale(levelOneR_img, (tile_size_x*1.5, tile_size_y*1.5))
    levelOneR_rect = levelOneR_img.get_rect(center = (tile_size_x*10,tile_size_y*7))

    levelTwoR_img = pygame.image.load("Assets/Rewards/chancla_b.png")
    levelTwoR_img  = pygame.transform.scale(levelTwoR_img, (tile_size_x*1.5, tile_size_y*1.5))
    levelTwoR_rect = levelTwoR_img.get_rect(center = (tile_size_x*10,tile_size_y*7))

    levelThreeR_img1 = pygame.image.load("Assets/Rewards/soap.png")
    levelThreeR_img1  = pygame.transform.scale(levelThreeR_img1 , (tile_size_x*1, tile_size_y*1.5))
    levelThreeR_rect1 = levelThreeR_img1.get_rect(center = (tile_size_x*10,tile_size_y*6.5))
    levelThreeR_img2 = pygame.image.load("Assets/Rewards/towel.png")
    levelThreeR_img2  = pygame.transform.scale(levelThreeR_img2, (tile_size_x*2, tile_size_y*1.5))
    levelThreeR_rect2 = levelThreeR_img2.get_rect(center = (tile_size_x*10,tile_size_y*7.5))

    levelFourR_img = pygame.image.load("Assets/Rewards/tapete_a.png")
    levelFourR_img  = pygame.transform.scale(levelFourR_img , (tile_size_x*2, tile_size_y*3))
    levelFourR_rect = levelFourR_img.get_rect(center = (tile_size_x*10,tile_size_y*7))


    #levelFiveBG_img = pygame.image.load("Assets/Background/BG_TUTO.png")
    levelFiveBG_img = pygame.image.load("Assets/Background/L5_BG_3.png")
    levelFiveBG_img  = pygame.transform.scale(levelFiveBG_img , (tile_size_x*20, tile_size_y*14))
    levelFiveBG_rect = levelFiveBG_img.get_rect(center = (tile_size_x*10,tile_size_y*9))
    l5_DOWN_img = pygame.image.load("Assets/Background/L5_DOWN.png")
    l5_DOWN_img = pygame.transform.scale(l5_DOWN_img , (tile_size_x*20, tile_size_y*14))
    l5_DOWN_rect = l5_DOWN_img.get_rect(center = (tile_size_x*10,tile_size_y*9))
    l5_UP_img = pygame.image.load("Assets/Background/L5_UP.png")
    l5_UP_img = pygame.transform.scale(l5_UP_img , (tile_size_x*20, tile_size_y*14))
    l5_UP_rect = l5_UP_img.get_rect(center = (tile_size_x*10,tile_size_y*9))
    l5_RIGHT_img = pygame.image.load("Assets/Background/L5_RIGHT.png")
    l5_RIGHT_img = pygame.transform.scale(l5_RIGHT_img , (tile_size_x*20, tile_size_y*14))
    l5_RIGHT_rect = l5_RIGHT_img.get_rect(center = (tile_size_x*10,tile_size_y*9))
    l5_LEFT_img = pygame.image.load("Assets/Background/L5_LEFT.png")
    l5_LEFT_img = pygame.transform.scale(l5_LEFT_img , (tile_size_x*20, tile_size_y*14))
    l5_LEFT_rect = l5_LEFT_img.get_rect(center = (tile_size_x*10,tile_size_y*9))
    perilla_img = pygame.image.load("Assets/Background/perilla.png")
    perilla_img = pygame.transform.scale(perilla_img , (tile_size_x*2, tile_size_y*6.5))
    perilla_rect = perilla_img.get_rect(center = (tile_size_x*10,tile_size_y*10.5))
    levelFiveR_img = pygame.image.load("Assets/Rewards/agua_t.png")
    levelFiveR_img  = pygame.transform.scale(levelFiveR_img , (tile_size_x*2, tile_size_y*2))
    levelFiveR_rect = levelFiveR_img.get_rect(center = (tile_size_x*10,tile_size_y*7))


    coin_img = pygame.image.load("Assets/Rewards/coin.png")
    coin_img  = pygame.transform.scale(coin_img, (tile_size_x*6, tile_size_y*6))
    coin_rect = coin_img.get_rect(center = (tile_size_x*10,tile_size_y*7))

    continue_img = pygame.image.load("Assets/Icons/Kenney_gameIcons/PNG/Black/2x/fastForward.png")
    exit_img = pygame.image.load("Assets/Icons/Kenney_gameIcons/PNG/Black/2x/exit.png")
    restart_img = pygame.image.load("Assets/Icons/Kenney_gameIcons/PNG/Black/2x/return.png")
    start_img = pygame.image.load("Assets/Icons/Kenney_gameIcons/PNG/Black/2x/next.png")

    AI_img = pygame.image.load("Assets/AI/image.png")
    AI_img_2 = pygame.image.load("Assets/AI/image2.png")
    CANVA_img = pygame.image.load("Assets/AI/canva_1.png")
    CANVA_img  = pygame.transform.scale(CANVA_img , (tile_size_x*10, tile_size_y*10))
    AI_rect = AI_img.get_rect(center = (tile_size_x*9.5,tile_size_y*7.5))
    CANVA_2_img = pygame.image.load("Assets/AI/canva_2.png")
    CANVA_2_img  = pygame.transform.scale(CANVA_2_img , (tile_size_x*9, tile_size_y*9))
    CANVA_2_rect = CANVA_2_img.get_rect(center = (tile_size_x*9.5,tile_size_y*8))
    canasto_img = pygame.image.load("Assets/Rewards/canasto.png")
    CANVA_3_img = pygame.image.load("Assets/AI/canva_3.png")
    CANVA_3_img  = pygame.transform.scale(CANVA_3_img , (tile_size_x*8.5, tile_size_y*8.5))
    CANVA_3_rect = CANVA_3_img.get_rect(center = (tile_size_x*10,tile_size_y*8.5))
    canasto_img = pygame.image.load("Assets/Rewards/canasto.png")
    canasto_img = pygame.transform.scale(canasto_img, (tile_size_x*2, tile_size_y*2))
    canasto_rect = canasto_img.get_rect(center = (tile_size_x*8,tile_size_y*13))

    #VIDEOS
    tuto = "Assets\VIDEOS\TUTORIAL.mp4"
    tuto_2 = "Assets\VIDEOS\TUTORIAL_2.mp4"

    # PERSONAJES
    # https://opengameart.org/content/tiny-characters-set
    # Sprites de 64x51 pixeles Ancho x Alto

    # POSICIÓN BOTONES
    continue_rect = start_img.get_rect(center = (tile_size_x*10, tile_size_y*12))
    #continue_bot = button.Button(tile_size_x*10, tile_size_y*14,continue_img,1) # Botón Continuar
    exit_rect = exit_img.get_rect(center = (tile_size_x*9, tile_size_y*8.5))
    exit_rect_2 = exit_img.get_rect(center = (tile_size_x*8, tile_size_y*12))
    #exit_bot = button.Button(tile_size_x*9, tile_size_y*8.5,exit_img,1) # Botón Salir
    restart_rect = restart_img.get_rect(center = (tile_size_x*11, tile_size_y*8.5))
    restart_rect_2 = restart_img.get_rect(center = (tile_size_x*12, tile_size_y*12))
    #restart_bot = button.Button(tile_size_x*11, tile_size_y*8.5,restart_img,1) # Botón Reinicio 
    

    # Texto en pantalla
    def draw_text(text, size, text_col, x, y):
        font = pygame.font.SysFont("adobedevanagaribold", size)
        text_surface = font.render(text, True, text_col)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        screen.blit(text_surface, text_rect)



    def draw_grid():
        for line in range(0, 20):
            pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size_y), (screen_width, line * tile_size_y))
            pygame.draw.line(screen, (255, 255, 255), (line * tile_size_x, 0), (line * tile_size_x, screen_height))

    # Función que presenta en pantalla del juego los resultados finales del nivel
    def RESULTS(level, points, used_time, actual_time, total_points, total_error):
        
        screen.blit(levelEND_img, levelEND_rect)
        draw_text("¡Lo lograste!",40, color_black, screen_width/2, tile_size_y*1.5)
        
        p_text = 'Puntaje Total de Objetos Recogidos en el Nivel ' + str(level) + ' -> ' + str(points)
        points_text = timer_font.render(str(p_text), True, color_black)
        points_rect = points_text.get_rect(center = (tile_size_x*10,tile_size_y*3)) 
        screen.blit(points_text, points_rect)

        ut_text = 'Tiempo utilizado para el Nivel ' + str(level) + ' -> ' + str(used_time) + ' segundos'
        ut_text = timer_font.render(str(ut_text), True, color_black)
        ut_rect = ut_text.get_rect(center = (tile_size_x*10,tile_size_y*4)) 
        screen.blit(ut_text, ut_rect)

        at_text = 'Tiempo restante del Nivel ' + str(level) + ' -> ' + str(actual_time) + ' segundos'
        at_text = timer_font.render(str(at_text), True, color_black)
        at_rect = at_text.get_rect(center = (tile_size_x*10,tile_size_y*5)) 
        screen.blit(at_text, at_rect)

        tp_text = 'Misiones Cumplidas en el Nivel ' + str(level) + ' -> ' + str(total_points)
        tp_text = timer_font.render(str(tp_text), True, color_black)
        tp_rect = tp_text.get_rect(center = (tile_size_x*10,tile_size_y*6)) 
        screen.blit(tp_text, tp_rect)
        
        te_text = 'Errores Totales en el Nivel ' + str(level) + ' -> ' + str(total_error)
        te_text = timer_font.render(str(te_text), True, color_black)
        te_rect = te_text.get_rect(center = (tile_size_x*10,tile_size_y*7)) 
        screen.blit(te_text, te_rect)

    def TIMER(level):
        begin_timer_rect = begin_timer_text.get_rect(center = screen.get_rect().center) # Centro de la pantalla
        timer_rect = timer_text.get_rect(center = (tile_size_x*19,tile_size_y*1.5)) 
        if begin == True:
            screen.blit(begin_timer_text, begin_timer_rect)
        screen.blit(clock_img, clock_rect)
        screen.blit(timer_text, timer_rect)
        screen.blit(cesta_img, cesta_rect)
        string_lvl = 'NIVEL' + str(level)
        draw_text(string_lvl,40, color_purple, screen_width/2, tile_size_y*0.5)

    def play_video(route, vel, screen_width, screen_height):
        
        cap = cv2.VideoCapture(route)
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                frame = cv2.resize(frame, (screen_width , screen_height ))
                cv2.namedWindow('Frame',cv2.WND_PROP_FULLSCREEN)
                cv2.setWindowProperty('Frame',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
                cv2.imshow('Frame', frame)
                key = cv2.waitKey(vel)
                #if cv2.waitKey(vel) & 0xFF == ord('a'):
                if key == ord('a') or key == ord('A'):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()
        pygame.display.update()

    # Matriz Background
    background_data = [
    [6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6],
    [6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6],
    [5, 4, 4, 4, 4, 4, 4, 4, 1, 1, 5, 1, 2, 2, 2, 2, 2, 2, 2, 5],
    [5, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 5],
    [5, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 5],
    [5, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 5, 5],
    [5, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 5, 5],
    [5, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 5],
    [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 5],
    [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 5],
    [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 5],
    [5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 5, 5],
    [5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 5, 5],
    [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 5],
    [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 5],
    [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    ]

    background_data_5 = [   #BG para el nivel 5
    [6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6],
    [6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    ]


    # Matrices de Niveles

    world_data1 = [
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  1,  1,  1,  1,  1,  1,  1,  1,  1, 20,  1,  1,  1,  1,  1,  1,  1,  1,  0],
    [0,  1,  5,  0,  6,  7,  0,  1,  8,  9,  3,  4,  1, 11, 10,  0, 14,  0,  1,  0],
    [0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  1,  0],
    [0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0],
    [0,  1,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0, 18,  0,  0,  1,  0],
    [0,  1,  1,  1,  1,  1,  1,  1,  4,  0,  0,  0,  1,  0,  0,  0,  0,  0,  1,  0],
    [0,  1,  0, 13,  0,  0, 17,  4,  0,  0,  0,  0,  1,  1,  1,  1,  1,  1,  1,  0],
    [0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1, 16,  0, 10,  0, 15,  1,  0],
    [0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  1,  0],
    [0,  1, 12,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0],
    [0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 19,  0,  0,  1,  0],
    [0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  4,  1,  0,  0,  0,  0,  0,  1,  0],
    [0,  1,  1,  1, 20, 20, 20,  1,  1,  0,  0,  1,  1,  1, 20, 20, 20,  1,  1,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0, 21, 21,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    ]

    world_data2 = [
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  1,  1,  1,  1,  1,  1,  1,  1,  1, 20,  1,  1,  1,  1,  1,  1,  1,  1,  0],
    [0,  1,  5,  0,  6,  7,  0,  1,  8,  9,  3,  4,  1, 11, 10,  0, 14,  0,  1,  0],
    [0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  1,  0],
    [0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0],
    [0,  1,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0],
    [0,  1,  1,  1,  1,  1,  1,  1,  4,  0,  0,  0,  1,  0,  0,  0,  0,  0,  1,  0],
    [0,  1,  0, 13,  0,  0, 17,  4,  0,  0,  0,  0,  1,  1,  1,  1,  1,  1,  1,  0],
    [0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1, 16,  0, 10,  0, 15,  1,  0],
    [0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  1,  0],
    [0,  1, 12,  0, 22,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0],
    [0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 23,  0,  0,  1,  0],
    [0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  4,  1,  0,  0,  0,  0,  0,  1,  0],
    [0,  1,  1,  1, 20, 20, 20,  1,  1,  0,  0,  1,  1,  1, 20, 20, 20,  1,  1,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0, 21, 21,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    ]

    world_data3 = [
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  1,  1,  1,  1,  1,  1,  1,  1,  1, 20,  1,  1,  1,  1,  1,  1,  1,  1,  0],
    [0,  1,  5,  0,  6,  7,  0,  1,  8,  9,  3,  4,  1, 11, 10,  0, 14,  0,  1,  0],
    [0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  1,  0],
    [0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0],
    [0,  1,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0],
    [0,  1,  1,  1,  1,  1,  1,  1,  4,  0,  0,  0,  1,  0,  0,  0,  0,  0,  1,  0],
    [0,  1,  0, 13,  0,  0, 17,  4,  0,  0,  0,  0,  1,  1,  1,  1,  1,  1,  1,  0],
    [0,  1,  0,  0,  0,  0,  0, 26,  0,  0,  0,  0,  1, 16,  0, 10,  0, 15,  1,  0],
    [0,  1,  0,  0,  0,  0,  0, 26,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  1,  0],
    [0,  1, 12,  0,  0,  0,  0, 26,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0],
    [0,  1,  0,  0,  0,  0,  0, 26,  0,  0,  0,  0,  0,  0, 24,  0, 25,  0,  1,  0],
    [0,  1,  0,  0,  0,  0,  0, 26,  0,  0,  0,  4,  1,  0,  0,  0,  0,  0,  1,  0],
    [0,  1,  1,  1, 20, 20, 20,  1,  1,  0,  0,  1,  1,  1, 20, 20, 20,  1,  1,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0, 21, 21,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    ]

    world_data4 = [
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  1,  1,  1,  1,  1,  1,  1,  1,  1, 20,  1,  1,  1,  1,  1,  1,  1,  1,  0],
    [0,  1,  5,  0,  6,  7,  0,  1,  8,  9,  3,  4,  1, 11, 10,  0, 14,  0,  1,  0],
    [0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  1,  0],
    [0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 30,  0,  0,  0,  0,  0,  1,  0],
    [0,  1,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0],
    [0,  1,  1,  1,  1,  1,  1,  1,  4,  0,  0,  0,  1,  0,  0,  0,  0,  0,  1,  0],
    [0,  1,  0, 13,  0,  0, 17,  4,  0,  0,  0,  0,  1,  1,  1,  1,  1,  1,  1,  0],
    [0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1, 16,  0, 10,  0, 15,  1,  0],
    [0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  1,  0],
    [0,  1, 12,  0,  0,  0,  0, 28,  0,  0,  0,  0, 30,  0,  0,  0,  0,  0,  1,  0],
    [0,  1,  0,  0,  0,  0,  0, 27,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0],
    [0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  4,  1,  0,  0,  0,  0,  0,  1,  0],
    [0,  1,  1,  1, 20, 20, 20,  1,  1,  0,  0,  1,  1,  1, 20, 20, 20,  1,  1,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0, 21, 21,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    ]

    # Background
    background_1 = background.BG (background_data, tile_size_x, tile_size_y)
    background_5 = background.BG (background_data_5, tile_size_x, tile_size_y)
    # Insumos Correctos y Trampas
    reward_group = pygame.sprite.Group() # Añadirlo a level y player
    trap_group = pygame.sprite.Group() # Añadirlo a level y player

    reward_group_2 = pygame.sprite.Group() # Añadirlo a level y player
    trap_group_2 = pygame.sprite.Group() # Añadirlo a level y player

    reward_group_3 = pygame.sprite.Group() # Añadirlo a level y player
    trap_group_3 = pygame.sprite.Group() # Añadirlo a level y player

    reward_group_4 = pygame.sprite.Group() # Añadirlo a level y player
    trap_group_4 = pygame.sprite.Group() # Añadirlo a level y player

    # Niveles
    level_1 = world.World (world_data1, reward_group, trap_group, tile_size_x, tile_size_y)
    level_2 = world.World (world_data2, reward_group_2, trap_group_2, tile_size_x, tile_size_y)
    level_3 = world.World (world_data3, reward_group_3, trap_group_3, tile_size_x, tile_size_y)
    level_4 = world.World (world_data4, reward_group_4, trap_group_4, tile_size_x, tile_size_y)
                
    # Personaje
    player1 = player.Player(screen, level_1, reward_group, trap_group, screen_width/2, screen_height/2)
    player2 = player.Player(screen, level_2, reward_group_2, trap_group_2, screen_width/2, screen_height/2)
    player3 = player.Player(screen, level_3, reward_group_3, trap_group_3, screen_width/2, screen_height/2)
    player4 = player.Player(screen, level_4, reward_group_4, trap_group_4, tile_size_x*3, tile_size_y*5)

    restart = 0
    level = 'INTRO_SAM'
    audio_intro = 1
    video_tuto_1 = 1
    video_tuto_2 = 1
    # Inicialización Variables Nivel #1
    level_1_state = 1 # Level instruction init
    audio_1_1 = 1
    audio_1_2 = 1
    audio_1_3 = 1
    total_error_l1 = 0
    total_points_l1 = 0
    used_time_l1 = 0
    results_l1 = 0
    level_1_error_1 = 0

    # Inicialización Variables Nivel #2
    level_2_state = 1 # Level instruction init
    audio_2_1 = 1
    audio_2_5 = 1
    audio_2_6 = 1
    total_error_l2 = 0
    total_points_l2 = 0
    used_time_l2 = 0
    results_l2 = 0
    level_2_error_1 = 0
    level_2_error_2 = 0

    # Inicialización Variables Nivel #3
    level_3_state = 1
    audio_3_1 = 1
    audio_3_2 = 1
    audio_3_3 = 1
    audio_3_9 = 1
    audio_3_11 = 1
    audio_3_12 = 1
    total_error_l3 = 0
    total_points_l3 = 0
    used_time_l3 = 0
    results_l3 = 0
    level_3_error = 0

    # Inicialización Variables Nivel #4
    level_4_state = 1
    audio_4_1 = 1
    audio_4_2 = 1
    audio_4_3 = 1
    audio_4_4 = 1
    audio_4_5 = 1
    audio_4_6 = 1
    audio_4_7 = 1
    audio_4_8 = 1
    audio_4_10 = 1
    audio_4_12 = 1
    total_error_l4 = 0
    total_points_l4 = 0
    used_time_l4 = 0
    results_l4 = 0
    level_4_error = 0

    # Inicialización Variables Nivel #5
    level_5_state = 1
    audio_5_1 = 1
    audio_5_2 = 1
    audio_5_3 = 1
    audio_5_4 = 1
    audio_5_5 = 1
    audio_5_6 = 1
    audio_5_7 = 1
    audio_5_8 = 1
    audio_5_9 = 1
    total_error_l5 = 0
    total_points_l5 = 0
    used_time_l5 = 0
    results_l5 = 0
    angle = 0

    audio_end = 1

    res = False
    con = False

    def release_all_keys(): #FUNCIÓN QUE PUEDE LLEGAR A SER UTIL, SIMULA EL SOLTAR LAS TECLAS, PONE LAS TECLAS EN EL ESTADO UP AL POSTEAR EL EVENTO EN EL EVENT QUEUE CON event.post
        key_up_event = pygame.event.Event(pygame.KEYUP, {'key': None})
        pygame.event.post(key_up_event)

    #main = 'MAIN_MENU'
    PAZ = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    begin = True
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                #SOLO podrá cerrar el juego en las pantallas donde exista la opción (logo de salir) # Cerrar juego con tecla "S", actualmente
                if event.key == pygame.K_s and (level == 'PAUSE' or level == 'T0' or level == 'INTRO_SAM' or level == 'TUTO_1' or level == 'TUTO_2' or level == 'results_l1' or level == 'results_l2' or level == 'results_l3' or level == 'results_l4' or level == 'results_l5' or level == 'FINAL'):
                    run = False
                    return PAZ
                    #return main, PAZ
                # else:
                #     run = True
                if event.key == pygame.K_o: # Reiniciar juego con tecla "O", actualmente
                    res = True
                # else: 
                #     res = False
                if event.key == pygame.K_a: # Continuar juego con tecla "a", actualmente
                    con = True
                else: 
                    con = False
                if event.key == pygame.K_p and (actual_level == 1 or actual_level == 2 or actual_level == 3 or actual_level == 4 or actual_level == 5):
                    #pause = True
                    #actual_level = level
                    level = 'PAUSE'
            if event.type == timer_event:
                if begin == True:
                    begin_time -= 1
                    begin_timer_text = begin_timer_font.render(str(begin_time), True, color_white)
                    if begin_time == 0:
                        begin = False
                if begin == False:
                    level_time -= 1 
                    timer_text = timer_font.render(str(level_time), True, color_black)
                    if level_time == 0 and (actual_level == 1 or actual_level == 2 or actual_level == 3 or actual_level == 4 or actual_level == 5):
                        pygame.time.set_timer(timer_event, 0)  
                        level = 'T0'
            if event.type == pygame.QUIT:
                run = False
            

        if level == 'PAUSE':# and actual_level == (1 or 2 or 3 or 4 or 5):
            pygame.mixer.Sound.stop(sL1_1)
            pygame.mixer.Sound.stop(sL1_2)
            pygame.mixer.Sound.stop(sL1_3)
            pygame.mixer.Sound.stop(sL1_4)
            pygame.mixer.Sound.stop(sL1_5)
            screen.blit(levelEND_img, levelEND_rect) # Fondo Pantalla Final
            draw_text("Nivel Pausado",80, color_black, screen_width/2, tile_size_y*2)
            draw_text("Salir",30, color_black, tile_size_x*9, tile_size_y*10)
            draw_text("Reiniciar",30, color_black, tile_size_x*11, tile_size_y*10)
            #draw_text("Continuar",30, color_black, tile_size_x*10, tile_size_y*13.5)
            screen.blit(restart_img, restart_rect)
            screen.blit(exit_img, exit_rect)
            if res == True:
                res = False
                restart = 1
                level = 0
            # Pausar y tener la opción de continuar en el punto pausado puede ser contraproducente para el paciente
            # if continue_bot.draw(screen):
            #     level = 0
            pygame.display.update()
        
        if level == 'T0':
            #pygame.time.set_timer(timer_event, 1000)
            pygame.mixer.Sound.stop(sL1_1)
            pygame.mixer.Sound.stop(sL1_2)
            pygame.mixer.Sound.stop(sL1_3)
            pygame.mixer.Sound.stop(sL1_4)
            pygame.mixer.Sound.stop(sL1_5)
            screen.blit(levelEND_img, levelEND_rect) # Fondo Pantalla Final
            draw_text("Se ha agotado el tiempo del nivel",40, color_black, screen_width/2, tile_size_y*1.5)
            draw_text("Salir",30, color_black, tile_size_x*9, tile_size_y*10)
            draw_text("Reiniciar",30, color_black, tile_size_x*11, tile_size_y*10)
            screen.blit(restart_img, restart_rect)
            screen.blit(exit_img, exit_rect)
            if res == True:
                restart = 1
                level = 0
            
                
            
            pygame.display.update()



        if level == 0:
            
            screen.fill(color_black)
            pygame.display.update()
            pygame.mixer.Sound.stop(sL1_2)
        
            # REINICIOS NIVEL 1
            if level_1_error_1 == 1:
                #screen.fill(color_bluep)
                screen.blit(levelEND_img, levelEND_rect) # Fondo Pantalla Final
                draw_text("¡Sigue Intentando!",80, color_bluep, screen_width/2, tile_size_y*1)
                screen.blit(AI_img, AI_rect)
                pygame.display.update()
                if audio_1_2 == 1:
                    channel.queue(sL1_2)
                    audio_1_2 = 0
                level_1_error_1 = 0
            
                
                

            level_time = actual_level_time
            pygame.time.set_timer(timer_event, 1000) # Reinicio Temporizador

            if actual_level == 1 and restart == 1:
                screen.blit(levelEND_img, levelEND_rect) # Fondo Pantalla Final
                draw_text("Reiniciando Nivel...",100, color_black, screen_width/2, tile_size_y*7)
                pygame.display.update()
                # REINICIO COMPLETO DEL NIVEL REINICIANDO TIEMPO
                begin_time = 8
                begin = True
                level_time = 121
                level_1_state = 1
                audio_1_1 = 1
                audio_1_2 = 1
                audio_1_3 = 1
                total_error_l1 = 0
                total_points_l1 = 0
                used_time_l1 = 0
                results_l1 = 0
                level_1_error_1 = 0
                background_1 = background.BG (background_data, tile_size_x, tile_size_y)
                reward_group = pygame.sprite.Group()
                trap_group = pygame.sprite.Group()
                level_1 = world.World (world_data1, reward_group, trap_group, tile_size_x, tile_size_y)
                player1 = player.Player(screen, level_1, reward_group, trap_group, screen_width/2, screen_height/2)
                restart = 0
                level = 1 # Nivel en el que se encontraba
                
            if actual_level == 1:
                # REINICIO COMPLETO DEL NIVEL MANTENIENDO TIEMPO 
                level_1_state = 1
                audio_1_1 = 1
                audio_1_2 = 1
                audio_1_3 = 1
                background_1 = background.BG (background_data, tile_size_x, tile_size_y)
                reward_group = pygame.sprite.Group()
                trap_group = pygame.sprite.Group()
                level_1 = world.World (world_data1, reward_group, trap_group, tile_size_x, tile_size_y)
                player1 = player.Player(screen, level_1, reward_group, trap_group, screen_width/2, screen_height/2)
                level = actual_level # Nivel en el que se encontraba
            
            # REINICIOS NIVEL 2
            if level_2_error_1 == 1:
                screen.blit(levelEND_img, levelEND_rect) # Fondo Pantalla Final
                draw_text("¡Sigue Intentando!",80, color_bluep, screen_width/2, tile_size_y*1)
                screen.blit(CANVA_img, AI_rect)
                pygame.display.update()
                pygame.mixer.Channel.stop(channel)
                channel.queue(sL2_3)
                level_2_state = 1
                background_1 = background.BG (background_data, tile_size_x, tile_size_y)
                reward_group_2 = pygame.sprite.Group()
                trap_group_2 = pygame.sprite.Group()
                level_2 = world.World (world_data2, reward_group_2, trap_group_2, tile_size_x, tile_size_y)
                player2 = player.Player(screen, level_2, reward_group_2, trap_group_2, screen_width/2, screen_height/2)
                level = actual_level # Nivel en el que se encontraba
                audio_2_1 = 1
                audio_2_5 = 1
                audio_2_6 = 1
                audio_2_7 = 1
                

            if level_2_error_2 == 1:
                screen.blit(levelEND_img, levelEND_rect) # Fondo Pantalla Final
                draw_text("¡Sigue Intentando!",80, color_bluep, screen_width/2, tile_size_y*1)
                screen.blit(AI_img_2, AI_rect)
                pygame.display.update()
                pygame.mixer.Channel.stop(channel)
                channel.queue(sL2_4)
                level_2_state = 1
                background_1 = background.BG (background_data, tile_size_x, tile_size_y)
                reward_group_2 = pygame.sprite.Group()
                trap_group_2 = pygame.sprite.Group()
                level_2 = world.World (world_data2, reward_group_2, trap_group_2, tile_size_x, tile_size_y)
                player2 = player.Player(screen, level_2, reward_group_2, trap_group_2, screen_width/2, screen_height/2)
                level = actual_level # Nivel en el que se encontraba
                audio_2_1 = 1
                audio_2_5 = 1
                audio_2_6 = 1
                audio_2_7 = 1

            if actual_level == 2 and restart == 1:
                screen.blit(levelEND_img, levelEND_rect) # Fondo Pantalla Final
                draw_text("Reiniciando Nivel...",100, color_black, screen_width/2, tile_size_y*7)
                pygame.display.update()
                # REINICIO COMPLETO DEL NIVEL REINICIANDO TIEMPO
                begin_time = 8
                begin = True
                level_2_state = 1
                level_time = 121
                audio_2_1 = 1
                audio_2_5 = 1
                audio_2_6 = 1
                audio_2_7 = 1
                total_error_l2 = 0
                total_points_l2 = 0
                used_time_l2 = 0
                results_l2 = 0
                level_2_error_1 = 0
                level_2_error_2 = 0
                background_1 = background.BG (background_data, tile_size_x, tile_size_y)
                reward_group_2 = pygame.sprite.Group()
                trap_group_2 = pygame.sprite.Group()
                level_2 = world.World (world_data2, reward_group_2, trap_group_2, tile_size_x, tile_size_y)
                player2 = player.Player(screen, level_2, reward_group_2, trap_group_2, screen_width/2, screen_height/2)
                restart = 0
                level = 2 # Nivel en el que se encontraba

            if actual_level == 3 and restart == 1:
                screen.blit(levelEND_img, levelEND_rect) # Fondo Pantalla Final
                draw_text("Reiniciando Nivel...",100, color_black, screen_width/2, tile_size_y*7)
                pygame.display.update()
                # REINICIO COMPLETO DEL NIVEL REINICIANDO TIEMPO
                begin_time = 8
                begin = True
                level_3_state = 1
                level_time = 121
                audio_3_1 = 1
                audio_3_2 = 1
                audio_3_3 = 1
                audio_3_9 = 1
                audio_3_11 = 1
                audio_3_12 = 1
                total_error_l3 = 0
                total_points_l3 = 0
                used_time_l3 = 0
                results_l3 = 0
                level_3_error = 0

                background_1 = background.BG (background_data, tile_size_x, tile_size_y)
                reward_group_3 = pygame.sprite.Group()
                trap_group_3 = pygame.sprite.Group()
                level_3 = world.World (world_data3, reward_group_3, trap_group_3, tile_size_x, tile_size_y)
                player3 = player.Player(screen, level_3, reward_group_3, trap_group_3, screen_width/2, screen_height/2)
                restart = 0
                level = 3 # Nivel en el que se encontraba
        
            if level_3_error == 1:
                screen.blit(levelEND_img, levelEND_rect) # Fondo Pantalla Final
                draw_text("¡Sigue Intentando!",80, color_bluep, screen_width/2, tile_size_y*1)
                draw_text("¡No debes caminar por zonas prohibidas!",70, color_bluep, screen_width/2, tile_size_y*3)
                screen.blit(CANVA_2_img, CANVA_2_rect)
                pygame.display.update()
                level_3_state = 1
                background_1 = background.BG (background_data, tile_size_x, tile_size_y)
                reward_group_3 = pygame.sprite.Group()
                trap_group_3 = pygame.sprite.Group()
                level_3 = world.World (world_data3, reward_group_3, trap_group_3, tile_size_x, tile_size_y)
                player3 = player.Player(screen, level_3, reward_group_3, trap_group_3, screen_width/2, screen_height/2)
                level = actual_level # Nivel en el que se encontraba
                audio_3_1 = 1
                audio_3_2 = 1
                audio_3_3 = 1
                audio_3_9 = 1
                audio_3_11 = 1
                audio_3_12 = 1

            if actual_level == 4 and restart == 1:
                pygame.mixer.Channel.stop(channel)
                screen.blit(levelEND_img, levelEND_rect) # Fondo Pantalla Final
                draw_text("Reiniciando Nivel...",100, color_black, screen_width/2, tile_size_y*7)
                pygame.display.update()
                # REINICIO COMPLETO DEL NIVEL REINICIANDO TIEMPO
                begin_time = 6
                begin = True
                level_4_state = 1
                level_time = 121
                audio_4_1 = 1
                audio_4_2 = 1
                audio_4_3 = 1
                audio_4_4 = 1
                audio_4_5 = 1
                audio_4_6 = 1
                audio_4_7 = 1
                audio_4_8 = 1
                audio_4_9 = 1
                total_error_l4 = 0
                total_points_l4 = 0
                used_time_l4 = 0
                results_l4 = 0
                level_4_error = 0

                background_1 = background.BG (background_data, tile_size_x, tile_size_y)
                reward_group_4 = pygame.sprite.Group()
                trap_group_4 = pygame.sprite.Group()
                level_4 = world.World (world_data4, reward_group_4, trap_group_4, tile_size_x, tile_size_y)
                player4 = player.Player(screen, level_4, reward_group_4, trap_group_4, tile_size_x*3, tile_size_y*5)
                restart = 0
                level = 4 # Nivel en el que se encontraba
            
            if level_4_error == 1:
                level_4_error = 0
                screen.blit(levelEND_img, levelEND_rect) # Fondo Pantalla Final
                draw_text("¡Sigue Intentando!",80, color_bluep, screen_width/2, tile_size_y*1)
                draw_text("¡Busca el tapete antideslizante!",70, color_bluep, screen_width/2, tile_size_y*3)
                screen.blit(CANVA_3_img, CANVA_3_rect)
                pygame.display.update()
                level_4_state = 1
                background_1 = background.BG (background_data, tile_size_x, tile_size_y)
                reward_group_4 = pygame.sprite.Group()
                trap_group_4 = pygame.sprite.Group()
                level_4 = world.World (world_data4, reward_group_4, trap_group_4, tile_size_x, tile_size_y)
                player4 = player.Player(screen, level_4, reward_group_4, trap_group_4, tile_size_x*3, tile_size_y*5)
                level = actual_level # Nivel en el que se encontraba
                audio_4_1 = 1
                audio_4_2 = 1
                audio_4_3 = 1
                audio_4_4 = 1
                audio_4_5 = 1
                audio_4_6 = 1
                audio_4_7 = 1
                audio_4_8 = 1
                audio_4_9 = 1

            if actual_level == 5 and restart == 1:
                pygame.mixer.Channel.stop(channel)
                screen.blit(levelEND_img, levelEND_rect) # Fondo Pantalla Final
                draw_text("Reiniciando Nivel...",100, color_black, screen_width/2, tile_size_y*7)
                pygame.display.update()
                # REINICIO COMPLETO DEL NIVEL REINICIANDO TIEMPO
                begin_time = 6
                begin = True
                level_time = 121
                level_5_state = 1
                level = actual_level
                audio_5_1 = 1
                audio_5_2 = 1
                audio_5_3 = 1
                audio_5_4 = 1
                audio_5_5 = 1
                audio_5_6 = 1
                audio_5_7 = 1
                audio_5_8 = 1
                audio_5_9 = 1
                total_error_l5 = 0
                total_points_l5 = 0
                used_time_l5 = 0
                results_l5 = 0
                level_5_error = 0
                angle = 0

                background_5 = background.BG (background_data_5, tile_size_x, tile_size_y)
                restart = 0
                level = 5 # Nivel en el que se encontraba

        if level == 'INTRO_SAM':
            actual_level = 'INTRO_SAM'
            if audio_intro == 1:
                    pygame.mixer.Sound.play(sIntro)
                    audio_intro = 0
            screen.blit(levelEND_img, levelEND_rect)
            screen.blit(sam_img, sam_rect)  
            draw_text("¡Saluda a SAM!",80, color_black, screen_width/2, tile_size_y*2)
            draw_text("Juntos deben superar los niveles del videojuego, recuerden prestar atención",50, color_black, screen_width/2, tile_size_y*3)
            draw_text("Inicio Tutorial",30, color_black, tile_size_x*10, tile_size_y*13.5)
            draw_text("Salir",30, color_black, tile_size_x*8, tile_size_y*13.5)
            draw_text("Reiniciar",30, color_black, tile_size_x*12, tile_size_y*13.5)
            level_time = 9999 # Tiempo para seleccionar reinicio tuto, salir o inicio lvl 1
            screen.blit(start_img, continue_rect)
            screen.blit(restart_img, restart_rect_2)
            screen.blit(exit_img, exit_rect_2)
            if res == True:
                res = False
                level = 'INTRO_SAM'
                audio_intro = 1
            if con == True:
                con = False
                level = 'TUTO_1' # Valor del siguiente nivel
                level_time = 9999  # Reinicio del tiempo para el siguiente nivel
                video_tuto_1 = 1

        if level == 'TUTO_1':
            actual_level = 'TUTO_1'
            pygame.mixer.Sound.play(sTuto_1)
            if video_tuto_1 == 1:
                    #play_video(tuto, 15, screen_width, screen_height) # PAZ
                    play_video(tuto, 10, screen_width, screen_height) # MINI PC
                    video_tuto_1 = 0
            pygame.mixer.Sound.stop(sTuto_1)   
            screen.blit(levelEND_img, levelEND_rect)
            draw_text("¡Ya puedes iniciar el Nivel 1!",80, color_black, screen_width/2, tile_size_y*3)
            draw_text("Inicio Nivel 1",30, color_black, tile_size_x*10, tile_size_y*13.5)
            draw_text("Salir",30, color_black, tile_size_x*9, tile_size_y*10)
            draw_text("Reiniciar",30, color_black, tile_size_x*11, tile_size_y*10)
            level_time = 9999 # Tiempo para seleccionar reinicio tuto, salir o inicio lvl 1
            screen.blit(start_img, continue_rect)
            screen.blit(restart_img, restart_rect)
            screen.blit(exit_img, exit_rect)
            if res == True:
                res = False
                level = 'TUTO_1'
                video_tuto_1 = 1
            if con == True:
                con = False
                level = 1 # Valor del siguiente nivel
                level_time = 121 # Reinicio del tiempo para el siguiente nivel
                begin_time = 6 # Reinicio del Conteo Regresivo Inicial
                begin = True

        if level == 'TUTO_2':
            actual_level = 'TUTO_2'
            pygame.mixer.Sound.play(sTuto_2)
            if video_tuto_2 == 1:
                #play_video(tuto_2, 20, screen_width, screen_height) #PAZ
                play_video(tuto_2, 15, screen_width, screen_height) # MINI PC
                video_tuto_2 = 0
            pygame.mixer.Sound.stop(sTuto_2)   
            screen.blit(levelEND_img, levelEND_rect)
            draw_text("¡Ya puedes iniciar el Nivel 5!",80, color_black, screen_width/2, tile_size_y*3)
            draw_text("Inicio Nivel 5",30, color_black, tile_size_x*10, tile_size_y*13.5)
            draw_text("Salir",30, color_black, tile_size_x*9, tile_size_y*10)
            draw_text("Reiniciar",30, color_black, tile_size_x*11, tile_size_y*10)
            level_time = 9999 # Tiempo para seleccionar reinicio tuto, salir o inicio lvl 1
            screen.blit(start_img, continue_rect)
            screen.blit(restart_img, restart_rect)
            screen.blit(exit_img, exit_rect)
            if res == True:
                res = False
                level = 'TUTO_2'
                video_tuto_2 = 1
            if con == True:
                con = False
                level = 5 # Valor del siguiente nivel
                level_time = 121 # Reinicio del tiempo para el siguiente nivel
                begin_time = 6 # Reinicio del Conteo Regresivo Inicial
                begin = True        
        
        if level == 1:
            channel = pygame.mixer.Channel(0)

            actual_level = 1
            actual_level_time = level_time

            background_1.draw(screen)
            
            level_1.draw(screen)
            #draw_grid()

            reward_group.update()
            reward_group.draw(screen)
            trap_group.update()
            trap_group.draw(screen)

            player1.update()
            points = player1.points
        

            TIMER(actual_level)
        
            
            if level_1_state == 1:
                draw_text("Ve por tu cepillo de dientes, recuerda que es azul",40, color_black, screen_width/2, tile_size_y*1.5)
                if audio_1_1 == 1:
                    channel.queue(sL1_1)
                    audio_1_1 = 0
                if player1.error == 1:
                    pygame.mixer.Sound.stop(sL1_1)
                    total_error_l1 += 1
                    actual_level_time = level_time
                    level_1_error_1 = 1    
                    level_1_state = 0
                    level = 0
                    total_points_l1 = 0
                player1.error = 0
                if player1.good == 1:
                    total_points_l1 += 1
                    level_1_state += 1
                    audio_1_3 = 1
                # if pause == True:
                #     actual_level_state = 1
                #     level = 'PAUSE'
                    

            if level_1_state == 2:
                draw_text("Ve al baño para limpiar tus dientes",35, color_black, screen_width/2, tile_size_y*1)
                draw_text("¡Recuerda el uso de crema dental para prevenir caries y mal aliento!",35, color_black, screen_width/2, tile_size_y*1.5)
                pygame.mixer.Sound.stop(sL1_1)
                pygame.mixer.Sound.stop(sL1_2)
                if audio_1_3 == 1:
                    channel.queue(sL1_3)
                    audio_1_3 = 0
                screen.blit(arrowUp_img, arrowUp_rect)
                if player1.rect.colliderect(arrowUp_rect):
                    total_points_l1 += 1
                    level_1_state += 1
                if player1.error == 1:
                    pygame.mixer.Sound.stop(sL1_1)
                    pygame.mixer.Sound.stop(sL1_2)
                    pygame.mixer.Sound.stop(sL1_3)
                    total_error_l1 += 1
                    actual_level_time = level_time
                    level_1_error_1 = 1    
                    level_1_state = 0
                    level = 0
                    total_points_l1 = 0
                player1.error = 0
                # if pause == True:
                #     actual_level_state = 2
                #     level = 'PAUSE'
            if level_1_state == 3:
                #draw_text("Lo lograste",40, color_black, screen_width/2, tile_size_y*1.5)
                pygame.mixer.Sound.stop(sL1_1)
                pygame.mixer.Sound.stop(sL1_2)
                pygame.mixer.Sound.stop(sL1_3)
                actual_level_time = level_time
                used_time_l1 = 120 - actual_level_time
                complete_level = 1
                audio_1_4 = 1
                level = 'FIN_L1'    
            pygame.display.update()
        
        if level == 'FIN_L1':
            actual_level = 'FIN_L1'
            level_time = 10000 # Tiempo para observar resultados sin que se termine el juego
            screen.blit(levelEND_img, levelEND_rect) # Fondo Pantalla Final
            screen.blit(coin_img, coin_rect)
            screen.blit(cesta_end_img, cesta_end_rect)
            screen.blit(levelOneR_img, levelOneR_rect)
            draw_text("Continuar",30, color_black, tile_size_x*10, tile_size_y*13.5)
            channel = pygame.mixer.Channel(0)
            screen.blit(start_img, continue_rect)
            if audio_1_4 == 1:
                    sL1_4.play(0)
                    audio_1_4 = 0
                    audio_1_5 = 1
            if con == True:
                con = False
                level = 'results_l1'
        if level == 'results_l1':
            if audio_1_5 == 1:
                channel.queue(sL1_5)
                audio_1_5 = 0
            RESULTS(complete_level, points, used_time_l1, actual_level_time, total_points_l1, total_error_l1)
            PAZ[0][0] = points
            PAZ[0][1] = used_time_l1
            PAZ[0][2] = actual_level_time
            PAZ[0][3] = total_points_l1
            PAZ[0][4] = total_error_l1
            
            draw_text("Inicio Nivel 2",30, color_black, tile_size_x*10, tile_size_y*13.5)
            draw_text("Salir",30, color_black, tile_size_x*9, tile_size_y*10)
            draw_text("Reiniciar",30, color_black, tile_size_x*11, tile_size_y*10)
            screen.blit(start_img, continue_rect)
            screen.blit(restart_img, restart_rect)
            screen.blit(exit_img, exit_rect)
            if run == False:
                pygame.mixer.Channel.stop(channel)
            if res == True:
                actual_level = 1
                res = False
                restart = 1
                level = 0  
            if con == True:
                con = False
                level = 2
                level_time = 121 # Reinicio del tiempo para el siguiente nivel
                begin_time = 6 # Reinicio del Conteo Regresivo Inicial
                begin = True
                pygame.mixer.Channel.stop(channel)
                
            #results_l1 = 1
            
            pygame.display.update()


        if level == 2:
            
            actual_level = 2
            actual_level_time = level_time

            background_1.draw(screen)

            level_2.draw(screen)
            #draw_grid()

            reward_group_2.update()
            reward_group_2.draw(screen)
            trap_group_2.update()
            trap_group_2.draw(screen)
            screen.blit(water_img, water_rect) # Obstaculo de piso mojado
            player2.update()
            points = player2.points
        
            TIMER(actual_level)

            level_2_error_1 = 0
            level_2_error_2 = 0
            
            
            channel = pygame.mixer.Channel(1)
            if level_2_state == 1:
                draw_text("¡Ten cuidado!  El piso del baño está mojado, ve por tus sandalias blancas",35, color_black, screen_width/2, tile_size_y*1.5)
                if audio_2_1 == 1:
                    channel.queue(sL2_1)
                    channel.queue(sL2_2)
                    audio_2_1 = 0
                    

            if player2.rect.colliderect(water_rect) and player2.good == 0:
                pygame.mixer.Channel.stop(channel)
                channel.queue(sL2_3)
                total_error_l2 += 1
                actual_level_time = level_time
                level_2_error_1 = 1   
                level = 0
                total_points_l2 = 0

            if player2.error == 1:
                total_error_l2 += 1
                actual_level_time = level_time
                level_2_error_2 = 1   
                level = 0
                total_points_l2 = 0
            
            if player2.good == 1:
                level_2_state = 0
                draw_text("¡Muy Bien!  Ve al baño",40, color_black, screen_width/2, tile_size_y*1)
                draw_text("Ingresa con cuidado, no corras",35, color_black, screen_width/2, tile_size_y*1.5)
                if audio_2_5 == 1:
                    total_points_l2 += 1
                    channel.queue(sL2_5)
                    audio_2_5 = 0

            if player2.rect.colliderect(water_rect) and player2.good == 1:
                actual_level_time = level_time 
                total_points_l2 += 1
                complete_level = 2
                used_time_l2 = 120 - actual_level_time
                level = 'FIN_L2'

            pygame.display.update() ########

        if level == 'FIN_L2':
            actual_level = 'FIN_L2'
            level_time = 10000 # Tiempo para observar resultados sin que se termine el juego
            screen.blit(levelEND_img, levelEND_rect) # Fondo Pantalla Final
            screen.blit(coin_img, coin_rect)
            screen.blit(cesta_end_img, cesta_end_rect)
            screen.blit(levelTwoR_img, levelTwoR_rect)
            draw_text("Continuar",30, color_black, tile_size_x*10, tile_size_y*13.5)
            channel = pygame.mixer.Channel(0)
            screen.blit(start_img, continue_rect)
            if audio_2_6 == 1:
                channel.queue(sL2_6)
                channel.queue(sL2_7)
                audio_2_8 = 1
                audio_2_6 = 0 
            if con == True:
                con = False
                level = 'results_l2'
        if level == 'results_l2':
            if audio_2_8 == 1:
                channel.queue(sL2_8)
                audio_2_8 = 0
            RESULTS(complete_level, points, used_time_l2, actual_level_time, total_points_l2, total_error_l2)
            PAZ[1][0] = points
            PAZ[1][1] = used_time_l2
            PAZ[1][2] = actual_level_time
            PAZ[1][3] = total_points_l2
            PAZ[1][4] = total_error_l2
            
            draw_text("Inicio Nivel 3",30, color_black, tile_size_x*10, tile_size_y*13.5)
            draw_text("Salir",30, color_black, tile_size_x*9, tile_size_y*10)
            draw_text("Reiniciar",30, color_black, tile_size_x*11, tile_size_y*10)
            screen.blit(start_img, continue_rect)
            screen.blit(restart_img, restart_rect)
            screen.blit(exit_img, exit_rect)
            if run == False:
                pygame.mixer.Channel.stop(channel)
            if res == True:
                actual_level = 2
                res = False
                restart = 1
                level = 0
            if con == True:
                con = False
                level = 3
                level_time = 121 # Reinicio del tiempo para el siguiente nivel
                begin_time = 6 # Reinicio del Conteo Regresivo Inicial
                begin = True
                pygame.mixer.Channel.stop(channel)
            #results_l2 = 1

            pygame.display.update()

        if level == 3:
            
            level_3_error = 0
            actual_level = 3
            actual_level_time = level_time

            background_1.draw(screen)

            level_3.draw(screen)
            #draw_grid()
            
            screen.blit(caution_img, caution_rect)

            reward_group_3.update()
            reward_group_3.draw(screen)
            trap_group_3.update()
            trap_group_3.draw(screen)
            player3.update()
            points = player3.points
        
            TIMER(actual_level)

            channel = pygame.mixer.Channel(2)
            if level_3_state == 1:
                draw_text("Ha llegado el momento de bañarse, necesitas jabón y toalla",35, color_black, screen_width/2, tile_size_y*1.5)
                if audio_3_1 == 1:
                    channel.queue(sL3_1)
                    channel.queue(sL3_2)
                    audio_3_1 = 0
                    
            if player3.points == 1:
                level_3_state = 0 # Se sale del estado inicial y el texto en pantalla puede cambiar
                draw_text("¡Muy Bien!  La toalla sirve para secar el cuerpo, ahora necesitas el jabón",35, color_black, screen_width/2, tile_size_y*1.5)
                if audio_3_2 == 1:
                    total_points_l3 += 1
                    channel.queue(sL3_3)
                    channel.queue(sL3_4)
                    audio_3_2 = 0
                if (player3.rect.colliderect(caution_rect) or player3.error == 1): 
                    draw_text("¡No debes caminar por zonas prohibidas!",35, color_black, screen_width/2, tile_size_y*1.5)
                    level_3_state = 0 
                    pygame.mixer.Channel.stop(channel)
                    if audio_3_11 == 1:
                        channel.queue(sL3_11)
                        audio_3_11 = 0
                    channel.queue(sL3_2)
                    total_error_l3 += 1
                    level_3_error = 1
                    level = 0
                    actual_level_time = level_time
                    total_points_l3 = 0
                audio_3_11 = 1

            if player3.points == 2:
                level_3_state = 0 # Se sale del estado inicial y el texto en pantalla puede cambiar
                draw_text("¡Muy Bien!  El jabón sirve para limpiar tu cuerpo, ahora vamos al baño",35, color_black, screen_width/2, tile_size_y*1.5)
                total_points_l3 += 1
                screen.blit(arrowUp_img, arrowUp_rect2)
                if audio_3_3 == 1:
                    pygame.mixer.Channel.stop(channel)
                    channel.queue(sL3_5)
                    channel.queue(sL3_6) #
                    audio_3_3 = 0
                if (player3.rect.colliderect(caution_rect) or player3.error == 1):
                    pygame.mixer.Channel.stop(channel)
                    if audio_3_11 == 1:
                        channel.queue(sL3_11)
                        audio_3_11 = 0
                    channel.queue(sL3_8)
                    total_error_l3 += 1
                    level_3_error = 1
                    level = 0
                    actual_level_time = level_time
                    total_points_l3 = 0
                if player3.rect.colliderect(arrowUp_rect2):
                    total_points_l3 = 3 # Cantidad de misiones cumplidas, valor fijo para evitar que incremente indefinidamente por la colisión o condición
                    actual_level_time = level_time 
                    complete_level = 3
                    used_time_l3 = 120 - actual_level_time
                    level = 'FIN_L3'
                    

            if (player3.rect.colliderect(caution_rect) or player3.error == 1) and player3.good == 0:
                draw_text("¡No debes caminar por zonas prohibidas!",35, color_black, screen_width/2, tile_size_y*1.5)
                level_3_state = 0 
                pygame.mixer.Channel.stop(channel)
                if audio_3_11 == 1:
                    channel.queue(sL3_11)
                    audio_3_11 = 0
                channel.queue(sL3_2)
                total_error_l3 += 1
                level_3_error = 1
                level = 0
                actual_level_time = level_time
                total_points_l3 = 0
            audio_3_11 = 1

        if level == 'FIN_L3':
            actual_level = 'FIN_L3'
            level_time = 10000 # Tiempo para observar resultados sin que se termine el juego
            screen.blit(levelEND_img, levelEND_rect) # Fondo Pantalla Final
            screen.blit(coin_img, coin_rect)
            screen.blit(cesta_end_img, cesta_end_rect)
            screen.blit(levelThreeR_img1, levelThreeR_rect1)
            screen.blit(levelThreeR_img2, levelThreeR_rect2)
            draw_text("Continuar",30, color_black, tile_size_x*10, tile_size_y*13.5)
            channel = pygame.mixer.Channel(0)
            screen.blit(start_img, continue_rect)
            if audio_3_9 == 1:
                channel.queue(sL3_9)
                channel.queue(sL3_10)
                audio_3_12 = 1
                audio_3_9 = 0 
            if con == True:
                con = False
                level = 'results_l3' 
        if level == 'results_l3':
            if audio_3_12 == 1:
                channel.queue(sL3_12)
                audio_3_12 = 0
            RESULTS(complete_level, points, used_time_l3, actual_level_time, total_points_l3, total_error_l3)
            PAZ[2][0] = points
            PAZ[2][1] = used_time_l3
            PAZ[2][2] = actual_level_time
            PAZ[2][3] = total_points_l3
            PAZ[2][4] = total_error_l3
            
            draw_text("Inicio Nivel 4",30, color_black, tile_size_x*10, tile_size_y*13.5)
            draw_text("Salir",30, color_black, tile_size_x*9, tile_size_y*10)
            draw_text("Reiniciar",30, color_black, tile_size_x*11, tile_size_y*10)
            screen.blit(start_img, continue_rect)
            screen.blit(restart_img, restart_rect)
            screen.blit(exit_img, exit_rect)
            if run == False:
                pygame.mixer.Channel.stop(channel)  
            if res == True:
                actual_level = 3
                res = False
                restart = 1
                level = 0 
            if con == True:
                con = False
                level = 4 # Valor del siguiente nivel
                level_time = 121 # Reinicio del tiempo para el siguiente nivel
                begin_time = 6 # Reinicio del Conteo Regresivo Inicial
                begin = True
                pygame.mixer.Channel.stop(channel)
                
            #results_l3 = 1

            pygame.display.update()

        if level == 4:
            
            actual_level = 4
            actual_level_time = level_time

            background_1.draw(screen)

            level_4.draw(screen)
            #draw_grid()

            screen.blit(tapete_img, tapete_rect)

            reward_group_4.update()
            reward_group_4.draw(screen)
            trap_group_4.update()
            trap_group_4.draw(screen)
            player4.update()
            points = player4.points
        
            
            TIMER(actual_level)
            
            channel = pygame.mixer.Channel(3)
        
            if level_4_state == 1 or level_time >= 115: #Tiempo para reproducir instrucción inicial (5s) y ver texto
                draw_text("Necesitas un tapete antideslizante para poder ingresar y salir de la ducha",35, color_black, screen_width/2, tile_size_y*1.5)
                if audio_4_1 == 1:
                    channel.queue(sL4_1)
                    audio_4_1 = 0
                    if audio_4_2 == 1:
                        channel.queue(sL4_2)
                        audio_4_2 = 0
                        level_4_state = 2
                if player4.error == 1:
                    audio_4_5 = 1
                    total_error_l4 += 1
                    if audio_4_5 == 1:
                        channel.queue(sL4_3) 
                        audio_4_5 = 0
                if player4.rect.colliderect(tapete_rect):
                    draw_text("¡Ese no es un tapete antideslizante!",35, color_black, screen_width/2, tile_size_y*1.5)
                    level_4_state = 0 
                    pygame.mixer.Channel.stop(channel)
                    if audio_4_6 == 1:
                        channel.queue(sL4_6)
                        audio_4_6 = 0
                    channel.queue(sL4_4)
                    total_error_l4 += 1
                    level_4_error = 1
                    level = 0
                    actual_level_time = level_time
                    total_points_l4 = 0
                    
            if level_4_state == 2 and level_time < 115: 
                draw_text("El tapete antideslizante se encuentra en el canasto de la sala",35, color_black, screen_width/2, tile_size_y*1.5) 
                if audio_4_3 == 1:
                    if player4.direction != 0 :
                        channel.queue(sL4_3) 
                        channel.queue(sL4_4) 
                        audio_4_3 = 0       
                if player4.error == 1 and player4.points == 0:
                    audio_4_5 = 1
                    total_error_l4 += 1
                    if audio_4_5 == 1:
                        channel.queue(sL4_5) 
                        audio_4_5 = 0
                if player4.points == 1:
                    audio_4_7 = 1
                    total_points_l4 += 1
                    level_4_state = 3
                    if audio_4_7 == 1:
                        channel.queue(sL4_7)
                        channel.queue(sL4_9)
                        audio_4_7 = 0
                if player4.rect.colliderect(tapete_rect):
                    draw_text("¡Ese no es un tapete antideslizante!",35, color_black, screen_width/2, tile_size_y*1.5)
                    level_4_state = 0 
                    pygame.mixer.Channel.stop(channel)
                    if audio_4_6 == 1:
                        channel.queue(sL4_6)
                        audio_4_6 = 0
                    channel.queue(sL4_4)
                    total_error_l4 += 1
                    level_4_error = 1
                    level = 0
                    actual_level_time = level_time
                    total_points_l4 = 0
                    
            
            if level_4_state == 3:
                screen.blit(arrowUp_img, arrowUp_rect2)
                draw_text("Debes llevar el tapete a la entrada de la ducha",35, color_black, screen_width/2, tile_size_y*1) 
                draw_text("Con el tapete puedes evitar resbalar al entrar y salir de la ducha",35, color_black, screen_width/2, tile_size_y*1.5)
                if player4.rect.colliderect(tapete_rect):
                    draw_text("¡Ese no es un tapete antideslizante!",35, color_black, screen_width/2, tile_size_y*1.5)
                    level_4_state = 0 
                    pygame.mixer.Channel.stop(channel)
                    if audio_4_6 == 1:
                        channel.queue(sL4_6)
                        audio_4_6 = 0
                    channel.queue(sL4_4)
                    total_error_l4 += 1
                    level_4_error = 1
                    level = 0
                    actual_level_time = level_time
                    total_points_l4 = 0
                if player4.error == 1:
                    draw_text("Debes llevar el tapete a la entrada de la ducha",35, color_black, screen_width/2, tile_size_y*1.5) 
                    draw_text("Con el tapete puedes evitar resbalar al entrar y salir de la ducha",35, color_black, screen_width/2, tile_size_y*1.5)
                    audio_4_8 = 1
                    total_error_l4 += 1
                    if audio_4_8 == 1:
                        channel.queue(sL4_8) 
                        channel.queue(sL4_9)
                        audio_4_8 = 0     
                if player4.rect.colliderect(arrowUp_rect2):
                    pygame.mixer.Channel.stop(channel)
                    total_points_l4 = 2 # Cantidad de misiones cumplidas, valor fijo para evitar que incremente indefinidamente por la colisión o condición
                    actual_level_time = level_time 
                    complete_level = 4
                    used_time_l4 = 120 - actual_level_time
                    level = 'FIN_L4'

            pygame.display.update() ########

        if level == 'FIN_L4':
            actual_level = 'FIN_L4'
            level_time = 10000 # Tiempo para observar resultados sin que se termine el juego
            screen.blit(levelEND_img, levelEND_rect) # Fondo Pantalla Final
            screen.blit(coin_img, coin_rect)
            screen.blit(cesta_end_img, cesta_end_rect)
            screen.blit(levelFourR_img, levelFourR_rect)
            draw_text("Continuar",30, color_black, tile_size_x*10, tile_size_y*13.5)
            channel = pygame.mixer.Channel(0)
            screen.blit(start_img, continue_rect)
            if audio_4_10 == 1:
                channel.queue(sL4_10)
                channel.queue(sL4_11)
                audio_4_10 = 0 
            if con == True:
                con = False
                level = 'results_l4'
        if level == 'results_l4':
            if audio_4_12 == 1:
                channel.queue(sL4_12)
                audio_4_12 = 0
            RESULTS(complete_level, points, used_time_l4, actual_level_time, total_points_l4, total_error_l4)
            PAZ[3][0] = points
            PAZ[3][1] = used_time_l4
            PAZ[3][2] = actual_level_time
            PAZ[3][3] = total_points_l4
            PAZ[3][4] = total_error_l4
            
            draw_text("Inicio Nivel 5",30, color_black, tile_size_x*10, tile_size_y*13.5)
            draw_text("Salir",30, color_black, tile_size_x*9, tile_size_y*10)
            draw_text("Reiniciar",30, color_black, tile_size_x*11, tile_size_y*10)
            screen.blit(start_img, continue_rect)
            screen.blit(restart_img, restart_rect)
            screen.blit(exit_img, exit_rect)
            if run == False:
                pygame.mixer.Channel.stop(channel)
            if res == True:
                actual_level = 4
                res = False
                restart = 1
                level = 0
            if con == True:
                con = False
                level = 'TUTO_2' # Valor del siguiente nivel
                level_time = 121 # Reinicio del tiempo para el siguiente nivel
                begin_time = 6 # Reinicio del Conteo Regresivo Inicial
                begin = True
                pygame.mixer.Channel.stop(channel)
            #results_l4 = 1

            pygame.display.update()

        if level == 5:
            
            actual_level = 5
            actual_level_time = level_time

            background_5.draw(screen)

            screen.blit(levelFiveBG_img, levelFiveBG_rect) # Fondo Nivel 5
            TIMER(actual_level)

            channel = pygame.mixer.Channel(4)
            
            if level_5_state == 1 or level_time >= 117: #Tiempo para reproducir instrucción inicial (5s) y ver texto
                draw_text("Debes ajustar la temperatura del agua de la ducha",35, color_black, screen_width/2, tile_size_y*1.5)
                if audio_5_1 == 1:
                    channel.queue(sL5_1)
                    audio_5_1 = 0
                    level_5_state = 2

            if level_5_state == 2 and level_time <= 116:
                draw_text("Debes bañarte con agua tibia",35, color_black, screen_width/2, tile_size_y*1.5)
                if audio_5_2 == 1:
                        channel.queue(sL5_2)
                        audio_5_2 = 0
                if audio_5_3 == 1:
                    channel.queue(sL5_3)
                    audio_5_3 = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        angle -= 5
                        if angle == -90:
                            angle = 0
                            if audio_5_4 == 1:
                                channel.queue(sL5_5)
                                audio_5_4 = 0
                                level_5_state = 3  

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        angle += 5
                        if angle == 90:
                            angle = 0
                            if audio_5_5 == 1:
                                channel.queue(sL5_4)
                                audio_5_5 = 0
                                level_5_state = 4
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        angle = 0
                        if angle == 0:
                            if audio_5_6 == 1:
                                channel.queue(sL5_6)
                                audio_5_6 = 0
                                level_5_state = 5

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        angle -= 5
                        if angle == -180:
                            if audio_5_7 == 1:
                                channel.queue(sL5_7)
                                audio_5_7 = 0
                                level_5_state = 6
                
                perilla_copy = pygame.transform.rotate(perilla_img, angle)
                screen.blit(perilla_copy, (tile_size_x*10 - int(perilla_copy.get_width()/2), tile_size_y*9.2 - int(perilla_copy.get_height()/2))) 

            if level_5_state == 3:
                screen.blit(l5_LEFT_img, l5_LEFT_rect) # Fondo Nivel 5 Agua Fría
                pygame.display.update()
                pygame.time.delay(2000)
                audio_5_3 = 1
                if audio_5_3 == 1:
                    channel.queue(sL5_3)
                    audio_5_3 = 0
                    audio_5_2 = 1
                    audio_5_4 = 1
                total_error_l5 += 1
                level_5_state = 2

            if level_5_state == 4:
                screen.blit(l5_RIGHT_img, l5_RIGHT_rect) # Fondo Nivel 5 Agua Caliente
                pygame.display.update()
                pygame.time.delay(2000)
                audio_5_3 = 1
                if audio_5_3 == 1:
                    channel.queue(sL5_3)
                    audio_5_3 = 0
                    audio_5_2 = 1
                    audio_5_5 = 1
                total_error_l5 += 1
                level_5_state = 2

            if level_5_state == 5:
                screen.blit(l5_DOWN_img, l5_DOWN_rect) # Fondo Nivel 5 Apagada
                pygame.display.update()
                pygame.time.delay(2000)
                audio_5_3 = 1
                if audio_5_3 == 1:
                    channel.queue(sL5_3)
                    audio_5_3 = 0
                    audio_5_2 = 1
                    audio_5_6 = 1
                total_error_l5 += 1
                level_5_state = 2

            if level_5_state == 6:
                screen.blit(l5_UP_img, l5_UP_rect) # Fondo Nivel 5 Tibia
                pygame.display.update()
                pygame.time.delay(4000)
                pygame.mixer.Channel.stop(channel)
                if audio_5_7 == 1:
                    channel.queue(sL5_7)
                    audio_5_7 = 0 
                
                points = 1
                total_points_l5 = 1 # Cantidad de misiones cumplidas, valor fijo para evitar que incremente indefinidamente por la colisión o condición
                actual_level_time = level_time 
                complete_level = 5
                used_time_l5 = 120 - actual_level_time
                level = 'FIN_L5'
            

            pygame.display.update() ########    
        
        if level == 'FIN_L5':
            actual_level = 'FIN_L5'
            level_time = 10000 # Tiempo para observar resultados sin que se termine el juego
            screen.blit(levelEND_img, levelEND_rect) # Fondo Pantalla Final
            screen.blit(coin_img, coin_rect)
            screen.blit(cesta_end_img, cesta_end_rect)
            screen.blit(levelFiveR_img, levelFiveR_rect)
            draw_text("Continuar",30, color_black, tile_size_x*10, tile_size_y*13.5)
            channel = pygame.mixer.Channel(0)
            screen.blit(start_img, continue_rect)
            if audio_5_8 == 1:
                channel.queue(sL5_8)
                audio_5_8 = 0 
            if con == True:
                con = False
                level = 'results_l5' 
        if level == 'results_l5':
            if audio_5_9 == 1:
                channel.queue(sL5_9)
                audio_5_9 = 0
            RESULTS(complete_level, points, used_time_l5, actual_level_time, total_points_l5, total_error_l5)
            PAZ[4][0] = points
            PAZ[4][1] = used_time_l5
            PAZ[4][2] = actual_level_time
            PAZ[4][3] = total_points_l5
            PAZ[4][4] = total_error_l5
            
            draw_text("¡Final!",30, color_black, tile_size_x*10, tile_size_y*13.5)
            draw_text("Salir",30, color_black, tile_size_x*9, tile_size_y*10)
            draw_text("Reiniciar",30, color_black, tile_size_x*11, tile_size_y*10)
            screen.blit(start_img, continue_rect)
            screen.blit(restart_img, restart_rect)
            screen.blit(exit_img, exit_rect)
            if run == False:
                pygame.mixer.Channel.stop(channel)
            if res == True:
                actual_level = 5
                res = False
                restart = 1
                level = 0
            if con == True:
                con = False
                level = 'FINAL' # Valor del siguiente nivel
                audio_end = 1
                level_time = 121 # Reinicio del tiempo para el siguiente nivel
                begin_time = 6 # Reinicio del Conteo Regresivo Inicial
                begin = True
                pygame.mixer.Channel.stop(channel)
            

            pygame.display.update()

        if level == 'FINAL':
            actual_level = 'FINAL'
            level_time = 10000 # Tiempo para observar resultados sin que se termine el juego
            screen.blit(final_img, final_rect) # Fondo Pantalla Final
            
            draw_text("Salir",30, color_black, tile_size_x*18.5, tile_size_y*14)
            #draw_text("Reiniciar",30, color_black, tile_size_x*1.5, tile_size_y*14)
            channel = pygame.mixer.Channel(0)
            if audio_end == 1:
                channel.queue(sEnd)
                audio_end = 0 
            # if res == True:
            #     res = False
            #     audio_intro = 1
            #     video_tuto_1 = 1
            #     video_tuto_2 = 1
            #     level = 'INTRO_SAM'
            

            pygame.display.update()    
        pygame.display.update() ########
            
        
    # pygame.quit()

    return PAZ
    #return main, PAZ

   


