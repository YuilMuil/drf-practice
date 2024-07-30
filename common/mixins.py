from typing import Optional
from rest_framework.viewsets import GenericViewSet


class MappingViewSetMixin:
    serializer_class = None
    permission_classes = None

    serializer_action_map = {}
    permission_classes_map = {}

    def get_permissions(self: GenericViewSet | Optional['MappingViewSetMixin']):
        permission_classes = self.permission_classes
        if not permission_classes:
            permission_classes = []
            if self.permission_classes_map.get(self.action, None):
                permission_classes.append(self.permission_classes_map[self.action])

        return [permission() for permission in permission_classes]

    def get_serializer_class(self: GenericViewSet | Optional['MappingViewSetMixin']):
        if self.serializer_action_map.get(self.action, None):
            return self.serializer_action_map[self.action]
        return self.serializer_class



