from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=16)
    msg=models.CharField(max_length=1500)
    def __str__(self):
        return self.name
