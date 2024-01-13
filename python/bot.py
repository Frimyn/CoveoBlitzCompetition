from game_message import *
from crew_movement import *
# from danger_detection import *
from actions import *
import random
import time

class Bot:
    def __init__(self):
        print("Initializing your super mega duper bot")
        self.crew_movement = CrewMovement()
        self.rotation_duration = 4.5  # Durée de rotation dans chaque sens en secondes
        self.last_rotation_time = time.time()
        self.rotation_direction = 1  # 1 pour sens horaire, -1 pour sens anti-horaire
        self.first_rotation = 2  # Indique si c'est la première rotation

    def get_next_move(self, game_message: GameMessage):
        actions = []

        team_id = game_message.currentTeamId
        my_ship = game_message.ships.get(team_id)
        other_ships_ids = [shipId for shipId in game_message.shipsPositions.keys() if shipId != team_id]

        operatedTurretStations = [station for station in my_ship.stations.turrets if station.operator is not None]
        for turret_station in operatedTurretStations:
            possible_actions = [
                # Charge the turret.
                TurretChargeAction(turret_station.id),
                # Aim the turret itself.
                TurretLookAtAction(turret_station.id, 
                                   Vector(random.uniform(0, game_message.constants.world.width), random.uniform(0, game_message.constants.world.height))
                ),
                # Shoot!
                TurretShootAction(turret_station.id)
            ]

            actions.append(random.choice(possible_actions))

        operatedHelmStation = [station for station in my_ship.stations.helms if station.operator is not None]
        
        if operatedHelmStation:
            current_time = time.time()
            elapsed_time_since_rotation = current_time - self.last_rotation_time

            # Vérifiez si c'est la première rotation
            if self.first_rotation > 0:
                # Inversez la direction de rotation à la moitié du temps déterminé
                if elapsed_time_since_rotation >= 2:
                    self.rotation_direction *= -1
                    self.first_rotation -= 1  # La première rotation est terminée
                    self.last_rotation_time = current_time

            # Vérifiez si le temps écoulé depuis la dernière rotation a dépassé la durée de rotation
            if elapsed_time_since_rotation >= self.rotation_duration:
                # Inversez la direction de rotation et réinitialisez le temps de la dernière rotation
                self.rotation_direction *= -1
                self.last_rotation_time = current_time

            # Effectuez la rotation en fonction de la direction actuelle
            rotation_angle = 45.0 * self.rotation_direction
            actions.append(ShipRotateAction(rotation_angle))

        operatedRadarStation = [station for station in my_ship.stations.radars if station.operator is not None]
        for radar_station in operatedRadarStation:
            actions.append(RadarScanAction(radar_station.id, random.choice(other_ships_ids)))

        # Get crew actions from CrewMovement
        crew_actions = self.crew_movement.send_crew_to_battlestations(game_message)
        actions.extend(crew_actions)

        return actions
