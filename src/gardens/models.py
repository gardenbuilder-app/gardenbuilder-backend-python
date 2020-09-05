from django.db import models
from django.utils.timezone import now
from django.conf import settings


class Garden(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField(blank=True, null=True)
    garden_name = models.CharField(max_length=100, blank=False)
    start_date = models.DateField(default=now)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        related_name="gardens",
        on_delete=models.CASCADE,
        default=1,
    )

    def __str__(self):
        return self.garden_name

    class Meta:
        ordering = ["created"]
