# Generated by Django 4.1.6 on 2023-04-12 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(max_length=255, null=True, upload_to='images/'),
        ),
    ]
