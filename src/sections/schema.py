import graphene
from graphene_django import DjangoObjectType
from beds.models import Bed
from beds.schema import BedType
from sections.models import Section
from django.utils.timezone import now
from datetime import date


class SectionType(DjangoObjectType):
    class Meta:
        model = Section


class CreateSection(graphene.Mutation):
    # Define final parameter types
    id = graphene.Int()
    bed = graphene.Field(BedType)
    end_date = graphene.Date(required=False)
    is_active = graphene.Boolean(required=False)
    end_date = graphene.Date(required=False)
    start_date = graphene.Date(required=False)
    xLocation = graphene.Int(required=True)
    yLocation = graphene.Int(required=True)

    # Define accepted arguments
    class Arguments:
        bed_id = graphene.Int(required=True)
        end_date = graphene.Date(required=False)
        is_active = graphene.Boolean(required=False)
        start_date = graphene.Date(required=False)
        xLocation = graphene.Int(required=True)
        yLocation = graphene.Int(required=True)

    def mutate(self, info, bed_id, xLocation, yLocation, **kwargs):
        # Get bed associated with id
        bed = Bed.objects.get(id=bed_id)

        # Retrieve optionally passed key word arguments
        end_date = kwargs.get("end_date", date(year=2100, month=1, day=1))
        is_active = kwargs.get("is_active", True)
        start_date = kwargs.get("start_date", now())

        # Save new section with all parameters
        section = Section(
            end_date=end_date,
            is_active=is_active,
            start_date=start_date,
            xLocation=xLocation,
            yLocation=yLocation,
            bed=bed,
        )
        section.save()

        # Return all parameters
        return CreateSection(
            id=bed.id,
            end_date=end_date,
            is_active=is_active,
            start_date=start_date,
            xLocation=xLocation,
            yLocation=yLocation,
            bed=bed,
        )


class Query(graphene.ObjectType):
    sections = graphene.List(SectionType)

    def resolve_sections(self, info):
        return Section.objects.all()


class Mutation(graphene.ObjectType):
    create_section = CreateSection.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
