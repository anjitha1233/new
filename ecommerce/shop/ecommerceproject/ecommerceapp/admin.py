from django.contrib import admin
from . models import category,product

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
admin.site.register(category,CategoryAdmin)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','stock','available','created','updated']
    list_editable=['price','stock','available']

    prepopulated_fields={'slug':('name',)}
    list_per_page = 20
admin.site.register(product,ProductAdmin)

# Register your models here.
