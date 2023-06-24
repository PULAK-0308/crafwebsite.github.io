from django.db import models

# Create your models here.

class DreamProduct(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="craft/images",default="")
    
    def __str__(self):
        return self.product_name

class ResinProduct(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="craft/images",default="")
    
    def __str__(self):
        return self.product_name




