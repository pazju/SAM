import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, position, scale):
        
        #self.sheet = pygame.image.load("Assets/Character/Females/F_06.png")
        self.sheet = pygame.image.load("Assets/Character/Males/M_03.png")
        self.sheet = pygame.transform.scale(self.sheet, (64*scale, 51*scale)) # Tamaño de la imagen
        self.sheet.set_clip(pygame.Rect(0, 0, 16*scale, 17*scale)) # Posición Inicial Personaje
        self.image = self.sheet.subsurface(self.sheet.get_clip()) # player.image
        self.rect = self.image.get_rect() # player.rect # Rectángulo del jugador (no visible)
        self.rect.topleft = position
        self.frame = 0
        self.left_states    = { 0: (48*scale, 0*scale, 16*scale, 17*scale), 1: (48*scale, 17*scale, 16*scale, 17*scale), 2: (48*scale, 34*scale, 16*scale, 17*scale)} # Posiciones de la imagen en pixeles de los diferentes estados 
        self.right_states   = { 0: (16*scale, 0*scale, 16*scale, 17*scale), 1: (16*scale, 17*scale, 16*scale, 17*scale), 2: (16*scale, 34*scale, 16*scale, 17*scale)}
        self.up_states      = { 0: (32*scale, 0*scale, 16*scale, 17*scale), 1: (32*scale, 17*scale, 16*scale, 17*scale), 2: (32*scale, 34*scale, 16*scale, 17*scale)}
        self.down_states    = { 0: ( 0*scale, 0*scale, 16*scale, 17*scale), 1: ( 0*scale, 17*scale, 16*scale, 17*scale), 2: ( 0*scale, 34*scale, 16*scale, 17*scale)}

        self.width = self.sheet.get_width()
        self.height = self.sheet.get_height()
        self.dx = 15
        self.dy = 15

    def get_frame(self, frame_set): # Obtiene el frame exacto de la animación / Realiza un loop de la animación
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect): # Hace los recortes de los rectángulos que se van definiendo
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction): # Mueve al personaje hacía la dirección indicada a una distancia de dx y dy pixeles (15 pixeles por pulsación)
       
        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -= self.dx
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += self.dx
        if direction == 'up':
            self.clip(self.up_states)
            self.rect.y -= self.dy
        if direction == 'down':
            self.clip(self.down_states)
            self.rect.y += self.dy

        if direction == 'stand_left': # Estados stand que dejan al personaje parado en la posición hacía la cual se estaba dirigiendo
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        if direction == 'stand_down':
            self.clip(self.down_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip()) # Se posiciona la imagen donde se encuentra el personaje

    def handle_event(self, event): # Eventos del teclado, presión de las flechas
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            if event.key == pygame.K_UP:
                self.update('up')
            if event.key == pygame.K_DOWN:
                self.update('down')

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                self.update('stand_left')
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
            if event.key == pygame.K_UP:
                self.update('stand_up')
            if event.key == pygame.K_DOWN:
                self.update('stand_down')

  