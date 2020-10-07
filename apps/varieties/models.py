from django.db import models
from django.utils.timezone import now
from apps.plants.models import Plant


class Variety(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(default=now)
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=100, blank=False)
    scientific_name = models.CharField(max_length=100, blank=False)
    plant = models.ForeignKey(
        Plant, related_name="varieties", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
