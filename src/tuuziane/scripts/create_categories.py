from oscar.apps.catalogue.categories import create_from_breadcrumbs

# define the categories list

categories = [
    "Headlights & Lighting > Turn Signals",
    "Headlights & Lighting > Fog Lights",
    "Headlights & Lighting > Headlights > Lights",
    "Interior Parts > Floor Mats",
    "Interior Parts > Gauges",
    "Interior Parts > steering wheels",
    "Interior Parts > cargo Accessories",
    "Repair Manual",
    "Fuel System",
]


for breadcrumbs in categories:
    create_from_breadcrumbs(breadcrumbs)

print("categories succesfuly  added")  # noqa: T201
