import graphene
from graphene_django import DjangoObjectType
from beds.models import Bed
from gardens.models import Garden
from gardens.schema import GardenType
from django.utils.timezone import now
import traceback

class BedType(DjangoObjectType):
    class Meta:
        model = Bed

class CreateBed(graphene.Mutation):
    id = graphene.Int()
    bed_name = graphene.String(required=True)
    garden_id = graphene.Field(GardenType)
    # start_date = graphene.Date(required=False)
    length = graphene.Int(required=True)
    width = graphene.Int(required=True)
    notes = graphene.String(required=False)

    class Arguments:
        bed_name = graphene.String(required=True)
        garden_id = graphene.Int(required=True)
        # start_date = graphene.Date(required=False)
        length = graphene.Int(required=True)
        width = graphene.Int(required=True)
        notes = graphene.String(required=False)

    def mutate(self, info, bed_name, length, width, garden_id, **kwargs ):
        try: 
        
            garden = Garden.objects.get(id=garden_id)
            bed = Bed(bed_name=bed_name, length=length, width=width, garden=garden)
            # start_date = kwargs.get('start_date', now)
            notes = kwargs.get('notes', '')
            # bed.start_date = start_date
            bed.notes = notes
            bed.save()
            
        except Exception as e:
            print(e) 
            print(traceback.format_exc())
        
        
        return CreateBed(
            # id=bed.id,
            bed_name=bed_name,
            # garden_id=garden_id,
            length=length,
            # notes=notes,
            # start_date=start_date,
            width=width
        )

class Query(graphene.ObjectType):
    beds = graphene.List(BedType)

    def resolve_beds(self, info):
        return Bed.objects.all()

class Mutation(graphene.ObjectType):
    create_bed = CreateBed.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)