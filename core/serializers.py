from rest_framework import serializers
from core.models import Movie, Rating, RentalCertificate, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'genre')


class RentalCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalCertificate
        fields = ('movie', 'number', 'country')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'movie', 'user', 'stars')
