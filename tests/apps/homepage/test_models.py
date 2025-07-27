import pytest
from wagtail.models import Page

from tuuziane.apps.homepage.models import IndexPage


@pytest.mark.django_db
def test_index_page_creation():
    """
    Test that an IndexPage can be created as a child of the root page.
    """
    root_page = Page.objects.get(id=1).specific
    homepage = IndexPage(
        title="Test Home",
        slug="testhome",
        body="<p>Welcome to the test homepage.</p>",
    )
    root_page.add_child(instance=homepage)
    root_page.save()

    created_page = IndexPage.objects.get(slug="testhome")
    assert created_page is not None
    assert created_page.title == "Test Home"
    assert created_page.get_parent() == root_page
