import graphene
from graphene_django import DjangoObjectType
from .models import Garden, Bed, Section, Plant, PlantVariety 
from users.schema import UserType

class GardenType(DjangoObjectType):
    class Meta:
        model = Garden

class CreateGarden(graphene.Mutation):
    id = graphene.Int()
    garden_name = graphene.String(required=True)
    posted_by = graphene.Field(UserType)

    class Arguments:
        garden_name = graphene.String(required=True)

    def mutate(self, info, garden_name):
        user = info.context.user or None

        garden = Garden(garden_name=garden_name, posted_by=user)
        garden.save()
        
        return CreateGarden(
            id=garden.id,
            garden_name=garden.garden_name,
            posted_by=garden.posted_by,
        )

class BedType(DjangoObjectType):
    class Meta:
        model = Bed

class SectionType(DjangoObjectType):
    class Meta:
        model = Section

class PlantType(DjangoObjectType):
    class Meta:
        model = Plant

class PlantVarietyType(DjangoObjectType):
    class Meta:
        model = PlantVariety

class Query(graphene.ObjectType):
    gardens = graphene.List(GardenType)
    beds = graphene.List(BedType)
    sections = graphene.List(SectionType)
    plants = graphene.List(PlantType)
    plant_varieties = graphene.List(PlantVarietyType)
    
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

class Mutation(graphene.ObjectType):
    create_garden = CreateGarden.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)