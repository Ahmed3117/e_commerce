# Generated by Django 3.2 on 2022-08-10 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220810_1235'),
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Country',
        ),
    ]
