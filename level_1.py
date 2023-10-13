import pygame
from pygame.locals import *

class L1():
    def __init__(self, level_time, background_1, screen, level_1, reward_group, trap_group, ):
        self.actual_level = 1
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
    
        timer_rect = timer_text.get_rect(center = (tile_size_x*19,tile_size_y*1.5)) # Centro de la pantalla: center = screen.get_rect().center
        screen.blit(clock_img, clock_rect)
        screen.blit(timer_text, timer_rect)
        screen.blit(cesta_img, cesta_rect)
        draw_text("NIVEL 1",40, color_purple, screen_width/2, tile_size_y*0.5)
    
        
        if level_1_state == 1:
            draw_text("Ve por tu cepillo de dientes, recuerda que es azul",40, color_black, screen_width/2, tile_size_y*1.5)
            if audio_1_1 == 1:
                pygame.mixer.Sound.play(sL1_1)
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
            draw_text("Ve al baño para limpiar tus dientes",40, color_black, screen_width/2, tile_size_y*1.5)
            pygame.mixer.Sound.stop(sL1_1)
            pygame.mixer.Sound.stop(sL1_2)
            if audio_1_3 == 1:
                pygame.mixer.Sound.play(sL1_3)
                audio_1_3 = 0
            screen.blit(arrowUp_img, arrowUp_rect)
            if player1.rect.colliderect(arrowUp_rect):
                total_points_l1 += 1
                level_1_state += 1
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
            #     actual_level_state = 3
            #     level = 'PAUSE'
        #print('Puntos ', points)
        pygame.display.update()
    
        