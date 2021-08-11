# Generated by Django 3.2.3 on 2021-08-02 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camsconfig', '0003_auto_20210526_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainsetting',
            name='device',
            field=models.CharField(choices=[('', 'GPU'), ('CPU', 'CPU')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='mainsetting',
            name='source_weight',
            field=models.CharField(choices=[('yolov5s.pt', 'yolov5s.pt'), ('yolov5m.pt', 'yolov5m.pt'), ('yolov5l.pt', 'yolov5l.pt'), ('yolov5x.pt', 'yolov5x.pt')], default='yolov5s.pt', max_length=50),
        ),
    ]