import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, world, reward_group, trap_group, x, y):
        self.success = pygame.mixer.Sound("Assets/Sounds/success.wav") #https://freesound.org/people/MLaudio/sounds/615099/
        self.wrong = pygame.mixer.Sound("Assets/Sounds/wrong.mp3") #https://freesound.org/people/AbdrTar/sounds/558121/
        self.good = 0
        self.error = 0
        self.points = 0
        self.screen = screen
        self.world = world
        self.reward_group = reward_group
        self.trap_group = trap_group
        self.images_x1 = [] # Listado de imagenes eje +X
        self.images_x2 = [] # Listado de imagenes eje -X
        self.images_y1 = [] # Listado de imagenes eje +Y
        self.images_y2 = [] # Listado de imagenes eje -Y
        self.index = 0
        self.counter = 0 
        for num in range(0,4):
            img_x1 = pygame.image.load(f"Assets/Character/SPRITES/g{num}.png") # toma lo que se encuentra en {}
            img_x1 = pygame.transform.scale(img_x1,(60,70))
            img_x2 = pygame.transform.flip (img_x1, True, False) # Animación Izquierda
            img_y1 = pygame.image.load(f"Assets/Character/SPRITES/gu{num}.png") # toma lo que se encuentra en {}
            img_y1 = pygame.transform.scale(img_y1,(60,70))
            img_y2 = pygame.image.load(f"Assets/Character/SPRITES/gd{num}.png") # toma lo que se encuentra en {}
            img_y2 = pygame.transform.scale(img_y2,(60,70))
            self.images_x1.append(img_x1) # Añade las imagenes al listado
            self.images_x2.append(img_x2)
            self.images_y1.append(img_y1)
            self.images_y2.append(img_y2)

        self.image = self.images_x1[self.index] # Frame Inicial
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.direction = 0 # Direcciones 0 (inicial), 1 (+X), 2 (-X), 3 (+Y), 4 (-Y)

    def update(self):
        dx = 0
        dy = 0
        walk_cooldown = 2 # Cooldown Frames
        # Obtener evento de teclado
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            dy -= 5
            self.counter += 1 
            self.direction = 3
        if key[pygame.K_DOWN]:
            dy += 5
            self.counter += 1 
            self.direction = 4
        if key[pygame.K_LEFT]:
            dx -= 5
            self.counter += 1 # Incrementa el contador para animación
            self.direction = 2
        if key[pygame.K_RIGHT]:
            dx += 5
            self.counter += 1 
            self.direction = 1
        if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False and key[pygame.K_UP] == False and key[pygame.K_DOWN] == False:
             self.counter = 0
             self.index = 0 # Posición Inicial
             self.image = self.images_x1[self.index]
        

        # Animación
        
        if self.counter > walk_cooldown: # Realentiza la animación
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_x1): # Todos los listados tienen la misma longitud = 4 
                self.index = 1 # Posición Inicial Dirección "X" "Y"

            if self.direction == 1: # Animación +X Derecha
                self.image = self.images_x1[self.index]
            if self.direction == 2: # Animación -X Izquierda
                self.image = self.images_x2[self.index]
            if self.direction == 3: # Animación +Y Arriba
                self.image = self.images_y1[self.index]
            if self.direction == 4: # Animación -Y Abajo
                self.image = self.images_y2[self.index]
            


        # Colisiones
        #   Se basan en la creación de los rectángulos que se generan al cargar imágenes image.get_rect()
        for tile in self.world.tile_list: ###
             # Colisiones en Y
             if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height): # Colisiones entre rectángulos antes de que ocurran, teniendo en cuenta la velocidad-desplazamiento del personaje (dx,dy)
                  dy = 0
                  
             if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height): # Colisiones entre rectángulos antes de que ocurran, teniendo en cuenta la velocidad-desplazamiento del personaje (dx,dy)
                  dx = 0
                    
        # Colisiones con objetos insumos correctos (reward)
        if pygame.sprite.spritecollide(self, self.reward_group, True):
            self.success.play()
            self.good = 1
            self.points += 1
            #print(self.points)
        #else: self.good = 0

        # Colisiones con objetos insumos incorrectos (trap)
        if pygame.sprite.spritecollide(self, self.trap_group, True):
            self.wrong.play()
            self.error = 1
            #self.points -= 1 # Estaba descontando puntos por error, ya NO lo hago
            #print(self.points)
        else: self.error = 0
        


        # Colisiones con factores de riesgo

        
        # Actualización coordeadas personaje
        self.rect.x += dx
        self.rect.y += dy
        
        # Dibujar al personaje en pantalla
        self.screen.blit(self.image, self.rect)