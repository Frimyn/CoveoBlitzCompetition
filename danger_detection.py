import game_message
import actions

class DangerDetection:
    def __init__(self):
        self.position = None
        self.velocity = None
        self.radius = None 
        
        
    def sense_danger(self, game_message: GameMessage):
        return