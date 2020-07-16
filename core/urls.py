from django.urls import path, include
from rest_framework.routers import SimpleRouter

from core.api import viewsets

router = SimpleRouter()
router.register('users', viewsets.UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('authenticate/', viewsets.CustomAuthToken.as_view())
]
