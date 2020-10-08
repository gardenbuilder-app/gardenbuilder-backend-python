from django.db import models
from django.utils.timezone import now
from apps.beds.models import Bed


class Section(models.Model):
    # name = models.CharField(max_length=100, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(default=now)
    is_active = models.BooleanField(default=True)
    bed = models.ForeignKey(Bed, related_name="sections",
                            on_delete=models.CASCADE)
    xLocation = models.PositiveSmallIntegerField(default=0, blank=False)
    yLocation = models.PositiveSmallIntegerField(default=0, blank=False)

    def __str__(self):
        return f"{self.xLocation}, {self.yLocation}"
