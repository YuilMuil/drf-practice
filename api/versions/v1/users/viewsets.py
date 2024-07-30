from django.http import Http404
from rest_framework import status, mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from drf_yasg.utils import swagger_auto_schema

from api.models.users.models import User

from common.mixins import MappingViewSetMixin

from .serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  MappingViewSetMixin,
                  GenericViewSet):
    """
    :comment: User CRUD, Login & Join.
    """
    serializer_action_map = {
        "create": UserSerializer,
        "retrieve": UserSerializer,
    }
    queryset = User.objects.filter(is_active=True, is_staff=False, is_superuser=False)

    def create(self, request, *args, **kwargs):
        """
        - 회원가입

        **Description**
        - 회원가입 시 사용하는 API입니다.
        """
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        - 유저 정보 조회

        **Description**
        - User Id에 해당하는 유저 정보를 가져옵니다.
        """
        return super().retrieve(request, *args, **kwargs)
