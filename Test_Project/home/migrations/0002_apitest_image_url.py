# Generated by Django 4.1 on 2022-09-07 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apitest',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
