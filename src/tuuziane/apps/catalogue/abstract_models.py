from django.db import models
from oscar.apps.catalogue.abstract_models import (
    AbstractCategory as CoreAbstractCategory,
    AbstractProduct as CoreAbstractProduct,
)


class AbstractProduct(CoreAbstractProduct):
    shop = models.ForeignKey(
        "shops.Shop",
        on_delete=models.CASCADE,
        related_name="products",
        null=True,
        blank=True,
    )

    class Meta(CoreAbstractProduct.Meta):
        abstract = True


class AbstractCategory(CoreAbstractCategory):
    shop = models.ForeignKey(
        "shops.Shop",
        on_delete=models.CASCADE,
        related_name="categories",
        null=True,
        blank=True,
    )

    class Meta(CoreAbstractCategory.Meta):
        abstract = True
