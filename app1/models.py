from django.db import models

# Create your models here.
class person(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=20)
    subject=models.CharField(max_length=30)
    message=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name