from rest_framework import status as HTTPStatusCode
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def health_check(request):
    return Response({"ping": "pong"}, status=HTTPStatusCode.HTTP_200_OK)
