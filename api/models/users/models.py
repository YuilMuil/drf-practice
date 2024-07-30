from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
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
        superuser = self.create_user(
            email=email,
            password=password,
            **extra_fields
        )

        superuser.is_active = True
        superuser.is_staff = True
        superuser.is_superuser = True

        superuser.save(using=self._db)
        return superuser


class User(DefaultModel, AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True, help_text="유저 아이디")
    email = models.EmailField(unique=True, max_length=30, null=False, blank=False, help_text="유저 이메일", )
    name = models.CharField(max_length=16, help_text="유저 이름")
    is_active = models.BooleanField(default=True, help_text="활성화 여부(0: 활성화, 1: 비활성화)")
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Use helper class
    objects = UserManager()

    # Enable to login using `email`
    USERNAME_FIELD = 'email'

    class Meta:
        get_latest_by = "id"
        ordering = ['id']

    def __str__(self):
        return f"({self.id}) {self.email}"
