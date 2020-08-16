import graphene
from graphene_django import DjangoObjectType
from api.models import Garden, Bed, Section, Plant, PlantVariety 

class GardenType(DjangoObjectType):
    class Meta:
        model = Garden
        fields = ('id', 'created', 'garden_name', 'start_date', 'is_active', 'user_id')

class BedType(DjangoObjectType):
    class Meta:
        model = Bed

class Section(DjangoObjectType):
    class Meta:
        model = Section

class Plant(DjangoObjectType):
    class Meta:
        model = Plant

class PlantVariety(DjangoObjectType):
    class Meta:
        model = PlantVariety

class Query(graphene.ObjectType):
    gardens = graphene.List(GardenType)
    beds = graphene.List(BedType)
    sections = graphene.List(BedType)
    plants = graphene.List(BedType)
    plant_varieties = graphene.List(BedType)
    
    def resolve_gardens(root, info):
        return Garden.objects.all()
    
    def resolve_beds(root, info):
        return Bed.objects.all()
    
    def resolve_sections(root, info):
        return Section.objects.all()
    
    def resolve_plants(root, info):
        return Plant.objects.all()
    
    def resolve_plant_varieties(root, info):
        return PlantVariety.objects.all()

schema = graphene.Schema(query=Query)