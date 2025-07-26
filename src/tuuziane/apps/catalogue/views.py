from oscar.apps.catalogue.models import Product
from tuuziane.apps.catalogue.serializers import ProductSerializer
from tuuziane.apps.core.views import BaseViewSetMixin


class ProductViewSet(BaseViewSetMixin):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(is_public=True).order_by("-date_created")
