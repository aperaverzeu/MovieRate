from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include

from core.views import MovieViewSet, GenreViewSet, RatingViewSet, RentalCertificateViewSet

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('ratings', RatingViewSet)
router.register('genres', GenreViewSet)
router.register('rentalCertificates', RentalCertificateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]