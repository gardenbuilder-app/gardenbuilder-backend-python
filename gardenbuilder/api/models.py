from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Garden(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    garden_name = models.CharField(max_length=100, blank=False)
    user_id = models.ForeignKey(User, related_name='gardens', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.garden_name

    class Meta:
        ordering = ['created']

class Bed(models.Model):
    bed_name = models.CharField(max_length=100, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    garden_id = models.ForeignKey(Garden, related_name='beds', on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    length = models.PositiveSmallIntegerField(default=0)
    width = models.PositiveSmallIntegerField(default=0)
    notes = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return self.bed_name

    class Meta:
        ordering = ['created']

class Section(models.Model):
    section_name = models.CharField(max_length=100, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    bed_id = models.ForeignKey(Bed, related_name='sections', on_delete=models.CASCADE)
    xLocation = models.PositiveSmallIntegerField(default=0)
    yLocation = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.section_name

    class Meta:
        ordering = ['created']
    