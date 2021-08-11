from django.contrib import admin
from .models import StoreNames,misdata
from import_export import resources
# Register your models here.
admin.site.register(StoreNames)

class MisResource(resources.ModelResource):

    class Meta:
        model = misdata
        exclude='id'
        