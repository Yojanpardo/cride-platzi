"""Circles serializers"""

# Django REST framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from cride.circles.models import Circle


class CircleSerializer(serializers.Serializer):
    """Circle Serializer,

    Are similar to Django Forms.
    """

    name = serializers.CharField()
    slug_name = serializers.SlugField()
    rides_taken = serializers.IntegerField()
    rides_offered = serializers.IntegerField()
    members_limit = serializers.IntegerField()


class CreateCircleSerializer(serializers.Serializer):
    """Create a circle throwght a serializer
    """
    name = serializers.CharField(max_length=140)
    slug_name = serializers.SlugField(
        max_length=40,
        # ponemos este validador aqui para que se capture el error lo mas arriba posible
        validators=[
            UniqueValidator(queryset=Circle.objects.all())
        ]
    )
    about = serializers.CharField(max_length=255, required=False)

    def create(self, validated_data):
        """create a new circle"""
        return Circle.objects.create(**validated_data)

