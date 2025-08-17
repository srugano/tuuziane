from wagtail.blocks import (
    CharBlock,
    ListBlock,
    PageChooserBlock,
    StructBlock,
    TextBlock,
    URLBlock,
)
from wagtail.images.blocks import ImageChooserBlock


class HeroBlock(StructBlock):
    """
    A block for creating a hero section with an image, title, text, and a call-to-action button.
    """

    title = CharBlock(required=True, help_text="The main title for the hero section.")
    text = TextBlock(required=False, help_text="The descriptive text under the title.")
    button_text = CharBlock(required=False, help_text="Text for the call-to-action button.")
    button_link = URLBlock(required=False, help_text="URL for the call-to-action button.")
    background_image = ImageChooserBlock(required=True)

    class Meta:
        template = "blocks/hero_block.html"
        icon = "image"
        label = "Hero Section"


class FeaturedProductsBlock(StructBlock):
    """
    A block to feature a list of selected products.
    We will build the Vue component for this later.
    """

    title = CharBlock(required=True, help_text="Title for the featured products section, e.g., 'New Arrivals'.")
    # This allows picking products. The Vue component will fetch their details.
    products = ListBlock(PageChooserBlock(page_type="catalogue.Product", required=True))

    class Meta:
        template = "blocks/featured_products_block.html"
        icon = "folder-open-inverse"
        label = "Featured Products"
