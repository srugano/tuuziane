from django.conf import settings
from django.db import models


class Shop(models.Model):
    """
    Represents a single merchant's shop in the multi-tenant platform.
    """

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="shops",
        help_text="The user who owns this shop.",
    )
    name = models.CharField(max_length=255, help_text="The public name of the shop.")
    subdomain = models.CharField(
        max_length=100, unique=True, help_text="The unique subdomain for the shop (e.g., 'my-cool-shop')."
    )
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Shop"
        verbose_name_plural = "Shops"

    def __str__(self):
        return self.name
