import pytest
from django.urls import reverse
from rest_framework import status

from oscar.test.factories import create_product


@pytest.mark.django_db
def test_product_list_view(api_client):
    """
    Test that the product list view is accessible.
    """
    url = reverse("product-list")
    response = api_client.get(url, headers={"Authorization": "VueTuuzianeApp"})
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_product_detail_view(api_client):
    """
    Test that the product detail view is accessible and returns the correct product.
    """
    product = create_product()
    url = reverse("product-detail", kwargs={"pk": product.pk})
    response = api_client.get(url, headers={"Authorization": "VueTuuzianeApp"})
    assert response.status_code == status.HTTP_200_OK
    assert response.data["id"] == product.id
