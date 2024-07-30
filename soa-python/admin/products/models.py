from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200, blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.title
