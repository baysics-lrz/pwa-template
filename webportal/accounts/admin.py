from django.contrib import admin
from .models import User


# Register your models here.
class FileAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(User, FileAdmin)
