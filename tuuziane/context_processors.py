from django.urls import resolve


def oscar_shop_tagline(request):
    url_name = resolve(request.path_info).url_name.capitalize()
    return {"OSCAR_SHOP_TAGNILE": url_name}
