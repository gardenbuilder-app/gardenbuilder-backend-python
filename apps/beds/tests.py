import json
from graphene_django.utils.testing import GraphQLTestCase

from apps.beds.models import Bed
from apps.users.models import CustomUser
from apps.gardens.models import Garden



class TestGraphQLQueries(GraphQLTestCase):
    """
    Test that querying all beds isn't possible as anonymous user
    """

    def test_beds_query(self):
        response = self.query(
            """
            query {
                beds {
                    id
                    name
                }
            }
            """
        )
        error_message = json.loads(response.content).get('errors')[
            0].get('message')
        assert 'You must be a superuser or staff' in error_message


class TestBedInstance:
    """
    Tests for Bed object
    """

    GARDEN_NAME = "Secret Garden"
    EMAIL = "test@test.com"
    PASSWORD = "testing1234"
    user = CustomUser(email=EMAIL, password=PASSWORD)
    BED_DESCRIPTION = "test description"
    bed = Bed(name='test_bed', garden=Garden(name=GARDEN_NAME, owner=user),
         description=BED_DESCRIPTION)


    def test_bed_description(self):
        """ ensure Bed has description field """

        assert self.bed.description == self.BED_DESCRIPTION