from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey
from camsuiV2 import settings

class Prediction(models.Model):
    Store_name=models.CharField(max_length=225)
    date=models.CharField(max_length=100)
    Upper_count=models.CharField(max_length=100)
    Lower_count=models.CharField(max_length=100)
    Expected_Count=models.CharField(max_length=100)


class StoreNames(models.Model):
    store_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'storenames'

    def __str__(self):
        return self.store_name

class misdata(models.Model):
    Market_Name=models.CharField(max_length=255)
    Store_Name=models.CharField(max_length=225)
    Store_uid=models.IntegerField()
    totalcount=models.IntegerField()
    date=models.DateField()
    
    def __str__(self):
        return self.Store_Name

