from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone

from user.manager import CustomUserManager


class User(AbstractBaseUser):
    ROLE = [
        ['DEAN', 'DEAN'],
        ['STAFF', 'STAFF'],
        ['STUDENT', 'STUDENT'],
    ]

    username_validator = UnicodeUsernameValidator()

    firstname = models.CharField(
        max_length=100,
        null=True
    )
    lastname = models.CharField(
        max_length=100,
        null=True
    )
    fathername = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    username = models.CharField(
        max_length=255,
        unique=True,
        validators=[username_validator],
    )
    email = models.EmailField(
        blank=True,
        null=True
    )
    is_active = models.BooleanField(
        default=True
    )
    created_at = models.DateTimeField(
        default=timezone.now
    )

    role = models.CharField(
        max_length=15,
        choices=ROLE,
        null=False
    )

    JSHIR = models.CharField(
        max_length=14,
        unique=True,
    )

    passport_number = models.CharField(
        max_length=10,
    )

    profile_image = models.ImageField(
        upload_to='profile_image/',
    )

    phone_number = models.CharField(
        max_length=12,
        blank=True,
        null=True
    )

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)
