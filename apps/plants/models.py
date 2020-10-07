from django.db import models
from django.utils.timezone import now
from apps.sections.models import Section


class Plant(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(default=now)
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=100, blank=False)
    section = models.ForeignKey(
        Section, related_name="plants", on_delete=models.CASCADE
    )
    square_footage = models.DecimalField(
        default=0.25, max_digits=3, decimal_places=2)
    square_footage_sfg = models.DecimalField(
        default=0.25, max_digits=3, decimal_places=2
    )

    def __str__(self):
        return self.name
