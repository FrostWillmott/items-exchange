import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

@pytest.fixture
def user1(db):
    return User.objects.create_user(username='user1', password='pass')

@pytest.fixture
def user2(db):
    return User.objects.create_user(username='user2', password='pass')

@pytest.fixture
def client1(user1):
    client = APIClient()
    client.force_authenticate(user=user1)
    return client

@pytest.fixture
def client2(user2):
    client = APIClient()
    client.force_authenticate(user=user2)
    return client
