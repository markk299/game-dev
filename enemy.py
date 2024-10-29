import pygame
import math
from settings import *

class Enemy():
    def __init__(self, x, y):
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))

    def move(self, player):
        dx, dy = player.rect.x - self.rect.x, player.rect.y - self.rect.y
        dist = math.hypot(dx, dy)
        if dist != 0:
         dx, dy = dx / dist, dy / dist
        self.rect.x += dx * 2
        self.rect.y += dy * 2

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def update(self, screen, player):
       self.move(player)
       self.draw(screen)