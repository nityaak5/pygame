# sys is used to exit the game when player quites, pygame for other functionalities
import sys
from time import sleep
import pygame
from settings import Settings
from machine import Machine
from bullet import Bullet
from alien import Alien
from game_stats import gameStats
from button import Button
from scoreboard import Scoreboard

"""Overall class to manage the behavior of the game"""

class bubbleBurst:
    
    def  __init__(self):
        pygame.init()      #background settings
        self.settings = Settings()   #instance of Settings assigned to self.settings
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # self.screen= pygame.display.set_mode((0,0), pygame.FULLSCREEN) #screen size
        # self.settings.screen_width= self.screen.get_rect().width
        # self.settings.screen_height= self.screen.get_rect().height
        
        
        pygame.display.set_caption("Bubble Burst")     
        self.stats= gameStats(self)
        self.sb= Scoreboard(self)
        self.machine= Machine(self)
        self.bullets= pygame.sprite.Group()
        self.aliens= pygame.sprite.Group()
        self.create_fleet()

        self.play_button= Button(self,'Play')
        

    # now, we shall create the event
    def run_game(self):

        while True:
            self.check_events()
            
            if self.stats.game_active:
                self.machine.update()
                self.update_bullets()
                self.update_aliens()

            
            self.update_screen()            #we don't need instance if calling method of same class
                
            
            

    def check_events(self):

        #get fun returns list of events form last call
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos= pygame.mouse.get_pos()
                self.check_playButton(mouse_pos)
                    
            
    def check_keydown(self, event):
        if event.key == pygame.K_RIGHT:
            self.machine.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.machine.moving_left= True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
            
    def check_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.machine.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.machine.moving_left = False

    def check_playButton(self,mouse_pos):
        button_clicked=self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic()
            self.stats.reset_stats()
            self.stats.game_active= True
            self.sb.prep_score()
            self.sb.prep_machine()
            self.aliens.empty()
            self.bullets.empty()
            self.create_fleet()
            self.machine.center_machine()
            

    def fire_bullet(self):
        if len(self.bullets)< self.settings.bullets_allowed:
            new_bullet= Bullet(self)
            self.bullets.add(new_bullet)

            
    
    def update_bullets(self):
        self.bullets.update()
        # removing bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)
        
        self.check_collision()
        
        
    
    def check_collision(self):
        
        collisions= pygame.sprite.groupcollide(self.bullets, self.aliens,False,True) 
        #set true if bullet dis
        if collisions:
            self.stats.score += self.settings.alien_points
            self.sb.prep_score()
            self.sb.check_high()

        if not self.aliens:
            self.bullets.empty()
            self.create_fleet()
            self.settings.inc_speed()


    def update_aliens(self):
        self.check_fleet_edges()
        self.aliens.update()
        
        # alien ship collision
        if pygame.sprite.spritecollideany(self.machine, self.aliens):
            self.ship_hit()

        self.check_alienBottom()

    def ship_hit(self):
        if self.stats.ships_remaining >0:

            # if ship is hit, decrement ships left
            self.stats.ships_remaining -=1
            self.sb.prep_machine()
            # remove left aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # then create a new fleet
            self.create_fleet
            self.machine.center_machine()
            sleep(0.5)
        
        else:
            self.stats.game_active= False

        

    def check_alienBottom(self):
        screen_rect = self.screen.get_rect()
        
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.ship_hit()  #treat as ship hit only
                break

    def create_fleet(self):
        alien= Alien(self)
        alien_width, alien_height= alien.rect.size
        
        # available space in columns
        available_horz= self.settings.screen_width - (2* alien_width)
        num_aliens_hor = available_horz//(2*alien_width)

        # available space in rows
        available_ver = self.settings.screen_height - (3* alien_width) - self.machine.rect.height
        num_aliens_ver = available_ver//(2*alien_height)


        for row_number in range(num_aliens_ver):
            # creating a row
            for alien_number in range(num_aliens_hor):
                self.create_alien(alien_number, row_number)

        
            

    def create_alien(self, alien_number, row_number):
        alien= Alien(self)
        alien_width, alien_height= alien.rect.size
        alien.x =alien_width + (2 * alien_width *alien_number)
        alien.rect.x = alien.x
        alien.rect.y = alien_height + (2* alien_height *row_number)
        self.aliens.add(alien)
        
    def check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break
    
    def change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def update_screen(self):
        self.screen.fill(self.settings.bg_color)          #background colour
        self.machine.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()
        #recently drawn screen visible in each pass of while loop
        # this creates an illusion of smooth movement
        pygame.display.flip() 


# create an instance of this class which runs only 
#when it's called directly
if __name__ =='__main__':
    bb= bubbleBurst()
    bb.run_game()
    
            



