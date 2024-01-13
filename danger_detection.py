import game_message
import math

class DangerDetection:
    def __init__(self):
        self.danger = [] # information related to imminent danger


    def sense_danger(self, ship_current_position, game_message.GameMessage.debris, game_message.GameMessage.rockets):
        for debris in game_message.GameMessage.debris:
            debris_position = debris.position
            debris_radius = debris.radius

            vector_to_debris = (debris_position[0] - ship_current_position[0], debris_position[1] - ship_current_position[1])
            distance_to_debris = math.sqrt(vector_to_debris[0]**2 + vector_to_debris[1]**2)

            if distance_to_debris > 0:
                relative_speed = (debris.velocity[0] * vector_to_debris[0] + debris.velocity[1] * vector_to_debris[1]) / distance_to_debris
                if relative_speed > 0:
                    self.danger.append(debris)

        for rocket in game_message.GameMessage.rockets:
            rocket_position = rocket.position
            rocket_radius = rocket.radius

            vector_to_rocket = (rocket_position[0] - ship_current_position[0], rocket_position[1] - ship_current_position[1])
            distance_to_rocket = math.sqrt(vector_to_rocket[0]**2 + vector_to_rocket[1]**2)

            if distance_to_rocket > 0:
                relative_speed = (rocket.velocity[0] * vector_to_rocket[0] + rocket.velocity[1] * vector_to_rocket[1]) / distance_to_rocket
                if relative_speed > 0:
                    self.danger.append(rocket)