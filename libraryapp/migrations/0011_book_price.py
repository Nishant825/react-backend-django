# Generated by Django 4.2.4 on 2023-12-07 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0010_bookborrowhistory_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
