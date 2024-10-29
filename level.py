import pygame
from settings import *
from player import Player
from enemy import Enemy

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.player = Player(500, 500)
        self.enemy = Enemy(100, 100)

    def run(self):
        self.player.update(self.display_surface)
        self.enemy.update(self.display_surface, self.player)
