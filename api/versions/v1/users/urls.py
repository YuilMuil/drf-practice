from rest_framework.urls import path
from rest_framework.routers import SimpleRouter

from .viewsets import UserViewSet

router = SimpleRouter(trailing_slash=False)

urlpatterns = [
    # GET http://127.0.0.1:8000/users -> 유저 목록 API -> UserViewSet 안에 있는 list 메소드로..
    path("users", UserViewSet.as_view({"post": "create", "get": "list"})),
    path(
        "users/<int:pk>",
        UserViewSet.as_view({"get": "retrieve"}),
    ),
]
