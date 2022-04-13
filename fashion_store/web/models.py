from django.db import models
from django.contrib.auth import models as auth_models

from fashion_store.web.managers import FashionUserManager


class FashionStoreUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 25

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = FashionUserManager()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=30,
    )

    picture = models.URLField(max_length=300, )

    description = models.TextField(
        null=True,
        blank=True,
    )
    user = models.OneToOneField(
        FashionStoreUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Products(models.Model):
    product_name = models.CharField(
        max_length=50,
    )

    product_picture = models.ImageField()

    price = models.FloatField()

    size = models.IntegerField()

