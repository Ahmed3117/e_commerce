# Generated by Django 3.2 on 2022-08-20 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rate',
        ),
    ]
