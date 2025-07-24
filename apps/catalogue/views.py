from rest_framework import viewsets, serializers, response
from oscar.apps.catalogue.models import Product

class ProductSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'price']

    def get_price(self, obj):
        if obj.stockrecords.exists():
            return str(obj.stockrecords.first().price_excl_tax)
        return None

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(is_public=True).order_by("-date_created")
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())[:20]
        serializer = self.get_serializer(queryset, many=True)
        return response.Response({"products": serializer.data})
