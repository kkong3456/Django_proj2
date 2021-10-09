from django.contrib import admin
from .models import Dsuser
# Register your models here.

class DsuserAdmin(admin.ModelAdmin):
    list_display=['user_id','email','password','register_date']

admin.site.register(Dsuser,DsuserAdmin)
