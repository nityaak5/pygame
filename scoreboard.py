import pygame.font
from pygame.sprite import Group
from machine import Machine

class Scoreboard:
    def __init__(self, bubble_game):
        self.bubble_game= bubble_game
        self.screen = bubble_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings= bubble_game.settings
        self.stats= bubble_game.stats

        self.text_color= (30,30,30)
        self.font= pygame.font.SysFont(None, 48, bold=True)
        self.prep_score()
        self.prep_highScore()
        self.prep_machine()
    
    def prep_machine(self):
        self.machines = Group()
        for machine_no in range(self.stats.ships_remaining):
            machine= Machine(self.bubble_game)
            machine.rect.x = 10+ machine_no*machine.rect.width
            machine.rect.y= 10
            self.machines.add(machine)
    
    def prep_score(self):
        score_str= str(self.stats.score)
        self.score_img= self.font.render(score_str,True,self.text_color,self.settings.bg_color)

        self.score_rect= self.score_img.get_rect()
        self.score_rect.right= self.screen_rect.right -20
        self.score_rect.top= 20
    
    def show_score(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.machines.draw(self.screen)

    def prep_highScore(self):
        high_score= round(self.stats.high_score,-1)
        high_score_str= "{:,}".format(high_score)
        self.high_score_img= self.font.render(high_score_str,True,self.text_color,self.settings.bg_color)

        self.high_score_rect= self.score_img.get_rect()
        self.high_score_rect.right= self.screen_rect.centerx
        self.score_rect.top= self.score_rect.top

    def check_high(self):
        if self.stats.score> self.stats.high_score:
            self.stats.high_score= self.stats.score
            self.prep_highScore()


