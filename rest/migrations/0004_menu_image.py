# Generated by Django 4.1.7 on 2023-05-06 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0003_alter_plate_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image_res'),
        ),
    ]
