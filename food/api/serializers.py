from rest_framework import serializers

from food.models import Sauce


class SauceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sauce
        fields = '__all__'
