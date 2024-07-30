from rest_framework.urls import path
from rest_framework.routers import SimpleRouter

from .viewsets import UserViewSet

router = SimpleRouter(trailing_slash=False)

urlpatterns = [
    path("users", UserViewSet.as_view({"post": "create"})),
    path("users/<int:pk>", UserViewSet.as_view({"get": "retrieve"})),
]

