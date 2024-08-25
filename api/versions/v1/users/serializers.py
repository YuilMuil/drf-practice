from rest_framework import serializers
from api.models.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
<<<<<<< Updated upstream
        fields = (
            "id",
            "email",
            "name",
            "gender",
            "is_active",
            "is_staff",
            "is_superuser",
            "last_login",
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
        del represented["is_active"]
        del represented["is_staff"]
        del represented["is_superuser"]
        del represented["last_login"]
        return represented
=======
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
            'resident_code': {'write_only': True},
        }

    def validate_gender(self, gender):
        if gender is not None and (gender > 2 or gender < 0):
            raise serializers.ValidationError("Gender must be 0, 1, or 2")
        return gender

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return email

    def validate_birth_date(self, birth_date):
        if birth_date and len(birth_date) != 8:
            raise serializers.ValidationError("Birth date must be in YYYYMMDD format")
        return birth_date

    def validate_phone_number(self, phone_number):
        if not phone_number.startswith('010') or len(phone_number) != 11:
            raise serializers.ValidationError("Phone number must start with '010' and be 11 digits long")
        return phone_number

    def validate_zip_code(self, zip_code):
        if len(zip_code) != 5:
            raise serializers.ValidationError("ZIP code must be 5 digits long")
        return zip_code

    def to_representation(self, instance):
        represented = super(UserSerializer, self).to_representation(instance)
        return {
            'id': represented.get('id'),
            'name': represented.get('name'),
            'email': represented.get('email'),
            'is_active': represented.get('is_active')
        }
>>>>>>> Stashed changes
