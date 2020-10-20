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

    user = CustomUser(email = 'bed@test.com', password = 'test123')
    user.save()

    garden = Garden(name = 'Garden Beds')
    garden.save()

    # positive test for setting a description
    testBed = Bed(name = 'Bed',
                  description = 'Test Description',
                  garden = garden,
                  start_date = '2020-10-19',
                  length = 8,
                  width = 4,
                  notes = 'This is a test',
                  owner = user)
    testBed.save()

    # negative test for not setting a description
    testBed = Bed(name = 'Bed 2',
                  garden = garden,
                  start_date = '2020-10-19',
                  length = 8,
                  width = 4,
                  notes = 'This is a test',
                  owner = user)
    testBed.save()

    print('Test bed created')
