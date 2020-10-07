import json
from django.test import TestCase
from apps.sections.models import Section
from apps.beds.models import Bed
from apps.gardens.models import Garden
from apps.users.models import CustomUser
from django.utils.timezone import now
from graphene_django.utils.testing import GraphQLTestCase, graphql_query


def _create_default_bed():
    GARDEN_NAME = "Secret Garden"
    BED_NAME = "Secret Bed"
    EMAIL = "test@test.com"
    PASSWORD = "testing1234"

    user = CustomUser.objects.create(email=EMAIL, password=PASSWORD)
    garden = Garden.objects.create(name=GARDEN_NAME, owner=user)
    bed = Bed.objects.create(name=BED_NAME, garden=garden)

    user.save()
    garden.save()
    bed.save()
    return bed


def _create_default_section():
    bed = _create_default_bed()
    default_section = Section.objects.create(bed=bed)
    default_section.save()
    return default_section


class SectionsTestCase(TestCase):
    def setUp(self):
        self.timer_start = now()
        self.section = _create_default_section()

    def test_section_created_with_default_x_location(self):
        assert self.section.xLocation == 0

    def test_section_created_with_default_y_location(self):
        assert self.section.yLocation == 0

    def test_section_created_with_default_is_active(self):
        assert self.section.is_active == True

    def test_section_created_with_default_start_date(self):
        "Default start should be 'now', which which is between the time the test start and end."
        assert self.section.start_date > self.timer_start
        assert self.section.start_date < now()

    def test_section_created_with_default_end_date(self):
        assert self.section.end_date == None

    def test_str_is_locations(self):
        assert self.section.__str__() == "0, 0"


class SectionQueryTests(GraphQLTestCase):
    SECTION_QUERY = """
      query {
        sections {
          id
          created
          endDate
          startDate
          isActive
          bed {
            name
          }
          xLocation
          yLocation
        }
      }
    """

    def test_sections_query_without_data(self):
        res = self.query(self.SECTION_QUERY)
        data = json.loads(res.content)['data']
        assert len(data['sections']) == 0

    def test_sections_query_with_data(self):
        section = _create_default_section()
        res = self.query(self.SECTION_QUERY)
        data = json.loads(res.content)['data']

        assert len(data['sections']) == 1
        assert data['sections'][0]['id'] == str(section.id)
        assert data['sections'][0]['bed']['name'] == 'Secret Bed'


class SectionMutationTest(GraphQLTestCase):
    def test_create_section_mutations(self):
        xLocation = 10
        yLocation = 5
        bed = _create_default_bed()

        res = self.query('''
    mutation {
      createSection(
        bedId: %s,
        xLocation: %s,
        yLocation: %s
      ) {
        id
        xLocation
        yLocation
        bed {
          id
        }
      }
    }
    ''' % (bed.id, xLocation, yLocation))

        section = json.loads(res.content)['data']['createSection']

        assert section['xLocation'] == xLocation
        assert section['yLocation'] == yLocation
        assert section['bed']['id'] == str(bed.id)
