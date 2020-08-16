from django.contrib import admin
from api.models import Garden, Bed, Section, Plant, PlantVariety

# Register your models here.
admin.site.register(Garden)
admin.site.register(Bed)
admin.site.register(Section)
admin.site.register(Plant)
admin.site.register(PlantVariety)
