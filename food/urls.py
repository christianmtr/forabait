from django.urls import path, include
from rest_framework.routers import SimpleRouter

from food.api import viewsets

router = SimpleRouter()
router.register('sauces', viewsets.SauceViewSets, basename='sauces')

urlpatterns = [
    path('', include(router.urls)),
]
