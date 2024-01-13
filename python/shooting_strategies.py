from game_message import *
from actions import CrewMoveAction
import math

class ShootingStrategies:
    def __init__(self) -> None:
        pass

    def angle_to_enemy_ship(self, my_position: Vector, enemy_position: Vector) -> float:
        return