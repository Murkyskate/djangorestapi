from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.name