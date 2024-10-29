import pygame
from settings import *

class Player():
    def __init__(self, x, y):
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.bullets = []
        self.direct = (0, -1)  

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 5
            self.direct = (-1, 0) 
            if keys[pygame.K_q]:
              self.rect.x -=15 
        if keys[pygame.K_d]:
            self.rect.x += 5
            self.direct = (1, 0)
            if keys[pygame.K_q]:
              self.rect.x +=15
        if keys[pygame.K_w]:
            self.rect.y -= 5
            self.direct = (0, -1) 
            if keys[pygame.K_q]:
              self.rect.y -=15
        if keys[pygame.K_s]:
            self.rect.y += 5
            self.direct = (0, 1) 
            if keys[pygame.K_q]:
              self.rect.y +=15

        if keys[pygame.K_SPACE]:  
            bullet = Bullet(self.rect.centerx, self.rect.centery, self.direct)
            self.bullets.append(bullet)

        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.rect.x < 0 or bullet.rect.x > width or bullet.rect.y < 0 or bullet.rect.y > height:
                self.bullets.remove(bullet) 

    def draw(self, win):
        win.blit(self.image, self.rect)
        for bullet in self.bullets:
            bullet.draw(win)

