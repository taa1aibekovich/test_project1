# Generated by Django 5.0.6 on 2024-07-10 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('name', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='director',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='director',
            name='name_en',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='director',
            name='name_ru',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
