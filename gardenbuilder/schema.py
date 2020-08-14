import graphene
from graphene_django import DjangoObjectType
from api.models import Garden

class GardenType(DjangoObjectType):
    class Meta:
        model = Garden
        fields = ('id', 'gardenName')

class Query(graphene.ObjectType):
    all_gardens = graphene.List(GardenType)
    
    def resolve_all_gardens(root, info):
        return Garden.objects.all()
        # return Garden.objects.select_related('category').all()

schema = graphene.Schema(query=Query)