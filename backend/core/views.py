from rest_framework import status as HTTPStatusCode
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.constants import DEFAULT_SEARCH_RADIUS_IN_KM
from core.service.food_truck_service import search_nearby_food_trucks


@api_view(["GET"])
def search_food_trucks(request):
    """
    Search food trucks by name and/or location.
    """
    lat = request.GET.get("lat")
    lng = request.GET.get("lng")
    radius = request.GET.get("radius", DEFAULT_SEARCH_RADIUS_IN_KM)

    # Null check
    if not lat or not lng:
        return Response(
            {"error": "latitude and longitude are required"},
            status=HTTPStatusCode.HTTP_400_BAD_REQUEST,
        )

    # Not a number check
    if str(lat).isalpha() or str(lng).isalpha():
        return Response(
            {"error": "latitude and longitude must be numbers"},
            status=HTTPStatusCode.HTTP_400_BAD_REQUEST,
        )

    # Check radius
    if radius and (str(radius).isalpha() or float(radius) <= 0):
        return Response(
            {"error": "radius must be a positive number"},
            status=HTTPStatusCode.HTTP_400_BAD_REQUEST,
        )

    # Typecast to float
    lat, lng, radius = float(lat), float(lng), float(radius)

    # Perform search on DB
    nearby_food_trucks = search_nearby_food_trucks(lat, lng, radius)

    # Return list of food trucks with their distances
    return Response(
        {
            "data": nearby_food_trucks,
            "error": None
        },
        status=HTTPStatusCode.HTTP_200_OK,
    )
