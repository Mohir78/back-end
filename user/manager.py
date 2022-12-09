from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    def create_student(self, username, email, password, **extra_fields):
        extra_fields.setdefault("role", "STUDENT")

        return self._create_user(username, email, password, **extra_fields)

    def create_dean(self, username, email, password, **extra_fields):
        extra_fields.setdefault("role", "DEAN")

        return self._create_user(username, email, password, **extra_fields)

    def create_staff(self, username, email, password, **extra_fields):
        extra_fields.setdefault("role", "STAFF")

        return self._create_user(username, email, password, **extra_fields)
