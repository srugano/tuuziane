from django.http import HttpRequest, JsonResponse
from oscar.apps.catalogue.models import Product


def api_products(request: HttpRequest) -> JsonResponse:
    products = Product.objects.filter(is_public=True).order_by("-date_created")[:20]
    data = [
        {
            "id": p.id,
            "title": p.title,
            "price": str(p.stockrecords.first().price_excl_tax) if p.stockrecords.exists() else None,
        }
        for p in products
    ]
    return JsonResponse({"products": data})
