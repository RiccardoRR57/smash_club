from django.db import models

# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    
    def __str__(self):
        return f"{self.pk}: {self.first_name} {self.last_name} ({self.birth_date})"
        