# Generated by Django 4.2.4 on 2023-08-27 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0006_alter_bookborrow_return_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookborrow',
            name='fine',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]