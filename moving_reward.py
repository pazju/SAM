import pygame

class Reward(pygame.sprite.Sprite): # Al incluir la clase sprite, viene con un método draw y update
     def __init__(self, x, y, reward, size_x = 80, size_y = 80):
          pygame.sprite.Sprite.__init__(self)
          self.img = reward
          self.image = pygame.transform.scale(self.img,(size_x,size_y))
          self.rect = self.image.get_rect()
          self.rect.x = x
          self.rect.y = y
          self.move_direction = 1
          self.move_counter = 0
    
     def update(self): # Movimiento de los factores de riesgo
          self.rect.x += self.move_direction
          self.move_counter += 1
          if abs(self.move_counter) > 10:
               self.move_direction *= -1 # Invierte la dirección
               self.move_counter *= -1  # Conteo regresivo -11 a 11
          

    