from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Product


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'slug')

translator.register(Category, CategoryTranslationOptions)


class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'slug', 'description')

translator.register(Product, ProductTranslationOptions)