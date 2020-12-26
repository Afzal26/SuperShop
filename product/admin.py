from django.contrib import admin

from product.models import Product, Images, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']

class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category', 'status', 'image_tag']
    list_filter = ['category']
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug':('title',)}

# class ProductSliderAdmin(admin.ModelAdmin):
#     list_display = ['title', 'status', 'image_tag']
#     readonly_fields = ('image_tag',)

# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['subject', 'comment', 'status', 'create_at']
#     list_filter = ['status']
#     readonly_fields = ('subject','comment', 'ip', 'user', 'product', 'rate', )

# admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images)