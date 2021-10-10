from django.contrib import admin
from .models import Tag
# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display=['name','register_date']

admin.site.register(Tag,TagAdmin)
