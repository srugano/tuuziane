from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class IndexPage(Page):  # type: ignore[misc]
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel("body", classname="full"),
    ]
