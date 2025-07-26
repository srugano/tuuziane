import pytest
from django.test import Client
from wagtail.models import Page, Site

from tuuziane.apps.homepage.models import IndexPage


@pytest.mark.django_db
def test_index_page_view(client: Client):
    """
    Test that a created IndexPage is accessible.
    """
    root_page = Page.objects.get(id=1).specific
    homepage = IndexPage(
        title="Test Home",
        slug="testhome",
        body="<p>Welcome</p>",
    )
    root_page.add_child(instance=homepage)
    root_page.save()

    site = Site.objects.first()
    site.root_page = homepage
    site.save()

    response = client.get(homepage.get_url())
    assert response.status_code == 200
    assert "Welcome" in response.content.decode()
