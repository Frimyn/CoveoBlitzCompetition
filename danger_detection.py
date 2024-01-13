# from game_message import GameMessage
# import math
# from shapely.geometry import Point, LineString
# import matplotlib.pyplot as plt
# import numpy as np

# class DangerDetection:
#     def __init__(self):
#         self.danger = [] # information related to imminent danger


#     def sense_danger(self, GameMessage.rockets, ship_current_position, GameMessage.debris):
#         for debris in GameMessage.debris:
#             debris_position = debris.position
#             debris_radius = debris.radius
#             debris_velocity = debris.velocity

#             if (line_circle_intersection(debris_velocity, debris_position, ship_current_position, GameMessage.ship_current_position.station.shield.radius)):
#                 self.danger.append(debris)

#         for rocket in game_message.GameMessage.rockets:
#             rocket_position = rocket.position
#             rocket_radius = rocket.radius
#             rocket_velocity = rocket.velocity

#             if (line_circle_intersection(rocket_velocity, rocket_position, ship_current_position, GameMessage.ship_current_position.station.shield.radius)):
#                 self.danger.append(rocket)


#     def line_circle_intersection(normalised_vector, point_on_line, circle_center, circle_radius):
#         # Create a line using the normalized vector and a point on the line
#         line_direction = np.array(normalized_vector)
#         line_coords = [point_on_line, point_on_line + line_direction]

#         line = LineString(line_coords)
#         circle = Point(circle_center).buffer(circle_radius)
        
#         return line.intersects(circle)
