from django.db import models

# Create your models here
class Gardens(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    gardenName = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ['created']
    