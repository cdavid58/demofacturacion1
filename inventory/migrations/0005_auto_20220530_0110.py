# Generated by Django 3.2.13 on 2022-05-30 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_subcategories_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='discount',
            field=models.TextField(default=0),
        ),
        migrations.AddField(
            model_name='inventory',
            name='ico',
            field=models.TextField(default=0),
        ),
    ]
