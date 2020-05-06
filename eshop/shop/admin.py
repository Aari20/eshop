from django.contrib import admin

# Register your models here.
from orders.admin import export_to_csv
from .models import Category, Product, SizePants, SizeShirt, SizeShoes






class SizePantsAdmin(admin.ModelAdmin):
    list_display = ['name', 'size']


admin.site.register(SizePants, SizePantsAdmin)


class SizeShirtAdmin(admin.ModelAdmin):
    list_display = ['name', 'size']


admin.site.register(SizeShirt, SizeShirtAdmin)


class SizeShoesAdmin(admin.ModelAdmin):
    list_display = ['name', 'size']


admin.site.register(SizeShoes, SizeShoesAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category',
                    'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    actions = [export_to_csv]


admin.site.register(Product, ProductAdmin)


