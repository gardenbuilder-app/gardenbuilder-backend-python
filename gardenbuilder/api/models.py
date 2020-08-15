from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Garden(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    gardenName = models.CharField(max_length=100, blank=False)
    owner = models.ForeignKey(User, related_name='gardens', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.gardenName

    class Meta:
        ordering = ['created']
    