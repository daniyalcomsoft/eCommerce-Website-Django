from django.contrib import admin
from shoesapp.models import *

from django.contrib.auth.admin import UserAdmin

# Register your models here.

class TypeAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Image']

class SizeAdmin(admin.ModelAdmin):
    list_display = ['Name']

class ConditionAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Image']

class BrandAdmin(admin.ModelAdmin):
    list_display = ['Name']

class ShoesAdmin(admin.ModelAdmin):
    list_display = ['Name', 'CutPrice', 'Price', 'Image', 'Type', 'Size', 'Condition', 'Brand', 'Description']

class ShoesImagesAdmin(admin.ModelAdmin):
    list_display = ['Shoes', 'Image']

class VideosAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Video', 'Description']

class ShoesReviewsAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Description', 'Image']

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Image']

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Telephone', 'Address', 'Message']

class QueryAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Telephone', 'Address', 'Image', 'Message']

class BestSellingAdmin(admin.ModelAdmin):
    list_display = ['Name', 'CutPrice', 'Price', 'Image', 'Type', 'Size', 'Condition', 'Brand', 'Description']

class DealsAdmin(admin.ModelAdmin):
    list_display = ['Name', 'CutPrice', 'Price', 'Image', 'Type', 'Size', 'Condition', 'Brand', 'Description']

class BSImageAdmin(admin.ModelAdmin):
    list_display = ['BestSelling', 'Image']

class DealsImageAdmin(admin.ModelAdmin):
    list_display = ['Deals', 'Image']

admin.site.register(Type, TypeAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Condition, ConditionAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Shoes, ShoesAdmin)
admin.site.register(ShoesImage, ShoesImagesAdmin)
admin.site.register(Videos, VideosAdmin)
admin.site.register(ShoesReviews, ShoesReviewsAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Query, QueryAdmin)
admin.site.register(BestSelling, BestSellingAdmin)
admin.site.register(Deals, DealsAdmin)
admin.site.register(BSImage, BSImageAdmin)
admin.site.register(DealsImage, DealsImageAdmin)
