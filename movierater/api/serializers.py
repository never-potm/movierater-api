from django.contrib.auth.models import User
from rest_framework import serializers

from movierater.api.models import Movie, Rating


# HyperlinkedModelSerializer -> Built-in Serializer for Django
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        # We are passing extra info to this serializer and assigning it set to write_only
        # so that it can be exposed
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


# ModelSerializer -> Custom Serializer for our models
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'avg_rating', 'number_of_ratings')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('stars', 'movie', 'user')
