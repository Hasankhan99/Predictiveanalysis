# Generated by Django 2.2.10 on 2021-03-12 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TS', '0002_auto_20210312_0642'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'storenames',
            },
        ),
    ]
