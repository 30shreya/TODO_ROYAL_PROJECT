from django.db import models

# Create your models here.
class Ticket(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=500)

    class Meta:
        db_table = 'ticket'