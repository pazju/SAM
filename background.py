import pygame


class BG ():
    def __init__(self, bg_data,tile_size_x, tile_size_y):
        
            
        self.tile_list = []
        

        #load images
        #floor_img = pygame.image.load("Assets/Background/woodFloor.png") # https://opengameart.org/content/wood-floor
        floor_img = pygame.image.load("Assets/Background/woodFloor_5.jpg") # https://opengameart.org/node/15650
        tapete_img_1 = pygame.image.load("Assets/Background/cerrar-detalle-textura-ropa-acogedora.jpg")    # Imagen de <a href="https://www.freepik.es/foto-gratis/cerrar-detalle-textura-ropa-acogedora_26406294.htm#page=2&query=tapete&position=47&from_view=search&track=sph">Freepik</a>
        tapete_img_2 = pygame.image.load("Assets/Background/lay-flat-textil.jpg") # Imagen de <a href="https://www.freepik.es/foto-gratis/lay-flat-textil_12063084.htm#query=tapete%20azul&position=2&from_view=search&track=ais">Freepik</a>
        baldosa_img = pygame.image.load("Assets/Background/baldosa.png")# https://opengameart.org/content/tiny-texture-pack-1
        grass_img = pygame.image.load("Assets/Background/grass.png")# https://opengameart.org/content/tiny-texture-pack-1
        white_img = pygame.image.load("Assets/Background/libre_paint_v2/texpaint/PT_WHITE.png")
        sky_img = pygame.image.load("Assets/Background/libre_paint_v2/texpaint/PT_SKY.png")
        black_img = pygame.image.load("Assets/Background/libre_paint_v2/texpaint/PT_BLACK.png")

        row_count = 0
        for row in bg_data:
            col_count = 0
            for tile in row: 
                if tile == 1:
                    img = pygame.transform.scale(floor_img,(tile_size_x, tile_size_y))
                    img_width = col_count * tile_size_x
                    img_height = row_count * tile_size_y
                    img_param = (img_width,img_height)
                    tile = (img, img_param)
                    self.tile_list.append(tile)
                
                if tile == 2:
                    img = pygame.transform.scale(tapete_img_1,(tile_size_x, tile_size_y))
                    img_width = col_count * tile_size_x
                    img_height = row_count * tile_size_y
                    img_param = (img_width,img_height)
                    tile = (img, img_param)
                    self.tile_list.append(tile)

                if tile == 3:
                    img = pygame.transform.scale(tapete_img_2,(tile_size_x, tile_size_y))
                    img_width = col_count * tile_size_x
                    img_height = row_count * tile_size_y
                    img_param = (img_width,img_height)
                    tile = (img, img_param)
                    self.tile_list.append(tile)

                if tile == 4:
                    img = pygame.transform.scale(baldosa_img,(tile_size_x, tile_size_y))
                    img_width = col_count * tile_size_x
                    img_height = row_count * tile_size_y
                    img_param = (img_width,img_height)
                    tile = (img, img_param)
                    self.tile_list.append(tile)

                if tile == 5:
                    img = pygame.transform.scale(grass_img,(tile_size_x, tile_size_y))
                    img_width = col_count * tile_size_x
                    img_height = row_count * tile_size_y
                    img_param = (img_width,img_height)
                    tile = (img, img_param)
                    self.tile_list.append(tile)

                if tile == 6:
                    img = pygame.transform.scale(white_img,(tile_size_x, tile_size_y))
                    img_width = col_count * tile_size_x
                    img_height = row_count * tile_size_y
                    img_param = (img_width,img_height)
                    tile = (img, img_param)
                    self.tile_list.append(tile)

                if tile == 7:
                    img = pygame.transform.scale(sky_img,(tile_size_x, tile_size_y))
                    img_width = col_count * tile_size_x
                    img_height = row_count * tile_size_y
                    img_param = (img_width,img_height)
                    tile = (img, img_param)
                    self.tile_list.append(tile)
                
                if tile == 8:
                    img = pygame.transform.scale(black_img,(tile_size_x, tile_size_y))
                    img_width = col_count * tile_size_x
                    img_height = row_count * tile_size_y
                    img_param = (img_width,img_height)
                    tile = (img, img_param)
                    self.tile_list.append(tile)

                col_count += 1

            row_count += 1
    
    def draw(self, screen):
         for tile in self.tile_list:
              screen.blit(tile[0], tile[1])
              #pygame.draw.rect(screen,(255,255,255), tile[1],2) # Permite ver los rectángulos de los objetos