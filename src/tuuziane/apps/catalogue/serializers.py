from rest_framework import serializers
from oscar.apps.catalogue.models import Product


class ProductSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["id", "title", "price"]

    def get_price(self, obj):
        # if obj.stockrecords.exists():
        #     return str(obj.stockrecords.first().price_excl_tax)
        return None
