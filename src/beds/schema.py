import graphene
from graphene_django import DjangoObjectType
from beds.models import Bed
from gardens.models import Garden
from gardens.schema import GardenType
from users.schema import UserType
from django.utils.timezone import now
import traceback
import datetime


class BedType(DjangoObjectType):
    class Meta:
        model = Bed


class CreateBed(graphene.Mutation):
    # Define final parameter types
    id = graphene.Int()
    name = graphene.String(required=True)
    garden = graphene.Field(GardenType)
    start_date = graphene.Date(required=False)
    length = graphene.Int(required=True)
    width = graphene.Int(required=True)
    notes = graphene.String(required=False)
    owner = graphene.Field(UserType)


    # Define accepted arguments
    class Arguments:
        name = graphene.String(required=True)
        garden_id = graphene.Int(required=True)
        start_date = graphene.Date(required=False)
        length = graphene.Int(required=True)
        width = graphene.Int(required=True)
        notes = graphene.String(required=False)

    def mutate(self, info, name, length, width, garden_id, **kwargs):
        # Get logged in user info
        user = info.context.user
        if user.is_anonymous:
            raise Exception("You must be logged in to create a bed!")
        # Get garden associated with id
        garden = Garden.objects.get(id=garden_id, owner=user)
        if not garden:
            raise Exception("Invalid garden id!")

        # Get startDate and notes if they were optionally passed as key word arguments
        start_date = kwargs.get("start_date", now())
        notes = kwargs.get("notes", "")

        print('adding bed')

        # Save new bed with all parameters
        bed = Bed(
            name=name,
            length=length,
            width=width,
            garden=garden,
            start_date=start_date,
            notes=notes,
            owner_id=user.id
        )
        bed.save()

        # Return all parameters
        return CreateBed(
            id=bed.id,
            name=name,
            garden=garden,
            length=length,
            notes=notes,
            start_date=start_date,
            width=width,
            owner=user
        )


class Query(graphene.ObjectType):
    beds = graphene.List(BedType)
    beds_for_user = graphene.List(BedType, gardenId=graphene.Int(required=False))

    def resolve_beds(self, info):
        user = info.context.user
        if not (user.is_superuser | user.is_staff):
            raise Exception("You must be a superuser or staff to view all beds")
        return Bed.objects.all()

    def resolve_beds_for_user(self, info, gardenId=None):
        user = info.context.user
        try:
            if user.is_anonymous:
                raise Exception("Not logged in, so you don't have beds")
        except Exception:
            raise
        else:
            filter_params = {}
            if gardenId:
                filter_params = {'garden': gardenId}
            filter_params.update({'owner': user})
            return Bed.objects.filter(**filter_params)


class Mutation(graphene.ObjectType):
    create_bed = CreateBed.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
