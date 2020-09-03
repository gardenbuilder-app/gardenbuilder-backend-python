# from django.test import TestCase
import pytest
from users.models import CustomUser

"""
Test whether creating a new user works
"""
@pytest.mark.django_db
def test_create_new_user():
    CustomUser.objects.create_user(email='johnlennon@thebeatels.com', password='John.john')
    assert CustomUser.objects.count() == 1


"""
Test that adding username when trying to create user throws error
"""
@pytest.mark.django_db
def test_creating_user_with_username_throws_error():
    with pytest.raises(Exception) as e:
        CustomUser.objects.create_user(username='JohnLennon', email='johnlennon@thebeatels.com', password='John.john')
        assert str(e.value) == "CustomUser() got an unexpected keyword argument 'username'"


