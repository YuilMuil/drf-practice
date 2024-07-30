from rest_framework import serializers

from api.models.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "name", "is_active", "is_staff", "is_superuser", "last_login")
