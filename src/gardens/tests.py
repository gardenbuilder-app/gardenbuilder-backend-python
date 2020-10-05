import pytest
import json
from gardens.models import Garden
from users.models import CustomUser
from datetime import datetime
from graphene_django.utils.testing import GraphQLTestCase, graphql_query


class TestGardenInstance:
    """
    Test that various properties are created by default on a new Garden object
    """

    GARDEN_NAME = "Secret Garden"
    EMAIL = "test@test.com"
    PASSWORD = "testing1234"
    user = CustomUser(email=EMAIL, password=PASSWORD)
    garden = Garden(name=GARDEN_NAME, owner=user)

    """ name is assigned to __str__ method """

    def test_str_matches_garden_name(self):
        assert str(self.garden) == self.GARDEN_NAME

    """ name matches what we entered """

    def test_garden_name_matches(self):
        assert self.garden.name == self.GARDEN_NAME

    """ start_date exists as a date """

    def test_start_date_property_exists_as_a_date(self):
        assert isinstance(self.garden.start_date, datetime)

    """ is_active property defaults to true """

    def test_is_active_property_exists(self):
        assert self.garden.is_active == True

    """ owner refers to the user passed as argument """

    def test_owner_is_passed_user(self):
        assert (
            self.garden.owner.email == self.EMAIL
            and self.garden.owner.password == self.PASSWORD
        )


class TestGraphQLQueries(GraphQLTestCase):
    """
    Test that GraphQL queries related to gardens work and throw errors appropriately
    TODO: Add test to ensure that a user who is_staff or is_superuser can call query w/o error
    """

    def test_gardens_query(self):
        response = self.query(
            """
            query {
                gardens {
                    id
                    name
                    owner {
                        id
                        email
                    }
                }
            }
            """
        )

        # Should throw exception since user is not staff or superuser
        self.assertResponseHasErrors(response)


    def test_incorrect_gardens_query_throws_error(self):
        response = self.query(
            """
            query {
                gardens {
                    id
                    name
                    dingdong
                    owner {
                        id
                        email
                    }
                }
            }
            """
        )

        self.assertResponseHasErrors(response)
