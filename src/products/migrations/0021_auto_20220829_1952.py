# Generated by Django 3.2 on 2022-08-29 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_alter_coupondiscount_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupondiscount',
            name='coupon_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coupondiscount',
            name='coupon_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
