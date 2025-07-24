from oscar.apps.catalogue.models import Product
from apps.catalogue.serializers import ProductSerializer
from apps.core.views import BaseViewSetMixin


class ProductViewSet(BaseViewSetMixin):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(is_public=True).order_by("-date_created")
