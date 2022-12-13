from django.db import models


class Faculty(models.Model):
    name = models.CharField(
        max_length=100
    )

    class Meta:
        verbose_name = "Faculty"
        verbose_name_plural = "Faculties"
        db_table = "Faculty"
