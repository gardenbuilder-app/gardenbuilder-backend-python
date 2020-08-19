from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.conf import settings

# Create your models here
class Garden(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField(blank=True, null=True)
    garden_name = models.CharField(max_length=100, blank=False)
    start_date = models.DateField(default=now)
    is_active = models.BooleanField(default=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='gardens', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.garden_name

    class Meta:
        ordering = ['created']

class Bed(models.Model):
    name = models.CharField(max_length=100, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField(blank=True, null=True)
    garden = models.ForeignKey(Garden, related_name='beds', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    start_date = models.DateField(default=now)
    length = models.PositiveSmallIntegerField(default=0)
    width = models.PositiveSmallIntegerField(default=0)
    notes = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created']

class Section(models.Model):
    name = models.CharField(max_length=100, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(default=now)
    is_active = models.BooleanField(default=True)
    bed = models.ForeignKey(Bed, related_name='sections', on_delete=models.CASCADE)
    xLocation = models.PositiveSmallIntegerField(default=0)
    yLocation = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name

class Plant(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(default=now)
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=100, blank=False)
    section = models.ForeignKey(Section, related_name='plants', on_delete=models.CASCADE)
    square_footage = models.DecimalField(default=.25, max_digits=3, decimal_places=2)
    square_footage_sfg = models.DecimalField(default=.25, max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name

class PlantVariety(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(default=now)
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=100, blank=False)
    scientific_name = models.CharField(max_length=100, blank=False)
    plant = models.ForeignKey(Plant, related_name='plant_varieties', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    