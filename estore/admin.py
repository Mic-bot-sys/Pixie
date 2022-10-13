from django.contrib import admin
from . import models
from .models import Item, Contactus, Subscribe
# Register your models here.

@admin.register(models.Item)
class ToluAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}

admin.site.register(Contactus)
admin.site.register(Subscribe)
