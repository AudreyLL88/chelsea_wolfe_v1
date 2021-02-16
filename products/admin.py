from django.contrib import admin
from .models import Product, Category, Review


class ReviewInline(admin.TabularInline):
    """ Allows view/edit of reviews from Product detail page """
    model = Review


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)

    inlines = [
        ReviewInline,
    ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    """ Creates the admin interface for Product Reviews """
    list_display = (
        'review_title',
        'reviewer',
        'product',
        'rating'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)

