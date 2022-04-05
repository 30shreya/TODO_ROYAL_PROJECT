from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)
    populations = models.IntegerField()
    
    
    class Meta():
        db_table = "city"
