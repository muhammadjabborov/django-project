from django.contrib import admin
from django.contrib.admin import ModelAdmin

from app.models import Product, Blog, Author, Arrival


@admin.register(Product)
class ProductModelAdmin(ModelAdmin):
    pass

@admin.register(Arrival)
class ArrivalModelAdmin(ModelAdmin):
    pass

@admin.register(Blog)
class BlogModelAdmin(ModelAdmin):
    pass

@admin.register(Author)
class AuthorModelAdmin(ModelAdmin):
    pass

