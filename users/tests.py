from django.test import TestCase
from .models import User
from django.urls import reverse
import pytest
# Create your tests here.
@pytest.mark.skip
@pytest.mark.django_db
def test_create_user():
    user = User.objects.create(
        name='Toni',
        email='toniyokd@gmail.com',
        password=True,
        published=True
    )
    assert user.name == "Toni"


@pytest.mark.skip
@pytest.fixture
def test_user(db, django_user_model):
    django_user_model.objects.create_user(
        username="test_username", password="test_password")
    return "test_username", "test_password"   # this returns a tuple@pytest.fixture


@pytest.mark.skip
def test_user(db, django_user_model):
    django_user_model.objects.create_user(
        username="test_username", password="test_password")
    return "test_username", "test_password"   # this returns a tuple