from oscar.apps.catalogue.models import AttributeOption, AttributeOptionGroup

# Material (you already have this, but included for completeness)
materials = AttributeOptionGroup.objects.create(name="Material")
for material in ["Steel", "Aluminum", "Carbon Fiber", "Leather", "Plastic", "Rubber"]:
    AttributeOption.objects.create(group=materials, option=material)

# Sizes (expanded)
sizes = AttributeOptionGroup.objects.create(name="Size")
for size in ["XS", "S", "M", "L", "XL", "XXL", "One Size"]:
    AttributeOption.objects.create(group=sizes, option=size)

# Shoe Sizes (EU & US)
shoe_sizes_eu = AttributeOptionGroup.objects.create(name="Shoe Size (EU)")
for size in range(35, 46):  # European sizes typically range from 35 to 45
    AttributeOption.objects.create(group=shoe_sizes_eu, option=str(size))

shoe_sizes_us_men = AttributeOptionGroup.objects.create(name="Shoe Size (US Men)")
for size in range(5, 16):
    AttributeOption.objects.create(group=shoe_sizes_us_men, option=str(size))

shoe_sizes_us_women = AttributeOptionGroup.objects.create(name="Shoe Size (US Women)")
for size in range(4, 15):
    AttributeOption.objects.create(group=shoe_sizes_us_women, option=str(size))


# Colors (expanded)
colors = AttributeOptionGroup.objects.create(name="Color")
for color in [
    "Red",
    "Orange",
    "Yellow",
    "Green",
    "Blue",
    "Purple",
    "Pink",
    "Brown",
    "Black",
    "White",
    "Gray",
    "Silver",
    "Gold",
]:
    AttributeOption.objects.create(group=colors, option=color)

# Brands (add your own relevant brands)
brands = AttributeOptionGroup.objects.create(name="Brand")
# Add your brand options here

# Other Attribute Groups and Options

# Fit (for clothing)
fits = AttributeOptionGroup.objects.create(name="Fit")
for fit in ["Slim", "Regular", "Relaxed", "Loose"]:
    AttributeOption.objects.create(group=fits, option=fit)

# Gender
genders = AttributeOptionGroup.objects.create(name="Gender")
for gender in ["Men", "Women", "Unisex"]:
    AttributeOption.objects.create(group=genders, option=gender)

# Age Group
age_groups = AttributeOptionGroup.objects.create(name="Age Group")
for age_group in ["Infant", "Toddler", "Kids", "Adult"]:
    AttributeOption.objects.create(group=age_groups, option=age_group)

# Condition (for used items)
conditions = AttributeOptionGroup.objects.create(name="Condition")
for condition in ["New", "Used - Like New", "Used - Good", "Used - Fair"]:
    AttributeOption.objects.create(group=conditions, option=condition)

print("Attributes created ")
