# Generated by Django 4.2.7 on 2023-12-15 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_alter_car_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]