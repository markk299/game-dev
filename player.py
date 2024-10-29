import pygame
from settings import *

class Player():
    def __init__(self, x, y):
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(x, y))
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
            if keys[pygame.K_q]:
              self.rect.x -=15 
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
            if keys[pygame.K_q]:
              self.rect.x +=15
        if keys[pygame.K_UP]:
            self.rect.y -= 5
            if keys[pygame.K_q]:
              self.rect.y -=15
        if keys[pygame.K_DOWN]:
            self.rect.y += 5
            if keys[pygame.K_q]:
              self.rect.y +=15

    def draw(self, screen):
      screen.blit(self.image, self.rect)
    
    def update(self, screen):
       self.move()
       self.draw(screen)
