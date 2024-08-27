from django.contrib import admin

from observations.models import Category1, Category2, Category3, Category4, Municipal, \
    ClimateStation, Hexagon

# Register your models here.
admin.site.register(Category1)
admin.site.register(Category2)
admin.site.register(Category3)
admin.site.register(Category4)
admin.site.register(Municipal)
admin.site.register(ClimateStation)
admin.site.register(Hexagon)
