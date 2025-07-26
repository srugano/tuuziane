from django import template

register = template.Library()


@register.filter(name="get_range")
def get_range(value: str, arg: str | None = None) -> range:
    return range(int(value)) if arg is None else range(int(value), int(arg))
