import pygame
import funciones
def memoria():
    while funciones.open_game:
    #screen.blit(fondo, (0,0)) # Función que dibuja el fondo

        if funciones.game_state == 'intro':
            funciones.intro()

        if funciones.game_state == 'instruc':
            funciones.instruc()
        
        if funciones.game_state == 'f_step':
            funciones.f_step()
            
        if funciones.game_state == 'q_nivel_prueba':
            funciones.q_nivel_prueba()

        if funciones.game_state == 'video_protesis1':
            funciones.video_protesis1()

        if funciones.game_state == 'video_instrumentos':
            funciones.video_instrumentos()

        if funciones.game_state == 'cont_rutina':
            funciones.cont_rutina()

        if funciones.game_state == 'personaje':
            funciones.personaje()

        if funciones.game_state == 'video_enjuague_agua':
            funciones.video_enjuague_agua()

        if funciones.game_state == 'video_sostener_hilo':
            funciones.video_sostener_hilo()

        if funciones.game_state == 'video_mover_hilo':
            funciones.video_mover_hilo()

        if funciones.game_state == 'video_ubicar_cepillo':
            funciones.video_ubicar_cepillo()

        if funciones.game_state == 'video_cepillar_circulos':
            funciones.video_cepillar_circulos()

        if funciones.game_state == 'video_enjuague_crema':
            funciones.video_enjuague_crema()

        if funciones.game_state == 'video_enjuague_bucal':
            funciones.video_enjuague_bucal()

        if funciones.game_state == 'exp_protesis2':
            funciones.exp_protesis2()

        if funciones.game_state == 'exp_prot2':
            funciones.exp_prot2()     

        if funciones.game_state == 'juego_fin':
            funciones.juego_fin()  

        if funciones.game_state == 'first_level_card':
            funciones.first_level_card()         
        
        if funciones.game_state == 'id_niveles':
            funciones.id_niveles()   

    #-------------------------------------------------Primero
        if funciones.game_state == 'first_level':
            funciones.first_level()

        if funciones.game_state == 'Fst_level':
            funciones.Fst_level()
            funciones.state_before_pause = 1
        
        if funciones.game_state == 'completed_1':
            funciones.completed_1()
        
        if funciones.game_state == 'recompensa_1':
            funciones.recompensa_1()

        if funciones.game_state == 'reflection_1':
            funciones.reflection_1()

        if funciones.game_state == 'uncompleted_1':
            funciones.uncompleted_1()

    #-------------------------------------------------Segundo
        if funciones.game_state == 'secondcard':
            funciones.actual_state = 1
            funciones.level_card(funciones.actual_state)
            
        if funciones.game_state == 'second_level':
            funciones.second_level()

        if funciones.game_state == 'Scnd_level':
            funciones.Scnd_level()
            funciones.state_before_pause = 2 

        if funciones.game_state == 'completed_2':
            funciones.completed_2()
        
        if funciones.game_state == 'recompensa_2':
            funciones.recompensa_2()

        if funciones.game_state == 'reflection_2':
            funciones.reflection_2()

        if funciones.game_state == 'uncompleted_2':
            funciones.uncompleted_2()
    #-------------------------------------------------Tercero
        if funciones.game_state == 'thirdcard':
            funciones.actual_state = 2
            funciones.level_card(funciones.actual_state)
            
        if funciones.game_state == 'third_level':
            funciones.third_level()

        if funciones.game_state == 'Thrd_level':
            funciones.Thrd_level()
            funciones.state_before_pause = 3 

        if funciones.game_state == 'completed_3':
            funciones.completed_3()
        
        if funciones.game_state == 'recompensa_3':
            funciones.recompensa_3()

        if funciones.game_state == 'reflection_3':
            funciones.reflection_3()

        if funciones.game_state == 'uncompleted_3':
            funciones.uncompleted_3()
    #-------------------------------------------------Cuarto
        if funciones.game_state == 'fourthcard':
            funciones.actual_state = 3
            funciones.level_card(funciones.actual_state)
        
        if funciones.game_state == 'fourth_level':
            funciones.fourth_level()

        if funciones.game_state == 'Frth_level':
            funciones.Frth_level()
            funciones.state_before_pause = 4 

        if funciones.game_state == 'completed_4':
            funciones.completed_4()
        
        if funciones.game_state == 'recompensa_4':
            funciones.recompensa_4()

        if funciones.game_state == 'reflection_4':
            funciones.reflection_4()

        if funciones.game_state == 'uncompleted_4':
            funciones.uncompleted_4()
    #-------------------------------------------------Quinto
        if funciones.game_state == 'fifthcard':
            funciones.actual_state = 4
            funciones.level_card(funciones.actual_state)
            
        if funciones.game_state == 'fifth_level':
            funciones.fifth_level()

        if funciones.game_state == 'Ffth_level':
            funciones.Ffth_level()
            funciones.state_before_pause = 5 

        if funciones.game_state == 'completed_5':
            funciones.completed_5()
        
        if funciones.game_state == 'recompensa_5':
            funciones.recompensa_5()

        if funciones.game_state == 'reflection_5':
            funciones.reflection_5()

        if funciones.game_state == 'uncompleted_5':
            funciones.uncompleted_5()

    #-------------------------------------------------Sexto
        if funciones.game_state == 'sixthcard':
            funciones.actual_state = 5
            funciones.level_card(funciones.actual_state)
            
        if funciones.game_state == 'sixth_level':
            funciones.sixth_level()

        if funciones.game_state == 'Sxth_level':
            funciones.Sxth_level()
            funciones.state_before_pause = 6 

        if funciones.game_state == 'completed_6':
            funciones.completed_6()
        
        if funciones.game_state == 'recompensa_6':
            funciones.recompensa_6()

        if funciones.game_state == 'reflection_6':
            funciones.reflection_6()

        if funciones.game_state == 'uncompleted_6':
            funciones.uncompleted_6()
    #-------------------------------------------------Septimo
        if funciones.game_state == 'seventhcard':
            funciones.actual_state = 6
            funciones.level_card(funciones.actual_state)
            
        if funciones.game_state == 'seventh_level':
            funciones.seventh_level()

        if funciones.game_state == 'Svnth_level':
            funciones.Svnth_level()
            funciones.state_before_pause = 7 

        if funciones.game_state == 'completed_7':
            funciones.completed_7()
        
        if funciones.game_state == 'recompensa_7':
            funciones.recompensa_7()

        if funciones.game_state == 'reflection_7':
            funciones.reflection_7()

        if funciones.game_state == 'uncompleted_7':
            funciones.uncompleted_7()
    #-------------------------------------------------Octavo
        if funciones.game_state == 'eighthcard':
            funciones.actual_state = 7
            funciones.level_card(funciones.actual_state)
            
        if funciones.game_state == 'eighth_level':
            funciones.eighth_level()

        if funciones.game_state == 'Eighth_level':
            funciones.Eighth_level()
            funciones.state_before_pause = 8 

        if funciones.game_state == 'completed_8':
            funciones.completed_8()
        
        if funciones.game_state == 'recompensa_8':
            funciones.recompensa_8()

        if funciones.game_state == 'reflection_8':
            funciones.reflection_8()

        if funciones.game_state == 'uncompleted_8':
            funciones.uncompleted_8()
    #-------------------------------------------------Noveno
        if funciones.game_state == 'ninthcard':
            funciones.actual_state = 8
            funciones.level_card(funciones.actual_state)
            
        if funciones.game_state == 'ninth_level':
            funciones.ninth_level()

        if funciones.game_state == 'Nnth_level':
            funciones.Nnth_level()
            funciones.state_before_pause = 9 

        if funciones.game_state == 'completed_9':
            funciones.completed_9()
        
        if funciones.game_state == 'recompensa_9':
            funciones.recompensa_9()

        if funciones.game_state == 'reflection_9':
            funciones.reflection_9()

        if funciones.game_state == 'uncompleted_9':
            funciones.uncompleted_9()
    #-------------------------------------------------Decimo
        if funciones.game_state == 'tenthcard':
            funciones.actual_state = 9
            funciones.level_card(funciones.actual_state)
            
        if funciones.game_state == 'tenth_level':
            funciones.tenth_level()

        if funciones.game_state == 'Tnth_level':
            funciones.Tnth_level()
            funciones.state_before_pause = 10 

        if funciones.game_state == 'completed_10':
            funciones.completed_10()
        
        if funciones.game_state == 'recompensa_10':
            funciones.recompensa_10()

        if funciones.game_state == 'reflection_10':
            funciones.reflection_10()

        if funciones.game_state == 'uncompleted_10':
            funciones.uncompleted_10()


        if funciones.game_state == 'Pausado': # PANTALLA DE PAUSA
            funciones.pausa(funciones.state_before_pause)

        #Controlar el cursor con la palanca
        if funciones.isGame:# and funciones.Fst_level:
            if funciones.game_state == 'Fst_level':
                tam_cursor = funciones.tam_imgs_fst
            if funciones.game_state == 'Scnd_level':
                tam_cursor = funciones.tam2
            if funciones.game_state == 'Thrd_level':
                tam_cursor = funciones.tam3
            if funciones.game_state == 'Frth_level':
                tam_cursor = funciones.tam4
            if funciones.game_state == 'Ffth_level':
                tam_cursor = funciones.tam5
            if funciones.game_state == 'Sxth_level':
                tam_cursor = funciones.tam6
            if funciones.game_state == 'Svnth_level':
                tam_cursor = funciones.tam7
            if funciones.game_state == 'Eighth_level':
                tam_cursor = funciones.tam8
            if funciones.game_state == 'Nnth_level':
                tam_cursor = funciones.tam9
            if funciones.game_state == 'Tnth_level':
                tam_cursor = funciones.tam10



            funciones.posX += funciones.movimiento_x
            funciones.posY += funciones.movimiento_y
            
            # Limitar las posiciones dentro de los límites de la ventana
            radius = (tam_cursor // 2)-11
            diameter = tam_cursor - 23
            funciones.posX = max(radius, min(funciones.posX, funciones.screen_width - radius))
            funciones.posY = max(radius, min(funciones.posY, funciones.screen_height - radius))
            
            funciones.screen.blit(pygame.transform.scale(funciones.pointer, (diameter, diameter)), (funciones.posX - diameter / 2, funciones.posY - diameter / 2))
            #pygame.draw.circle(screen, color_black,  (funciones.posX, funciones.posY), 125, 15)
            #pygame.draw.circle(screen, color_red, (funciones.posX, funciones.posY), 20)

            pygame.display.update()  

        # Event Handler
        for event in pygame.event.get(): # Evento de pygame
            if event.type == pygame.KEYDOWN: # Evento: Tecla presionada
                if event.key == pygame.K_p: # Tecla e para pausar
                    funciones.paused_game = True
                if event.key == pygame.K_a: # Tecla s para continuar
                    funciones.next_window = True
                if event.key == pygame.K_s: # Tecla a para atrás
                    funciones.back_window = True
                if event.key == pygame.K_f: # Tecla o para volver a la intro de memoria
                    funciones.ret_intro = True
                if event.key == pygame.K_x: # Tecla  para continuar con el juego
                    funciones.cont_game = True
                if event.key == pygame.K_o: # Tecla reinicio
                    funciones.reinicio = True 
                if event.key == pygame.K_v and funciones.game_state == 'personaje':
                    funciones.s1 = True
                if event.key == pygame.K_n and funciones.game_state == 'personaje':
                    funciones.s2 = True  
                if event.key == pygame.K_c and funciones.game_state == 'personaje':
                    funciones.s3 = True    
                if event.key == pygame.K_e and funciones.game_state == 'personaje':
                    funciones.s4 = True               
                        
                # Si hicieron clic y el usuario puede jugar...
                # Primer nivel seleccionar tarjeta con tecla b
                if event.key == pygame.K_b and funciones.puede_jugar and funciones.game_state == 'Fst_level':
                    funciones.prueba = True
                else:
                    funciones.prueba = False
                # Segundo nivel seleccionar tarjeta con tecla b
                if event.key == pygame.K_b and funciones.puede_jugar_2 and funciones.game_state == 'Scnd_level':
                    funciones.prueba2 = True
                else:
                    funciones.prueba2 = False
                # Tercer nivel seleccionar tarjeta con tecla b
                if event.key == pygame.K_b and funciones.puede_jugar_3 and funciones.game_state == 'Thrd_level':
                    funciones.prueba3 = True
                else:
                    funciones.prueba3 = False
                # Cuarto nivel seleccionar tarjeta con tecla b
                if event.key == pygame.K_b and funciones.puede_jugar_4 and funciones.game_state == 'Frth_level':
                    funciones.prueba4 = True
                else:
                    funciones.prueba4 = False
                # Quinto nivel seleccionar tarjeta con tecla b
                if event.key == pygame.K_b and funciones.puede_jugar_5 and funciones.game_state == 'Ffth_level':
                    funciones.prueba5 = True
                else:
                    funciones.prueba5 = False
                # Sexto nivel seleccionar tarjeta con tecla b
                if event.key == pygame.K_b and funciones.puede_jugar_6 and funciones.game_state == 'Sxth_level':
                    funciones.prueba6 = True
                else:
                    funciones.prueba6 = False
                # Septimo nivel seleccionar tarjeta con tecla b
                if event.key == pygame.K_b and funciones.puede_jugar_7 and funciones.game_state == 'Svnth_level':
                    funciones.prueba7 = True
                else:
                    funciones.prueba7 = False
                # Octavo nivel seleccionar tarjeta con tecla b
                if event.key == pygame.K_b and funciones.puede_jugar_8 and funciones.game_state == 'Eighth_level':
                    funciones.prueba8 = True
                else:
                    funciones.prueba8 = False
                # Noveno nivel seleccionar tarjeta con tecla b
                if event.key == pygame.K_b and funciones.puede_jugar_9 and funciones.game_state == 'Nnth_level':
                    funciones.prueba9 = True
                else:
                    funciones.prueba9 = False
                # Decimo nivel seleccionar tarjeta con tecla b
                if event.key == pygame.K_b and funciones.puede_jugar_10 and funciones.game_state == 'Tnth_level':
                    funciones.prueba10 = True
                else:
                    funciones.prueba10 = False

                if event.key == pygame.K_LEFT and funciones.yes_no_question:
                    funciones.no = True
                if event.key == pygame.K_RIGHT and funciones.yes_no_question:
                    funciones.yes = True


            if event.type == pygame.KEYDOWN and funciones.isGame:
                
                # Para el movimiento del cursor
                if event.key == pygame.K_UP and funciones.isGame:
                    funciones.movimiento_y -= funciones.velocidad

                if event.key == pygame.K_DOWN and funciones.isGame:
                    funciones.movimiento_y += funciones.velocidad

                if event.key == pygame.K_LEFT and funciones.isGame:
                    funciones.movimiento_x -= funciones.velocidad

                if event.key == pygame.K_RIGHT and funciones.isGame:
                    funciones.movimiento_x += funciones.velocidad
                
        
            # si se suelta la tecla
            if event.type == pygame.KEYUP and funciones.isGame:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN and funciones.isGame:
                    funciones.movimiento_y = 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT and funciones.isGame:
                    funciones.movimiento_x = 0   
            
            
            #-----------------Tiempos primer nivel-----------------------------

            # Cronometro del primer nivel
            if event.type == funciones.timer_event and funciones.game_state == 'first_level':
                funciones.level_time -= 1 
                funciones.timer_text = funciones.timer_font.render(str(funciones.level_time), True, funciones.color_black)
                if funciones.level_time <= 0:
                    pygame.time.set_timer(funciones.timer_event, 0)
                    funciones.timer_active = False
                    funciones.game_state = 'Fst_level'
                    ##Puedo poner variables para cambiar de nivel o pantallas

            # Temporizador del primer nivel
            if event.type == funciones.start_timer_event and funciones.game_state == 'Fst_level': 
                funciones.start_time += 1 
                funciones.start_timer_text = funciones.timer_font.render(str(funciones.start_time), True, funciones.color_black)
                if funciones.start_time == funciones.time_limit_1:
                    funciones.start_time = 0
                    pygame.time.set_timer(funciones.start_timer_event, 0)
                    funciones.start_timer_active = False
                    funciones.ganar_rein1 = 0
                    funciones.game_state = 'reflection_1'
                    funciones.used_time_1 = funciones.time_limit_1
                    funciones.unused_time_1 = 0

                if  funciones.aux_cronometro: 
                    pygame.time.set_timer(funciones.start_timer_event, 0)
                    funciones.start_timer_active = False
                    funciones.aux_cronometro = False


                ##Puedo poner variables para cambiar de nivel o pantallas

            #-----------------Tiempos segundo nivel-----------------------------
            # Cronometro del segundo nivel
            if event.type == funciones.timer_event_2 and funciones.game_state == 'second_level':
                funciones.level_time_2 -= 1 
                funciones.timer_text_2 = funciones.timer_font_2.render(str(funciones.level_time_2), True, funciones.color_black)
                if funciones.level_time_2 <= 0:
                    funciones.timer_active_2 = False
                    pygame.time.set_timer(funciones.timer_event_2, 0)
                    funciones.game_state = 'Scnd_level'

            # Temporizador del segundo
            if event.type == funciones.start_timer_event_2 and funciones.game_state == 'Scnd_level': 
                funciones.start_time_2 += 1 
                funciones.start_timer_text_2 = funciones.timer_font.render(str(funciones.start_time_2), True, funciones.color_black)
                if funciones.start_time_2 == funciones.time_limit_2:
                    funciones.start_time_2 = 0
                    pygame.time.set_timer(funciones.start_timer_event_2, 0)
                    funciones.start_timer_active_2 = False
                    funciones.game_state = 'reflection_2'
                    funciones.used_time_2 = funciones.time_limit_2
                    funciones.unused_time_2 = 0

                if  funciones.aux_cronometro2: 
                    pygame.time.set_timer(funciones.start_timer_event_2, 0)
                    funciones.start_timer_active_2 = False
                    funciones.aux_cronometro2 = False
        

            #-----------------Tiempos tercer nivel-----------------------------
            # Cronometro del tercero nivel
            if event.type == funciones.timer_event_3 and funciones.game_state == 'third_level':
                funciones.level_time_3 -= 1 
                funciones.timer_text_3 = funciones.timer_font_3.render(str(funciones.level_time_3), True, funciones.color_black)
                if funciones.level_time_3 <= 0:
                    funciones.timer_active_3 = False
                    pygame.time.set_timer(funciones.timer_event_3, 0)
                    funciones.game_state = 'Thrd_level'

            # Temporizador del tercero
            if event.type == funciones.start_timer_event_3 and funciones.game_state == 'Thrd_level': 
                funciones.start_time_3 += 1 
                funciones.start_timer_text_3 = funciones.timer_font.render(str(funciones.start_time_3), True, funciones.color_black)
                if funciones.start_time_3 == funciones.time_limit_3:
                    funciones.start_time_3 = 0
                    pygame.time.set_timer(funciones.start_timer_event_3, 0)
                    funciones.start_timer_active_3 = False
                    funciones.game_state = 'reflection_3'
                    funciones.used_time_3 = funciones.time_limit_3
                    funciones.unused_time_3 = 0

                if  funciones.aux_cronometro3: 
                    pygame.time.set_timer(funciones.start_timer_event_3, 0)
                    funciones.start_timer_active_3 = False
                    funciones.aux_cronometro3 = False

            #-----------------Tiempos cuarto nivel-----------------------------
            # Cronometro del cuarto nivel
            if event.type == funciones.timer_event_4 and funciones.game_state == 'fourth_level':
                funciones.level_time_4 -= 1 
                funciones.timer_text_4 = funciones.timer_font_4.render(str(funciones.level_time_4), True, funciones.color_black)
                if funciones.level_time_4 <= 0:
                    funciones.timer_active_4 = False
                    pygame.time.set_timer(funciones.timer_event_4, 0)
                    funciones.game_state = 'Frth_level'

            # Temporizador del cuarto
            if event.type == funciones.start_timer_event_4 and funciones.game_state == 'Frth_level': 
                funciones.start_time_4 += 1 
                funciones.start_timer_text_4 = funciones.timer_font.render(str(funciones.start_time_4), True, funciones.color_black)
                if funciones.start_time_4 == funciones.time_limit_4:
                    funciones.start_time_4 = 0
                    pygame.time.set_timer(funciones.start_timer_event_4, 0)
                    funciones.start_timer_active_4 = False
                    funciones.game_state = 'reflection_4'
                    funciones.used_time_4 = funciones.time_limit_4
                    funciones.unused_time_4 = 0

                if  funciones.aux_cronometro4: 
                    pygame.time.set_timer(funciones.start_timer_event_4, 0)
                    funciones.start_timer_active_4 = False
                    funciones.aux_cronometro4 = False
            #-----------------Tiempos quinto nivel-----------------------------
            # Cronometro del quinto nivel
            if event.type == funciones.timer_event_5 and funciones.game_state == 'fifth_level':
                funciones.level_time_5 -= 1 
                funciones.timer_text_5 = funciones.timer_font_5.render(str(funciones.level_time_5), True, funciones.color_black)
                if funciones.level_time_5 <= 0:
                    funciones.timer_active_5 = False
                    pygame.time.set_timer(funciones.timer_event_5, 0)
                    funciones.game_state = 'Ffth_level'

            # Temporizador del quinto
            if event.type == funciones.start_timer_event_5 and funciones.game_state == 'Ffth_level': 
                funciones.start_time_5 += 1 
                funciones.start_timer_text_5 = funciones.timer_font.render(str(funciones.start_time_5), True, funciones.color_black)
                if funciones.start_time_5 == funciones.time_limit_5:
                    funciones.start_time_5 = 0
                    pygame.time.set_timer(funciones.start_timer_event_5, 0)
                    funciones.start_timer_active_5 = False
                    funciones.game_state = 'reflection_5'
                    funciones.used_time_5 = funciones.time_limit_5
                    funciones.unused_time_5 = 0

                if  funciones.aux_cronometro5: 
                    pygame.time.set_timer(funciones.start_timer_event_5, 0)
                    funciones.start_timer_active_5 = False
                    funciones.aux_cronometro5 = False
            #-----------------Tiempos sexto nivel-----------------------------
            # Cronometro del sexto nivel
            if event.type == funciones.timer_event_6 and funciones.game_state == 'sixth_level':
                funciones.level_time_6 -= 1 
                funciones.timer_text_6 = funciones.timer_font_6.render(str(funciones.level_time_6), True, funciones.color_black)
                if funciones.level_time_6 <= 0:
                    funciones.timer_active_6 = False
                    pygame.time.set_timer(funciones.timer_event_6, 0)
                    funciones.game_state = 'Sxth_level'

            # Temporizador del sexto
            if event.type == funciones.start_timer_event_6 and funciones.game_state == 'Sxth_level': 
                funciones.start_time_6 += 1 
                funciones.start_timer_text_6 = funciones.timer_font.render(str(funciones.start_time_6), True, funciones.color_black)
                if funciones.start_time_6 == funciones.time_limit_6:
                    funciones.start_time_6 = 0
                    pygame.time.set_timer(funciones.start_timer_event_6, 0)
                    funciones.start_timer_active_6 = False
                    funciones.game_state = 'reflection_6'
                    funciones.used_time_6 = funciones.time_limit_6
                    funciones.unused_time_6 = 0

                if  funciones.aux_cronometro6: 
                    pygame.time.set_timer(funciones.start_timer_event_6, 0)
                    funciones.start_timer_active_6 = False
                    funciones.aux_cronometro6 = False
            #-----------------Tiempos septimo nivel-----------------------------
            # Cronometro del septimo nivel
            if event.type == funciones.timer_event_7 and funciones.game_state == 'seventh_level':
                funciones.level_time_7 -= 1 
                funciones.timer_text_7 = funciones.timer_font_7.render(str(funciones.level_time_7), True, funciones.color_black)
                if funciones.level_time_7 <= 0:
                    funciones.timer_active_7 = False
                    pygame.time.set_timer(funciones.timer_event_7, 0)
                    funciones.game_state = 'Svnth_level'

            # Temporizador del septimo
            if event.type == funciones.start_timer_event_7 and funciones.game_state == 'Svnth_level': 
                funciones.start_time_7 += 1 
                funciones.start_timer_text_7 = funciones.timer_font.render(str(funciones.start_time_7), True, funciones.color_black)
                if funciones.start_time_7 == funciones.time_limit_7:
                    funciones.start_time_7 = 0
                    pygame.time.set_timer(funciones.start_timer_event_7, 0)
                    funciones.start_timer_active_7 = False
                    funciones.game_state = 'reflection_7'
                    funciones.used_time_7 = funciones.time_limit_7
                    funciones.unused_time_7 = 0

                if  funciones.aux_cronometro7: 
                    pygame.time.set_timer(funciones.start_timer_event_7, 0)
                    funciones.start_timer_active_7 = False
                    funciones.aux_cronometro7 = False
            #-----------------Tiempos octavo nivel-----------------------------
            # Cronometro del octavo nivel
            if event.type == funciones.timer_event_8 and funciones.game_state == 'eighth_level':
                funciones.level_time_8 -= 1 
                funciones.timer_text_8 = funciones.timer_font_8.render(str(funciones.level_time_8), True, funciones.color_black)
                if funciones.level_time_8 <= 0:
                    funciones.timer_active_8 = False
                    pygame.time.set_timer(funciones.timer_event_8, 0)
                    funciones.game_state = 'Eighth_level'

            # Temporizador del octavo
            if event.type == funciones.start_timer_event_8 and funciones.game_state == 'Eighth_level': 
                funciones.start_time_8 += 1 
                funciones.start_timer_text_8 = funciones.timer_font.render(str(funciones.start_time_8), True, funciones.color_black)
                if funciones.start_time_8 == funciones.time_limit_8:
                    funciones.start_time_8 = 0
                    pygame.time.set_timer(funciones.start_timer_event_8, 0)
                    funciones.start_timer_active_8 = False
                    funciones.game_state = 'reflection_8'
                    funciones.used_time_8 = funciones.time_limit_8
                    funciones.unused_time_8 = 0

                if  funciones.aux_cronometro8: 
                    pygame.time.set_timer(funciones.start_timer_event_8, 0)
                    funciones.start_timer_active_8 = False
                    funciones.aux_cronometro8 = False
            #-----------------Tiempos noveno nivel-----------------------------
            # Cronometro del noveno nivel
            if event.type == funciones.timer_event_9 and funciones.game_state == 'ninth_level':
                funciones.level_time_9 -= 1 
                funciones.timer_text_9 = funciones.timer_font_9.render(str(funciones.level_time_9), True, funciones.color_black)
                if funciones.level_time_9 <= 0:
                    funciones.timer_active_9 = False
                    pygame.time.set_timer(funciones.timer_event_9, 0)
                    funciones.game_state = 'Nnth_level'

            # Temporizador del noveno
            if event.type == funciones.start_timer_event_9 and funciones.game_state == 'Nnth_level': 
                funciones.start_time_9 += 1 
                funciones.start_timer_text_9 = funciones.timer_font.render(str(funciones.start_time_9), True, funciones.color_black)
                if funciones.start_time_9 == funciones.time_limit_9:
                    funciones.start_time_9 = 0
                    pygame.time.set_timer(funciones.start_timer_event_9, 0)
                    funciones.start_timer_active_9 = False
                    funciones.game_state = 'reflection_9'
                    funciones.used_time_9 = funciones.time_limit_9
                    funciones.unused_time_9 = 0

                if  funciones.aux_cronometro9: 
                    pygame.time.set_timer(funciones.start_timer_event_9, 0)
                    funciones.start_timer_active_9 = False
                    funciones.aux_cronometro9 = False
            #-----------------Tiempos decimo nivel-----------------------------
            # Cronometro del decimo nivel
            if event.type == funciones.timer_event_10 and funciones.game_state == 'tenth_level':
                funciones.level_time_10 -= 1 
                funciones.timer_text_10 = funciones.timer_font_10.render(str(funciones.level_time_10), True, funciones.color_black)
                if funciones.level_time_10 <= 0:
                    funciones.timer_active_10 = False
                    pygame.time.set_timer(funciones.timer_event_10, 0)
                    funciones.game_state = 'Tnth_level'

            # Temporizador del decimo
            if event.type == funciones.start_timer_event_10 and funciones.game_state == 'Tnth_level': 
                funciones.start_time_10 += 1 
                funciones.start_timer_text_10 = funciones.timer_font.render(str(funciones.start_time_10), True, funciones.color_black)
                if funciones.start_time_10 == funciones.time_limit_10:
                    funciones.start_time_10 = 0
                    pygame.time.set_timer(funciones.start_timer_event_10, 0)
                    funciones.start_timer_active_10 = False
                    funciones.game_state = 'reflection_10'
                    funciones.used_time_10 = funciones.time_limit_10
                    funciones.unused_time_10 = 0

                if  funciones.aux_cronometro10: 
                    pygame.time.set_timer(funciones.start_timer_event_10, 0)
                    funciones.start_timer_active_10 = False
                    funciones.aux_cronometro10 = False

            # Quit Game
            if event.type == pygame.QUIT: # Si el evento es .QUIT (Darle click en la X de la ventana generada) se deja de ejecutar el while
                funciones.open_game = False


        pygame.display.update() # Actualiza Display
        funciones.resultados()

    funciones.reiniciar_variables()

    return funciones.LI
