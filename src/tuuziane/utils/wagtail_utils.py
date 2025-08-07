from django.urls import reverse
from wagtail.models import Page


def get_wagtail_page_or_fallback(slug, default_title, default_content):
    """
    Safely get a Wagtail page by slug, with fallback to default content if not found.
    Returns a dict with title, content and url that can be used in templates.
    """
    try:
        page = Page.objects.get(slug=slug).specific
        return {"title": page.title, "content": page.body if hasattr(page, "body") else str(page), "url": page.url}
    except (Page.DoesNotExist, AttributeError):
        return {
            "title": default_title,
            "content": default_content,
            "url": reverse("flatpage-fallback", kwargs={"slug": slug}),
        }
