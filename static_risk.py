import pygame

class RiskFactor(pygame.sprite.Sprite): # Al incluir la clase sprite, viene con un método draw y update
     def __init__(self, x, y):
          pygame.sprite.Sprite.__init__(self)
          img = pygame.image.load("Assets/Obstacles/sierrassets_furniture_pack/furniture/individual_sprites/handw.png")
          self.image = pygame.transform.scale(img,(60,70))
          self.rect = self.image.get_rect()
          self.rect.x = x
          self.rect.y = y
        