from math import sin, cos, sqrt, atan2, radians
from typing import List

from core.models import FoodTruckModel


def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate the distance between two coordinates using the haversine formula.
    """
    # Approximate radius of Earth in km
    R = 6373.0

    # Convert latitude and longitude from degrees to radians
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # Difference in coordinates
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c

    return distance


def search_nearby_food_trucks(lat: float, lng: float, radius: float) -> List[dict]:
    """
    Search nearby food trucks by latitude and longitude within a given radius (default 5 km).
    Returns a list of dictionaries containing all fields of the food truck along with the distance.
    Results are sorted by distance, nearest first.
    """
    food_trucks_with_distance = []

    # Iterate through all food trucks in the database
    for food_truck in FoodTruckModel.objects.all():
        # Calculate the distance from the input coordinates
        distance = calculate_distance(
            lat,
            lng,
            food_truck.latitude,
            food_truck.longitude
        )

        # Check if the food truck is within the specified radius
        if distance <= radius:
            # Convert the food truck object to a dictionary and add the distance field
            truck_data = food_truck.__dict__
            # Delete _state key
            del truck_data["_state"]
            truck_data["distance"] = round(distance, 2)
            food_trucks_with_distance.append(truck_data)

    # Sort the list by distance
    food_trucks_with_distance.sort(key=lambda x: x["distance"])

    return food_trucks_with_distance
