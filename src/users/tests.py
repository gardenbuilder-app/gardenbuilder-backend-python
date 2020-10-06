# from django.test import TestCase
import pytest
import json
from graphene.test import Client
from users.models import CustomUser
from config import schema
from graphene_django.utils.testing import GraphQLTestCase, graphql_query

"""
Test whether creating a new user works
"""


@pytest.mark.django_db
def test_create_new_user():
    CustomUser.objects.create_user(
        email="johnlennon@thebeatels.com", password="John.john"
    )
    assert CustomUser.objects.count() == 1


"""
Test that adding username when trying to create user throws error
"""


@pytest.mark.django_db
def test_creating_user_with_username_throws_error():
    with pytest.raises(Exception) as e:
        CustomUser.objects.create_user(
            username="JohnLennon",
            email="johnlennon@thebeatels.com",
            password="John.john",
        )
        assert (
            str(e.value) == "CustomUser() got an unexpected keyword argument 'username'"
        )


class TestGraphQLQueries(GraphQLTestCase):
    """
    Test that querying all users isn't possible as anonymous user
    """

    def test_users_query_throws_error(self):
        response = self.query(
            '''
                query {
                    users {
                        id
                        email
                    }
                }
            '''
        )
        error_message = json.loads(response.content).get('errors')[
            0].get('message')
        assert 'You must be a superuser' in error_message
