import pygame
from pygame.sprite import Sprite

class Machine(Sprite):
    
    def __init__(self,bubble_game):
        super().__init__()
        self.screen= bubble_game.screen        
        self.screen_rect= bubble_game.screen.get_rect() #starting location
        self.settings= bubble_game.settings            #to use this instance in update

        self.image= pygame.image.load('//home/nityaa/Documents/PYTHON/game/images/ship.bmp')
        self.rect= self.image.get_rect()

        #to start at bottom mid
        self.rect.midbottom= self.screen_rect.midbottom

        # rect attributes only take integer, so we chanigng
        self.x = float(self.rect.x)

        #for ship movement
        self.moving_right= False 
        self.moving_left= False
        
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x+= self.settings.machine_speed               #writing self.x instead of self.rect.x , float chanegd
        if self.moving_left and self.rect.left >0:
            self.x-= self.settings.machine_speed
        
        self.rect.x = self.x         #finally rect is updated, only integer part will be stored

    # drawing img on screen
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    
    def center_machine(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)