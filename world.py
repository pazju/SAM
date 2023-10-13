import pygame
import moving_reward
import moving_trap
import moving_reward_2


class World ():
    def __init__(self, data, reward_group, trap_group, tile_size_x, tile_size_y):
        
            
        self.tile_list = []
        
        #load images
        wall_img = pygame.image.load("Assets/Obstacles/brickGrey.png")
        floor_img = pygame.image.load("Assets/Background/woodFloor.png") # https://opengameart.org/content/wood-floor
        table_img = pygame.image.load("Assets/Obstacles/table.png") # https://opengameart.org/content/brackeys-game-jam-20221-pack
        plant_img = pygame.image.load("Assets/Obstacles/sierrassets_furniture_pack/furniture/individual_sprites/plant.png")
        ducha_img = pygame.image.load("Assets/Obstacles/sierrassets_furniture_pack/furniture/individual_sprites/ducha.png")
        ino_img = pygame.image.load("Assets/Obstacles/sierrassets_furniture_pack/furniture/individual_sprites/inodoro.png")
        handw_img = pygame.image.load("Assets/Obstacles/sierrassets_furniture_pack/furniture/individual_sprites/handw.png")
        sillaf1_img = pygame.image.load("Assets/Obstacles/sierrassets_furniture_pack/furniture/individual_sprites/silla4.png")
        sillaf2_img = pygame.image.load("Assets/Obstacles/sierrassets_furniture_pack/furniture/individual_sprites/silla5.png")
        cama1_img = pygame.image.load("Assets/Obstacles/sierrassets_furniture_pack/furniture/individual_sprites/cama1.png")
        sofa1_img = pygame.image.load("Assets/Obstacles/sierrassets_furniture_pack/furniture/individual_sprites/sofa1.png")
        sofa2_img = pygame.image.load("Assets/Obstacles/sierrassets_furniture_pack/furniture/individual_sprites/sofa2.png")
        sofa2r_img = pygame.transform.rotate(sofa2_img, 90)
        piano_img = pygame.image.load("Assets/Obstacles/sierrassets_furniture_pack/furniture/individual_sprites/piano.png")
        mueble1_img = pygame.image.load("Assets/Obstacles/sierrassets_furniture_pack/furniture/individual_sprites/mueble1.png")
        mueble2_img = pygame.image.load("Assets/Obstacles/sierrassets_furniture_pack/furniture/individual_sprites/mueble2.png")
        mueble3_img = pygame.image.load("Assets/Obstacles/sierrassets_furniture_pack/furniture/individual_sprites/mueble3.png")
        mesita1_img = pygame.image.load("Assets/Obstacles/sierrassets_furniture_pack/furniture/individual_sprites/mesita1.png")
        roof_img_1 = pygame.image.load("Assets/Background/roof_1.png")# https://opengameart.org/content/tiny-texture-pack-1
        roof_img_2 = pygame.image.load("Assets/Background/roof_2.png")# https://opengameart.org/content/tiny-texture-pack-1
        brick_img = pygame.image.load("Assets/Background/brick.png")# https://opengameart.org/content/tiny-texture-pack-1
        glass_img = pygame.image.load("Assets/Background/glass.png")# https://opengameart.org/content/glass
 
        # Reward Images / Insumos Correctos
        reward_1 = pygame.image.load("Assets/Rewards/cepillo_azul.png") # <a href="https://www.flaticon.com/free-icons/toothbrush" title="toothbrush icons">Toothbrush icons created by Freepik - Flaticon</a>
        reward_2 = pygame.image.load("Assets/Rewards/chancla_b.png") # <a href="https://www.freepik.es/foto-gratis/zapatos-playa-chancleta-amarillean-aislado-fondo-blanco_2624953.htm#query=flip%20flops&position=29&from_view=search&track=ais">Imagen de kstudio</a> en Freepik
        reward_3_1 = pygame.image.load("Assets/Rewards/towel.png") # Imagen de <a href="https://www.freepik.es/foto-gratis/surtido-panuelos-blancos_18037063.htm#page=2&query=towel&position=30&from_view=search&track=sph">Freepik</a>
        reward_3_2 = pygame.image.load("Assets/Rewards/soap.png") # Imagen de <a href="https://www.freepik.es/foto-gratis/surtido-panuelos-blancos_18037063.htm#page=2&query=towel&position=30&from_view=search&track=sph">Freepik</a>
        reward_4 = pygame.image.load("Assets/Rewards/tapete_a.png") # CANVA

        
        # Trap Images / Insumos Distractores
        trap_1 = pygame.image.load("Assets/Rewards/cepillo_rojo.png") # <a href="https://www.flaticon.com/free-icons/toothbrush" title="toothbrush icons">Toothbrush icons created by Freepik - Flaticon</a>
        trap_2 = pygame.image.load("Assets/Rewards/chancla_a.png") # <a href="https://www.freepik.es/foto-gratis/zapatos-playa-chancleta-amarillean-aislado-fondo-blanco_2624953.htm#query=flip%20flops&position=29&from_view=search&track=ais">Imagen de kstudio</a> en Freepik
        trap_3 = pygame.image.load("Assets/Rewards/caution.png") # <a href="https://www.freepik.es/foto-gratis/big-no-espera-firmar_1037469.htm#page=6&query=prohibido&position=23&from_view=search&track=sph">Imagen de kues1</a> en Freepik
        trap_4 = pygame.image.load("Assets/Rewards/tapete_b.png") # CANVA

        # Canasto Nivel 4
        canasto_img = pygame.image.load("Assets/Rewards/canasto.png") # CANVA
        

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row: 
                if tile == 1:
                    img = pygame.transform.scale(brick_img,(tile_size_x, tile_size_y))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size_x
                    img_rect.y = row_count * tile_size_y
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 2:
                    img = pygame.transform.scale(roof_img_1,(tile_size_x, tile_size_y))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size_x
                    img_rect.y = row_count * tile_size_y
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                
                if tile == 3:
                    img = pygame.transform.scale(table_img,(tile_size_x, tile_size_y))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size_x
                    img_rect.y = row_count * tile_size_y
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                
                if tile == 4:
                    img = pygame.transform.scale(plant_img,(tile_size_x*0.7, tile_size_y*0.7))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size_x
                    img_rect.y = row_count * tile_size_y
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 5:
                    img = pygame.transform.scale(ducha_img,(tile_size_x*1.5, tile_size_y*1.5))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size_x
                    img_rect.y = row_count * tile_size_y
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 6:
                    img = pygame.transform.scale(ino_img,(tile_size_x, tile_size_y))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size_x
                    img_rect.y = row_count * tile_size_y
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 7:
                    img = pygame.transform.scale(handw_img,(tile_size_x, tile_size_y))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size_x
                    img_rect.y = row_count * tile_size_y
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 8:
                    img = pygame.transform.scale(sillaf1_img,(tile_size_x*0.8, tile_size_y*0.8))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size_x
                    img_rect.y = row_count * tile_size_y
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 9:
                    img = pygame.transform.scale(sillaf2_img,(tile_size_x*0.8, tile_size_y*0.8))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size_x
                    img_rect.y = row_count * tile_size_y
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 10:
                    img = pygame.transform.scale(cama1_img,(tile_size_x*1.2, tile_size_y*2))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size_x
                    img_rect.y = row_count * tile_size_y
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 11:
                    img = pygame.transform.scale(sofa1_img,(tile_size_x, tile_size_y))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size_x
                    img_rect.y = row_count * tile_size_y
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 12:
                    img = pygame.transform.scale(sofa2r_img,(tile_size_x*1.2, tile_size_y*2))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size_x
                    img_rect.y = row_count * tile_size_y
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 13:
                    img = pygame.transform.scale(piano_img,(tile_size_x*2, tile_size_y*2))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size_x
                    img_rect.y = row_count * tile_size_y
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 14:
                    img = pygame.transform.scale(mueble1_img,(tile_size_x*2, tile_size_y))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size_x
                    img_rect.y = row_count * tile_size_y
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 15:
                    img = pygame.transform.scale(mueble2_img,(tile_size_x, tile_size_y))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size_x
                    img_rect.y = row_count * tile_size_y
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 16:
                    img = pygame.transform.scale(mueble3_img,(tile_size_x*1.5, tile_size_y*1.5))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size_x
                    img_rect.y = row_count * tile_size_y
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 17:
                    img = pygame.transform.scale(mesita1_img,(tile_size_x*0.7, tile_size_y*0.7))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size_x
                    img_rect.y = row_count * tile_size_y
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 18:  # Insumo Correcto (reward) / Cepillo Azul Nivel 1
                    reward = moving_reward.Reward(col_count*tile_size_x, row_count*tile_size_y, reward_1)
                    reward_group.add(reward)

                if tile == 19:  # Insumo Distractor / Cepillo Rojo Nivel 1
                    trap = moving_trap.Trap(col_count*tile_size_x, row_count*tile_size_y, trap_1, 80)
                    trap_group.add(trap)
                
                if tile == 20:  # Vidrio
                    img = pygame.transform.scale(glass_img,(tile_size_x, tile_size_y))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size_x
                    img_rect.y = row_count * tile_size_y
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 21:  # Muro 
                    img = pygame.transform.scale(wall_img,(tile_size_x, tile_size_y))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size_x
                    img_rect.y = row_count * tile_size_y
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 22:  # Insumo Correcto (reward) / Chanclas Blancas Nivel 2
                    reward = moving_reward.Reward(col_count*tile_size_x, row_count*tile_size_y, reward_2)
                    reward_group.add(reward)

                if tile == 23:  # Insumo Distractor / Chanclas Amarillas Nivel 2
                    trap = moving_trap.Trap(col_count*tile_size_x, row_count*tile_size_y, trap_2, 80)
                    trap_group.add(trap)

                if tile == 24:  # Insumo Correcto (reward) / Toalla Nivel 3
                    reward = moving_reward.Reward(col_count*tile_size_x, row_count*tile_size_y, reward_3_1)
                    reward_group.add(reward)

                if tile == 25:  # Insumo Correcto (reward) / Jabón Nivel 3
                    reward = moving_reward.Reward(col_count*tile_size_x, row_count*tile_size_y, reward_3_2)
                    reward_group.add(reward)

                if tile == 26:  # Insumo Distractor  / Señal de Prohibido Nivel 3
                    trap = moving_trap.Trap(col_count*tile_size_x, row_count*tile_size_y, trap_3, 50, 50)
                    trap_group.add(trap)
                
                if tile == 27: # Canasto Nivel 4
                    img = pygame.transform.scale(canasto_img,(tile_size_x*2, tile_size_y*2))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size_x
                    img_rect.y = row_count * tile_size_y
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 28:  # Insumo Correcto (reward) / Tapete_a Nivel 4
                    reward = moving_reward_2.Reward(col_count*tile_size_x+(tile_size_x/3), row_count*tile_size_y, reward_4, 85,120)
                    reward_group.add(reward)

                if tile == 29:  # Insumo Distractor  / Tapete_b Nivel 4
                    trap = moving_trap.Trap(col_count*tile_size_x, row_count*tile_size_y, trap_4, 120, 220)
                    trap_group.add(trap)

                if tile == 30:  # Insumo Distractor  / Señal de Prohibido Nivel 4
                    trap = moving_trap.Trap(col_count*tile_size_x, row_count*tile_size_y+(tile_size_y/2), trap_3, 60, 60)
                    trap_group.add(trap)
                

                col_count += 1

            row_count += 1
    
    def draw(self, screen):
         for tile in self.tile_list:
              screen.blit(tile[0], tile[1])
              #pygame.draw.rect(screen,(255,255,255), tile[1],2) # Permite ver los rectángulos de los objetos