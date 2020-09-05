import graphene
from graphene_django import DjangoObjectType
from sections.models import Section
from sections.schema import SectionType
from plants.models import Plant
from django.utils.timezone import now
from datetime import date


class PlantType(DjangoObjectType):
    class Meta:
        model = Plant


class CreateSection(graphene.Mutation):
    # Define final parameter types
    id = graphene.Int()
    section = graphene.Field(Section)
    end_date = graphene.Date(required=False)
    is_active = graphene.Boolean(required=False)
    start_date = graphene.Date(required=False)
    name = graphene.String(required=True)
    square_footage = graphene.Float(required=False)
    square_footage_sfg = graphene.Float(required=False)

    # Define accepted arguments
    class Arguments:
        section_id = graphene.Int(required=True)
        end_date = graphene.Date(required=False)
        is_active = graphene.Boolean(required=False)
        start_date = graphene.Date(required=False)
        name = graphene.String(required=True)
        square_footage = graphene.Float(required=False)
        square_footage_sfg = graphene.Float(required=False)

    def mutate(self, info, bed_id, xLocation, yLocation, **kwargs):
        # Get bed associated with id
        section = Section.objects.get(id=section_id)

        # Retrieve optionally passed key word arguments
        end_date = kwargs.get('end_date', date(year=2100, month=1, day=1))
        is_active = kwargs.get('is_active', True)
        start_date = kwargs.get('start_date', now())
        square_footage = kwargs.get('square_footage', .25)
        square_footage_sfg = kwargs.get('square_footage_sfg', .25)

        # Save new section with all parameters
        plant = Plant(
            end_date=end_date,
            is_active=is_active,
            start_date=start_date,
            square_footage=square_footage,
            square_footage_sfg=square_footage_sfg,
            section=section
        )
        plant.save()

        # Return all parameters
        return CreateSection(
            id=plant.id,
            end_date=end_date,
            is_active=is_active,
            start_date=start_date,
            square_footage=square_footage
            square_footage_sfg=square_footage_sfg
            section=section
        )


class Query(graphene.ObjectType):
    sections = graphene.List(SectionType)

    def resolve_sections(self, info):
        return Section.objects.all()


class Mutation(graphene.ObjectType):
    create_section = CreateSection.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
