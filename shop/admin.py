from django.contrib import admin
from .models import Product, Order

# Register your models here.
admin.site.site_header = "E-commerce Site"
admin.site.site_title = "Ping Shopping"
admin.site.index_title = "Manage Ping Shopping"

class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self, request, queryset): # Add actions to admin site
        queryset.update(category="default")

    list_display = ('name', 'price', 'disc_price', 'category')
    search_fields = ('name', 'category')
    actions = ('change_category_to_default',)  # Add function of actions here to use in admin site
    list_editable = ('price', 'category',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)