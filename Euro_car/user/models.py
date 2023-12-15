from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class History(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='histories', null=True, blank = True)
    date = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    def __str__(self) -> str:
        return self.name