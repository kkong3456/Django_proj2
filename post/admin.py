from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=['name','img_url','register_date']

admin.site.register(Post,PostAdmin)
