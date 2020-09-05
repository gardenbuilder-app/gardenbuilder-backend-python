import graphene
from graphene_django import DjangoObjectType
from .models import Garden
from users.schema import UserType


class GardenType(DjangoObjectType):
    class Meta:
        model = Garden


class CreateGarden(graphene.Mutation):
    id = graphene.Int()
    garden_name = graphene.String(required=True)
    owner = graphene.Field(UserType)

    class Arguments:
        garden_name = graphene.String(required=True)

    def mutate(self, info, garden_name):
        user = info.context.user or None

        garden = Garden(garden_name=garden_name, owner=user)
        garden.save()

        return CreateGarden(
            id=garden.id,
            garden_name=garden.garden_name,
            owner=garden.owner,
        )


class Query(graphene.ObjectType):
    gardens = graphene.List(GardenType)

    def resolve_gardens(self, info):
        return Garden.objects.all()


class Mutation(graphene.ObjectType):
    create_garden = CreateGarden.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
