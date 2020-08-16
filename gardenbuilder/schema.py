import graphene
from graphene_django import DjangoObjectType
from api.models import Garden

class GardenType(DjangoObjectType):
    class Meta:
        model = Garden
        fields = ('id', 'created', 'garden_name', 'start_date', 'end_date', 'is_active', 'user_id')

class Query(graphene.ObjectType):
    all_gardens = graphene.List(GardenType)
    
    def resolve_all_gardens(root, info):
        return Garden.objects.all()

schema = graphene.Schema(query=Query)