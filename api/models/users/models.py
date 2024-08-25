from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from common.models import DefaultModel


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email not found")
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        superuser = self.create_user(email=email, password=password, **extra_fields)

        superuser.is_active = True
        superuser.is_staff = True
        superuser.is_superuser = True

        superuser.save(using=self._db)
        return superuser


class User(DefaultModel, AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True, help_text="유저 아이디")
    email = models.EmailField(
        unique=True,
        max_length=30,
        null=False,
        blank=False,
        help_text="유저 이메일",
    )
    name = models.CharField(max_length=16, help_text="유저 이름")
    gender = models.PositiveSmallIntegerField(
        help_text="0: 남자, 1: 여자, 2: 알수없음", null=True, blank=True
    )
    birth_date = models.CharField(
        max_length=8, help_text="생년월일 (YYYYMMDD)", null=True, blank=True
    )
    zip_code = models.CharField(
<<<<<<< Updated upstream
        max_length=8, null=False, blank=False, help_text="고객 ZIP 코드"
    )
    resident_code = models.CharField(
        max_length=16, null=False, blank=False, help_text="고객 주민등록번호"
=======
        max_length=8, null=True, blank=True, help_text="고객 ZIP 코드"
>>>>>>> Stashed changes
    )
    address = models.CharField(
        max_length=255, null=True, blank=True, help_text="고객 주소"
    )
    address_detail = models.CharField(
        max_length=255, null=True, blank=True, help_text="고객 상세 주소"
    )
<<<<<<< Updated upstream
    ci = models.CharField(max_length=128, null=True, blank=True, help_text="고객 CI 값")
=======
    ci = models.CharField(max_length=128, null=False, blank=False, help_text="고객 CI 값")
>>>>>>> Stashed changes
    di = models.CharField(max_length=256, null=True, blank=True, help_text="고객 DI 값")
    password = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        help_text="고객 비밀번호 해쉬 값(sha3_256)",
    )
    phone_number = models.CharField(
        max_length=16,
<<<<<<< Updated upstream
        null=False,
        blank=False,
=======
        null=True,
        blank=True,
>>>>>>> Stashed changes
        help_text="고객 휴대전화 번호(010XXXXYYYY)",
    )
    is_active = models.BooleanField(
        default=True, help_text="활성화 여부(0: 활성화, 1: 비활성화)"
    )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Use helper class
    objects = UserManager()

    # Enable to login using `email`
    USERNAME_FIELD = "email"

    class Meta:
        get_latest_by = "id"
        ordering = ["id"]

    def __str__(self):
        return f"({self.id}) {self.email}"