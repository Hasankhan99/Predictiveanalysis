# Generated by Django 2.2.10 on 2021-03-11 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Store_name', models.CharField(max_length=225)),
                ('date', models.CharField(max_length=50)),
                ('Upper_count', models.CharField(max_length=3)),
                ('Lower_count', models.CharField(max_length=3)),
                ('Expected_Count', models.CharField(max_length=3)),
            ],
        ),
    ]
