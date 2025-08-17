from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from .blocks import HeroBlock, FeaturedProductsBlock


class HomePage(Page):
    """
    The HomePage model, which uses a StreamField for flexible content creation.
    """

    shop = models.ForeignKey(
        "shops.Shop",
        on_delete=models.PROTECT,
        related_name="home_pages",
        null=True,
        blank=True,
    )

    body = StreamField(
        [
            ("hero", HeroBlock()),
            ("featured_products", FeaturedProductsBlock()),
        ],
        use_json_field=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("shop"),
        FieldPanel("body"),
    ]
