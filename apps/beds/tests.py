import json
from graphene_django.utils.testing import GraphQLTestCase
from apps.beds.models import Bed
from apps.gardens.models import Garden
from apps.users.models import CustomUser



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

class TestBed:

    user = CustomUser(email = 'bed2@test.com', password = 'test123')
    user.save()
    garden = Garden(name = 'Bed Garden 2')
    garden.save()

    testBed = Bed(name = 'Bed 1',
                  description = 'Test Description',
                  garden = garden,
                  start_date = '2020-10-19',
                  length = 8,
                  width = 4,
                  notes = 'This is a test',
                  owner = user)
    testBed.save()
    print ('Test bed created')
