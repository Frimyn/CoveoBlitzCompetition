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
        crew_types = ['turret', 'shield', 'helm']

        # Send crew members to other stations based on the original logic
        for i, crew_member in enumerate(my_ship.crew):
            crew_type = crew_types[i % len(crew_types)]  # Cycle through the types

            # Fetch the distances from available stations of the crew_type
            distances_from_stations = getattr(crew_member.distanceFromStations, crew_type + 's', [])

            # Exclude radar stations from possible destinations
            valid_distances = [distance for distance in distances_from_stations if not isinstance(distance, RadarStation)]

            # Sort valid distances by distance value
            sorted_distances = sorted(valid_distances, key=lambda distance: distance.distance)

            # Select the station with the shortest distance as the destination
            shortest_distance_station = sorted_distances[0] if sorted_distances else None

            if shortest_distance_station:
                destination = shortest_distance_station.stationPosition
                actions.append(CrewMoveAction(crew_member.id, destination))

        # Check if there is no one operating the helm station
        helm_station_operators = [station.operator for station in my_ship.stations.helms]
        if None in helm_station_operators:
            # Find a crew member that is not already assigned to a station
            unassigned_crew = [crew_member for crew_member in my_ship.crew if crew_member.currentStation is TurretStation]

            if unassigned_crew:
                # Send the first unassigned crew member to the helm station
                destination = my_ship.stations.helms[0].gridPosition
                actions.append(CrewMoveAction(unassigned_crew[0].id, destination))

        # Check if there is no one operating the turrets station
        turrets_station_operators = [station.operator for station in my_ship.stations.turrets]
        if None in turrets_station_operators:
            # Find a crew member that is not already assigned to a station
            unassigned_crew = [crew_member for crew_member in my_ship.crew if crew_member.currentStation is ShieldConstants]

            if unassigned_crew:
                # Send the first unassigned crew member to the helm station
                destination = my_ship.stations.shields[0].gridPosition
                actions.append(CrewMoveAction(unassigned_crew[0].id, destination))

        return actions
