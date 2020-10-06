import graphene
from graphene_django import DjangoObjectType
from .models import Garden
from users.schema import UserType


class GardenType(DjangoObjectType):
    class Meta:
        model = Garden


class CreateGarden(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String(required=True)
    owner = graphene.Field(UserType)

    class Arguments:
        name = graphene.String(required=True)

    def mutate(self, info, name):
        user = info.context.user or None
        garden = Garden(name=name, owner=user)
        garden.save()

        return CreateGarden(
            id=garden.id,
            name=garden.name,
            owner=garden.owner,
        )


class Query(graphene.ObjectType):
    gardens = graphene.List(GardenType)
    user_gardens = graphene.List(GardenType)

    def resolve_user_gardens(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Not logged in!")
        return Garden.objects.filter(owner=user)

    def resolve_gardens(self, info):
        user = info.context.user
        if not (user.is_superuser or user.is_staff):
            raise Exception("You must be a superuser to view all gardens")
        return Garden.objects.all()


class Mutation(graphene.ObjectType):
    create_garden = CreateGarden.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
