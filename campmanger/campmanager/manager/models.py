from django.db import models

# Create your models here.

class subscriber(models.Model):
    emailid = models.TextField(max_length=50,unique=True)
    first_name = models.TextField(max_length=50)
    issubscribed = models.BooleanField(default=True)
    isactive = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.first_name
