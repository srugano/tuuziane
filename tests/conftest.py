import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()


@pytest.fixture
def user(db):
    """A sample user for tests."""
    return User.objects.create_user("test@example.com", "password")


@pytest.fixture
def api_client():
    """A DRF API client."""
    return APIClient()


@pytest.fixture
def authenticated_api_client(api_client, user):
    """A DRF API client authenticated as the sample user."""
    api_client.force_authenticate(user=user)
    return api_client
