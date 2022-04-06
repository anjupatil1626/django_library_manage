from django.contrib import admin
from .models import lab
# Register your models here.
@admin.register(lab)
class labadmin(admin.ModelAdmin):
    list_display=['book_name','author','isbn','quantity','category']
