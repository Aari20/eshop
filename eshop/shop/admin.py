from django.contrib import admin

# Register your models here.
from orders.admin import export_to_csv
from .models import Category, Product, SizePants, SizeShirt, SizeShoes
from parler.admin import TranslatableAdmin





class SizePantsAdmin(admin.ModelAdmin):
    list_display = ['name', 'size']


admin.site.register(SizePants, SizePantsAdmin)


class SizeShirtAdmin(admin.ModelAdmin):
    list_display = ['name', 'size']


admin.site.register(SizeShirt, SizeShirtAdmin)


class SizeShoesAdmin(admin.ModelAdmin):
    list_display = ['name', 'size']


admin.site.register(SizeShoes, SizeShoesAdmin)


class CategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'slug']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(TranslatableAdmin):
    list_display = ['name', 'slug', 'category',
                    'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'stock', 'available']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}
    actions = [export_to_csv]


admin.site.register(Product, ProductAdmin)


