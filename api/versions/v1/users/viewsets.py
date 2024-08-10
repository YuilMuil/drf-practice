from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.models.users.models import User

from common.mixins import MappingViewSetMixin

from .serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  MappingViewSetMixin,
                  GenericViewSet):
    """
    :comment: User CRUD, Login & Join.
    """
    serializer_action_map = {
        "create": UserSerializer,
        "retrieve": UserSerializer,
        "list": UserSerializer,
        "update": UserSerializer,
        "partial_update": UserSerializer,
        "destroy": UserSerializer
    }
    queryset = User.objects.filter(is_active=True, is_staff=False, is_superuser=False)

    def create(self, request, *args, **kwargs):
        print("AHAHAHA")
        return super().create(request, *args, **kwargs)