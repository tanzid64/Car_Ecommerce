# Generated by Django 4.2.7 on 2023-12-15 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_alter_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]