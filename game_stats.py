class gameStats:
    def __init__(self, bubble_game):
        self.settings= bubble_game.settings
        self.reset_stats()
        
        self.game_active = False   #game won't start unless play button pressed
        self.high_score = 0
    #redifining when game reset
    def reset_stats(self):
        self.ships_remaining= self.settings.ship_limit
        self.score = 0

