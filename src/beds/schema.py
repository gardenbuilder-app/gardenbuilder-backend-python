import graphene
from graphene_django import DjangoObjectType
from beds.models import Bed
from gardens.models import Garden
from gardens.schema import GardenType
from django.utils.timezone import now
import traceback
import datetime


class BedType(DjangoObjectType):
    class Meta:
        model = Bed


class CreateBed(graphene.Mutation):
    # Define final parameter types
    id = graphene.Int()
    bed_name = graphene.String(required=True)
    garden = graphene.Field(GardenType)
    start_date = graphene.Date(required=False)
    length = graphene.Int(required=True)
    width = graphene.Int(required=True)
    notes = graphene.String(required=False)

    # Define accepted arguments
    class Arguments:
        bed_name = graphene.String(required=True)
        garden_id = graphene.Int(required=True)
        start_date = graphene.Date(required=False)
        length = graphene.Int(required=True)
        width = graphene.Int(required=True)
        notes = graphene.String(required=False)

    def mutate(self, info, bed_name, length, width, garden_id, **kwargs):
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

        # Save new bed with all parameters
        bed = Bed(
            bed_name=bed_name,
            length=length,
            width=width,
            garden=garden,
            start_date=start_date,
            notes=notes,
        )
        bed.save()

        # Return all parameters
        return CreateBed(
            id=bed.id,
            bed_name=bed_name,
            garden=garden,
            length=length,
            notes=notes,
            start_date=start_date,
            width=width,
        )


class Query(graphene.ObjectType):
    beds = graphene.List(BedType)
    # beds_by_garden = graphene.Field(Bed, gardenId=Int(required=False))
    
    # def resolve_beds_by_garden(self, info, gardenId):
    #     try:
    #         user = info.context.user
    #         garden = Garden.objects.filter(id = gardenId)
    #         print(garden)
    #         if user.is_anonymous:
    #             raise Exception("Not logged in!")
    #         return Bed.objects.filter(owner=user, garden=gardenId)

    #     except IOError as (errno, strerror):
    #         print "I/O error({0}): {1}".format(errno, strerror)

    #     except ValueError:
    #         print "Could not convert data to an integer."

    #     except:
    #         print "Unexpected error:", sys.exc_info()[0]
    #         raise


    def resolve_beds(self, info):
        user = info.context.user
        if not ( user.is_superuser or user.is_staff ):
            raise Exception("You must be a superuser to view all beds")
        return Bed.objects.all()


class Mutation(graphene.ObjectType):
    create_bed = CreateBed.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
