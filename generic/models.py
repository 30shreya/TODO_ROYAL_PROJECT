from django.db import models

# Create your models here.
class BaseField(models.model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        abstract = True
        
