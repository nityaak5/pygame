class Settings:
    
    #initialise the game settings
    def __init__(self):
        self.screen_width= 1400
        self.screen_height= 800
        self.bg_color= (230,230,230)
        # self.machine_speed= 1.5
        # self.bullet_speed = 2.0
        self.bullet_width= 5
        self.bullet_height =15
        self.bullet_color =(60,60,60)
        self.bullets_allowed= 3
        # self.alien_speed= 1.0
        self.fleet_drop_speed =5
        #1 for right, -1 for left
        # self.fleet_direction =1
        self.ship_limit= 3
        self.speedup_scale= 1.1

        self.initialize_dynamic()
    
    def initialize_dynamic(self):
        self.machine_speed = 1.5
        self.bullet_speed = 2.0
        self.alien_speed = 1.0
        self.alien_points = 10
        self.fleet_direction = 1
    
    def inc_speed(self):
        self.machine_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
