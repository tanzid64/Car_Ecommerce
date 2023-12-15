from django.db import models
from brand.models import Brand
# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/')
    price = models.IntegerField()
    quantity = models.IntegerField(null=True, blank = True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
    details = models.TextField()

    def __str__(self) -> str:
        return f'{self.brand.name}-{self.name}'