from rest_framework.serializers import HyperlinkedModelSerializer
from core.models import *


# Custom serializers
class FoodTruckModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = FoodTruckModel
        fields = "__all__"
