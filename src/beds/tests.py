import json
from graphene_django.utils.testing import GraphQLTestCase


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
                    bedName
                }
            }
            """
        )
        error_message = json.loads(response.content).get('errors')[0].get('message')
        assert 'You must be a superuser or staff' in error_message