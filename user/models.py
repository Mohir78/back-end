from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from user.custom_permission import CustomPermissionsMixin
from user.manager import CustomUserManager


class User(AbstractBaseUser, CustomPermissionsMixin):
    ROLE = [
        ['DEAN', 'DEAN'],
        ['STAFF', 'STAFF'],
        ['STUDENT', 'STUDENT'],
    ]

    SEX = [
        ['MALE', 'MALE'],
        ['FEMALE', 'FEMALE'],
        ['OTHER', 'OTHER'],
    ]

    fio = models.CharField(
        max_length=150,
        null=True
    )

    sex = models.CharField(
        max_length=10,
        choices=SEX
    )

    date_of_birth = models.DateField()

    region_of_birth = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    nation = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    type_of_school = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    from_course_to_course = models.CharField(
        max_length=500
    )

    profile_image = models.ImageField(
        upload_to='profile_images/',
        null=True,
        blank=True
    )

    role = models.CharField(
        max_length=15,
        choices=ROLE,
    )

    # after group creates
    # student_group = models.ForeignKey(
    #     "Group",
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True
    # )

    passport_series = models.CharField(
        max_length=10,
        unique=True,
        null=True,
        blank=True
    )

    JSHIR = models.CharField(
        max_length=14,
        unique=True,
        null=True,
        blank=True
    )

    id_number = models.CharField(
        "ID",
        max_length=50,
        unique=True,
    )

    order_number = models.BigIntegerField(
        null=True,
        blank=True
    )

    order_date = models.DateField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        default=timezone.now
    )
    is_active = models.BooleanField(
        default=True
    )
    is_staff = models.BooleanField(
        default=False,
        null=True,
        blank=True
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "id_number"

    class Meta:
        db_table = 'user'
        ordering = ['fio', ]
