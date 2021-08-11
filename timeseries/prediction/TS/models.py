from django.db import models

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

# Create your models here.
