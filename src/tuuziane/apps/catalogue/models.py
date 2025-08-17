from .abstract_models import AbstractCategory, AbstractProduct
from oscar.apps.catalogue.models import *  # noqa: F403


class Product(AbstractProduct):
    pass


class Category(AbstractCategory):
    pass
