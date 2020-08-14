from django.db import models

# Create your models here
class Garden(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    gardenName = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.gardenName

    class Meta:
        ordering = ['created']
    