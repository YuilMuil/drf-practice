from rest_framework import serializers

from api.models.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "name",
            "gender",
            "is_active",
            "is_staff",
            "is_superuser",
            "last_login"
        )

    def validate_email(self, email):
        print(email)
        return email

    def validate_name(self, name):
        print(name)
        if len(name) > 3:
            return "INVALIDUSER"
        return name

    def validate(self, attrs):
        # attrs -> attributes
        if list(attrs.get("name"))[0] == "황" and attrs.get("gender") != 0:
            raise ValueError

        return super().validate(attrs)

    def to_representation(self, instance):
        represented = super().to_representation(instance)
        del represented['is_active']
        del represented['is_staff']
        del represented['is_superuser']
        del represented['last_login']
        return represented
