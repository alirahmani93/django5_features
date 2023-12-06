from django.contrib import admin
from core.models import Product, Quote, Author, Landmark, Booking


class ProductAdmin(admin.ModelAdmin):
    list_display = ['slug', 'version', ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Quote)
admin.site.register(Author)
admin.site.register(Landmark)
admin.site.register(Booking)
