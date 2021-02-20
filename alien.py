import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,bubble_game):
        super().__init__()
        self.screen= bubble_game.screen
        self.settings= bubble_game.settings

        self.image= pygame.image.load('/home/nityaa/Documents/PYTHON/game/images/alien.bmp')
        self.rect= self.image.get_rect()

        self.rect.x= self.rect.width
        self.rect.y= self.rect.height

        self.x= float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x