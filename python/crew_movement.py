from game_message import *
from actions import CrewMoveAction

class CrewMovement:
    def __init__(self) -> None:
        pass
        
        
    def send_crew_to_battlestations(self, game_message: GameMessage) -> List[CrewMoveAction]:
        actions = []
        team_id = game_message.currentTeamId
        my_ship = game_message.ships.get(team_id)

        # Assuming there are 4 crew members and 4 station types
        crew_types = ['turret', 'shield', 'radar', 'helm']

        for i, crew_member in enumerate(my_ship.crew):
            crew_type = crew_types[i % len(crew_types)]  # Cycle through the types

            # Fetch the distances from available stations of the crew_type
            distances_from_stations = getattr(crew_member.distanceFromStations, crew_type + 's', [])

            # Sort distances by distance value
            sorted_distances = sorted(distances_from_stations, key=lambda distance: distance.distance)

            # Select the station with the shortest distance as the destination
            shortest_distance_station = sorted_distances[0] if sorted_distances else None

            if shortest_distance_station:
                destination = shortest_distance_station.stationPosition
                actions.append(CrewMoveAction(crew_member.id, destination))

        return actions