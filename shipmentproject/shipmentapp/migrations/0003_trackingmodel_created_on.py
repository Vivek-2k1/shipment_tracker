# Generated by Django 4.1.5 on 2023-06-30 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipmentapp', '0002_trackingmodel_cargomodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackingmodel',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
