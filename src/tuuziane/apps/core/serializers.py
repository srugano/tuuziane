from oscarapi.serializers import basket


class BasketSerializer(basket.BasketSerializer):
    lines = basket.BasketLineSerializer(many=True, read_only=True)

    class Meta(basket.BasketSerializer.Meta):
        fields = basket.BasketSerializer.Meta.fields + (
            "shipping_incl_tax",
            "shipping_excl_tax",
        )
