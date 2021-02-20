import pygame
from pygame.sprite import Sprite  #to group similar elements

class Bullet(Sprite):

    def __init__(self,bubble_game):
        super().__init__()      #properties of sprite
        self.screen= bubble_game.screen
        self.settings= bubble_game.settings
        self.color= self.settings.bullet_color

        self.rect= pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        
        self.rect.midtop= bubble_game.machine.rect.midtop

        # storing bullet speed
        self.y= float(self.rect.y)


    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y=self.y
        
        # drawing the bullet

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
