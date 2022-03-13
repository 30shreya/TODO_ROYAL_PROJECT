from django.db import models

# Create your models here.
class Payment(models.Model):
    amount = models.FloatField()
    payment_status = models.CharField(max_length=100)
    
    class Meta:
        db_table ='payment'
        
        
class Cart(models.Model):
    cart_name = models.CharField(max_length=50)
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE) 
    
    
    class Meta:
        db_table = 'Cart'
    
       
