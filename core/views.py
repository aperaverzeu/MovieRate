from django.shortcuts import render
from rest_framework import viewsets
from core.models import Movie, Rating, RentalCertificate, Genre
from core.serializers import MovieSerializer, GenreSerializer, RentalCertificateSerializer, RatingSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class RentalCertificateViewSet(viewsets.ModelViewSet):
    queryset = RentalCertificate.objects.all()
    serializer_class = RentalCertificateSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
