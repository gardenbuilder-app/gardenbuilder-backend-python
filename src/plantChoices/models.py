from django.db import models
from django.utils.timezone import now
from sections.models import Section


class PlantChoice(models.Model):
    genus = models.CharField(max_length=100, blank=False)
    genus_common_name = models.CharField(max_length=100, blank=False)
    species = models.CharField(max_length=100, blank=False)
    species_common_name = models.CharField(max_length=100, blank=False)
    square_footage = models.DecimalField(
        default=0.25, max_digits=3, decimal_places=2)
    square_footage_sfg = models.DecimalField(
        default=0.25, max_digits=3, decimal_places=2
    )
    additional_information = models.CharField(max_length=100)

    def __str__(self):
        return self.genus_common_name

    class Meta:
        unique_together = ("species", "additional_information")
