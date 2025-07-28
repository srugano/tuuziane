import pytest
from django.test import Client
from wagtail.models import Site

from tuuziane.apps.homepage.models import IndexPage


@pytest.mark.django_db
def test_index_page_view(client: Client):
    """
    Test that a created IndexPage is accessible.
    """
    site = Site.objects.get(is_default_site=True)
    root_page = site.root_page.specific
    homepage = IndexPage(
        title="Test Home",
        slug="testhome",
        body="<p>Welcome</p>",
    )
    root_page.add_child(instance=homepage)

    response = client.get(homepage.get_url())
    assert response.status_code == 200
    assert "Welcome" in response.content.decode()
